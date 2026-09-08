---
name: "rar-cowork-cookbook-report-develop-code-of-conduct"
description: "Builds a read-only summary report of develop code of conduct activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_code_of_conduct", "rar_sha256": "3629354d9aa547aadd7ad15a0dac74d8ebaa7120ba1ea467eb2a82913a17b8d6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
