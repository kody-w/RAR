---
name: "rar-cowork-cookbook-report-define-research-and-development-approach"
description: "Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_research_and_development_approach", "rar_sha256": "032bf02d04939fd498580e7158edb499c5414f44accafc0a7e4d46be8ead9e59", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_research_and_development_approach`. The original RAPP
agent is preserved byte-for-byte in `report_define_research_and_development_approach_agent.py` and in the RCI capsule.

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

Define research and development approach Summary Report — Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-research-and-development-approach
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
    "breakdown_dimensions": {
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. report-define-research-and-development-approach-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 032bf02d04939fd4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_research_and_development_approach_agent.py` first:

```bash
python3 report_define_research_and_development_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_research_and_development_approach_agent.py   # or on stdin
python3 report_define_research_and_development_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define research and development approach Summary Report — Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-research-and-development-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_research_and_development_approach',
    "version": '3.0.3',
    "display_name": 'Define research and development approach Summary Report',
    "description": "Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s",
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
        "upstream_slug": 'report-define-research-and-development-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-research-and-development-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '25ecf8fab327859a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/define-research-and-development-approach'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-define-research-and-development-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-research-and-development-approach-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define research and development approach stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define research and development approach for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-research-and-development-approach-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define research and development approach records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s", 'example_request': "Run a define research and development approach summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-research-and-development-approach-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of define research and development approach with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineResearchAndDevelopmentApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineResearchAndDevelopmentApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-research-and-development-approach-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(ReportDefineResearchAndDevelopmentApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
