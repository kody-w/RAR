---
name: "rar-cat-agent-skills-institutional-knowledge"
description: "Preserve a departing senior leader's institutional knowledge \u2014 decisions, rationale, relationships, and tribal knowledge \u2014 by mining their M365 signals into a structured, multi-phase archive a successor can ground on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/institutional_knowledge", "rar_sha256": "b9574a93f4efeb61a83d8e843f8caae6f11d146b20edaca294837c209bc4723a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.1", "author": "Srinivas Varukala", "tags": ["knowledge", "handoff", "leadership", "m365", "offboarding", "documentation", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/institutional_knowledge`. The original RAPP
agent is preserved byte-for-byte in `institutional_knowledge_agent.py` and in the RCI capsule.

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
