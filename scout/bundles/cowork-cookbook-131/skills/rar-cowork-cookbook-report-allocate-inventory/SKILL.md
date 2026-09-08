---
name: "rar-cowork-cookbook-report-allocate-inventory"
description: "Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_inventory", "rar_sha256": "70015336d1ae19e195dbd7d966918c86b786a1536a7dc77211faf81bb0e927cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_allocate_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_allocate_inventory_agent.py` and in the RCI capsule.

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

Allocate inventory Summary Report — Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 70015336d1ae19e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_inventory_agent.py` first:

```bash
python3 report_allocate_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_allocate_inventory_agent.py   # or on stdin
python3 report_allocate_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory Summary Report — Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_allocate_inventory',
    "version": '3.0.3',
    "display_name": 'Allocate inventory Summary Report',
    "description": 'Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-allocate-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-allocate-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a740e02d0c538647',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/allocate-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-allocate-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'posted_period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where allocate inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of allocate inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-allocate-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an allocate inventory summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'posted_period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of allocate inventory activity with totals, by-dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAllocateInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAllocateInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportAllocateInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abOjSJblX9G8NpvMbEU8dpCircwGCQESixASSCijLJJ933ey67+PIykiM6siq6vM5sso3gsEuF+/6znXH/z6ZrZNkFdvn97OrpktODNJwsCtFmbmLLZ5n1cxOOSxBX4Xdp41VWi1TV7Vbx/eHLe2q7BowjwD0zdtmDj1wlxUrul8zLNkXABZuW027iLMOjcDs8ZF3aapCY6VW+RVs/CqPF0wY2amoV0vMJJYsP/7vJUWXg40WCSubyYLMDNsxodCRV43Lji4VZg7H4CQpq2yMPPBzcVusN1kMSv80LUPm2Bxfq72YcG4jRkmHx5CLnmBwIs6cN2mfgdmuIOZFolbv336+a8f3kLw/e3Tr292Ytbg0pv6UJR+WbL/agiYl5iZDwYUI/BfBs6BVkDtFFxyXG/xOvuxdhPvw+I//zPuzcqvf/r0OVu8Pp/f5n9qmy2awF00ufmwzTYL0woTYPH7gk56c6xfZs6urYH7M//9OfM3SXmx+Mt878fnIu++2/z4+S0HKphzcD6//bQA/vz8VrXz9/dZSvHjT+9J3rvVjz/9Jqdurci1m1kY0Pr9y+v8JRYM/G1o6C2+nJXd9rVW5dph4QLhv7Nv/jxVf4l7ueTLc/CPefFh8X3Jsz1/Afo+E8wCcr8vFvgAzHx7j/Iw+/G1RpWDCJmZ7f7405+JtQPXjpOwbv4luT8/BQcgq4G3Xi756cMjfH9dLF+2fZP558sWIGH+HUvA8K/LfXPUn8l+RPbvRCdh5tbfYvldcd+bsPzL4uc/te2fTfiw8D6/MW4SdiDvrMT9tPj1kSI//+D8dvGHv/4NiP4fxZzztrIfEr6kZhZ6bt18+fLzD/Xj8g9//fmHtgBZ7Jrpl7ZKvifze359rPMHD75G/fjHuWB9LYuzvM8W32po8Wte/K/qb+8L3UxC57fr9afF7ytx/iwXsxFfF3264HfVWANdf+fHn97+BkAnA9a09uM2wI//+I+FFNpVXudeszjbedssQICbMHVn5S9BWC/Az4walQv8WofAsa9xIP/nCM8a597il/9jPyD8o/2CcOiJu1++IvOXb8j8y/viAgTmVeiHGUBdlVaUz5npg7vzYkXl1m7VAYCyxsb9COr44/wFIPvilz+V+eUx/b0Yf3kAb/hEOnW7n1GubhP3fbbnGrjZS3sb4Lg7uHYLJM/CkoUXAmSekb7Okw6g5Gx7HYdJsnBCgCMPTpllA/98moX98ssvllkHn7MnLGOLJ0XVEBjwTZ3Fx4/AHi8J/aD5nLl2kC9++PVvPyz+e/HPZj2Ez2sogBle3gcaHs5HeQGqqU3BMBAYEEoAFQ/v//q3l1eBmAxwKohV6IXuczLIxth1vrr4zNMfUYJcWC5wLXBrOrt0ZraweV/svcU3fV/MObNBANhw4biFmzluZo9AqgnM+ebJLG8WNUi52gME2NbuY9VfrMp8qJiCsjabXxbSVgHckyfgv1nNxyAwOc9C4P5vCfC8DoRUP9SLzVcR7wt5zr9FYVZmEVTmaw3PfMZl5vDXdCDcXGRu/zmb+dWdXfUohqd7wCDgGfsV0o9zzEGvAag7c+qvaz/GmDNDXh5MWX3O6leim9UcChsAP1jUb0Nnhv//eqVUHeRt4jz8BzSdJb2i4Lyi8shB+h87lVfvsHg2AIvPLQoj+OL/zy7nYSLHqTuOvuyYxU6+qMbT9XNLN4fo2QXOGsxKPcrst07kK9p8Bd3PWRKCPKrG/3qOfATsNeYJZG0FDFBp9SEfZAtw/Sz3kcxzclbVXAbm5+wrugOlFw8oA/EE7gSVMSfk1wXnu181DUB5z+e/Mf0j+JUzmw0SdlG0VgKSyXNdxzLtGGg1x+prAEFmu3Nx9kFoB3+wag4BiBmQvwBKhKDEAAO8f0Pc592vqv9h4rOhmac8mr0W1GP1EAD0cGcF54DMoQLqNc8OGtj56SEEmJEWzWy7BSoCWPq86FZu2YZ12Mzo9/SrWwDI/Tgfn5bOV92hAEUAnAVSvWiBdx/FMedKCtoVoAPAB1AraZgB+gZOeTnhIdBM50oHSPrqL58SH5dfBrmPipp55+vE2ZB5zkzlz7Q2s/H3gHD5XpoAeek84rHu32fat9Vm2TMo1gDYwIpf7z45//1J28++YPFV7qd/2KL8+O/tYh5ErP0xAT4tgqYp6k8Q9CTPr9z5DiAJeupav3j049fa//it9v8g8Gnrp8W/p9QfRLyK4tMCeYff4fmW+Eqq1wf4YPtxY3zE57ufM9X9DSnB8nkKsmqO2AiI+xutfR0CuM2vAPyAwU+aq2d27AEhP3AduP9z9vssn6sM0Ebmz1lZ57+r/ge/g4x/Rusb/YBbWQPWdub+z3fn7dajJmr37VPWJsmHNwCK7j/dZs3kks5JXM/bMlAuABeb0H2cWUCx2AFl+sUBSZrVz/7p17/bmTLf7j2S6tukerYUcIdZFECpOaU/LNx3/33mVLNqZpL6sJjV8fMZXUEPUgAZj2YLzAbMAbRrxmJW/7kxm1u5B0wNzT9qcXx8MZP3F0zXv8/9F0vNLP27En16HHjaBkZ/WDhAlXpmVeDx2R9zeZt1/LDqu7o8mOXLk1m+45aZiP5APnML8GQs039U9Msf2lliv7vAt6b2H6VfQXcxC3TyTzPRfngBHTiCjQhw69c9BTDrtct77MWzFmygf573M3PoH1PmL2AOOHyb9O2PD5b79tfv6fVAwy9zZj7z6++1k2eUAywwe/nvKBXoDNZ1WvtrNvxpqX9EYZT8CBMfUfx9SOrhuy56kvmXJ5n/oyLK77l+XvvZOoQTaGAc1zPbBBRVkz8UTed+D+TEzIJ/6BEWZgcS6oHJr26pmZmx+Y5CQKMHswB+nv38WwB/c2P+2CM+dE/M5vknjV/fQAmaIAHNVxG+NhlgOADij/XcakEAocCC4PyJJeDev779eE2sAxN0wWAmBcMIgWGkg5gusgY/hGM5lLMmyTWyslekRa1IE4wgTcqxKQpFEM/0Vohlwe4apWwbyHtC0Ze5kQxnZWZNgA8+AjRzf7sNLjkvK55azy76ttuZrX0ZA9CGxMFIHq/39POzhdYIuEhZ4+G2rEg3vxtbPdkFGorJ1njsWFRGUePMoBxHKH7M8vE2HQ+yBqu3g1HIjZDju5V6wPsLJXpHXWdXJmCA6ujeZaPf79P6mN3Km0hM5bVSVv1dwSNf9uG9kNzG0/nOpy7GulRmbJQGEkQJFlfGEoJ0eCXqmm2q3P5GW6q8w8LuFJI76uqkh/ZATpMTWvJ61w5aKek3DMOjrIOypRtXtUZM2r5KDrnP3st8OxwO+7sQtweGiKvmkNPhgU3Pdom628RVjCEROfzcKaJ+L9wwbHRrg1o7bJeGMMPuRmsUa9jN6HCdWOIJSpmekK5is1q7Cp9h1K5fuRDWUtpy6Yquvo/HC+23Yr4dUVOjqh3csXoaq5sk7bVot+7J1dZfNRK7jhAr2Fa6QSF8kW7MQRfl/sSMAWP7XYtd1vi41OhESt2x7Bh27IXdChkOIb/tt4OAJFVO90uBmURd2PWseksPaKxbIqx3PDFZpytUOsQ52fHncxDwl628X+djL61ExB22tW6Oqa8HB88PncsujLuzui9g0SRRoenRdXwMA5Kgrzi90V0mEnJ+jzV8OzEdb6OSqSfmvaDj8Ravd6l2Goll4p/UQ1XQ9zO8pfMwGZvR31sZI8krERK3TQULoa81qe+OybTUwrLZlnGmF/iYkhSqQVUsOgdmeeEuezXZX4P7fWtyy3MvOzGP1X4e4bv7rr6LxCW0xSjmPWXY7x2ZJqpGNZPNWr+ANDgEnbFldqmrKtNlydEsY0nyZgVCLKGBFm1habS0xq9OaLOjb9Wh0de6oDLFdTS1Kzqcq9aySdGTT6fuvs0U+Yab0XG4JoKeLxXkEC1JdtryCEkr1JXF90no9uGdOdXLydMMmV/XZta3TXxVSS+p2U7cwRI19dgJk/CpTG98UN6U0XRvsXMr0gxTBvM86YIeURle81CeQH7kQM3uHkMoDxXrY6bAKDTU3eZKpepKKOmI3ojFVBu7c1KKiEVn0eZ2NdnMqv0R5YbxRPccPjY4gpFoMHS+rBpJfYLKQ4wdWY5k7jsJLeWjGa1ldBRHOU5BwO7766mVdS1livOetzd1NdGCyRDOgVhj+4LPu4q+Ylt4ubsiLS8Hd5u/Xu6Jk1pGfbEHCudOu3TJY0PLXg4IV23M68XvxLPfMMe1IkTjHdqckiVxJ/hz6gw1uyLHzA09Rle5mDXzai1jvGtJ3v2whHx4i92mEN1GkteE5UHIAwGrk6mUOXvJ7SbWTtTcryDtXG+sMCbweyDIXateK44TLclXNdFo4K15628H7aRLyf50Z9p1f09NOOH1LBC33KpYoSNeb0YVZ+zT0UULufTC5cEeczlExMMl9uxj4qDX7QHF6RMKt2t9n/JoUIVw1aWn8/kw8n1WEBRGHIspMTd6yQ/8anWE7giu4Vpwo0ZMuuZ3wQqOKxVf0gMk1MNkOyeJ7469uhzp1RiIlq9ajBeiKeE7/NBXF8Hps45WC1PuTrcDe9eaULArrfWOTUIJGx/LQqc2aGGjMKubTgmjyzmctdZildV66MhhN/6Y6CUHT8dx4iTTpTsBCW1ieR6QG0fkWMLn1B1B1ugBO2V5h6nlKDHWbYNxMQIbJjPbFEhyo9/XdQ4Zjp2d5x5C5jY6k3OqBaO1I8UKdeRhnZnW5yutSo5o7RnX4Henje0nXMCWoXQBhuOYEbPk2ju6ViINqRQdaDY97aTmhPJECmvDRjhOl4vparbuWuerY3HMPpbElIYNwlbdazzRuQ83bb30Oy3VzpO8jUHQHaTT8LxXrW2HSTfMp+WjzDJjLVgxoxudTg42c2WsKzta2cXUFKRjyWvBXe2sjsa1klHw0lve+63X7tBoqQjNLvfzdRG3OMnypST2pWAcLW45rStcbuTpRJrkbsextwlbG/HKVUMnkNertQ55Xoc6zbmmRrM9pZyzFOVwS7M4ACqaavnYHdj8HJQVcs31hDmOltPvsEO8QddVvNNB/XNlPGLtJNCpAsdR2MV252dGyekuvdpcAmV772UqkfbXo1GwTBrHR/bkIWWswdZavcLG5m652kUhNMNIMlbi6wNdiNzZvDfCFhIm3lHdWquEqjBqucfi9bIJb8MFjwgyZ0uputQkY8BlfRQpm96U92rcBV4ZhWmm98qJ9BPsBBPF3g8GkQmZ256WsQajqxHnfSNQp/x8KM8rVRoBEhqRtJ9csV1aoRWywVZYennW5dWOTszd4B8YtsUvFGveUviW9mIxOlBOTd4pjP39Bm3LJSf4h9iXfGrgj/oJw4NIavD1uEoEvy33o5EP7LS7Eld63561rcspSSZdlhADmUGtnfcrYTPElno3jqcuF85Gx1cEuwwLO2TqPMbYgpSOsIafg4vkiecVKUj6tkjFankPPemE01ovqVe/0sOuSTOppM/8QAvXXS5dCzvlt5mR+Lg4dsNtI5adRRXpuVWZFUnGFwCqYjMZhg6JIXRM9bzki7bd1LDCllfhYhOp0XN7Js+OYLtWtzEl3lbAt86dcBTS2V3cSDhJW2rns06hS9bo6PnqgnP1BO1t+ZRcpDzHL4fg1m8UQFh+mOnWHobdNBZuuBLsqM3WGEuFDUQFjfYXUj6xB4Vfozcr3HOtABkJs3PZ4XScjOvheDiNAksuO3iMIE8tQWDctOUI1DK6zPetTSic7PFWZZ5OsGbBYeq22CUbM6tA35pVQeryLh5wGgWgKLwRE6Nd1L1l7035hEbXadgW8u4s4fGWFW60V8HaiRDuaca7Aaty+R45t0ERps2uljKKXppbodSDeKvI9rRJTpNqJ7wE0cS9M1OWxBLH32y5oOyz423vZCtmG+fJuSGYDZ43dmxUWBxxPui9Go6TLjRSJ8V+qCAfz1Ylc9uEd+KWUsd1JJQ7lTzQGi2KYRmHhRJHimGhOLPjb/qRA6m33HodtKRA48k7MclY+ykeXenWKBa23hNsfLxGFHNAhrE6B5sDBFKWlPYOEpQjcztWq9X9dIP1DAkOZz41gztduXqoSuetvB36VkI80FsZPoMZaQg83he2WtH9nb5bt6Sd+kqp2CVZcrtrJGSMJh8mdi9AqByt0K0Z76iU9m+ckKLIJsmFY1UbgObck40C2kG8lhFkPFhfkal0O5u76uWh9o9qheZtes85VF/tJW3YqYeUoffH0yEaDA2xS/jgSfIWYgdzJTtW30nVwKmnvm5QHa6P3DFeY6do6XZZ0BD1KFyL7Xq7L8UxzekDFdt2cy7SeC+VeXSA/Sg2EcFWLgOxPE4YiF7Vm9A6qhhoNEoDvRGVmR3upDZC19AqC8jRvdixtzqtxFcidzkIum20dN+LjUrsO59GLyJ00Y0d6cn6bnVVch0loCZmSpOWcUsXjvzdAj09tJNOyTju2WkjcOJOAjAFldPBR6Pc313F25Y7r3DfTip44BMaBXTdqD2d5hguyYGdG7ymQVYkhTeBVN1yw6mOtQOR6ouLXEYYM9GWpO/7qzitNeVMHmGP5G5tFkigSTcjJ8HMJWh8IXyqPePosLBt04cEw5fmyT+rZjlcU9R28jbuiI19QQd6jxZwXooJ32tUmqGjZ8Tn6qRdKZ3f1upAR3s/vAKGIV1F9I/LqLqrInfXTkMHMwktUSjcVwJZ+cip8SF/cxnlvXNeyuWmPFFCpGE3YWAYB41TvhhAP8ataDne31fmsj5wFQprFhbUTNB5TbtPp4Q52NsuKTvX5Y6ndB8iflusU8mrgxiPhVZwJBUmaBwr7/A5iS7T2bxix1WAuNhFqu1WBnRsebVcaOCX3EurCiNwdxmuxzvLxKftNIKWZ5qq6nqKcy7mIbh0JiGEVowscLlS0zwrJQWoWoZGiXwrkL18CvShvG60C8YR6RG7KcJ17e0bTtI6IxU3w+lM6VUymgBM76fjXhKPYj7dx0Jeshcm2VwtZQtP7r5G04KmyHh9cyPLdPRQ6H2/ri6Rud8sOdMUQlG5wSnKI6k/9OaxyssupiAaxrw+wXwEvo7jbZMyZ9Pl8tO+yhS2pssjlTNhEW1d346cg8NjkDrml6HZNugV0ECEibWBrXy7pQ8t7FHb2Mq4cyQV5FEBKarFUe6gbHPhB9WRuQCOOjWrGGO3q1mG664Ez99oktHo9OyuFfK2PbfL/eZwd+jlyAR51BwKxCb8DACAgg0Rmwf8KjQuzHapeFu8lzmBw/fjCr/LMerLIRciJ62oYaw5Tq2F2D3BcXuLhXBnX606ferD/AyFO90EPUWSZ+1gQTo+deV+m+dXsElY3vHpjkLdTRW4ASV3laXjoJe5FxU3kGrJOdF0x3b4yPlIhvVLZzk1pqOSnHJbDh69P6+UTW1YnGMqDm7glUCUF6LtruhVWZ+Vc7i8iWrWxLjHDXIlItW0lLaxT0GOq8AFVii3k0Z6GnJP1mR8xA+jTsQ3omMqc5OR5ChIJH41CD+h8JI9UxYzFufuxqeEObgTpFqX6mreShE6NaurU572bJlIVFFz+niUD5vodFJbAmfk1KeY0IDOUuUQmFEtk6hOjmfIiC81bjpO461EO9dQfbLXl9RT8lBaWiSlYYrVovVo0bCgcwxuLnt0JaGMpgrQ0CsmCkE81i05CJVyfA9JqIKtLhDa5VZ5VCk98G7+jVAb55RFTK61xIE/K0oUayyRsdw5gaTTSYdOa81zS7htVvGOb+R1U+wCKlXw7fbCb2jUlaH7IVsnOXYIUyS10k6Qw3hFWg2uXHvYMtBMFIeWEu2EiKJS6qSr5Uo7goAINMabAq71JnAzltn4Yp44POQeEQQhSGugWco+KRDOxZhjGDUckBeZpZJxc3JDvGEzSG2sNQzLFcZ2W7jlOguvzQBGDppdmcuzlhF36B40Sxr0WHnCxfSwjy8DvtzDmFV3x0hYHkJ3O5aW5hr2TSvO8r2+Ote2upu37MyatUGwekD66wKdpCj16r70VvTIBxle3uP1erBCBoigTskQqegQB2HH7DMWlyJYxtQzR1yJzZ5zAd8pmDc3sQf3jLj3spcl/sRxuxWqyif9GJ3YBo/Zpl/7B2zUJtB3o9mZ6NfpqTeXK/l+b6/I8QglWztjBojs0uVydzA7lj04SuYdMBnfEavCZSiu5G+Z1Hv9lcFbtLwwkGM4I21dnbSpBnZNXgB9T0verI7euSBdYitKKmIeNRtJgIXK6RpShap37uWYJj1fC6s0T5PuYsLkoarybXohV+bKuKCXg326e1dfrhknX3GUvUvulu95isPWF2RNFbiFj9lKkQUcdqZGoTPZNeUotw+IdjFDR7rcDSWPUtuP3GRkNtoRkpOjWOQcXyF17QH/bFRaO2Ox6yK8LW3HDbTOkKMebfMQh3ifib0ibItkV6dKU4IeEpkYPmXMAGocFATo2ikoJY6mXi03jluvHLi5AvRhlOP6aN2UFj5p6WBP1RTqiOKn/i2wPRrasPpNWi5xf6pLyy3XjYO3hDVC920r0HV2JTGN4KNmmQypvXKk4urDLLSh+uBi0AiepgXlWQU6WNmtrMq9BlZvXLlVTbdTzp4Tr4v1qjHklSATiVgPq2WywVLNF+OQiIQ+Oyu3rRt1YRvveqE7Nnx261KEXy2XGqvX27SK8hQjhlPBx2J+6rZLQ8/KDcPxq1gDSbsqBoETsmOMBOGdW8OAPWI9JO8YsWH5vlgn9c2QcUoOYRQO23UJWueaHtejX0cI49wjiV8hOsXciimgTNrZ2NNhFI/9PnBU32/Rrj8h2J3PpyYIpWlsiCn3mAillrtUXh6aHNuLmCQwiGUiLXWmNnIj9naxXJv7Fb+RjFLFPf2IVZdLdJMJ03QU7iZgU7I6lcWV65EIrm1U9fiiuRuzOpIVdflV9bFmXdQADaLEu4f61GlyY56FdoV3zOmyE3KikKLSBFEfsdSLUpUQ3VvFGnCxyvxtiShbg6XINB5xTLuQRru7HqwjpcPCpc+ovieas9IfO9FITKRrbApDIR1mVqUNO+tIM9dQlED6qthQSzKnLWUQx3pEmj25nzbb6uAIoLg4T2KEnL9aductkTVqkwS5hWzyaEVrwM7NDmfapG4pQiORqFu3tysGNuumLt0VkayTtPaYhiQLJpNa3Alv64OzZsK0CDOLU82WU9MwqHLjmrjWCl+TZ5QKun0kM/BIOsbavHVKO0LwrhudA8XRprCbUos/N9x0wRoxXrr4weJt13f7k2TXdUsXrN9dpbA8LCtsxOkjr0Yr4SA2KY5Zq+kOh1EEj8ZSu1aDfMetqSlapO/ygRCObt4GZMKuuDJya3sP6QjvXbKpyVSkFQK0BIztDEwHI1Sws+92B60StyrD0UMVejJqozvV7mBjFC3M0a9uTp0kp1pXEet0RdAM5acEXpO2rzd8cPTGOnU7rUTiaiXJvoWxRuuguFw5g7Tqwe5gmRpXbJLu7R7yKCy7XCQ+y6/d3Y1JT7R0i7lR/hojb/iNH70+NW1AtYxWZUNZ9GlKhwe8zHNfgcmOVC4+KBWHd1emed5lUau4ibTmYO6+vcYNu4FsZYzd88gXMBXqmLiFSvjYdBNjqFSzhUgEtLR9vR4iD4vYzsET0hxwRRDv5yOShWt3yGw2Ejsf24rXMdFUrZ/oohhNMcqR6IaFFGDpzof3vOcLOwKi6GENn+96nQxm4e083yCPN4M2lj3ulL7mctPKYSD81vl+jxPJlqbpv7x9ePvtmdzb//ze2PyY5v/ZE6Hng52vL408njK6pvPpsdanf0GXv354q+wQaPJ8zlUnrf96cPR3T7k+/ukTw3na+Hz56utj4udT8Mb05/eP38LMaesGrFrnyeMlETDDauv5xcV6frfVBsffPxh9rjS7Na9c26ybL03+5fW0NMzmNz9cJwQqvE7918O+D2/O622kLxhJfHGrYrbu9aoBMAp7h9+xt7/9Xz2xxusdLgAA -->
