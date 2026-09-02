---
name: "rar-cowork-cookbook-report-process-change-orders"
description: "Builds a structured summary report of process change orders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_change_orders", "rar_sha256": "d8922cdfa3df2fe14978c2a269743730364de3646da290a9b55993c67db6858c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_process_change_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-process-change-orders:a0b2a689a6f9971792c79c1ea8c18e7fe546dcfe63096cdccf047a726c2e44fc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_process_change_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_process_change_orders_agent.py` is
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

Process change orders Summary Report — Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 d8922cdfa3df2fe1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_change_orders_agent.py` first:

```bash
python3 report_process_change_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_change_orders_agent.py   # or on stdin
python3 report_process_change_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change orders Summary Report — Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_change_orders',
    "version": '2.0.0',
    "display_name": 'Process change orders Summary Report',
    "description": 'Builds a structured summary report of process change orders activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-process-change-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-change-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa0273976fb2b6ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-orders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-process-change-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportProcessChangeOrders(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessChangeOrders'
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
    print(ReportProcessChangeOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
