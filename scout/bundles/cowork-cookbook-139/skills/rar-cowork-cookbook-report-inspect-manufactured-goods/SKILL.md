---
name: "rar-cowork-cookbook-report-inspect-manufactured-goods"
description: "Builds a read-only summary report of inspect manufactured goods activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_inspect_manufactured_goods", "rar_sha256": "96a7b8e41fc94bc752b64234e69dd1017d501e502ad7fefcb41e5a419b02e1ac", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
