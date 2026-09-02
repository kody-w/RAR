---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "b9574a93f4efeb61a83d8e843f8caae6f11d146b20edaca294837c209bc4723a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "institutional_knowledge_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/institutional-knowledge:368cedcf3965caa166b3fee19a64f963d9a3a7c96e3430d8e8f691593bc0b505", "kind": "skill"}, "version": "2.0.1", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/institutional_knowledge`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `institutional_knowledge_agent.py` is
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

Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `institutional_knowledge_agent.py` and embedded as the fenced Python below (sha256 b9574a93f4efeb61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `institutional_knowledge_agent.py` first:

```bash
python3 institutional_knowledge_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 institutional_knowledge_agent.py   # or on stdin
python3 institutional_knowledge_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Institutional Knowledge Archivist — Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a convert capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#institutional-knowledge
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/institutional_knowledge',
    "version": '2.0.1',
    "display_name": 'Institutional Knowledge Archivist',
    "description": "Preserve a departing senior leader's institutional knowledge — decisions, rationale, relationships, and tribal knowledge — by mining their M365 signals into a structured, multi-phase archive a successor can ground on.",
    "author": 'Srinivas Varukala',
    "tags": ['knowledge', 'handoff', 'leadership', 'm365', 'offboarding', 'documentation', 'productivity'],
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
        "upstream_slug": 'institutional-knowledge',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#institutional-knowledge',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3ac7896e76455716',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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


class InstitutionalKnowledge(BasicAgent):
    """Convert agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'InstitutionalKnowledge'
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
    print(InstitutionalKnowledge().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
