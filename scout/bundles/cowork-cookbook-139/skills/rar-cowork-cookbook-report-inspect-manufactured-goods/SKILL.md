---
name: "rar-cowork-cookbook-report-inspect-manufactured-goods"
description: "Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_inspect_manufactured_goods", "rar_sha256": "96a7b8e41fc94bc752b64234e69dd1017d501e502ad7fefcb41e5a419b02e1ac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_inspect_manufactured_goods`. The original RAPP
agent is preserved byte-for-byte in `report_inspect_manufactured_goods_agent.py` and in the RCI capsule.

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

Inspect manufactured goods Summary Report — Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (recipe default: USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-inspect-manufactured-goods-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_inspect_manufactured_goods_agent.py` and embedded as the fenced Python below (sha256 96a7b8e41fc94bc7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_inspect_manufactured_goods_agent.py` first:

```bash
python3 report_inspect_manufactured_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_inspect_manufactured_goods_agent.py   # or on stdin
python3 report_inspect_manufactured_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect manufactured goods Summary Report — Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-inspect-manufactured-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_inspect_manufactured_goods',
    "version": '3.0.3',
    "display_name": 'Inspect manufactured goods Summary Report',
    "description": 'Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-inspect-manufactured-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-inspect-manufactured-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e1516b3600be73d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/inspect-manufactured-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-inspect-manufactured-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (recipe default: USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-inspect-manufactured-goods-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where inspect manufactured goods stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of inspect manufactured goods for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-inspect-manufactured-goods-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads inspect manufactured goods records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet', 'example_request': 'Build the inspect manufactured goods summary report for USMF as an Excel workbook with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'D365 legal entity to report on (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-inspect-manufactured-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of inspect manufactured goods activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportInspectManufacturedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportInspectManufacturedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-inspect-manufactured-goods-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportInspectManufacturedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
