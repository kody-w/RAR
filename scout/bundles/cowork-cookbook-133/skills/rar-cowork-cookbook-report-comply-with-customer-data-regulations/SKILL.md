---
name: "rar-cowork-cookbook-report-comply-with-customer-data-regulations"
description: "Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_comply_with_customer_data_regulations", "rar_sha256": "d7c742212ddccb4d5b3e96d1361f3904ca535ad0fcaabb52137a6f5e191b4b5c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_comply_with_customer_data_regulations`. The original RAPP
agent is preserved byte-for-byte in `report_comply_with_customer_data_regulations_agent.py` and in the RCI capsule.

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

Comply with customer data regulations Summary Report — Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 d7c742212ddccb4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_comply_with_customer_data_regulations_agent.py` first:

```bash
python3 report_comply_with_customer_data_regulations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_comply_with_customer_data_regulations_agent.py   # or on stdin
python3 report_comply_with_customer_data_regulations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Comply with customer data regulations Summary Report — Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_comply_with_customer_data_regulations',
    "version": '2.0.1',
    "display_name": 'Comply with customer data regulations Summary Report',
    "description": 'Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-comply-with-customer-data-regulations',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-comply-with-customer-data-regulations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32e4d9fa3dd2fc30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/comply-with-customer-data-regulations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-comply-with-customer-data-regulations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportComplyWithCustomerDataRegulations(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportComplyWithCustomerDataRegulations'
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
    print(ReportComplyWithCustomerDataRegulations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
