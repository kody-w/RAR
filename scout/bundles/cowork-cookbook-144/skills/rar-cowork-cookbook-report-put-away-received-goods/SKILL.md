---
name: "rar-cowork-cookbook-report-put-away-received-goods"
description: "Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_put_away_received_goods", "rar_sha256": "0d50bab438a0b828ec2d5eb92e3684cb812630ec183d3db4d7fd5123c0130425", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_put_away_received_goods`. The original RAPP
agent is preserved byte-for-byte in `report_put_away_received_goods_agent.py` and in the RCI capsule.

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

Put away received goods Summary Report — Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-put-away-received-goods
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-put-away-received-goods-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 0d50bab438a0b828…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_put_away_received_goods_agent.py` first:

```bash
python3 report_put_away_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_put_away_received_goods_agent.py   # or on stdin
python3 report_put_away_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Put away received goods Summary Report — Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-put-away-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_put_away_received_goods',
    "version": '3.0.3',
    "display_name": 'Put away received goods Summary Report',
    "description": 'Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-put-away-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-put-away-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c51fabfe5e2fbfe7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/put-away-received-goods'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-put-away-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-put-away-received-goods-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where put away received goods stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of put away received goods for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-put-away-received-goods-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads put away received goods records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a put away received goods summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-put-away-received-goods-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a put away received goods summary with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPutAwayReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPutAwayReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-put-away-received-goods-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPutAwayReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
