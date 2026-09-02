---
name: "rar-cowork-cookbook-report-recognize-project-revenue"
description: "Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_recognize_project_revenue", "rar_sha256": "1e28adf9ce869381248a1e78b8875fe54155d4e98d007821aa22eeeac82c56f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_recognize_project_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-recognize-project-revenue:9126cf45494d9f15ca5c55a20c44bfaebcedd3eed7229ac8160af6da73d00e8e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_recognize_project_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_recognize_project_revenue_agent.py` is
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

Recognize project revenue Summary Report — Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 1e28adf9ce869381…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_recognize_project_revenue_agent.py` first:

```bash
python3 report_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_recognize_project_revenue_agent.py   # or on stdin
python3 report_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Summary Report — Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_recognize_project_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize project revenue Summary Report',
    "description": 'Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '208e8ac554e6b3cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRecognizeProjectRevenue(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecognizeProjectRevenue'
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
    print(ReportRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
