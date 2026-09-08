---
name: "rar-cowork-cookbook-report-pack-goods"
description: "Builds a read-only pack goods summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pack_goods", "rar_sha256": "66f6c90ab778047775c548fa90c47e56844a1d8442127153346a5f8730c3dd89", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abObWLblX1HfF9GZ+WRf5kF+URGNQCAQIIEQAtIVTmYxIwYBys7/3gdJdmZWuup1RfSXlu2rK3HOPntca2/Dr29u312q5u3T2zF0y4Xg5nlyCZuFWwYLthqqJgNvVeaBfwu/Krsm8fquatq3D29B2PpNUndJVYLt6z7Jg3bhLprQDT5WZT4tatfPFnFVga/bvijcZgIX66rpFlFTFQtuKt0i8dsFRhIL/n8eWWURVeDkRZzcwnKRh7GbL8KyS7rpoU5dtV0I3sImqYIPQFTXN2VSxuDiYjP6Yb6Y1X1oOiTdZXF8nvlhwYWdm+QfHkKMql4g8MKbFjc378NFewnDrn0H5oSjW9R52L59+vnvH94S8Pvbp1/f/NxtwVdv+kPxA7BImA0C63O3jMGFegL+K8FnoBdQvwBfBWG0eH36sQ3z6MPiP/8zG9wmbn/69LlcvF6f3+Y/el8uuku46Cr3YZ3v1q6X5MDm9wWTD+7UvgydXdsC95fx+3Pn75KASX+br/34POQ9DrsfP79VQAV3Ds7nt58WwK+f35p+/v19llL/+NN7Xg1h8+NPv8tpey8N/W4WBrR+//L6/BILFv6+NIkWX46HDfs6qwn9pA6B8D/YN7+eqr/EvVzy5bn4x6r+sPi+5NmevwF9nwnmAbnfFwt8AHa+vadVUv74OqOpQO64pR/++NM/E+tfQj/Lk7b7v5L781PwBWQ18NbLJT99eITv74vly7ZvMv/5sTVImH/HErD863HfHPXPZD8i+w+i86QM22+x/K64721Y/m3x8z+17V9t+LCIPr9xYQ6Kt3G9PPy0+PWRIj//EPz+5Q9//w2I/m/FHKu+8R8SvhRumURh23358vMP7ePrH/7+8w99DbI4dIsvfZN/T+b3/Po4508efK368c97wfmnMiuroVx8q6HFr1X9P5rf3hemmyfB79+3nxZ/rMT5tVzMRnw99OmCP1RjC3T9gx9/evsNgE0JrOn9x2WAH//xHwsl8ZuqraJucfSrvluAAHdJEc7KG5ekXYC/M2o0IfBrmwDHvtaB/J8jPGtcRYtf/pf/gPCP/gvCoSf+fpmR+csDmX95XxhAUNUkcVICvNWZw+Fz6cYAd+dD6iZsw+YGgMmbuvAjqN+P8y+LpFz88hdZXx7b3uvplwfUJk9k01lxRrW2z8P3Wf/zBYD7U1sfIHc4hn4PJOaVD46PEoDAM7a3VX4DqDjb2mZJni+CBOAGYJ4nFwB/fJqF/fLLL57bXj6XTxjGFk9KaiGw4Js6i48fgR1RnsSX7nMZ+pdq8cOvv/2w+N+Lf7XrIXw+4wAY4OVtoKF03KsLUD19AZaBQIDQAWh4ePvX317eBGJKwKEgNkmUhM/NIPuyMPjq2uOW+YgS5MILgUuBO4vZlTOXJd37QowW3/R9MeaM/hfAf4sgrMMyCEt/AlJdYM43T5ZVt2hBirURoLy+DR+n/uI17kPFApSx2/2yUNgD4JoqBz9mNR+LwOaqTID7vwX++T0Q0vzQLtZfRbwv1DnfAK83bn1p3NcZkfuMy8zdr+1AuLsow+FzOfNoOLvqkfxP94BFwDP+K6Qf55iD3gKQdRm0X89+rHFnRjQezNh8LttXYrvNHAofAD04NO6TYIb7/3qlVHup+jx4+A9oOkt6RSF4ReX9GdJvncmrS1g8CX7xuUdhBF/8/93NzCYygqBvBMbYcIuNauj20/VzCzeH6Nn1zbrMSj7K7PfO4yu6fAXZz2WegDxqpv96rnwE7LXmCVx9A0zRGf0hH2QLcP0s95HMc3I2zVwG7ufyK5oD9RcP6ALxBJUPKmNOyK8Hzle/anoB5T1//p3ZH8FvgtkBIGEXde/lIJmiMAy8OUTdZY7Z10CCzA7n4hwuiX/5k1VzMEAMgfwFUCIBJQYQ//0bwj6vflX9TxufDcy85dHc9aAem4cAoEc4KziHZg4aUK97dszAzk8PIcCMou5m2z1QEcDS55dhE177pE26Gf2efg1rALUf5/enpfO34ViDIgDOAqle98C7j+KYs6YA7QnQAeADqJUiKQFdA6e8nPAQ6BZzpQMkffWTT4mPr18GhY+Kmnnm68bZkHnPTN3PNHfL6Y+AYHwvTYC8Yl7xOPcfM+3babPsGRRbAGzgxK9Xnxz//qTpZx+w+Cr3019Gkh//vanlQbynPyfAp8Wl6+r2EwQ9yfIrV74DSIKeurYv3vw4Y8DHBwb8SdDTxk+Lf0+ZP4l4FcOnBfIOv8PzJfmVTK8XsJ39uLY/4vPVz6Ue/o6Q4PiqANk0R2qaweArnX1dAjgtbgAAgcVPemtnVhwAET/wHLj9c/nH7J6rC9BFGc/Z2FZ/qPoHr4NMf0bpG+2AS2UHzg7mPi8O53HqUQtt+Pap7PP8wxsAx/C7Y9RMJsWctO08boHyAIjYJeHjkwcUygJQll8CkJRl++yPfv2HyZP7du2RRN82tbOFgCvcugbKPFtSQJ9u08189AEo34VxNUMqaDdqsP3RR4GNgCSAYt1Uzxo/Z665S3sg0tj9VYH94xc3f39hc/vHNH8R0kzIf6jGp5OBc31g74dFAFRpZwIFTp5dMVey22YPg76ry4NOvjzp5DsemTnoT4wzs/2TrNz4UbwfFuF7/L44HRX+uwd861f/Kv0MGolZYFB9mjn1wwvTwDuYMYBbv44LwKzXAPcYr8sezMY/z6PKHPXHlvkXsAe8fdv07f8VvPDt79/T6wF8X+ZkfKbUP2r3D9w5L3rZ+pca/ojCKPkRJj6i+PuYtyMIh3t7MhFX+c8GD3pWMPQ8F/qur54c/ldVDn+k+Fnqs29I7qBbCcLI7XNQSV31SIhibu5AVsyU96fWYOHeQErN2fuds8HhD+IA9Dv79veg/e666jHyPdTM3e75PxS/voGKc0HSua+ae80MYDnA2Y/t3ElBAIjAgeDzEzLAtf9+mnhtaC8uaG7BDpKMSH8Fux5F0TBOURThEzgduSvYx6mQIGkcd5EA/EQRlEIIDMNJl4hoCoN9LAjoFZD3RJovc3+YzEoQKyqCVys0whEUDoAbURysJGnSJygUdleeS3jEyvV+35olZfCy7GnJ7LZvg83sgZeBAHBIHKzc4q3IPF8stEK8EIW8SbYgi1glctydTkmno+E97bL63trlXRPXBUKxd1l3+4rnsuN+54qASOCKuAr7ZEuyUStRBeSjriCkRLZHcwxFYU1bi4S/9JQwuu9t2g2JAdnH0ProyWJ76nc02qOsnUB7R8LNOkq3GIT3ZR6McRqud4KmGZ4Co/aNVjaCw9rnsGXJqbSS0cDVYMs249IM5jqBDumK2K0ch9Gu3nJzLcRa8MT1ZpJDdZJxEd6URXGsssPZ1x2VEeo2acCQg8W1lRKic5R6hdxNyPls2U3Tq6MrgX76cpy4vZQNmRU4ckpQEu9Qvn7Kcl2/7tBzDSnbGA1vljOtogN2w+jKxJc+SrXL1Yo+443uJLlkxppmmn2Li7ioe7Lnjhthb6x3GVUJFmkK/D2/tkYf4EpmXUx7aWdhL+KGawextj6z3vKeUmrmZAOUmGtHURNiRbv2Bnd3onTSCJQx65vkXtf7W3K82Nd7wp5l+b6huF2Tk3ssb1ddJXvwfqKniVuL2pARFzPT4dDehjzZZWl8cqci5c9FiUk78izydZ5d9ca3EDUmsTRCtc2VoeC1E4ssNfoOwjr7VRVA14DwspE73ra9q0lKnh90yRTanqvtzebokpp26k7xTmkTKz/lanophX4N5UQIk6apjV0CPBzLy7NiXqnk5BZytosOtZsuc2OFJwdHi/xLcbyedbMwfY1s2vbEms6UkGKypvXJFM/9PVFpI80wYz/aTKiuYdBEbVqVvAbFbhQVSjvZWTpJy100DlrlOnW7hxsEtzI2t4WkNNxLx7ssUg0C7ah9T9ZnMVjvyhyuW4UcC4y8trtMlFCtG+/5kq+NypLG0jnc8YnSjqk/lIeQwZZ4Am+M0fA0+tKeD2sHTPnx0kQMHNuPst/593N4z9hQcGo8cprecXJD7TbdYQqKktoP/dZDoT6KcTMfdmNPlXh6gLKIFj2IqFIlogeKONTtEioxcp3jyr13tkNdsaeUPN+39rTlZa28IMFlE4Z50WWXCWXvO42ZBHG6ofJ2ou+YsiWX407MKVyqpr0p4FwgqqhD7bbqsqCcteMuLUbsRHiHW+yVMjbwZRs36oVxdYIJ5LV/vq5CuTUN39jHhhVfMUW83uRySBLuUNP3PcfdUOlWrTJeTqho3TR2UiP2UYfqXXZDjZqjYUW8h+6Ky7IVla+27elq4PIKzkU66RsEFATv4OmqLbehlzWeFGIlPt2Ne7LkUl9uE1Tw9YvZOvLqdPZlXHUmEXfrI7M953nFjhsJgg1WcaNjr4TMqdAGJu6R5Rk1dkdWL3ZRRg3STrG7Ioc8lJ0u5Zit5etGk8JpEn15QM4irfdahcGEj177iBzYJI9kpXbpgErHJmvGkSHikEWzc9vASeNiVwGOc5i7qYwhwNjh5t5lAz3Wmu9eVuNd5aLJ3JMrLk0gv5ATNBUEwrhVITRsl7sbs8awM7PmsBsLxcFNaXW0UkyNog0d77nsLGzIS9hv8olRsXPv7u6SzuamvnFXMobF9n4KbWQky8ZlBIYbIRPRJx/M1uMEpUemv+KWxVFp2hgJlpJ67vBapt4Y1cFO+fmQ9aa57l0E33pYt8VkTDzdylu9P6fsfj/s8SLpV3u84w8hLY3NuO9JI/CP+yPhIAp1TBmXn1huoGFoq0lpqkF0IYUHcjWwUlLLzrqKNljCyBmLD1sjFUck2ZDJ6jJgDUEQyx6eUK1RMraohtNosl5ZyIbBbaqOV9Wa0E0k6CQHabVtchw6mx1TfuR5xxWXunS1Awdizp1SZVbFiztsQzW+ozvKhKpRj1u3IZxad7eNqt025BC3NXfIaX3nbGFC7ZJzrYOZFWiRbwsluqUFsbcwYoI6PtlEugj+SWaVb4QtJcIodqpW60vAS8b6LlJYhHBMi9y2XF1XmuYi0O2OWdDQLzvUSlfR2oRkzIINoWmHrIGdqLwVF4dp2fNGQAnVion8rO02hS24kOWbcT7INcGjjHHdFeh9OuNF1d0yhkrvLn5VTnaXWPutxRC3VMhtzneM+CCcBv6SHvztsm2TeNpt9pvBq2v0hHYnkGGAxDQuI/3CEYwzj1+HO1qlCEKkaRfXpsQ3Z/h0ZvAA3auhWfY+JjbSeDcPNb4lTFuu8ZDb1iljMpZ0VVr8aKdYgW5E53ykRM3fK75RmNSQc11NdojT8veIE/c6rie7DShWkVP5ozMI7uT1ecS1ekCwYuLSUQYB+tms86t6Cv2r7g99uQOUUYl5YiFpDY1ORtNX+1j43X5lmlvHZnxuLIRwfbKu9SQobNnB99X5ui4qrU7iUZZGzzytY4lBQCTIY0sgF+UAkSiiicnpKpvr1m6k24aXreOGpqMK3pyoQT+abI4HnhbDfMlyNQF+3A/sstkp1OYu2JOCbcKhFBnRu6IKZVUrw5EF8RZf8pQ5CTvQCRr4Sep7h18fx8ZPWsFEijtiCJeQje5npEr4CQ/cDcbXYckWq/ScV12CExx1pN2LXcdUFnCMHe/7kOjr9Hj0CsOxL/iIlbmPNXAq4YokDvJ0oNGErDdRvTcbOoasi81fY7Ko1+ZYcOwNP7pHl+L9Kr5spJQ6Sseap+3SFvVJ12z4YC+ziIv4eq1K6LJPlt1aGYctxdeNMaL8enDXnTLueFtzKHJ1Pp0pN7KU0RtOMX1byc6KPg02La6Y+8VN57YwsBk30NS0FOUjfbsDcCz4Gg+oZAq0FhBzDXmqqjPUBbnTMAn4tC4mnnUlTRrlzc5YMpFRV0vWuKu7/eq4S2RGb3LFMHi1S2zpgK3pgUdOMldtmMmZtru14OI7IcCFC3EoQ4amphbkL6udqiBrmvU9XMdHo7o4PLfGq87P7OaerQMeDy37qgpSTC6P8MbGILMNKFM6xLqCNXcn63UT9cU7HO/WG0EVyuVRRC8HK1W0IDyN0xX36GYJQQTP5zallJpxLnyyJ5JVTUURaLB4xqyWwxT4/gXEPKMmTScEP0QHRGKbwllGCi6TllofY+K40XeBQ8eMBOdXnT2y6jTGvcwHRx13Y3Zrk8l1jIfa1xtmJBjJsS79fdAjVF4hp4O4Yk/rc+sameQV6D4S+fhIj+oFnwQzS5rtSkpd1YkrFvVCgiHhUQ58InYlD60lwnOyTHLMK9tqq/11nx0JN9uTfKasN7qkXdkDI2i+RPDe2WVKS4IO0tHaA25RAk+su4ZXWMY3FWo9dj1AwM2KC5fLPUVTx7ZzO28NGl9e3Oinc3Ye16kQInbpwnR42JY0EkVGvjpsLKgKNpHGNYNj9tJIGep1eU0w3qXUY3cvilC+lelt2plrVxSO8uZ0CLx9A1+PmyOPVWRlDfo5O5LNtHMkz5yijqRrH0WEVC38+/XYgeb8KpWrcNCCpOVYUYzWtzKW14gmyBx2EbCeMzHe7xosqLI9tvX4o9mWeoXZHKp0Z0TP9spSdOVEuGQCm+GZ3g0ak/rXmsK3wagMe9RhbKZ08IKtx8i5BRvbC6qC3+MKaBAvBklxymHkj9Sw1Udtsz+p6qqe4uNmVwpui9M2NKrYxESFlF4PRYIV13WoU/wZiZeDJokRgjanjk35hHfXbuk6OM/uhY252TBdFEUQDp8jiL2jq6O/z5IkyfIp3g4qvzwne5OF21Q/nLgNu1FbONk0IwxcxtlnLpyYlG9X3k44cjYYPs88e7oHY5cOVktHWAfTA3YtHA0kjnI0xbKgsXK/LQaD44+lNRYDii3tqXP4E7IaRNOPtxQiToS7dZxaFb3O1aab45jnNZYkhtSV4+5sclxyjMdot4KW8q26+QTNEFt2gLtY9mkyW95HdY/FBlGYvHGSI9BzA271GBGTlHqnp83W5fj1xtI2q0k8C4GNMdF5hx6h3odvm5wGA7q9hNZDywjIQCBg+FCrQ8OTN1kTXXMXAysD6TzsPPF6Qfyq0QSiwp2pMcPOsHvzuj0wU1WlrArqaC/C09QikCXZt8nlhGWd9Hsq5G603DfhpqU3vbE8Hu1NdzWMAUu23NZomXFJWfzF1pJA849bMb+3kLDeXiWv49kbXJvdcelGm73eOQKUsch96ooUmsj92FKJtLQwGcqPdcGjpAqiYC/18riFW2OJbUjC05grU2UIDtUcjnbRWZc7GRBRfSZUAtXWWYZzhNiDMcJrNBLr8MBGJ2XHt3vtnoHk6NY6CulnzqQ60bxcyq3Ar80bmG5dQkLurZdTViswwzLFrSHFr3mzircJeWEU2wxrstqeADXLTFJswpWGIjtMv2n6ErQvpesickqq60Zh4M0dUgaN8u9SeUoHabASWrnouz4nDiphn5fl0OdKz6OSDfyNh2s7XO4K2JuGEW+R5lTeg/CmwBzG3oRkacl6qcb44Tzug2CJEBZDHUUPuZZqeqLIfKvtwlwIb/sC07cnsbomiBid13C3K2nUkVWVC2Dedn0KkeBALqnrvjluC8Spl9elaKdog4goe0uspSHB2UlEp72DmgaDl8o1YUVB9g4KIxhhxziDXnfR7dRlSpQQMLtc0XpgVfYVvQ3ldJJdTh3QpZoSTYyDKfRybszOwZwCu+DMFYwJcHC5DVIjlIljp1oI+kj0cINoFaLNs5QWTnegiARKb7EcS+rVC6JtFvDrWx5z+fp+tfwTnJF0O9oIn4UOEcG6Q080F53o69Zy822DH5anpi5UdbuJBtiP90dQz/I0GlCj6MuD0G2TzqFxatd5dY/hlMshrb7zOxXllFt8L7lS8S0xGyHbHQF8ckWVeZgt9XoIxkQ9E8GUJUDLEAEvKrjIW5w+dQdxV2JepQiWtpKKgt7VjHgA/Vdyp+qCdnEqq8kEyz2LM1rSVHWSjJu9WUFGciPgZb31aHVrShJACinTxCYbfPV2s3gvKK+0OLnstPPOYXU0T8pSdZRzeA5vrrstdd6tQgcxY5JBfSpM9HuEVaZFyo4xTPRaWYVLvBsFiB+DysBjm7ITc7zDrnFmpr3BLXNxta92iSauxPES3oRORvGqNkzYxjD3vtJ0k0sO23Vu4Mpgway99O+uUoJWXZ5Azq5uNVMEh6GRUSMpHHV3DKGrSa726WivIGylByyFnBVDsg+GtaNUWqhbNeAaAZ+2pTLcaIurCvh6l6HmxLlil6qaAlFsOHrHkz5G++5UqhXVy63OYqIu3K/b1C6vWYckuJ7nkRjWWQ+fRBptCpAJxZ2UmqbaF4aAuzTu9Hh2FRWqvnIGa1m3dY+tpfMZ3xwMdPQ2qyicwo0LEiK5n3t1q1HcIN2tIrXJkrHMDXFPq6Mnr1cbP21YD0zDth8TrWDjvVA54W05jP7QMeY+AuOvQLSoajMHAF6wcq7JvTttY7pXAh1QLZmBggbtp79iKqxlQnvVb3Z86oVF4NIId73VVGHVIek703JMamdF7qPgesb2B6++89zhDgocKw83ClG3iSlxtyxsOOQY+k1qIVYOiZtbEEkpGEMZMydKoy6Fyr3B6OGKXfpEOdXkLTYhER/WgcvURDZ1xDUo6HBldiafcnUAqOZq3yuSMoqiTFPrxrdWi0PFKXKvE+1vQ6dfo+w6V6hdKKonmVyiojtE6+tBw9RltVR3B/xOt3IqrhHZMkENnS/Hg7LT9HCTDN3hBEaQAwG6I9UgjOmkBKEjYgYzqVTFyFULmivsNh33+wsHcRXgVLxWExiBwQBNFOG2ZSZ4l7YpaDOcVNnSiHkXsOJ+oVzG5KLameRwEC+Bfor78TZoYKTcVvfukiirKR+PVcSlBUjkQl3KXYWJ8tDuONhzx56cIFbtmoGpacSV6S1TVVcT95c316ydu1ws207I067ziCN6PcHp2sZHUth74i2l0VbxY6SIBNxDtxnOk5Fr7cOwpTCDzgHA8l5eXT28lwZIvLGTtJXgyLAmC/WS82qU9mXH2+0FOmfslT/INiIPZXYbdrs8ANh7GWUHdYvcCDdUKFg7P0ZhK/Tvu7EJXDArdGFTbR2T0ko410Vsubcga8q2N4qJ1y20C0/FGUm3uuBIvZ3BNSYyDqQp5Xq/66kIWjWUMiIJLC0j2LN4AWEJVxqRQPY6uTuB1qCjes/CDB51TcY9yMtbjmYhE0xkzS3tsFJjLNjvjpKqVY5x44aK1MVzs+HhQ+qWhyVueBe+c2X0cGdqHsOu+xPiUSJtHNZU1mr7utqyjkIICFUdaJj1SDAp9Ko5gsGZGVgWo1hRYwObkmIZWx3GnvHZi4ArluXtesy5XytS1e9VIEUCd8KLlkaICcFc3IJFOt+eSbkKCT1aTxXWHNgDEugYjNCUB+MYR5OmhPUXX6JWaoiDVjOSIUiydkLVYqtuADMO38DytrXUy8AWhTFeEcyrnVPDnwIU5tPAgVKaDw5hKYpFOmAH/GwcLN/tHBHiOFtYjWe5DHrVsVwLJD99uoHGpaNTwUgOWKESMHyXxi5vYNA25jsUOw8m5N3csDzzF7qkVaGQThsG2RF0qSpzT6cfVJPPpFWGYDpJ79nk3p4pPW/EJNzj6vJ033hHJ+OuAG64ixbl4qbPBQI4ZIR2CddgS9CTGrhGrXqI4sNG1mxsvN+p1JRDMg8N4KPNtnZFzOqJaG0dt3dRS7BeUlnL12CRZPoL7spejt3bQ0qVOH9gMHGb9jIMjNJ4FJ6MOpCru7Hc04i+xCgOlcPqtFaX1xtyPxwukCcGwTW5sAzD/O3tw9vv9+Le/vkjYfPtmP9nd4WeN3C+Pg/yuKsYusGnx1mf/oUOf//w1vgJ0OB5b6vN+/h1Y+gf7mx9/Mu9wnn59HyO6utt4OeN7c6N50eG3xKQI23XTF/aKn887wF2eH07P3PYzo+l+uD9jzc+nye8zQ//ATvmB6i+dNWX16OSj6/nBznCIHG78PUxft3c+/AWvB42+oKRxJewqWfLXk8QAIOwd/gde/vt/wComInv3C0AAA== -->
