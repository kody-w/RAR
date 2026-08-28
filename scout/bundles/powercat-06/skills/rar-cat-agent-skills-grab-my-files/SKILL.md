---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "7bf1e47a108ee4b7ac096b531ca8a1a6518e55f1e5b25c33b597b31f435852d3", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/grab_my_files`. The original RAPP
agent is preserved byte-for-byte in `grab_my_files_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Grab My Files — One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#grab-my-files
  Upstream author: Rafael Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The input to convert \u2014 path, URL or payload.",
      "type": "string"
    },
    "target_format": {
      "description": "Optional. The desired output format.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `grab_my_files_agent.py` and embedded as the fenced Python below (sha256 7bf1e47a108ee4b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `grab_my_files_agent.py` first:

```bash
python3 grab_my_files_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 grab_my_files_agent.py   # or on stdin
python3 grab_my_files_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Grab My Files — One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#grab-my-files
  Upstream author: Rafael Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/grab_my_files',
    "version": '2.0.0',
    "display_name": 'Grab My Files',
    "description": 'One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download.',
    "author": 'Rafael Alcaraz',
    "tags": ['files', 'export', 'zip', 'download', 'productivity'],
    "category": 'pipeline',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'grab-my-files',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#grab-my-files',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '846bd7a050af6ac5',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['tag:export', 'word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class GrabMyFiles(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GrabMyFiles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The input to convert — path, URL or payload.', 'type': 'string'}, 'target_format': {'description': 'Optional. The desired output format.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(GrabMyFiles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
