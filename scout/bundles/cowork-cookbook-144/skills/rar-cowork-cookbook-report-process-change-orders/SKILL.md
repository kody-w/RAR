---
name: "rar-cowork-cookbook-report-process-change-orders"
description: "Builds a structured summary report of process change orders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_change_orders", "rar_sha256": "d8922cdfa3df2fe14978c2a269743730364de3646da290a9b55993c67db6858c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_change_orders`. The original RAPP
agent is preserved byte-for-byte in `report_process_change_orders_agent.py` and in the RCI capsule.

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
