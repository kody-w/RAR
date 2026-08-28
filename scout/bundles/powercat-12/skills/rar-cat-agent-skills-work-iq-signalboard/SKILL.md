---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "952f4d5714c90395e690cd9cb0dca9eae1d70e15f5a568f375f573ac5d4fe3d2", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "version": "3.0.0", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/work_iq_signalboard`. The original RAPP
agent is preserved byte-for-byte in `work_iq_signalboard_agent.py` and in the RCI capsule.

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

Work IQ Signalboard — Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard
  Upstream author: Andreas Adner
  Upstream version: 2.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `work_iq_signalboard_agent.py` and embedded as the fenced Python below (sha256 952f4d5714c90395…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `work_iq_signalboard_agent.py` first:

```bash
python3 work_iq_signalboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 work_iq_signalboard_agent.py   # or on stdin
python3 work_iq_signalboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Work IQ Signalboard — Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard
  Upstream author: Andreas Adner
  Upstream version: 2.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/work_iq_signalboard',
    "version": '3.0.0',
    "display_name": 'Work IQ Signalboard',
    "description": 'Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts.',
    "author": 'Andreas Adner',
    "tags": ['work_iq', 'microsoft_365', 'dashboard', 'visualization', 'work_patterns', 'analytics'],
    "category": 'general',
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
        "upstream_slug": 'work-iq-signalboard',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#work-iq-signalboard',
        "upstream_version": '2.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '267a75f8911138e0',
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
_SPEC = {'archetype': 'convert', 'checks': ['Record counts reconcile between input and output.', 'Every unmapped field is listed with its disposition.', 'A round-trip on the sample is lossless, or the loss is documented and intended.', 'The conversion is rerunnable and produces identical output.'], 'confidence': 1.0, 'deliverable': 'Converted output plus a mapping table, an unmapped-field list, and a reconciliation showing nothing was lost silently.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The input to convert — path, URL or payload.', 'target_format': 'Optional. The desired output format.'}, 'refined_by': 'rules', 'signals': ['word:into'], 'steps': ['Characterise the input completely before writing any mapping: schema, encoding, size, and every optional field actually present.', 'Define the target contract with the same rigour, including what the consumer requires versus merely accepts.', 'Map field by field, and write down the fields with no counterpart — silent drops are how conversions lose data.', 'Decide the policy for the unmappable: fail, default, or carry through as an extension. Never drop by accident.', 'Convert a representative sample first and diff it against the input on the fields that matter.', 'Run the whole set, then reconcile counts and checksums between input and output.'], 'subject_label': 'input to convert', 'verb': 'Convert'}


class WorkIqSignalboard(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkIqSignalboard'
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
    print(WorkIqSignalboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
