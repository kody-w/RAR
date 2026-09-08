---
name: "rar-cowork-cookbook-report-define-environment-strategy"
description: "Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_environment_strategy", "rar_sha256": "9c85f68c134374ed6850054f006b044c118b4c6c1c640e496727fdda65338efe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Summary Report — Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
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
      "description": "Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 9c85f68c134374ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_environment_strategy_agent.py` first:

```bash
python3 report_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_environment_strategy_agent.py   # or on stdin
python3 report_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Summary Report — Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_environment_strategy',
    "version": '3.0.3',
    "display_name": 'Define environment strategy Summary Report',
    "description": 'Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7af29d2e0c7b88e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define environment strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define environment strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-environment-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define environment strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define environment strategy activity from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a define environment strategy summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of define environment strategy with totals, by-dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineEnvironmentStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineEnvironmentStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-environment-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObSLrmX9GcGzFVdWUfdpB8oyMGsWpBSOxQ7nCxCRD7KlBN/fdJpHNsV7e7+/bEfBrZVRKQ+ea7Ps+bTn5/cfsuLpuXTy9q6BYLwc2yJA6bhVsEC6a8lU0KvsrUA/8t/LLomsTru7JpXz68BGHrN0nVJWUBpm/6JAvahbtoQjf4WBbZtGj7PHebCdypyqZblJdFEF6SIlyExZA0ZZGHRbdou8btwmhauH6XDEk3LS5NmS/YqXDzxG8XGEks+P+pMtLiUgK1FlEyhMUiCyM3A3K6ecKsa1W2XQi+wiYpgw+PW2XfVX0HVCoW3OiH2WK25mHILenihfrU7sOCDTs3yZ5ztLJC4EUbh2HXvgIbw9HNqyxsXz79+tcPLwn4/fLp9xc/c1tw60V5GMY+jOK+2aS+mQTmZ24RgYHVBJxcgGugHzAjB7eAKxZvVz+3YXb5sPjP/0xvbhO1v3z6XCzePp9f5j9KXyy6OFx0pfuw0ncr10syYPvrgs5u7tQCH3d9U8z+Bw5Niuj1OfObpLJa/GV+9vNzkdco7H7+/FICFdw5gp9fflkA/35+afr59+sspfr5l9esvIXNz798k9P23jX0u1kY0Pr1y9v1m1gw8NvQ5LL4op445m2tJvSTKgTCv7Nv/jxVfxP35pIvz8E/l9WHxY8lz/b8Bej7zEIPyP2xWOADMPPl9Vomxc9vazQlyCG38MOff/lHYv049NMsabv/ltxfn4JjkPrAW28u+eXDI3x/XSzfbPsq8x8vW4GE+XcsAcPfl/vqqH8k+xHZvxGdgcxtv8byh+J+NGH5l8Wv/9C2fzbhw+Ly+YUNM1DEjetl4afF748U+fWn4NvNn/76BxD9L8WoZd/4DwlfcrdILmHbffny60/t4/ZPf/31p74CWRy6+Ze+yX4k80d+fazzJw++jfr5z3PB+nqRFuWtWHytocXvZfU/mj9eF4abJcG3++2nxfeVOH+Wi9mI90WfLviuGlug63d+/OXlDwA+BbCm9x+PAX78x38spMRvyra8dAvVB2C3AAHukjycldfipF2AvzNqNCHwa5sAx76NA/k/R3jWGGDyb//Lf+D8R/8N56EnXn95gvWX78D6yztY//a60IDkskmipABArNCn0+fCjWZAB6tWTdiGzQCQypu68CMo6I/zj0VSLH7718K/POS8VtNvD0hOntinMNsZ99o+C19nC80Y0MDTHh8gfDiGfg+WyEof6HNJAGZ/AJa3ZTYA3Jy90aZJli2CBCALILAnawCPfZqF/fbbb57bxp+LJ1BjiyeztRAY8FWdxcePwLBLlkRx97kI/bhc/PT7Hz8t/vfin816CJ/XOAHOeIsH0HCnyscFqK9+Nh2ECgQXgMcjHr//8eZeIKYAVAyil1yS8DkZ5GcaBu++VkX6I0qQCy8EPgb+zWffAvRfJN3rYntZfNX3jYNnfogBUwIirsIiCAt/AlJdYM5XTxYl4GSQhO0FUGPfho9Vf/Ma96FiDgrd7X5bSMwJsFGZgf/Naj4GgcllkQD3f82E530gpPmpXWzeRbwujnNGLiq3cau4cd/WuLjPuMws/zYdCHcXRXj7XMzMG86uepTH0z1gEPCM/xbSj3PMQYsCSL0I2ve1H2PcmTO1B3c2n4v2LfXdZg6FD6gALBr1STATwn+9pVQbl30WPPwHNJ0lvUUheIvKIwfZf9LOvLUXi2ePsPjcozCCL/4/7JJmR9CCoHACrXHsgjtqiv0M0Nwvzso/W8yH0mXzLMZvHcw7Sr2D9eciS0C2NdN/PUc+wvo25gmAfQNMUGjlIR/kFAjQLPeR8nMKN81cLO7n4p0VgNKLBwSCqAN8APUzp+37gvPTd01jAALz9bcO4ZEiTTCbDdJ6UfVeBlLuEoaB5/op0GoO5Ht0Qf6HcwBvceLHf7JqDgKIMZC/AEokwN+AOV6/IvXz6bvqf5r4bITmKY8msQdV2zwEAD3CWcE5IHOogHrdsz0Hdn56CAFm5FU32+6BugGWPm+GTVj3SZt0M0Y+/RpWAKE/zt9PS+e74ViBUgnfU+T1WUIzuuSgzQE6gEQFFZUnBaB94JQ3JzwEuvmMBwBv3/rSp8TH7TeDwkfdzXz1PnE2ZJ4ztwDP9HaL6XvY0H6UJkBePo94rPu3mfZ1tVn2DJ0tgD+w4vvTZ6/w+qT7Zz+xeJf76e/2Pz//e1ukB4Hrf06AT4u466r2EwQ9Sfedc18BcEFPXds3/v34hIGP38HAx3cY+JPkp9GfFv+edn8S8VYdnxbIK/wKz48Ob9n19gHOYD5u7I/4/PRzoYTfgBUsX+YgvebQTYDwv7Lg+xBAhVEDkAgMfrJiO5PpDfD3gwZAHD4X36f7XG6AZYpoTs+2/A4GHu0ASP1n2L6yFXhUdGDtYG4go3Detz2Kow1fPhV9ln14ASgZ/rf2azMn5XNWt/M+D9QPgMouCR9XHlAwDUDdfglA1hbtsxH7/W/2wezXZ48s+zqpnS0GlONWFVDu2fsCFnabblbhAzAGqFDOSAu6lgpMfzRsYCLgGqBYN1WzBc/N3dwOPiBr7P5eAfnxw81e3yC7/b4O3nht5vXvyvXpdOBsH9j7YREAVdqZh4HTZ1fMpe626cOgH+ry4JkvT575gUdmcvoTFc1Nw5Pt3OhR3R8W4Wv0utBVif/hAl8b47+XboJ+ZBYYlJ9mav7wBnrgG2xmgFvf9yXArLed4mNfX/RgE/7rvCeao/6YMv8Ac8DX10lf/5XDC1/++iO9Hsj4ZU7OZ4r9rXZ/Q6nzoDdb/3WRf0RhlPwIEx9R/HXM2vGHnnlS+d8vfPqe6Wf/PBqd/5p7C7fPQA115SP0+dwNgvjP7Pen7mDhDiB55jz9wbpg4QeHACaevfgtPN+cVD52kQ8VM7d7/qPH7y+gtlyQXu5bdb1tQ8BwALkf27n1ggAEgQXB9RMswLP/iw3Km4Q2dkF7DESs/RVxIVc+guEYhYcBuSJgmMAvMEx6MI77CLLycJ/0EZ/E4RBfkxRKXYLAJQkMW4EeEMh7gs6XucNMZq1mlYAzPgLc+u4xuBW8mfNUf/bV1/3QbPabVQBPSByMFPF2Sz8/DLRGPAinvLGxlha8Gh2ba2rHLLtASofLDuGsDvOUZMutTk1HJ2iUTsoWz5ykPd4mHj4kN4vkRIw5pTnko66wTbJ9j3lX7OoKkWNtc+1Y3EtogHaJQmD5WqJySZ+yNIyxYt9h227DkNP2yDSNl5Td2EbFrcHaSiJsCx/X0PJQkZav7CrOjv1Nx9uVn5ku29ZH8qTrqSK6tBNzBiSOht36lK446xZGJTXms/Vq7Rr4SltZFQnxeq9HA14Pjlqq/blUYSYrz9VG2GYymZ6i6wqJ+S1GplOybRiK0ZNBOpX6nbv69cCnVZA4PW4e2vVVUp3DdotL1imsw7uSBJtmfx66NdacrIZYhRA1od5wlzBxiXk9doKaBDPqvb7X+VYh9dFosju7s/drd+Rz4byxW7w0L7iRb265KYhSd4XTIlFsCi6cnp60+uxFEZ+ZuzOxFCGKYlCNnZi8kAohVtchrzI+QYmcU9TedotaehxEJn8/WJK/xzM25k3bqrNaxq7lEsH5EIb81iA2Qbq11X2UGWInmCEWh4dqi/McYAFYP1slV8AJ3xwN48yPCtbiFBuYErQT7yXfnHlhG8UOZmrnXBtc8ZIXoUxIZ7gZiTxltJ1zTVVHuR4K0txsuLxPN9nufJiS/Ykn9Y1m447SRBdCMjo543VJs8siLX0ouwthj6dilRJqfl+ZW6pqlivFKssTep52G2l0Iv5Yp7Tle6WaT3RyyRk/9m+YrzRX308oBz1sNnF5SiPVP8NhRWXGiTLsVDiWe4lRCG7gTzgu8UdpQsW94q20SVRb8TxW8RmdKtqFJTaUctQy9IYL01Srl7DJ9C3REbURunEsT3wvM6dbJgRJduSNcgVN1XWJcwdGREhmwKLjTTnx65iehNFdTYN+Porr0i1uNZKaChlmKTccOFii7mfKdATOQ8bDdYWerlQve4O9vAyBv8tvyGn0vbuxN2Ix31YiVGZQdL1czLyfoInZwpB4F1cBdJOG0KRy1d8v6YbmD/UNbRNNRflzTxvVVTRdrvDaaGXukamkYQGfjmh5QloGg2h3GverHjI8p1/ts5tI2rWku73bro/oJJHHLqcT1y3pC5YYfBaRdE1le/Sq0JCHEsWpIAaZCJmqD6nzTsODJt+mGG/goXPMbdTJonFNbQc6SNXm3l1QCZYwt27D2hYwS3KXtS1jFnw4p426P0wbXSNiqw1HrTpEPeYfLuKN5DdKyrlwNtSDxJN4oVT3KkWWBSdQS928wVW8Rm1IqyVl2WFyx7XeBkqvME+agnZQQ/pGsNDeKDZxUekokR2GauMcNhIxHJm7YQlIehvwSrlpqTNSlxZoga0nrprYtJAdh0Icwu1SWe1XCdI1rFvYw1BINUsfp3UyOa0o5vc9z0E+LXmVJZTT+dhcmsNe0pitVDECs9EwbEjEe5HcGNG+CMT9Rq0Pl0RTLPZyEsNNExO8dAL94+UmQXFQ9FbkXaH6xsqX9ggxzISOrBmP933EE+JNZLM4Pm29Q2z4EevoXh61k7WtCF3BB2a9JnfXFsnZMHTbKaIjfHUhQstvFMpZeSd8FW3rXuigCzLe+85FOmls25smFBFX9r1WiPdcTjLrKK+XmEz6l2FZs7eVVJwH3d6mynAlt9wt6Aj5SA+9tIbtxPIdH90OTtk2mDfE7dHfOeutjHgcVgWHSD/IGmzcsZVucmdpzTZb1tuKus3q8VZIssaXNM2Ntle3Q0goXKoe2+K5wu42uuAXcKcjg9KjUtxs7buluHt9MhgZ7txJPinc1pakaeTwfNXRqaDsGjtwILropDI1bX570DiqCwH2nRWPacXVFY6iUTp2R3RwrZ5H/JZ3kZSlENukErdg1d4+bPZIzjOqBBUoEhZEMF4KtiZvGsnuK4TLhNS6nV2jbuEwvt3qa0lHudfcofTmJVhgteU2LRx+c9msBhEa23WWXGIEbyEo45dOiO21YVtHsuuItxrdSrTjcN2SRYlws83NeN+MfpyLznkLFzLB+vQWMS42sUECbaXAk0fdnYy2BJLNRiuRrZuxvgqZt1kr8e2kuvixF+htK60MZJMW02F3iBMJJDh6MzemAHcbAmLPqnffcXmxQiQ7OWlFPrJH85AVNiaZR6g5g8b0frCrXsnXemLK1t00mJY0dOx8W224mNXSHbpMKpk7FhePJbm+C7P7asOvE+GyCZcODoA03ogdgZK+dB7T+AxV98NGO2rnKkZZso+pXpG5bbJriKXWk1fpLBvDVZDSvdRxjRvtWfN0L48ZHt6xDhnNLac36clpAz6sjEjbHgghTzbB2IAGgdlLd2tY35PzXpgqXSGvsCWMfralS8eFa7ySLV3hitWApOLmsq9uqbjbJ/aJZvh1NN5FfB1svRbIPyuZUOPdyUlW557d45HiULChKA2ncoQva77CMzzNTruYgUdPOKK9IfHNRvcEuvKVSEkLvMk24bSl1SPFRbLgIOgd0dg4YS53BC0TfsKDWqD0KiwEcn3N8xLsG3yFrULW7vVNgCHhFT4Xl52vr3MnqhmzPkc4k5jDfVkoEtao6Z3ux61n7ZNSWzpwbSVRRIGms1zuYjW1lf5WaEy1iTBhu4wh4crEiR1W6RQ5or0VGOV8RjB7mV7YC19tuFJYNicITjGOPvlKfj8IOH7gm9IfuaZjGNdSjohfoyUx7JJ7BLIhzFHQuFb5DVc5RjZ8B1u3Qs0dbJtdw2OSlncVCovdOgxzkIdYy+y0QdAC8WzRJ6XzlwGzqRGjErrUFFTmaDobjq+dlLmcyuo4qWNnMqtET3i7xHBas8Q1e3WIYRX4+gYzWWybxjQJe3IiJNjedE/sXVORlUYNdZrQ6Y01NvlqWLMbUqg2RsJfU6noIyQxokFWJZdAoQuAYhtlS8LTtetw9x1arRx/vy+Q0GknUqt5htlsmWTjqIburQ+rSCGYEGLswsUrfu3cMEJbQxDqMGnHGDnKUistFYkTtj55lLGjslLW7xdpm4HOJVsl54sjlPrScg5rL02XQ3BXMvZk26cDb2xVveZz7HxOVabjd4CMD6WJOzxmnzdFevMdLj0b0pKpmUzltdvp4KY9ejGCNW6t9Rudok5LevHuoCL7i72LIn08jVvQxlIRf23Y9S4mFSIqfdQLnTiEx1Pgn+lw5626sxWuTluLa3SnjUje6vbICd8ynLS1BSVhEoeT6WNUane3r6jNpd4vQzPreQbVbRJTWM+qd/gGpxyaRTwfHssd6a5XKx90cmMgIPuJld18f96C1l2uKhrdrkgIv4HuYLUCG6SVn1s46FNW7CpdRvIAkhNwBppbbaT5k7Dvh9vONkM64AZtuzzlfbKpOM7GkgK0fZwsVxv1YjfO3e32932oHkdN2Yeau61jBmKrvdpBqYpEXpNxHAe71JUVGITlYhoF7Tsv+lyDHgn7XtfORhSFeNquhYyDVNAK5serEWuXnl/uokPM+SVP8kaqrkmRLlqyzP1DwEiTLJw729oTU74ZAoiFyNLu8VE6KOHcd6k9Z9L5Jdl7GC4HbXw7l0uROvO0ujUEGUGvY7OGUWx7ki5o6NCrndAdmMtqs45Kxjk3MlozvLCjJ/yAKlEqk3hsKbQyrnzzdIXB/u+M8YPesNX2Vg4bvxRbNgmyKTZiNNmU15uMbBi1d86MAmG2kJ7grZuLo7uFrr2R6H6RMSt7gNnkpue3Azqd0X45rLVVuLmUJ8+vdxJsOAfbIsJDkVnXcZdEnXuoMac9UCdHbpiGKRzOD8+HDX6n4UpFzNpQZVxIzyRWt9No6WjimB10njL1toJLFxuHYUg88oDskpus0PF5T7PiKUxaZydc3Xsv69xIIUJBMIIpRWKYHCdtr6bngh4T4uwjMOtL190y0ze3M9J22R0rxAMiO4eDeuAh2xSiEeEPx5DjjFKphf5G08SU6QjG7KYwr7JrVrf3SD3WpSJQSZhfDPI4xAcVtu6K73sELd2QWCEcg4QEEwpTxF9zyGhZprKkIPNwPcSBziLr6h5p1H45yL5p2oRwlT0zsSwmvuPx0VKRzVQG1mF3GZmsuyna5mDz0PlKRWm5EdxWNHx7QA9js3dvg+fs+WYyVivJ4puukqOm1SGDaspQjiV9udruzowg9Rl8ROszjKUbP43JC1yKxfoGs1PSbWRc3BsXt1aaC7G9HnqSJX2LKPDBGlNZYdSkTwxa4HH9JO5JjT3WQ4EIiHsChnoCn0IbkxlU3DrBnOkTycpw/Yrnm2K82txhc030S3wWVxIs+rddoRUH0P5VpL+rXW/TqF0sR8uAKAWWFGu5ttHNqfetftyfjBA6EKDDu1cGD5ovzeMhhDLlAWMHHfHiLmAxPzc7LjwaS+x+BbtikrTuTnhft2CLZzqN3SNBOFJWamnGmQ3lhGwwhJ+iLULx/WAIy0kqb45B2Dp1YDP3Ct1d3A/gM3wn4mp9Mxqx8y8yznSl7BkpRqkrFb5mZs2mJ4srljEfq6WSV/vxzlwxkzu5SbJFRT1oOdHz7xvizFf9qTEusG8lVm4tl+djshk7Y3WhHAlnUbzwAyxXTpUqLUOX1FHR89B2osSLqgssbi8jhJamqxaDDdodcnsIErFhKUCm1KbbpYRY0KqBukuE4naAEsKyj4opc6mNvBUPWTCqldbcKD5OM4Uosou2ETnttgPFWQaX2q7aCCKUKba5mMpPOM2ogHKS8Agpu2KdReguMg8rTCIdcn/39W5FeVbYJVsVHXrsGK9BoJu7KNg735ME2I4paK3uTOKYUaVxRQPMYVja2BTryeyHHtL83ZaS2nuH0/CSqu/H1L+o5+rE1Qrc3Az+Lve1MoTLMPfD4ljlyAh7TKHBZlZi2A6+VKPZNqd6XN5ZBRoV0lPo3Xazd7YiS0H3OMec/MIhksLZx8Yyt+4E2lA93UOepHaBOVHHdelUoxaZplUvUVGTp15Z3qd+OV45X7jkVa5RqLM8oLglVgwm7MSGUXpCidR2TW5IEyp91q79W8qIpmxbBdhuId1+7spR/ubYcrkViVFh61vl07jkbuSTG4MeZYjyvBK5MsRaGg1EtznAWLZxXT1dQ2ZH+MMBb0OIIiI5Xk87QWuHYl8VXr5kUlRuI+OqX9l7bmOgD0OutkE0UK8zhN8Vx5MMUWo4eqqrIJf0aory1Qosu3Z6Gu0KSXYTIlewfDSPq6auul1YVL0o7df5mEcDJ2Ho3bOsTMo6G2yMinqr4tHUm7dTe1fylUC5HGJ40Q052UirZgFVU6CmCu943NvUcJeubNG59jEAnTNiay5j7DXCQcqgvviamk7s0ZKDTS4f4l6wGqyVREk881oM763cNTGxBe2uAq0K3g3ZBDAaehhE/eLwa7U+EnTgSURqeDl3kmQs0NR1exHW7mo89N2uMgd8hwQ7krKnzl3nQkjBa9ACUsromnYeBFSwxghRYgPuyK/ugekPdyoO9mgFIMfMqCuoGHltTHi5IYPDKlPXSwEhLQnSrEPpHewtD23x2yZw6QpuPHOdIPl6HxiNeRJ4kzSug3wFONqFUhoiKpV1JKmK+O2KHTD7ji+nQyuNtF5lBI9s9plsCmvRYv2tkutLgJb9+S7vIWpa3ejGNjhUJHatllyVQQgn1hepSlBrbnX2p9ixSYg0udIv/TrseCL1MBg1wtE9jCer4KLLpjDdMWihJEVFRXLYoIk9n2ql23Hf9Vdje9lB+5BIGhgZvFAMIhrm7/sCrwhaPQHIl3ET4tmhOx+v65WsCKY1tAaLr0L4tK89rMzh66rt/VspG12jU5mFplSoR06wcrmQkM/lTfeWUN3V+nTvzS7TnO5+1AGnoJ0el4K7xlgpvaCEJzjHs2dopo1TfGnL3tVygtqvEOq2M+wJwQbgrN2YI1B/LTNFOBqpf2XXTWgu7/4ZOxEsHJQNnw44TBtqRahcFUqrLNxpury3Q07YeTJlwHvtVlC3G9GdTzd5ONiZiwydTmEoZMCbVe3D/pKs9zA0ekEd+sn6YnD0ccAJJ7RdIwo4p7waXJ+vJ1q4SOy+LIzBH6Blth59Eq6Zy7QWj2PWnXtzAnwwdj1F6CTG9ktxd6CIfNnWqSRmIK0o87Tc4r17plKxZm0DO4snPS93foXGpdEopVtyBoQ2bndc6v2a1oK71Wr5ZvKCPvK7Bkt5IhcYjNimxyt95BlHOzaNqTiliGaTdfKFjs1PZ/q2FfpQX9IVHw26lNS7ZSyOPi0eyjE8OKcuxzFvdYvhhL3ak76U82Y8Ojf33lU9civKmNjLYdnHZMavxP01bFd7yMi4y46iYFDlWCY6hgNhMq5hpItMdi8tLQi9DToI9HAXI6I2D/dIP+G9w9LHoyw2StND57oK96Wb1QeTsNa78tJD8S31PYVir+uGuDaI29l7sEm08yVietewv5uYx56k/cqAtPbgETmHcZchpAZNkwqwjS2cMCLDxtM81qCGEAoO/eE6nnD9KCtbelMbdxKBQXNEK9zK0M1zQUaefEVwn+etkeoEs012OEXfCU9Sul1+RrKDgrUyuyq5tI3JQF6lwVQOKCnqmFO12245XAIVMlNbD/Gqo8Ya6X31crzBYsbsTfZoUIVVNOIZ2M0JBJpxO2Nkz9eSyUWw5133vROvLj5EE2uSoHF/DPMC7mjL03YygcnN8YQTpMws8xvBYiTPdcFGw0mIxa6gXd84lkMTLE3Tf3n58PLt2O3l33irbD6r+X92LPQ83Xl/WeRxohi6wafHWp/+HaX++uGl8ROg0vP4q8366O0Y6W8Ovz7+64PDef70fFnr/ZD4eQzeudH8JvNLUgQ9GDx9acvs8boImOH17fzqYzu/HeuD7++PRZ9Lgh9u8HzbI2y+dOWX57HffPiVFPOLIGGQfLuM3k4EP7wEby8pfcFI4kvYVLOtby8cABOxV/gVe/nj/wCCghoziS4AAA== -->
