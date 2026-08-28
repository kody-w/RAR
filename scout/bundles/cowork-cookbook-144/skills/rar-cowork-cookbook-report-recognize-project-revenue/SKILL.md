---
name: "rar-cowork-cookbook-report-recognize-project-revenue"
description: "Builds a structured summary report of recognize project revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_recognize_project_revenue", "rar_sha256": "1e28adf9ce869381248a1e78b8875fe54155d4e98d007821aa22eeeac82c56f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_recognize_project_revenue`. The original RAPP
agent is preserved byte-for-byte in `report_recognize_project_revenue_agent.py` and in the RCI capsule.

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
