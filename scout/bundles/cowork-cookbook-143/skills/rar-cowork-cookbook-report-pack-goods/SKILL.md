---
name: "rar-cowork-cookbook-report-pack-goods"
description: "Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pack_goods", "rar_sha256": "66f6c90ab778047775c548fa90c47e56844a1d8442127153346a5f8730c3dd89", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_pack_goods`. The original RAPP
agent is preserved byte-for-byte in `report_pack_goods_agent.py` and in the RCI capsule.

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

Pack goods Summary Report — Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-pack-goods
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
      "description": "Excel workbook name, e.g. report-pack-goods-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pack_goods_agent.py` and embedded as the fenced Python below (sha256 66f6c90ab7780477…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pack_goods_agent.py` first:

```bash
python3 report_pack_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_pack_goods_agent.py   # or on stdin
python3 report_pack_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pack goods Summary Report — Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-pack-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_pack_goods',
    "version": '3.0.3',
    "display_name": 'Pack goods Summary Report',
    "description": 'Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-pack-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-pack-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3948d852fa6e94d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pack-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-pack-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-pack-goods-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where pack goods stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of pack goods for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-pack-goods-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pack goods records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a pack goods summary report for USMF for the latest posted period as an Excel file with Summary, Detail, and Top10 sheets.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-pack-goods-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a pack goods summary report with totals, by-dimension breakdowns, and a top 10 by value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPackGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPackGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-pack-goods-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPackGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
