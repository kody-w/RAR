---
name: "rar-cat-agent-skills-work-iq-signalboard"
description: "Turn four weeks of Calendar, Mail, and Teams chat activity into a colorful dashboard of reconciled Work IQ counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/work_iq_signalboard", "rar_sha256": "952f4d5714c90395e690cd9cb0dca9eae1d70e15f5a568f375f573ac5d4fe3d2", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "work_iq_signalboard_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/work-iq-signalboard:5d3b030873073eff0381f875b582cfb1315d4c9a76610ce9e262308db56afd74", "kind": "skill"}, "version": "3.0.0", "author": "Andreas Adner", "tags": ["work_iq", "microsoft_365", "dashboard", "visualization", "work_patterns", "analytics"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/work_iq_signalboard`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `work_iq_signalboard_agent.py` is
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
