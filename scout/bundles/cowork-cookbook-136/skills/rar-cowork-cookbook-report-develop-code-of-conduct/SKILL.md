---
name: "rar-cowork-cookbook-report-develop-code-of-conduct"
description: "Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_code_of_conduct", "rar_sha256": "3629354d9aa547aadd7ad15a0dac74d8ebaa7120ba1ea467eb2a82913a17b8d6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_code_of_conduct`. The original RAPP
agent is preserved byte-for-byte in `report_develop_code_of_conduct_agent.py` and in the RCI capsule.

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

Develop code of conduct Summary Report — Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-code-of-conduct
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
      "description": "Dimensions to break out by where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-code-of-conduct-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 3629354d9aa547aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_code_of_conduct_agent.py` first:

```bash
python3 report_develop_code_of_conduct_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_code_of_conduct_agent.py   # or on stdin
python3 report_develop_code_of_conduct_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop code of conduct Summary Report — Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-code-of-conduct
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_code_of_conduct',
    "version": '3.0.3',
    "display_name": 'Develop code of conduct Summary Report',
    "description": 'Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-code-of-conduct',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-code-of-conduct',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c3d160726a85735',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-code-of-conduct'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-develop-code-of-conduct', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break out by where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-code-of-conduct-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop code of conduct stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop code of conduct for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-code-of-conduct-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop code of conduct records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a develop code of conduct summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break out by where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-code-of-conduct-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change summary report of develop code of conduct activity from D365 ERP with totals, dimension breakdowns, and a top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopCodeOfConduct(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopCodeOfConduct'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break out by where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-code-of-conduct-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopCodeOfConduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
