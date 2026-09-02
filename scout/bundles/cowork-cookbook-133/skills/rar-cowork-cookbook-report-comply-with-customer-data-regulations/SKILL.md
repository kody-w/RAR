---
name: "rar-cowork-cookbook-report-comply-with-customer-data-regulations"
description: "Builds a structured summary report of comply with customer data regulations activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_comply_with_customer_data_regulations", "rar_sha256": "209ba471781f5a72783e1c08e1451279aef740a93d7fd5530f5b7c7d01a7f321", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_comply_with_customer_data_regulations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-comply-with-customer-data-regulations:f4c7a0cff93da24055ed37b8ec4bcf19f5a603c0de462eefb49aa9966de40ad1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_comply_with_customer_data_regulations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_comply_with_customer_data_regulations_agent.py` is
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
