"""
PublishPrivateAgent — generate a public RAR stub from a local agent
file that lives in your private RAR.

Reads `agent_path`, AST-extracts its __manifest__, and emits the
matching `.py.stub` file ready to commit to public RAR. The stub
points back at your private repo via __source__, and the brainstem
resolves it at install time using the user's GitHub credentials.

This agent does NOT push anything anywhere. It produces the stub
content and (optionally) writes it to disk. You move it from there.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/publish_private_agent",
    "version": "1.0.0",
    "display_name": "PublishPrivateAgent",
    "description": "Generate a public RAR stub from a private agent.py — pure metadata, points back at your private repo for the bytes.",
    "author": "Kody Wildfeuer",
    "tags": ["registry", "private", "publish", "stub", "federation"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import ast
import os
from pathlib import Path

from agents.basic_agent import BasicAgent


REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]


def _extract_manifest(agent_path: Path) -> dict | None:
    """AST-parse a Python file and return its __manifest__ dict, or None."""
    try:
        tree = ast.parse(agent_path.read_text())
    except (SyntaxError, OSError):
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


def _render_dict(d: dict, indent: int = 4) -> str:
    """Render a dict as pretty Python source. Keeps key order and quotes
    consistent with hand-written manifests in the rest of the repo."""
    pad = " " * indent
    lines = ["{"]
    for k, v in d.items():
        lines.append(f"{pad}{repr(k)}: {repr(v)},")
    lines.append("}")
    return "\n".join(lines)


class PublishPrivateAgent(BasicAgent):
    def __init__(self):
        self.name = "PublishPrivateAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate a public RAR .py.stub from a local agent.py "
                "that lives in your private RAR. Returns the stub source. "
                "Optionally writes it to disk."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "agent_path": {
                        "type": "string",
                        "description": "Path to the local agent.py file you want to publish a stub for.",
                    },
                    "private_repo": {
                        "type": "string",
                        "description": "owner/name of your private repo (e.g., 'kody-w/example-private-rar').",
                    },
                    "private_path": {
                        "type": "string",
                        "description": "Path inside the private repo where the agent.py will live. Defaults to the same relative path as agent_path.",
                    },
                    "ref": {
                        "type": "string",
                        "description": "Git ref in the private repo (branch or tag). Defaults to 'main'.",
                    },
                    "write_to": {
                        "type": "string",
                        "description": "If provided, write the generated stub to this path. Otherwise just return its content.",
                    },
                },
                "required": ["agent_path", "private_repo"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        agent_path = kwargs.get("agent_path", "")
        private_repo = kwargs.get("private_repo", "")
        private_path = kwargs.get("private_path", "")
        ref = kwargs.get("ref", "main")
        write_to = kwargs.get("write_to", "")

        if not agent_path:
            return "Error: 'agent_path' is required."
        if not private_repo or "/" not in private_repo:
            return "Error: 'private_repo' must be owner/name (e.g., 'kody-w/example-private-rar')."

        p = Path(agent_path)
        if not p.exists():
            return f"Error: agent file not found at {agent_path}"

        manifest = _extract_manifest(p)
        if manifest is None:
            return f"Error: could not extract __manifest__ from {agent_path}"
        missing = [f for f in REQUIRED_MANIFEST_FIELDS if f not in manifest]
        if missing:
            return f"Error: manifest missing required fields: {missing}"

        # Force quality_tier to private for stubs — they aren't reviewable.
        manifest["quality_tier"] = "private"

        if not private_path:
            private_path = str(p).replace(os.sep, "/")

        source = {
            "schema": "rapp-source/1.0",
            "type": "github_private",
            "repo": private_repo,
            "ref": ref,
            "path": private_path,
        }

        docstring = (
            f'"""\n'
            f"Gated stub for {manifest['name']} — bytes live in the private repo\n"
            f"{private_repo} at {private_path}. Public RAR carries only this\n"
            f"manifest pointer; the brainstem resolves the source at install\n"
            f"time using the installer's own GitHub credentials.\n"
            f'"""\n\n'
        )

        stub_src = (
            docstring
            + "__manifest__ = " + _render_dict(manifest) + "\n\n"
            + "__source__ = " + _render_dict(source) + "\n"
        )

        if write_to:
            out = Path(write_to)
            try:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(stub_src)
            except OSError as e:
                return f"Error writing stub to {write_to}: {e}"
            return (
                f"Stub written to {out}\n\n"
                f"Next step: commit it to public RAR at the same path under\n"
                f"agents/@<publisher>/private/, push, and the registry will\n"
                f"rebuild automatically.\n\n"
                f"-- stub content --\n{stub_src}"
            )

        return (
            f"Generated stub for {manifest['name']}\n\n"
            f"Save this as agents/@{manifest['name'].split('/')[0][1:]}/private/"
            f"{p.name}.stub in your public RAR clone, then commit + push:\n\n"
            f"{stub_src}"
        )


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python publish_private_agent_agent.py <agent_path> <owner/repo> [ref]")
        sys.exit(2)
    agent = PublishPrivateAgent()
    ref = sys.argv[3] if len(sys.argv) > 3 else "main"
    print(agent.perform(agent_path=sys.argv[1], private_repo=sys.argv[2], ref=ref))
