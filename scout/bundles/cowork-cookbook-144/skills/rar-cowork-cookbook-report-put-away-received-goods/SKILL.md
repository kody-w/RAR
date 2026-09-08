---
name: "rar-cowork-cookbook-report-put-away-received-goods"
description: "Builds a read-only summary report of put away received goods from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_put_away_received_goods", "rar_sha256": "0d50bab438a0b828ec2d5eb92e3684cb812630ec183d3db4d7fd5123c0130425", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1VX7Et1vIgRIBBICAQCSbg6yuz7IhYJ8PN3n4OkKtvd1f26I+avUS1XwDm55y8z7+HXN6fv4qp5+/RmBE65EJ08T+KgWTilv+Cqe9Vk4EeVueDfwqvKrkncvqua9u3Dmx+0XpPUXVKVYDvbJ7nfLpxFEzj+x6rMx0XbF4XTjOBOXTXdogoXdd8tnLsz3/KC5Bb4i6iqwK6wqYoFP5ZOkXjtAiOJhfC/DU5ZhBWQZJEHkZMvgrJLuvEhWF21HdhbB01S+R8Asa5vyqSMwMPFevCCfDEL/pD5nnTxwngK8mHBB52T5B8eRI5VvUDghTsubk7eB4s2DoKufQeKBYNT1HnQvn36+a8f3hLw/e3Tr29e7rTg1pv+0EbruxVQRH/pIc5qgK25U0ZgTT0Co5bgGogIdCjALT8IF6+rH9sgDz8s/vM/s7vTRO1Pnz6Xi9fn89v8R+/LRRcHi65yHop6Tu24SQ7Uf1+scsC2fek827sFPimj9+fO3ykB7f5rfvbjk8l7FHQ/fn6rgAjO7LHPbz8tgHE/vzX9/P19plL/+NN7Xt2D5seffqfT9m4aeN1MDEj9/uV1/SILFv6+NAkXXwxtzb14AR8ndQCI/0G/+fMU/UXuZZIvz8U/VvWHxfcpz/r8F5D3GXUuoPt9ssAGYOfbe1ol5Y8vHk11C0qn9IIff/pHZL048LI8abt/ie7PT8IxCHVgrZdJfvrwcN9fF9BLt280/zHbGgTMv6MJWP6V3TdD/SPaD8/+Dek8KYP2my+/S+57G6D/Wvz8D3X7Zxs+LMLPb3yQgxxpHDcPPi1+fYTIzz/4v9/84a+/AdL/Ixmj6hvvQeFL4ZRJGLTdly8//9A+bv/w159/6GsQxYFTfOmb/Hs0v2fXB58/WfC16sc/7wX8zTIrq3u5+JZDi1+r+n81v70vLCdP/N/vt58Wf8zE+QMtZiW+Mn2a4A/Z2AJZ/2DHn95+A7hTAm167/EY4Md//MdCSbymaquwWxheBZAUOLhLimAW/hgn7QL8nVGjCYBd2wQY9rUOxP/s4VligMG//B/vgesfvReuL5/4/AWA85cZnL98BecvD3D+5X1xBFSrJomSEuCwvtK0z6UTATyeOdZN0AbNDOXu2AUfQTJ/nL8sknLxyz8n/OVB470ef3ngcfLEPJ2TZrxr+zx4nzU7xUH50sMD8B4MgdcD8nnlAVnCBMD0XADaKr8BvJyt0GZJni/8BDADhepZMIClPs3EfvnlF9dp48/lE6CxxbOCtUuw4Js4i48fgVJhnkRx97kMvLha/PDrbz8s/nvxz3Y9iM88NFAmXn4AEsqGul+AvOoLsAy4CDgVgMbDD7/+9jItIFOCkgu8loRJ8NwM4jIL/K92NjarjyhBLtwA2BfYtpjtOhe8pHtfSOHim7yvWjvXhRgUyYUf1EHpB6U3AqoOUOebJcuqW7Qg+NoQ1MW+DR5cf3Eb5yFiARLc6X5ZKJwGqlCVg/9mMR+LwOaqTID5v0XB8z4g0vzQLtivJN4X+zkSF7XTOHXcOC8eofP0y1zaX9sBcWdRBvfP5Vxsg9lUj7R4mgcsApbxXi79OPsctCKgopd++5X3Y40z18rjo2Y2n8v2FfJOM7vCAyUAMI36xJ8LwV9eIdXGVZ/7D/sBSWdKLy/4L688YlD7B23Lq69YPFuCxecehRF88f9LJzRrvhJFfS2ujmt+sd4f9cvTI3MjOHvu2TvOssziPbLv91blKxx9ReXPZZ6A8GrGvzxXPvz4WvNEur4Bqugr/UEfBBHwyEz3EeNzzDbNnB3O5/Ir/APxFw+sA24GgAASZo7Trwznp18ljUHWz9e/twKPmGj82QAgjoE/3BzEWBgEvut4GZBq9t5Xl4KAD2av3ePEi/+k1ewM4FhAfwGESEDmgRLx/g2Sn0+/iv6njc+OZ97y6AZ7kKbNgwCQI5gFnF0zOw2I1z37bqDnpwcRoEZRd7PuLkgUoOnzZtAE1z5pk24GxaddgxrA8cf551PT+W4w1CA3gLFABoA4fH/mzBw1BehngAwANkAKFUkJ6jswyssID4JOMQMAANhXA/qk+Lj9Uih4JNpcmL5unBWZ98y1/hngTjn+ESeO3wsTQK+YVzz4/m2kfeM2056xsgV4Bzh+ffpsCt6fdf3ZOCy+0v30d4PNj//e7POo1OafA+DTIu66uv20XD6r69fi+g6QavmUtX0V2o/A5h/n3P/4Nfc/PnL/T1SfCn9a/HuS/YnEKzM+LZB3+B2eH+1ekfX6AENwH9nLR3x++rnUg99RFLCvChBas9vGGRm+lryvS0DdixqARmDxswS2c+W8g2L9wHzgg8/lH0N9TjVQUspoDs22+gMEPGo/CPuny76VJvCo7ABvf+4So2Ceyx6J0QZvn8o+zz+8AYwM/qd5bK49xRzM7TzCgbQBSNklwePKBbJlPkjXLz4I1rJ9Nlq//s1cy3979giub5vaWVlQWpy6BnI9e1tQbZ2mm8vXB6BHF0TVDLWgO6nB9kdDBjaCmgIE68Z6Fv45vM3t3gOphu7vBVAfX5z8/YXZ7R/D/1W/5vr9hyx92hvY2QP6flj4QJR2rrfA3rMp5gx32uyh0HdleZSZL88y8x2LzFXpT5UIgO61D2Zdg/fofWEaivBdut/63b8negLtxkzHrz7NlffDC+LATzCjAGt+HTeANq8B8DGplz2YrX+eR53Z2Y8t8xewB/z4tunbLyvc4O2v35PrgYNf5nB8BtXfSref8Q3g/2zcvymrQGbA1++94KX9P0/yjyiMkh9h4iOKvw95O3zXTs9y/vdiaH+s9o+W7NVPlH8BZgmdPgd51FUPMYu5/Zt5g+r3py5h4dxAFM0B+x3egPmjhoBKPNv1d4f9brbqMS4+xMyd7vnbjV/fQJI5IM6cV5q95g2wHEDux3butZYAhgBDcP0EDPDs35xEXrvb2AG9MNgO+wTsOi6O0Q7s0igdeKhPBC6DBhhJ455LIyiJwYGH0JiP+S7uU6FPICjmwQgG4ygB6D1B58vcTiazRARDhTDDoCGOoLAPbIrivk+TNOkRFAo7jOsQLsE47u9bs6T0X2o+1Zpt+G0oms3x0hYADomDlRu8lVbPD7dkEHd5otxxd16eYXrI76e+FpwkK6bjKqun9lJ27Ep0GlEoT+PgRc5GyrwDop8lwmYnVtlzG5LVUCOsKBu9VGGWo22LBX6lrLI2sRU0VAeIoad9PJSKQJwO6XLoIPm8uoxQEvOtSR1Nqdx5zQ2hCRTPhMIRoG0YLqFNIOSi4lO4qF438GTIPry1TTcLcodY+xUfbDMIw0vjDO3bylS3rjbdrWZJYXRvdKetSWwVe6Q8n5Mzy6QkI4w5eWddRKLwxnQvj6uTsCkM22hpa+uFhzrbiZSx3FztugsTOanQvENlVQaraPMo3yRo8o6pjm6J9bBkelnnXOfQ5nx7uW1SBup3LXO5YTYZJtQeo5KB8egznur2qmCt6BDmeQvXd1wKnO3R0de4GEJK1dTiGbdEYSiu1QoMJQp+6u0LZGdBL9WJc/GjA1usXGhK8dYUsmWQ6qqt7JPao53LCj+OmiwdSFSr5U7eXlfqLanowcq5S3Ks9s3EUYaT5qSzLD1IrPkbpdBLIzpq9yzjjtj+wDT0SlnubP0uXBIr7zWDd5bsOin2llxkiWG1WDGml71m80bFcgerX0VOuhpgmMtctMSCHMv7UNxv755tS8W4iZD1yTTGeiyjuyU3ssAZgsnfxnR0hOyEqpznXPila7mHuvah9UncQdeNQphMXm9l7loVek2PxcigplYWO0ZgobHQV3W9PbGnu1ZkA2PZXO5q6AFixXgnGlBqS1J61wJN16aO4fANHYpdZ0RBcUWldnM4Vqt4tFUpHJrbjhTirrgs0UtxVq3DNga9a7yvTyurdsWW3XU9ej1VuTQgwth4h2I4NWhjNjtN5g43nTsvBetyLfdDVu8YfNSsY8qRucYpCLS6oRl/13drJlZGkbWXhRONDjZ5iBYHbtWmZshfdoEoR0STs32N1HpnKdAyM6OaNDIY6jJ4aY9Bt2ZObonfNPyaK/djujqnDLKhEpWGXHWQNUU7pIl9uw0xVPb0Rpik7qI30Okgn/jGv9eydJpuYxifM9NygDWxBAo6hG+P7GUzCUx9cqlgtQskRDBCh+9z9KjfTVdDiqPkXGGiT+CNKw+NUVx0YpvFFovnun5RK72iUxMmV2zFEkR59qdp2OwHlWT3Ktdc7mvD68/sqNF9MSm4omKXAkrhlQntOlrou9zJrQQRBRax8HrVaNdWTq3DtPe5/bq6rfaDluxDnRC3VTuMhLw8sUllZ21nZhqBDNKF0hyY8neq1jIkFU7cebwpt7gWDSvl0tIJjEIRb6qw5uUgP8T6YYy0ng2TzB4qjrS6nuXgu+hEapv2N2OHHIZCV6C0jIvDPUW3S+Z2sW1xuY3Xjrkxz9U44ZfdHTmt6FN/qDDMInLdWyJHUlA5Wqq3tL9MmS6b7sOKiDSFzOniOGaug1239zjDeUpes4dKDdUOPW5b8nSrMp7KUVVcZo5nUZutoDOKpGkctyWsUGK1uxeOu5WPYUHE7bBJ1KKrptAGWimnodJtnJ7gw0U614KKW2dJgf0tU+/a/LJ1HSFwD9ezqgqUwkZn0JV2lbSVNZ4OLWo7hqS/6RkB0DDvk7rBzpvTiDQiPKnjJCpOsDK2JKG2IX+3crR3/GEMAzIMbtCOv++gc7BCIFE5N9EUDaZQ9UIbU1is7h32jDiGkOWj4/YD5sAHNlIPhnPu04NTKvlJceXknBIRvUou1wMaXikdvTNMzZKKsDvR9nZMQ/06Gi7C0AxlifYgh1tDq9f5znZi4Bu5tsfRrI2kgOFav2ZG2ZKjvIsluaTpaqDxlO6kbM2ytbu3GTbt1HueXoULL66bW1izxo4ruNa68M2KFVtny9cXEzs65BDs8pLnUg7bJxGmovnlLt7tmm5t+ShOGkUT6rnDgpOtc7c287QqAbxTmodyw206U02G+351W8qZTy3JKtro2P7YVXiUUMRe22wxiMiyZZ4NJrQs0nbMhnGbT0Vh09su4effZOyWEdGfb8WQVUYBnyqLPZmKIA9YdQzEImkoRuGt827g7QrGUGq3ElVTJyZrFMM7XBVr67imWRhROUeHhS3H4sGhFvjSXClHITpd9aN4V06dszadiFRLOdfhMbZrgCOUk0yHO0lflJPhnzPUiqaSucTZOXaoVBhboTlcQ3pJX66KgHjaPgwjVo2qxGR8fbNXC7fy2E7W+3gYmoFljVMoB6pHNIoVE+cOVpcXlpeU7HS4eYfjWtbkO+ngkJbciF6SxkOC930J8bjDISvbKVtJ3cUkrTiJxd9JBgmEvX8Lvd1pxW+HVdHsrVC3LrixR3RBSs7ZidheL6y7hikIpnMy3l4PyaXC0Xt1lu2VnBgp54l6Viq+oG2Wdq+cx620TUa+SVb3MN4f9kp83ZzH/U04MWtK9uWW38AXNavx/HAazLja4e2YCtLQ0qV2FEBU8HKUkHh4dBGqhfOUTUpcHi73nE357W4ZIBSzI/XA3CW4HFulb7eQSd/P0RlGO0eKvZYX9L6WzjLi36Th6jRRrYoJeisyaxv0uBjdRWkqi37XxXCTM7vj2oCJcILlI0IeTFpct6BiaiuU97rLLet3FnQgbKxQL9WldsxzK9P3ZrNqcgPMs1wGZxC399lci0o86vD4YCObaJnfKH0tg0mUvUYpROzUYc1Tgt8aca+l+oZCWn1NiW1U79zwfA1jt6ymy12ggjLpOwjdCrS8jnU+cxWBcjHgEofQ96gsckZM5JBfykigbnq8LbONnJeCL0zH80FY+V6lsnqBGbBsQMo6X5PrkZM0s6rW9Nl39CxvnFYYxGJlJelNhgqUv4gFdacuHFkNbEOqobRMEK+4tHtBNUqz3+RBwjTTLW3W/D3mfGcqtinJx6Owie1Y4CulDDI4GbJOTTzXHtzykEhilzGquNdwClxFxsoEEyzRTaXOXaPLio4cbl2sD7nqaAibOhEdtr6J1g2+o+R+Wm5gCrRQo1HZ/UVl9vUA3flbCPcAwglnlyklxsuWadgqnW04vRJuGmIcRnIVlqXKqdXkOO3RjKWxEh2L5XRpm53FiDf6cBddz2bli+HkYVBVtdVBPuPBXUkO0knA7bbVjmQc3q5DLVZcPiGp4cW7CzpMBNtyfCHTkqiTFWRd3HrtntYK6GGn3SBvi0SmqFhkCu2cy9AVu9nsLXcSYb05XKna6FuC3cTxahUruhnh8Z1t11zgW4hCjcjxPI1wNwSnMdmIkOxuCV25a6J6YpV4czw3txSie7jZndanm+k5Uj/GY0BLSc/eh3XS5KuLxfF0u0LLaiMtc3gMtHLuUfq0ZpTyhpnQALWHhqy3vpBebwjoMVHsImeFt65SytiZJ61zoSbKW3GldnMXTqfDqnLAmIuLKFMMRk9ifqdW8LZM0PTaQAST+NC52oNAKOEDHeNr1Fo1tqWVVnqPLV7YuJCWuZO+sZQxNbU9Lx2pmCcMilOlTkT0TN0H8naXcHEmOrmeGf5Qror2WpEXeT+u7ioqry6bjX1tN8fiVi/99cX1q0KoYPF8dvUTu1tzt5g1qPtGH3RcNdWBacbIWG9LMCxZxLJuqG6NhZIYXArJWS2nrNuOGs4yUcHZSqMWNSmIMsh6WUMR/X5ehyspAb3sloECbVfROhR3vC+vZS8eQo/TD9oFheEG3dYpsorisGK2o5K1O1VoWMIjE949pUc25IWeabn1yNMkdz6JibULhv3tTlMDHVC0Hnv+frkmvbp2DyZOalZ6uzUyZ/aXpvDsSiN3tSqnrkge197hQNr4UUPNynEb3xgJGtZIlLRApYWv6wR47Fjm+h3Dqvo4REsqdltFU5MQ1Q9StJV4TlM7Tkn5Q7dDy9qy74iwxNfHkzKU+9V+dHemdCGh4uoethiyNlh+Sk/tNfL7404T0D4wr5ubtFNUc3modqvJVE/XRJWoVWAp9GVFQRiSwQJnQ2tSlJPS8UFj7eunGBkNCGuNfu9Mgx2aB5JtRnMjFkcwq8p1UVtXqNQvN8M+btQ66fvqwGOMtTlJnF1C7uBLaSnvnYNB72P2rnA0yqx7RWFZW7pUzbQ5DPr5QvgYsLSaVecbgG1tmiCU5MOR43BOJPXlztuQTANmyHN1Wl4aeVRPEXZxECXcInR13B0g4OTMlw4AlRSHoTJn7/HV+QCmOQpeVpKsuvhE5RnNUhq0NqCJ3CH8Bg+2yVA5u25N6JiJKce2CzbIdiw5X12ftZMtHrMgmhI+kZrTKNl7s6VllALTt7KW7kyKb3GdsgxiqYspgq9s8erWqiPDYjFyd1tmN5i57/g9MsGifyfQ87CKroyi1fQxqDzKb/W6DSN1hRckTm1qtbIKcd+0x6XjbE7+mSdrSkQKRK7OjOcKNM+e77QY263dVYwVT1PUtLVWkIxt2yHsMU5DeJ0YoMekdNdoezuBoQfa6k2EVkMtHBgbJ7lSzwpKFkszx1juBCvJEk78lF3fDudoaNwVGJfWmCuE9tnBA7mxSJjBdoctatM6urlKFoOutbZe1ufLMQH9c7kmHPl2mzayvs22U6eIbFg3UNTiXIZtiNolt9pg4sQy6zYDS4KZvGEEONui0eQxbmKpF0mF7IQwi5sbou1ELS8XS9zhjnpHD2uMP+pqOETasQ+pUluS6hKVUhwf25O2pJtlHEbY6uib9yV0a8SJCa5sD/C780cdPV9HXkjNE06UomYIGKzcfeZArXz1igedgm9Kf+93tVRQIo9z43EdR6qqnH253McVVmdmo521wHQFFVme3UPQxdJkd72ApExh4iBqN6Z9ucAofUnr+1J2Chw5YlcrjQNMFtmVMOTQhlEDBrUuoz9cBMq7G3sczVEQo2oVj8bemrIx6sPE6dZl6CsEgiI7exJuoLETtTPdb2MEkc2w0eGsvpEExPC2x3JbO+b2EnvVpU060VNcYLYTbhBaX9N7oG4F3S99c8ic6aKMnS+O8K3PdhZO3rf8DmHdY0faG2UZ1OfwohcbXhvWE4FT3HJNea41xrtUSPNYxpRQl1mHXzGaRrorZLdR5FWKpIVAwAReu2MB7zEzDdcof+W4xDMlUtmeV1tejI4p2rpDRuFJXZyG7abzJXGSYd9Wg8C09NqYlsxJKxuYkMqmv1W7KvTGQ9bs6vFqY/YtKvdpLVk2Ih1ootjfkou/RoXAWVL5Co127nScNGgsM9CtZ2DAmyx9qhDMQuXYjfapPPJFdaszj0jMY7gl89qQmXC/IuKzgplwh5un81nx96I1okSENWpwjfkkTUmYJZpKwSrEvRdVQ6si4Yq3ZExLG0PPhUnZIJg3jKMXFw9pjvrtxldFzVHhWI2gb99rIHavF1O82FeZqhQd8fYHkgmYOiFYg7t6fVLQzYhekGgFORp1Gaq8whsp4Ed8QESyKq/HWNser/YN5prgzhIpusyr8x64C2kGWwWojgSMt7GRckdD27zEKoJBa9fD/f4Km0qoXj1c9Pk7V0WgJQwpcnnNmLDERBLpdMq3rR22gVLUup8ExkBrkLSW4uDuufamUtO2cH2AuWXs44e6XV3oo30iTjlKLbuhsSxsfd1vEbQQUF0MGi0ILxlT+zTjdrS0J/IdfKGXOYsVl2ifpXa6vZeGduaC9Jag2fq+vaHdpjTDIt/QBGQKesuRaVplGDEc6k25qVY3DrJP6VXnxQ0dmae+oU+HnM+PueHgk5IaZDBS41b39xRdRTzuQffTrsto8zSQdiq56aXGeopVuqByFULbGaBJwRTLg1WyxX10tTcwRQ2TMmOl9HCUQFWlzZWKsqhK4WaiKY1/2WojTlzpjLgFiWto40hMXESIIJJbGIInd4Q329veTDAW2jhcGWCd1W1pGM8n/4Q2h+EE3ejdUdg6etJ6hyW/2RfnO+qeROGAFaGIu+gmw9dk6JxBFrQZZtG5RyGCW1SpuxTrpVZN3JVzjhGU33ah38kNRUSOgVnjKDKyJ1frquPhkg2Mkq1IMAOcT8J6f3OujrXHjzlh00ldnqdz5gWtuxkb0M+HzdWnTNUxl7mzC27dtNxeTzEzufu7HuEIc7QbR/BNNivyqMsCYs3fknWebTpa3UFLB/JuzJZgb/B+s0ea2+pkXWl30NHQZRzLibHzJkdaYscYiHE636Fd7TQlBhJSl8PjhK2UE1RdbqVnjozpXqadcJ+UzNiTYl2dRUzVoHrfS2dESi9LRSxBqY2J6dze+EGj08QY4lMRKXIxwa7VT9N0IG5Ny50IRJSUYM3z0s5tJV2SEZCEUVjF0HnF3knFjXTbb7ETpTJ6aWzV/VE+4oRzWyNlcVPRgjpzULLJKoJMyM3VPN+D656c7i3UXCUadOxFCd27LURep7DX7psbjLjZ5BF0t1SOXn3th1DE+AnJzrco8gd6FFeO4WhoY/lejRw864A0ntUVN0TjO4wZLlDqabQXdq7iB43VsBs8bLgJ3S49N5+anrrYAJaSG2nHbigNGZ4yTBP4e2X0XNZhLJKvp67fA3JoijX1KfZCecmzdWKxIKb7ULyWnFtxUplck2SFHYtlxag8q1uwTw11LRmBijOkOcHHg53JjgGbG/6+3LLETgrKYy+fvWoHNQcSXSr7WOgxatmcyXvJTdh6vwyUE4Ml5/q6iehKNyK/ue1JhpdIYZK8CFOlKnaukmPaq/MB3wsMShLFZmAmmi/vbsbHk0CeoKgylo4t63iZr50lhJWkEgsxJTQrR3ZwKkeRcBOdmT1uY7x2iFartw9vvx/Yvf2Lr5rN5zb/z46Pnic9X18oeZxDBo7/6cHr078q0F8/vDVeAsR5Ho+1eR+9jpP+5nDs4z8/WJz3js83t76eJD+PyTsnmt9kfktKv2+7ZvzSVvnjVRKww+3b+f3Hdn5FFsBB+8dD1Ce7t/lFRKDh/MrWl6768npt83F7fkck8EFTErwuo9dh4Yc3//UG0xeMJL4ETT2r+XofAWiHvcPv2Ntv/xerZOmqfS4AAA== -->
