---
name: "rar-cowork-cookbook-planned-order-summary"
description: "Summarizes planned production orders by resource for the next four weeks, including load vs capacity."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/planned_order_summary", "rar_sha256": "a96f9bd059fa1a5b1ec9e6f88a8049daf82de5b4d3a63df7594a94542a1244ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "planned_order_summary_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/planned-order-summary:c38f5d16702541abe064e7a0b992afe22a155977fecb97daa965d852ef4bc0f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/planned_order_summary`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `planned_order_summary_agent.py` is
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

Planned Order Summary by Resource — Summarizes planned production orders by resource for the next four weeks, including load vs capacity.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `planned_order_summary_agent.py` and embedded as the fenced Python below (sha256 a96f9bd059fa1a5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `planned_order_summary_agent.py` first:

```bash
python3 planned_order_summary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 planned_order_summary_agent.py   # or on stdin
python3 planned_order_summary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Planned Order Summary by Resource — Summarizes planned production orders by resource for the next four weeks, including load vs capacity.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/planned_order_summary',
    "version": '2.0.0',
    "display_name": 'Planned Order Summary by Resource',
    "description": 'Summarizes planned production orders by resource for the next four weeks, including load vs capacity.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'planned-order-summary',
        "upstream_url": 'https://coworkcookbook.com/recipes/planned-order-summary',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0eb3dd922e7ca635',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/planned-order-summary', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PlannedOrderSummary(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PlannedOrderSummary'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(PlannedOrderSummary().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
