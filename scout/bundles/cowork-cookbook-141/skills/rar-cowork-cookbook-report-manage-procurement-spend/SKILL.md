---
name: "rar-cowork-cookbook-report-manage-procurement-spend"
description: "Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_procurement_spend", "rar_sha256": "75279a07273c869ab4d38cc9a30a3010b6941d5f3d94e91c546229d0af6de3e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_procurement_spend_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-procurement-spend:342678dc28545c0686e3326f75e1bcdc1dd61833ab30af59f1bc89d7adf8e2fc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_procurement_spend`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_procurement_spend_agent.py` is
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

Manage procurement spend Summary Report — Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 75279a07273c869a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_procurement_spend_agent.py` first:

```bash
python3 report_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_procurement_spend_agent.py   # or on stdin
python3 report_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Summary Report — Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_procurement_spend',
    "version": '2.0.0',
    "display_name": 'Manage procurement spend Summary Report',
    "description": 'Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27098e13b13153e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageProcurementSpend(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProcurementSpend'
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
    print(ReportManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
