---
name: "rar-cat-agent-skills-grab-my-files"
description: "One-tap way to bundle every file your Copilot Studio agent produced in a session into a single timestamped .zip and hand it back as a download."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/grab_my_files", "rar_sha256": "7bf1e47a108ee4b7ac096b531ca8a1a6518e55f1e5b25c33b597b31f435852d3", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "grab_my_files_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/grab-my-files:542df6206e14edd4341365b47b709e2846e496ac70168f11225606e392641cad", "kind": "skill"}, "version": "2.0.0", "author": "Rafael Alcaraz", "tags": ["files", "export", "zip", "download", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/grab_my_files`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `grab_my_files_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
