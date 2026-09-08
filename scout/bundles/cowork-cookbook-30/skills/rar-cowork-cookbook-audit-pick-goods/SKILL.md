---
name: "rar-cowork-cookbook-audit-pick-goods"
description: "Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pick_goods", "rar_sha256": "410995b78d5cddcd39daee4cf0b2715232f309a03d93f8c09bdf2c8aef636894", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_pick_goods_agent.py` and in the RCI capsule.

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

Pick goods Completeness Audit — Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
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
    "date_window": {
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pick_goods_agent.py` and embedded as the fenced Python below (sha256 410995b78d5cddcd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pick_goods_agent.py` first:

```bash
python3 audit_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pick_goods_agent.py   # or on stdin
python3 audit_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Completeness Audit — Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pick_goods',
    "version": '3.0.3',
    "display_name": 'Pick goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80e33ae3e1aae1fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit pick goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to pick goods. Output an Excel workbook 'audit-pick-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no pick goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pick goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit pick goods records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants pick goods records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPickGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPickGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObyJbnV9HcjpiqamyDhBDCHR0xIEAgCYkdQfmFi31fxA419d0n0b1eqp6re17E/DVy2CyZefbzOyed/P5id21U1i8fXxTfLlZHO8viyK9XduGtDuVQ1im4lKkD/q7csmjr2Onasm5e3r14fuPWcdXGZQGWy13RrOxV7dve+7LIJjA7rzK/9Qu/aZ7kqjKL3Wlld17crspgVcVuugrL0mvAKreswTUuVvRU2HnsNit0h63Y/6kchFVQAnlWYdz7xSrzQztb+UUbt9M7sK7t6iIuQsBgxYyun60WkZ/SDnEbrcrCXzWR77erCigVxIW3THbt1g/LelpVWbcIrXR5boPH15lANLfsirb5AJT0R3tRo3n5+Os/3r3E4P7l4+8vbmY34NULuegiAj2OixpgemYXIXhfTcCoBXgGXIH0OXjl+cHq7ennxs+Cd6t///d0sOuw+eXjp2L19vv0svwBtly1kb9qS7tpfQ/IW9lOnAGVP6zIbLCn5k3zRfgG+KQIP7yu/EaprFb/uYz9/MrkQ+i3P396KYEI9uKxTy+/rIBZP73U3XL/YaFS/fzLh6wc/PrnX77RaTon8d12IQak/vD57fmNLJj4bWocrD4rInN44wWcGlc+IP6dfsvvVfQ3cm8m+fw6+eeyerf6MeVFn/8E8r5GnQPo/pgssAFY+fIhKePi5zcedQlCxy5c/+df/o6sG/lumsVN+39F99dXwhEIdmCtN5P88u7pvn+soDfdvtL8e7YVCJh/RRMw/Qu7r4b6O9pPz/6FdBaDdPzqyx+S+9EC6D9Xv/6tbv/Vgner4NML7Wcgd2vbyfyPq9+fIfLrT963lz/94w9A+r8lo5Rd7T4pfM7tIg78pv38+defmufrn/7x609dBaLYt/PPXZ39iOaP7Prk8ycLvs36+c9rAX+tSItyKFZfc2j1e1n9j/qPDyvdzmLv2/vm4+r7TFx+0GpR4gvTVxN8l40NkPU7O/7y8gfAmgJo07nPYYAf//ZvKyF267Ipg3alAIBqV8DBbZz7i/BqFAP0bJ6oUfvArk0MDPs2D8T/4uFFYoBtv/0v94nr7903XIefiPx5gePPTzj+7cNKBXTKOg7jAqCtTIrip8IOAeouPKrab/y6B7jkTK3/HqTv++VmAe/f/krq83PVh2r67VkC4ldckw/8gmlNl/kfFumNCCD7q6wuAHJ/9N0OEMxKF3APYgC/C9Q3ZdYDTFw0bdI4y1ZeDFCjXXB8oQ2s8XEh9ttvvzl2E30qXkEYXb1WqQYGE76Ks3r/HqgRZHEYtZ8K343K1U+///HT6n+v/qtVT+ILDxHA/5utgYQn5XZdgdzpcjBtKWIAtG3vaevf/3gzJiBTgAoEPBMHsf+6GMRe6ntfLKtw5PsNtls5PrAosGZelXW7VKu4/bDig9VXeQHTZWjB/qhs2pXnV37h+QWorW1kA3W+WrIo21UDAqwJQK3sGv/J9Tentp8i5iCJ7fa3lXAQQaUpM/DPIuZzElhcFjEw/1e/v74HROqfmhX1hcSH1XWJtlVl13YV1fYbj8B+9ctSuN+WA+L2qvCHT8VSRP3FVM/QfzUPmAQs47659P3i86WBAHn+2hW0X+bYSz1Un3Wx/lQ0b2Ft1/6zhwCiTKuwi70F7P/jLaSaqOwy72k/IOlC6c0L3ptXnjEofutGDt93Ls8Sv/rUbZD1dvX/Y5OzKE8ejzJzJFWGXjFXVTZfnbL0e4vzXltEIMtTyGcCfutIvqDOF/D9VGQxiLB6+o/XmU9Xvs15BbSuBpaXSflJH8TRIjOg+wzzJWzrekkQ+1PxBeXfAemfkAY8DTAB5MwSql8YLqNfJI1A4i/P3yr+m9UX34BQXlWdA/yzCnzfc2zgmTZafPnFvcViSWCZIYrd6E9aLc4AtgP0gbWBqOAyFB++Iu/r6BfR/7TwtbFZljybvg5kav0kAOTwFwGXqFncCMRrX9troOfHJxGgRl61i+4OyBWg6etLv/YfXdzE7YKLr3b1K4DB75frq6bLW3+sQHoAY4EkqDpg3WfaLKGRg7YFyACQA2RRHhegjAOjvBnhSdDOFwwAGPvWZ75SfL5+U8h/5tpSf74sXBRZ1iwlfRUA0cGb6XuoUH8UJoBevsx48v1rpH3lttBe4LIBkAc4fhl9rf0fXsv3a3+w+kL34z/tX37+17Y4z4Ks/TkAPq6itq2ajzD8WkS/1NAPAAjgV1mb13r6fsn898/M/xOdVxU/rv41Wf5E4i0XPq7WH5APyDJ0eYultx9Q/fCeMt9vl9FPhex/g07AvsxBMC2OmkAB/1rnvkwBxS6sAf6Aya91r1nK5QAq9BPogdU/Fd8H95JcoI4U4RKMTfld0j8LPgj0Vyd9rUdgqGgBb29p/0J/2WQ9U6HxXz4WXZa9ewHY6P9oc7UUmXwJ2WbZg4HkAHDXxv7z6YkAY7vc/nlfenve2NmHFe0DtMma78PqrTQspfG76H/VCmjjAg7vVh6wRbOUMqDVwnzJHLsBoQiicJG+napF3Nd92NK5LQs+DwCGy+Gf5aHB4Kpe7LWA2GLGhdrK7ep6QbAe2Ku1M1C8NEVgQYbm5SKAvUBoDqo9MBxrAknxH3J+Fo7Pr4XjB6y/rzrf15hFkmfQvlv5H8IPT9Y/pP+1Yf1n4gboJRY6XvlxKavv3sALXMEm493q634B2PNtB/fcXhcd2Bz/uuxVFgc/lyw3YA24fF309X8bHP/lHz+S64lwn5ewew2ev0p3XZALIPvi3r+UUCAz4Ot1rv+m/V/T9/0G2ezeI9j7zfbDmDXjDywDRHhiMqhsizbfzPRN2PK5y1qEBcq1r/8p8PsLCGd7ce9bQL+16WA6gLD3zdK+wCDJAUPw/JqOYOy/beDf5jeRDRpKsGC7RggCc/C9h7me53oo4dm+v3UDxNnga2yDbgIUIWwE9Qg02LsI4XjBxt3bfrBDd3tiC+i9JvHnpSeLFxkWAYDq70EA+9+GwSvvTfhXYRfLfN0vLEq+6fD7i7PbgpnctuHJ198BJtYObOLOdOLgOwLL40AWZ4spg408U3C2N7j+eA1n5p6Lx3xDjowfGhvrvJUw1g2a0TySkxTtQxVLi+kBVd0jzWRhcy2ICbOGLZk2dbfrEgzWPTTxPTyUxtGPC8OQbW07ORZWxg/9UfPaBSoB4qoBDJeoq9tFZR1ijT7bVp5PzI7B1YctTxchpQvvsK/k5hTwxKydWcPkxBtlFN1a7rY4qakwPCT3hCggt8D30uOMUBinQ5V+kB8X+RYh8aPzIlF4QGWceMKajQ69WLoPxvMs1ymEJm1HTned1NbPGdVl5+pYS485vp4vVGnP2i1uN3xKPMz+sUfzbRZ0D9k8oMIOzIJdLhytBrV2sN+LyXaXKXu/h0ec9ILgOpQ9sxvroXIeqmWR2s4cjVLNpoM3bQwXocX9Izls56Y5a216S4vIMk964XfkQ60kLwzZdXzalMppIm5HcRLS3cm0DtfzGtrX2mF7PvKsE3pO7pq1rpuqy+2yOLnc+JPZ9ILanPPOKHHfmLdIc4Ul/DJfeO1sR0LEF700Dz2LHa7GOdMviqYxjzWvGpOR3RT+IE+9WdCq0cAVqfL0RYqs++GUQI3G9y3fEWJ/EaDW1kNsjvSrJmQPvisRLdRFaujOxuHq8L52tVhN3zvnrhEYDBloeINPsaoQGWvcLtADMGSI9V0ARo+9YxE/gkvhqVAntUgqrm+6F1EKm3nW/c7cak49mXruXg25UcT4eGhH1bqZ83DzA09Qj7vItdJ0bOuzFIiawxhUaSGktC0LJtgj93gXbWXdHKub57MZWYHhB7Ip7dEIW1uj+qN6r6uHHnOSUmF+tjnK5uxs2wYvedaQ+pHOYNZyHtwNO3PlUVQvPbtjZ0ondmSPhvQgiywekdNxtPZ6JSeIOEF1cMQ2rKzfG6xoMLKIctunt1Bga87leO+xjB33U4x3acs5+bbpt3slM4URukQ4nsAj54tXzpz7nMMtQihQbIBV1KfTrbZpmFI7K3jNIm15b1MO25hhfqe3zbbePyxOvvCEU5GJwIYBq2lUwHs1BfWNEp18iLKFPpO6E1fl6dTP1Hyvuo2kG703HGjlem6ZWPeqyNYS+XKNaWuNxecdzV+oGyepceeEFnKw90I7k+fLhO3Jh4Wtr7m1NT1/FAmuZJWtjw7GbsM9dINhC4wcQsKEGGEezPiKJRO7PeE2tmZdrCxcynLCwjtCua0gODlT9424b9e9TqUdDtNntQ2EulO2I7Q584TRmPO0LZutmmwKMo6abpcwGU+6JydmiF0VC15gXW0sPM3NnZBQSdfZVHrwkqjMU/Z4KMmx6ub+qs2WxkOCSIq8sKZYMRvM6jFINtvfCt6pik11spWpNBvdieYd6pll4YUUh2pnPdQevc35lzGhpsg++FGYEMR1xkGpQttKzrjjI9g3s4RuQ1HVnGlUfLUu+TJKWr1AIs9GKTe89DRHnnDftaCDsp/Hix2OckEqNsyifT4OhXTOAGxIen2MbRurb0JahoPBBsfHvkSLxrsdfH9z2oSxPfB0wW1bWw2cnhDDMKmV0Gi3W5EaC9gek9uMJLvpHIV3l7lzvpJphHTqDRsrjMS9wSFEuFu2lfFJzajocZtv20gNzgXqhFdkRruYseFYTNNExsSHQuv0bXxQuoTIJ5dA0lopKaKEbzLTByNlyvx8TpQR0U+2TPFJuL+RYXLhbpt1wVi92OGaF5gzQ5uWxMBXdjqezGPMTLsNLw5Ria05h5alk01bGmpoPNVJh5tWuhEls4xzJg/yKXc8C6f1K/PQ7iFH6RsOQPE4qQcdTe7ilqtnPw7tHac+dndDXPtNurvI3Gkd29KsYfat2rfpZsD4OZwgSHTSddDPa0LmD5lW5MeA5Q9QHNfy46YWF2GzoUZ55xx2SmbN1j7YiSf7YtWGwOF6RFH9PUgIVa3WPKGbUKbzxD11mFrYZ7UUwyLMTiPALk1ynBSB6LzVxrMsM/P9gcYNs5V2vs1tVYPKoxqnBVq/X0Yua46Oo68jlUolbNhi2Claq8LN1uiRPZ8w5Xy1qSI/QdpRBmWYLg6UWFRrbdPeWWgrTZnDnRBMmIS8uQxZE8Vp4Gi5f0MOazM3dDl099SAx5K934H882VdjavHnZ7ua4BHVelTw3SgcuWeahl+VLSziw4j/ThcHDrJqvhw3PSddHUl5+7j+qHDQ2uqqPkopVIaImUsuTZ5DH0cc0ZcU11J4fO+wM744zaSJyPSi5o31DM5rfX1ZAuXzn40TrA7DipK6uRdamIUPzysM9m71J1P7q7OGshIHisV3VVjlVGUdmXWsnd9uK29VYKYJ2WCPTw6F+sgDiJS+S5pxzs90mW+G+xoH9X8eBPv5AmNay1KC9N0pAHOiwMXYRxzuHKVL+m+lQOAEEaxkOitTpZhRyAj5tfoiSkxxmX4xjxEY3k4Df2BuGdIZURn32CPlYUajhjdqMOeJW61EfP3SzjuHFtmt7fUm5nrrJsgTejLY2PLiNC3Jk2SiFqI68DQqa68DRE9XhvorNRTKk9wOWk01VE0im50ubAT1AgMu79ddc0mFVOrbCZoTvvJMeVjmYUhteY9GlNYv80EpjDLNpVJc42WUBbMKlONR3LfyyN0PQHj0zhr9cqYC+rg7FSB4nAyNLMJ9++Gozj3hjAHnvHvXdRC0JkVzgxMJplTgBY2oYPKvism2wlaxl9mekfcLslAoGyzDzG+3Y512xIeiUXjJG4pELwXXj+Xg2Kr0Z1nwlZWQnUk2PJ4NtrHcGcMLTION0nNrs16y17RaD+waymgDY3ij26SMcXFZdmjN5fboKCUPT71j4qMRi330ktRzh0bkadGaqYo3DNKr7rydlLAjpu7byQ/5kN7oyKIicBJ5+E6G4XVdULz+XY97Gw/QsOQOZ8E+qhiJXwWHIkD3WKdJ1RzCLzrJtjDhWFFvaLT1222rmqOxakbASuYXg16CckDtLXOdX4gt5PklsnlYgePNGLnC0xgo/wQIP2iXnnFJDHcKLlUoVr2lIYVx5wG7J5rXSHwZIdd9Yyx0Is9F54b7WuG3bk2f6k8ZntIj1EYKHZU7brwQHZkTTGuyuhczEaZHpO5C1rhLj0MvYLxlz2C0GHepYk/2VnSZvzuOBXrqsOYErmX8lrT6aEzTnwWHsbgDkN4oqedizCg/DX+qdN1EYLhjjuV+wAeHQWraM1KzBxvu9rocMmwCP+kibhtQSf7Ec9deJEPe9Pm+3MwkJOfzHfzbK4P1HAWdjpv3a6bq1jM425fBlW5gXIVxfsAwc/zvM00EKYnLvLoTaO3cRWvM0qd1/ipOlr5HCmtXtUKulajKs6ks8BLJ3mGb7WOpeVpmryN1WXJKeVaxNWzSecjnUk4LSsB5KJb5axFUf7Y5FWzJkkzOzDaiR8eli9cyP68r87ouaM51hkt9MHS7BlLVEUB1WMIZaeDd6K4uY385TpZRyJXC/7MEMFNT33INy6B6U/IuYYI66opj9YqZ3W3wwDSbCz8EsTq8VzkphQOdhFLKhMd/A1zFNG7ok+iQTTDLKVluZMb7iqO1DnuR/m23j1SuGXO+7Q+XXPm6mrldq+Vp8OwWd91Dl1Hia5bQ3Yr5rbV8G5N0/0BEw5038oD3LuOGEtZa6T9JmAFBLCqxpw6kFW5t2vOuYqD694dVNs+zkk0lO7heDPPRWpdR9IUXD6OQ7D58a51Htfi2c1A/9PVlc6pIr5te7OsHhDik4FzpC2cySN+F1u8LPGObeDiMGb26IoX8RSA3fb6YDl3S0rygQH5pYcUa8yEWsmo0EQIxOja3ZOE7QV0xgJVWSbNoM6+4uDtBopVqvGU6lba58tmj7FZsYsfOYrFGwK6C+ckB3X5ykhJGupKpaQaThvtuWweO4kXIiJCEGvw1xkRFnhBUTjJh5blT5gBNnOnrQcJHnclzVyUmQ3lS2ndFo/2lurDcXO6XIzELEMbdi6JwR/XWrQFtVcxCi6nw1t2US9n+LJTAxpL7uzDPnbZ2PfHAHv4+FaDpnvL7w5kWSvHezRdtPwQFDbp1PcEHy+waT+uNdJiPulNbaQc9a6lW0UMLq5JXeF4zQySPmSwKsY63Dxi7LjLegTbauncnDyIu176Migr7OTnOzsXgrsUSkEFS6mH35nEkE+MfAXhZcLI41RRD+/CqvTe7xRRvwpZVqBCHtGhKDQdU8sRjoTepSVjzkGdu5BtaUyuh5mnmj4MxLFyMUIczuUmsy7onjmRjdKpir0OYthFoofZzQp1DqMWbL8cdw+pR89xkLgt0U3lQBU6w8Ig3V31lCKek2LD6OAwChUlxE3MmmhKlyppJ7uGm5uV3ujE4C5R1Up4E+oEbbcnCFWLozvs9QtR9iyxsWrntp9TtbjfXZ/dXBE7223m9GETayVC4Cwbq3o+lW5y4PJH2Z442cBO3khCQZcqM2qqnthRvb32iGAzaY5cQBoWQbSQxieMzcvH3tlqMAObdKPEDgM9TJzcQ8yNAUOFctpfjB1dwVV/39hQj4uRKU5tG4i1h2ycpG30tePAZGRNIldXwlbYwGiSYQl0TJp2d2aJLtswVLjsA9c4CuNneHdJtGpqMpzYEzDId8FRpRBVPfVir/NGmbyjFh9gHaS0fhDFhNGrLc3yZQztvD0eaOLjeH8E4xQiXMQgpWMrJ2gMIbJJR9/Bi+SOKta8tdudw57n9Rw8qDhR7+sNwhWm0pfOcKBK/UBc9jfgmKm4HE9CDzEDJiLiA5gC1ZMWuzjsRc744kGdIRbqOwg/N5iwnaZ1t5W2e9yzsolUFRO7HB/DOdrV+dYQ5ROKy7hnw1djP+HbxymaMegipz6XPsT1FpeNfjdCBG3tc+92DUcmJdd8So8YtNtu8KYVE05lZfFY1bXmmQfHmBXWaXJz0yWWeY+Qi77dDWf6sqGaESGaGgl6t+4bfuQogA7WHiKiIPZA6cekdgzl3ZDKSq2cKJvmCQFGaDbUKfdMcfVRuKDbdeSiFCVdUT0OTPq6ljnqaE3X5FAOBePVjLkJ6A2ZBXZ7Vm4X2xv2tEUOsoGG/sHmHW2Pw1oybgnfv+B9jx2k+3QSz5NIFmf8usfmoWuidSEXSZKbKMRGiKrpWEusz6du7Br6llzgAdRfzYTFVimQ29ZPOimeGdVIUo4uuyr1dvFWrzNhk+WkIBmmNNSzCQmop7NlkN/y5IKByupA4UEqy225628kd5NJCD5yBrtmg2gYrrHViacb0XsZZEQlmkdNsJdorJ5v7ZWDovPN2lLjrmULP95YsHDtDB5spLAxVgaCZSfi4GTzOnfCmzQOiNxV/hadmSYUZxmejxdkzdIWPfjoTSij3WmXI86jmTKeIEu0IX2T6DGFUS1IOK8JHxV9lRN7mBgwUNPvLIXiiLAXK9TECCj0VXcWssG/V5fUUzNExcv7nGgZYYmx0OgAQfZIxqMcXOvZzOuZFG/Xnb6+Vvg9qFxjLbhQptQWdYEolGXZkC5yO+scvC7IGTFaPRqPSZgXwuFI3ChTgKPdXsFmYsLC+6DJoL87riEfOyCHRivOfH32T1fNWdeNtR52B83Peqe1iPP5sl3vBVZuDjuXTnN0e44VsQ1hmuTZ0ferlB/hMFJ252QuBl6g7+d0PwvTFa8fNV/mLIL2g8xySAVKlJNae9bAdspOvoOE6a8INyEnzrqLpn0UpgCX74LnzTTsSKpJ74KOctGTwD9Mhtx4G5LbVAnRqOaAKqmM5TWLyVDACWqAYn17XGdBpkt+QivXwr5jOlH6g86DbbEdiU3XV0482+vaWBc344qZttcfnTM6Z4RUVoYxjAkiuBs54KrWsjGqFrrriO4v5JbdBbZ6vYm+i2eG0hG7sFX2+tV1GPii6REmJOlZHNfNce9AlMVJR6g3yLmqxytJThtRcVn84R6SMjab1jhKG7yWkPS0pbq961bjbNLBlJ+MK+hNbp3Trz0G0m72XWX9hzHDx9qQsQnHdvdhb8GKVVhFy8ipkcV0RUITNQ8HBaGxOQnhftP3NKwqEkcUsu6NdUNlZm+E7oVq201267yzN0HoPttp2eCctyKbNesZ9W717RTcMSQUNAgzb6l1Y/zHCQRBYgqgmiVBFNvs2M4J7NLtfPCjo8NhMbIbd+teNLPUdE9B6isbgUe0UyJs/HCnIwjYwV8JIlTQW7SjuYoE22dE5MFud500OdkHJLHZgv6YdcLR5yx2g0M2KVqMiXEENwjaxNUw67qEtQYGJ4NwRLrD5lilwWhp3LqI7lBn1jun42scleG74QUe6DiwGwggqEXgGQvgSsAIA5b62QmJcEOhoSGOzYajmGH2PaXFvcsl4x9JlaetU1/24lCXeLqfYlskXDiyjlC3XduDDHG7oSXiHj2u3d3QxTff0rctlJsGOuQkG/cw2pLSMMtbS8fxtdeF7OZy9zPYvcq8qUFqR6oSkJ7MDui+YG8MKrHy7Vidzcv+dOlyZCtwLKp3/bGnpNC+bdc4b4HKfsTIncapw/4s7ylG2W2c/I7SrOsxh76fOScpaBzOUNhMkJKgkgClxc7jW9yWMfFceNItqxPCxzKXDc4BEzMGMZ5KJYs3USZliEiPBgtKK72Hdnu5GJyUrmZ2ZxNdqcC2dRqOoc7YMHSPHty1Nm+zU15pKbBxzwWbFmoOxDsZPiSJJF/evXw77Hr526+ulpOZ/2eHQK9nOV8+rHie2vm29/HJ6+Pfi/CPdy+1GwMBXg+ymqwL346I/nKM9f6vB2/L7On1Q6Uvp7uvB8StHS4f5L7Ehdc1bT19bsrs+dkEWOF0zfJJX7N89emC6/fHik8GL8undUCJ5QOlz235+e1DxOfr5XMI34vt1n97DN/O8d69eG+Hp5/RHfbZr6tFr7eDeKAO+gH5gL788X8A0PNuv08tAAA= -->
