---
name: "rar-cowork-cookbook-report-define-research-and-development-approach"
description: "Builds a read-only summary report of define research and development approach activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, output as an Excel workbook with Summary, Detail, and Top10 s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_research_and_development_approach", "rar_sha256": "032bf02d04939fd498580e7158edb499c5414f44accafc0a7e4d46be8ead9e59", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
