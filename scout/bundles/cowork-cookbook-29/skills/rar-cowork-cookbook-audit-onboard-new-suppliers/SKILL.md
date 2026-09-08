---
name: "rar-cowork-cookbook-audit-onboard-new-suppliers"
description: "Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_suppliers", "rar_sha256": "3ebbf67a3bcd1357e2c585a70d1799fee4e3ec4423152d6435a209740f157ea2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_suppliers`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_suppliers_agent.py` and in the RCI capsule.

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

Onboard new suppliers Completeness Audit — Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
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
      "description": "Date range for staleness checks; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 3ebbf67a3bcd1357…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_suppliers_agent.py` first:

```bash
python3 audit_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_suppliers_agent.py   # or on stdin
python3 audit_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Completeness Audit — Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_suppliers',
    "version": '3.0.3',
    "display_name": 'Onboard new suppliers Completeness Audit',
    "description": 'Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df5998672b9f08fe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit onboard new suppliers records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to onboard new suppliers. Output an Excel workbook 'audit-onboard-new-suppliers-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no onboard new suppliers data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads onboard new suppliers records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits new-supplier onboarding records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning an Excel workbo', 'example_request': 'Audit our new supplier onboarding records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of supplier onboarding records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditOnboardNewSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for staleness checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-suppliers-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObSLbmX9G8N2Kq6sp+2Tff6IhBAiGEQBIgJFHucLHvi9ihpv/7JJK8VHd1z+2I+TRy2EKQefKsz3PSye9vVtuERfX26U3zrHwhWGkahV61sHJ3sS76okrAV5HY4O/CKfKmiuy2Kar67cOb69VOFZVNVORgOtu6UVMvcq//WLdlmUZASJHbhVW5UR4sKs8pKrdeRPmCG3Mri5x6gZHEYvM/tbW8+Dn1AitdeHkTNePirMmbX8AMy/1Y5Om48ItqkUV1PcvxIy916w+LurFSb+FajQd+2KmVJ4sf9AH3otxymqjzPr6EVp7vVV7uzONn48oijZxx0UVFar2mVF7TVvm8CvAEPzheupgdYBfAWG+wsjL16rdPv/71w1sErt8+/f7mpFZdfzX+8LRW8Xrt5YDZS0C1AIwoR+DmHPwuvQrYk4FbrucvXr9+rr3U/7D4z/9MeqsK6l8+fc4Xr8/nt/mP2uaLJvQWTWHVjecuHKu07CgFhr0v2LS3xvqlfb2wgG8qYMT7c+Z3SUW5+Mv87OfnIu+B1/z8+a0AKjwc8PntlwVw9Oe3qp2v32cp5c+/vKdF71U///JdTt3asec0szCg9fuX1++XWDDw+9DIX3zRjvz6tRZIgqj0gPAf7Js/T9Vf4l4u+fIc/HNRflj8ueTZnr8AfZ9xt4HcPxcLfABmvr3HRZT//FqjKjovt0A2/PzLPxPrhJ6TpFHd/Lfk/voUHIKkBd56ueSXD4/w/XWxfNn2TeY/X7YECfPvWAKGf13um6P+mexHZP9OdBrlXv0tln8q7s8mLP+y+PWf2vavJnxY+J/fOC8FpVlZdup9Wvz+SJFff3K/3/zpr38Dov+vYrSirZyHhC+ZlUe+Vzdfvvz6U/24/dNff/2pLUEWe1b2pa3SP5P5Z359rPMHD75G/fzHuWD9c57kRZ8vvtXQ4vei/B/V394XhpVG7vf79afFj5U4f5aL2Yiviz5d8EM11kDXH/z4y9vfAOrkwJrWeTwG+PEf/7GQI6cq6sJvFppTtM0CBLiJMm9WXg8jgLb1AzUqD/i1joBjX+NA/s8RnjUu/MVv/8t5IP1H54X0kDXj2ZcXfH8BmP7lK6bXv70vdCCyqKIAQGy6UNnj8XNuBQBm5+XKyqu9qgMQZY+N9xFU8sf5Ysb93/6F1C8PAe/l+NsDnKMn2qlrcUa6uk2999mmS+jlLwscANHe4DktkJ0WDlDEj1LvAeJ1kXYAKWf76yRK04UbASwBpDU+ZAMffZqF/fbbb7ZVh5/zJzRjiyd71BAY8E2dxcePwCI/jYKw+Zx7Tlgsfvr9bz8t/vfiX816CJ/XOAJ6eEUAaLjTDsoCVFSbgWEzFQIot9xHBH7/28uvQEwOmBPEKwJU95wMMjLx3K9O1rbsR5QgF7YHnAscm5VF1cykFTXvC9FffNMXLDo/mhkhLOoG8GPp5S6gwBFItYA53zyZF82iBmlX++OHRVt7j1V/syvroWIGSttqflvI6yPgnyIF/8xqPgaByUUeAfd/S4HnfSCk+qlerL6KeF8ocw4uSquyyrCyXmv41jMugHe+TgfCrbmL+JzPJOvNrnoUxNM9YBDwjPMK6cc55qAtyUD1P3uL5usYa2ZJ/cGW1ee8fiW7VXmPTgSoMi6CNnJnCvivV0rVYdGm7sN/QNNZ0isK7isqjxx8sfys4uJb+oIeaVa2ASuDgD+6gcXnFoURfPH/c180+4MVBJUXWJ3nFryiq7dnnOZWcY7ns7uc15mVfdTk99blKzx9RenPeRqBpKvG/3qOfET3NeaJfG0FgqGy6kM+SC3gy1nuI/PnTK6quWasz/lXOgA2LR7YB4IPYAKU0Zy9Xxecn37VNARYMP/+3hq8YjN7BWT3omxt4JmF73mubTkJ0GqOxNcwgzLw5kruw8gJ/2DVHD2QbUA+iPtizgVAGe/fIPr59Kvqf5j47IDmKY/usAXFWz0EAD3miD3i1UcNwDCreXbmwM5PDyHAjKxsZtttEEZg6fMmCPW9jerokR5Pv3olQOiP8/fT0vmuN5SgYoCzQF2ULfDuo5LmDMhAfwN0AEkFCiuLcsD3wCkvJzwEWtkMCwB2Xw3pU+Lj9ssg71F+M1F9nTgbMs+ZuX/hA9XBnfFH9ND/LE2AvGwe8Vj37zPt22qz7BlBa4CCYMWvT59NwvuT55+NxOKr3E//sPX5+d/bHT2Y+/zHBPi0CJumrD9B0JNtv5LtO8Av6Klr/STejy98+PgjaNR/EPm09tPi31PrDyJeZfFpgbzD7/D8aP9Kq9cHeGH9cXX7iM9PP+eq9x1YwfJFBvJqjtkImP4bC34dAqgwqAB2gcFPVqxnMu0Bfz9oAATgc/5jns91BlgmD+a8rIsf6v/RDoCcf8brG1uBR3kD1nbnljHw3ued1qx+7b19yts0/fAGwNT711uzmYyyOY/reS8HKgY0X03kPX49YGFo5ss/7nMPjwsrfV9wHoCgtP4x114UMlPoDyXxtA/Y5YAVPjzBeaY8YN+8+FxOVg3yE6TmbEczlrPiz13c3PfNE770Ue4W/T/qw4GHi2r23CO1H/j/YKFHP17/14M1QLlmxbywNeNpBroB4LrNDWhI/emKD9r58mSIP1lyJqg/MNNM2rOfPyy89+D9seSfyv3W3v6j0AvoMWY5bvFpptsPLwQD34DEPiy+7S4+LL7u9+YVvLwFW+lf553NHNDHlPkCzAFf3yZ9+98K23v765/p9YC5L3PCPdPm77VTZvgC8D6H80cGBAUGdAbruq3jvaz/FzX8EYVR8iNMfETx9yGthz9xEtDmgdGA6WbDvnvsu97FY3s26w3sbJ7/m/D7G8hka47wK5df/T0YDiDtYz13OBCodLAg+P2sSfDs3+n8X1Pr0ALtJ5iLebbtk5SF2Y6LYATloQ5BExYFuwjFMIAncQ/zHBxHMYRAXRLHCAuFGQqHfQQMtlAg71nUX+YOLprVIRjKhxkG9XEEhV3X81HcdWmSJh2CQmGLsS3CJhjL/j41AWXxsvFp0+zAb5uQ2RcvU39/s0kcjNzitcg+P2uIQWwSpWxtv19WpF/0vexodq3lTlqbuXdOcGVnC87ptj2scjff9Ou639ti6pzH4WBPN/7Uc8uBo8JjnRBkd7eLeyIp3c4+3sYw2OzNrYu4BgrdM4LKYxfPRhKe1gf1njWqsckuw7rohv3WM8Xkblh36RSPXVEFZx+CKowe86A2D5gRhdyNx6+31An1+3EdCjmeafaYwM6m3Vc2QYopxEx+N1jxSkKSIj1Zana9QFtu6bXXGz2eYEPLR+NWuxqOOgZ/yi+XOrlHt0iSzpEqqfvVZblfSea1KMXNhfdM9FKfp3F/HrILbV6sy10iLvfSKTVBSdEkkUuMxw3TGfS76ib3dozKo6VeTAC0x+Jc8Y2Ddxus6L0jSATUy7GJgXysiPRmSR+hTt0soatWnMhQHSTRasbqqlihETQIxoenMt+p5nSSsb6S7ViKwh2FBqPm7bZ7/9iduc0koKLjBsHGWK+I804mvXzaEILlnHY7QdGQJS0lPD6hirHm8tvIqd79vuf9+mQooqJEvLZNidAl84Lw2g6/yk2ku8vpulmWBi/ejIhOkpPgGX0tqtoIvH8bO1Y9lqx6sclS3/mqdpWg2FEwi0OTBht2DblpT5wXV8iKlrHm2E5ct3XQ2jIKfFJV5VyXoygVyHlqjiu2zXbN9eSmy3a1l2v6mmpJqeY6e1zalaQqe5KlbIWnwy0B9pRiZJZ1T6e66e4FF04hT4yR83aSjTRca1V9r4OU8y0kO5fHixKLgS9spJJOUGfIA4duSTNTBhafdrtqB58D6F5it2J9QupVGKpHsSPKbjOwPdz28dq1aU3aavX2NJThCRlL1oJlzpOz9uqCoHpJokf0vnbN22TDjbu7bNeVeMXLHlonLrKqnPRC33zudryk6A6uMi7F8APksdiKp68tz4n2ppoO0bQpoIa7LPmxHiexMhN3K55pmdJ7CNnVcY+Gw26d1LoABxlnxSdGSKztjeQJSDB2hzVzW5tLuYQIDlpnE2PJlAglMjcw8uUIM1BIeCu5UtcQAP4skK7IKjP5e3OXBsO6SRvRaTVhdZWQcVg78pD4deevp73aryqKL9ZX6qQI5VhibAMPhnmzePuaULYIstEqdk0pJa1621ytW5aKsFb57BXxbhETjKseCmEeLzNccNmsW++cfiLpzF+N2cXQzdYRD9AtI2I4utN7G7+6ws445Dx52PaHIgxW5PoSMNyBcaVEMiFOTZeUSWwdkwdFX+NowChr6EpfjTEjbShTDwJqy6Ppdk25arEsxXbG7WhvZJ6M13cL4U5312FZR6/V/nwRtvz2wB7YAF1jZXaKdkyS2Ogti+X9OkQSOWmOt1CPsvoeRbzMYKihwSB7W/EgHgiWcNPerpKdfCVTesSachJyorNzLZWiNXwvktpmE0ESj9i+O2hTfg/Cs5dcqKzxhERLeUhXefvO5VjuJgjv7C+OFtK6fuQ6pKMt4nCxKfx2VExeBhXXiZzLIt1Iyc50gHPBiPUzZF6WOzxtAr7RQ0GBdl13CnaXjKdC68Cnmlzjsn66GubApwcxoiQKrvTlGMsCTZ+XMcSVDn7MqW4j6ZjeVgkRepxeLw9N7xPI2N4mmRHJmi5uG0w96Nlu7fkFH903DkqJ8IRNVQO1JycJNpQUazGf2D0R7Tarm6ZHQZ4flzRr4nuKTtxyV1haX6itIkqjEElhvqscsmY1+8Dhlz2Gny+8JkfVFairXZOTjooCGwn1KrEViYmb6HatGJIaatEkhGOSrBQ10rm+la6a6o0835cZj28LRhVNlDEzlD/zK4blhPPkhK1qDObqJGm7q++Uey5S+My4nFj1jB4R6zzhd8I2UcFlOGm7jgLzvuX0S1dv78jteL4AJSqBsQ5x2t2PSJF4+YaXDnYRk8uDziydHNnBo3HJ6vOST5wlcIMqLQ0BtPrKtnB8mj9yaaJ2HYScgkGBUUpi3ZMTBUV70W0KYvrJg3xqwt0uLzi4SSmnPNBtyU6cDKXZsFoL69P+mpDtNikTeKcKInodp6hOcpHKD9gWY9X7vYX1pRkLxy0FL3ddWYy+PsBMMUi3u2Qkm0aUBfQ0ekKn9BtACZGi6FEjZ9BGztZbUQlPeOkQES6vMSSV9lDHCUJSd0t+HdShvz1jca6kDoKRU1DFXeF6MintvFq67sTbFBbluMerZkiJy1rZIR7pjdedUjF3GlslsLxvWV+s9iAdC3HyOV6q1GwU8k0s8OuVRR9pSjbb5uCtHOxEV6ja4gl+WhNiX8pk7NJYhFUonuEBrMr+EXUw3o25qEA1/FbjPdteNhacGdjYbS9lTBc8u2c1UjB1Zmd45UmtV+vC2C8PtCQ5oS33+NKhjXUo3o+jVWDINF4QTdRW21Aio/jMHfRVt6E600pZUZ2Si2wktMCdt7xCHvaDha4u9BmUdVJxjXXerhlf1DeZw8qjlzJrZ5M4B0Idd/TADhy33WxEEoX3wCO4xvFQr62RUNrua/ECaBjDLxrOe9LqbPhIFbsyLDD8sb+eR8cSQ6+1DbIlnHNB5oZ8gi6judZLjzvXfH0ntqdeELkqbi1Tk6cIYs8G38kpfC2KK3MIiKOaFOjK1fpL7Rq3lCzo9ioEW1SRGXXk2LTAYzfcJK4/SsiGF9h1eAz8TL9f4Qrhqc3KjyRbaCHAMrRCXxJeCrZkDUGa7pxYZhBsubZjpz60u4lXW6jYbhwGS6fK0u/L40VerwSTBO1vF7U2Z4qsSBjL3Lsw9lW4tHA+5vFmp61pzMuHwfMEj1JyeL+Lc54jmqYSd8mhtRW2YG5kHZ87HfReB0MONBnekYqy5azsVp6wSj2fyJXQOHy2lkhk2Y9+zRHFXrqTWznwQwdcmkJKSbKy5kfMU2wOqySYSLTj1iCEoMUmBRc2bDmsh1HgJtUaDsM1360VnjpiQaIr+xXiNHdxqGgE9MMbKQ5Ks7tmNtsmVTeuNmNk9XtRkyKlhO7B7YR1fbZD27XXXxxleYZ8iItOZMWpGTnZxnaV4Y5vrTEbUUAferhMA3/eV5m8tlrdZzlZUrZNGgJ+9Y9HAh8j3zKdw3knsd2uTOGDuBKyZmRPYXyu3Spgr2N02mZOq+jaKWtdBcXyHSOtFD9fxTJ6GCGWcw2JtU7hskITKYED2V073GlYWR7L7ddD0oL8WWljux7Efd1j3ClqEz2HQZOI9Ym5vp4Ol+3Ga658YbPYJDUakbSKsMbUCW0ZftOcEA/qYhw2PMgkSmerNMmQ6LsqLQwZFhGwFdmdj5RkkjshiiYv2KssfTtnHbnpWdKLJt2orjutLlhxpSKXYr+DKbq7wGrsQfREZ8PZ88/3cJJ3EnE3LwqTVoYctXmVXzpzIw5X1JM2ESVnqU6e3Y4luDaotXoUuph2vVIDpBwHXU0aNnkWdR+gXs03nRLcc1w0pfv1DCj2PI6RJOpge7c2iH6aIkLU+Ninxd0uhXYbT7xm5+mCO5Hrh0uHE5cGVOwjfOCDBisTAy0Sk+i7ipikFaYTkU0N/cV0g2O1KiLEuDfyedm24vnO5OWKR+tzW7kcoQMKWsEWplXBLh6GjVpQtC6pdyRtdpUJ8TpKl5ReieYmbFlSd1axmq1CJIA8S5tqrpd1z/fjNVGoB6pPlwe/549Db6XGxu6QoDJud3kKM1npky0ROYlT73yCMbITBtoZQs3ZxlHVlZhnNZuaboO3nqGcb9w4aLV+SKo72nEqi99cmB2UTAwQ7yCI6t2IrmVVT5Vxv+uKHyu4raVaOy3xfYhK0qGD85Q1ovXIJMYp0W05DRTbsRIShspMuo4ojlKUZ2opclDaM52E5IkwMEETw0uFWDu8wU+oanURe9+gYVw7S1rUqYuTa1y2go4bDD75nGhd9ruzdrnt8tzKqmxPxGhNdY2hMMTR3i7P1gn03ZIhaGOj8qRViRVoOEfG2yQGkvBIDhXLk0XRjsIDAIDulrJqBzzFVjR75y0r6Dk8STdDgzeKziprPFlGZcCpKw50lRfBDqjYqK1NKwuTWQg5yl780z712b28RYNctk7bs3G38sM925PmJoLKNsAUziCoW8xdMRTLdGm/2ydgC3I4w1ZCJOM5ttdV3kuUGVOFmuipeXZ0S9h3rumm0XE54WXpyO04yKGLqL0DWh5R9vbqxG2u3pXg6PXezo0siWqb4rtVcbKOW31ARoSQz9Jdy8smbyoTUYItK12xATvdRw1pNTM4GzdCbi8TwN7W8+5oSPuHW4zvGiqdPHMS2/hMO+pdQG8k4yZH50KfigItdpOao9NWB4RcwwOJOLewaO60qvRAGTE0Lsldo8mBStDDmsbb+25ZXC2eVNFeYrqpif37splMOIuvxn7tsjU0ycoV3msmMlyYY+5cW03a6wdoT1R7Adu5m+Kk6zZHK9yRhbfhUGgKiaCh3saVmB7QO00NOKY4zHrP1A3honZV7Pmp9oX2gNP7E1dNe6TYHnyDIoPqlFhNZl/vOqTyvGcYXpYfajPMiA08Lt1NXh7CKCMc3kMlHO7gvqaMDD3j0zKo9NOJGttlVxcQkbEiHm68xGTNvUjZ8GadFxHJT6xaBUwQVRqM5kPLkcJxsFFtWS6ti104mG/dKq2pl8c1ssny63EoJhtzltdsi1uHETsV5kBQNhT3HtpCHdZBsNGhUpMUvYxgExNDYbPiAxu+YEem21nEvQVb9XgXaJSRVvtk3Cvx+bLDY5EqAjQ36NE7o+T2SvrKmPSyysOFLXjiMiwY1kmGA4WlcQ5pZuxYjeVvtWk3NXc3DFRIQeFtfou6oRLZc4Ecpr3TEEEcyzf5YnsOq49Q6GywG1bimKlh/nQJbnEBUVPbJt1R96REoZYbE1rD6GhySnHzklj1CCdCJ1rfdDxENlVTX/LO85WbsekRikmm86G5X7cS7JfElay7YkChVarGTqiWrKzteNo7Ro2ypKSpGLpITNdnpKmOzk66i4ZQZ/tjtTWaRp/8DVmYBKIG5Am20ImPUage7lB/GbEwwWU3Y+rRjpilFJHnfGARdOBLrVzvOJD8uHyE3dwwBcMi2EJwZBhvOv+64Vplq8UObB5SZSsLXq9UUtYfWa04IzTiBr1b76612CdchuRHjENv4jplcPyUjVeEWkNGAXvHLdQu7Yk4HTd0sDJbPaRBORgHj97eReSCBqeeylwsAqCLbpYXmkz5xrte1XxAGHyCD/d+DzrRfQYVdr2XVQcrTGNCt+wgMxIQ2wgXA7qg54PmneLJSuTJw92sy5ZtQJmynVZTmMC1ttrkrnI2b9JSwxUUF8mxZcPlYaPXespQA3UXuxzWFdAVN3qps7nimUpTuHflpAuZU9umiRVN5rKUl46CUDhetcO9KDK9GBkHfHJBS2oF8Z1yeuuA3zYJB5HHZYJvXYMf2uPqeCPHPVleLeu0RO8VX21ZzsM4jN/1HkNaSEVgBzLLlREOsSk/XDX4uj3W0wRZqTvFKDmq8kTTV4+6EG1vKM3kI1jXMKUeRb58HyqSQpdEpLfdkqhsRNxbzVVtrqv7qktdL+3vMDKSnDYlbE5s5dP1EkgeWR8Bu5GO2hkWsp0291a54bSIldB+m1dbX2vF2G31kgGIQWjjwc/bk8vmm90YCWMe6QbYF1KC6yhBCjYcNFovkRVI1uV2TY6sfkImbY8TqrlFD/6w5GW8O/KHza3rV6WyUomRXnOcMZacTMmxR2YSNh5CV6FoXl0xkm/am4H3hMlpFFesGs+iJnfldI4qGFR/SCO5Y8oKlbr1EmoKs2anE7bJ7CDnjX3H7iWK1aHztBx3td+VoziOygQXkB+j1z7MGNi2jda8HsAeRkKRyp0qSlW6/cm5LxVt7zB+pGwEps0oK5Vpe0SSylZa857by8SIkiagru3NTOIltL8Bt3FZdJu2ndNw7NQyZoLijDoBYt4R+f2I5qe73Ul77JQ06/tB0FlqjfU2ap+OPmhSC0oFtO4jBHuPQkLjS29Nn72Nfk7Iy4Hb7uwNUpBrGQrys3LAlyMhXPN6bCzsEPgVdr2TO/ruwGKSM06ZL4F3OSrFpmUY4gijmXeCcflVEqYBpx2YlOsiPjlvY/nALSFtyRwZmWB9lBMUjGl7wYgYc+gbEs3gBtHLrr1mVHnU6HZv6iucbsjWI03ERPZZcUhXY4xuwPWuz5ATA8hky3HjjkXwog1d+2z6KPDD0j5ETEz3kmozJJc22jI78lN/Ifb86m6t+kwX1MYjsG7HgnKddqDHwNUYDkR1ZVeJH5yjHot4VeGXAjXc2O2+QLw9cWyyBKPoiZjWccwP9TL18l4xcXOqyhYZuhOHCwcT6EGlG/qSrhkTN3wj3fr6dSpzD7T8gD2n1mq6bQcjVJE6O7qD6Nzb3mO1m7YBk6AcFpyPQ41uV3xPea7WUO5+n4r3uM2Sxs519DqlMDN65qBs24M/1vH1YiFWbywFsleYZYMJiJNBbSF4loHHy+x2wYYM9IgdlCvbYJwI3EypyQjb3ED3trdZ4sxVvJ0JvV3FJ9hbs+kao7PM2ZWBFMk7/XqaO2wyg3F5u8Guiqd46/DUOwOFniaQTUq0ak7KdtUTx5FVOXOSSYZgqbCIERK6YaZb6DbjQeRm2ayKm48TJTGUSOdokNKfq4yDa96qMKcLqHmnI0fYcTis87MK0yRbhr01dX6VFX6KYcvjkjsF7pKt9Y6OuS2m7loZXkuTtuToCDRqHX8bmA1A1A2IiTrARyhcHvUxmFh+Pl75y1/ePrx9P057+++8+jUf6vw/O1t6HgN9fZXjcUToWe6nx1qf/lva/PXDW+VEQJfnqVmdtsHroOnvzsw+/osDv3ni+HyH6uuB8vN0urGC+V3ityh327qpxi91kT5e3wAz7Lae30Gs59dUHfD948nmY63vx19N8aW0Zs9F+fw+hudGVuO9fgavg8MPb+7rzaIvGEl88apytu11/D/7+h1+x97+9n8ASwjfgQsuAAA= -->
