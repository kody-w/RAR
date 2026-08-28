---
name: "rar-cowork-cookbook-report-comply-with-customer-data-regulations"
description: "Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_comply_with_customer_data_regulations", "rar_sha256": "209ba471781f5a72783e1c08e1451279aef740a93d7fd5530f5b7c7d01a7f321", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_comply_with_customer_data_regulations_agent.py` and embedded as the fenced Python below (sha256 209ba471781f5a72…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_comply_with_customer_data_regulations_agent.py` first:

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
    "version": '2.0.0',
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
