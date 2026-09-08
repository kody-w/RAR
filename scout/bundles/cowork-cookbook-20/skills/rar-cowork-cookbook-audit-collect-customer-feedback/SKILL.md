---
name: "rar-cowork-cookbook-audit-collect-customer-feedback"
description: "Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_collect_customer_feedback", "rar_sha256": "c7f49e4ff5249854f3e8d4207651305760fe41df49e17ef80c02de538ed60a5e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `audit_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Completeness Audit — Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
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
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 c7f49e4ff5249854…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_collect_customer_feedback_agent.py` first:

```bash
python3 audit_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_collect_customer_feedback_agent.py   # or on stdin
python3 audit_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Completeness Audit — Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_collect_customer_feedback',
    "version": '3.0.2',
    "display_name": 'Collect customer feedback Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '18abbf505d465066',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit collect customer feedback records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to collect customer feedback. Output an Excel workbook 'audit-collect-customer-feedback-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no collect customer feedback data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads collect customer feedback records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of', 'example_request': 'Audit collect customer feedback records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants collect customer feedback records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCollectCustomerFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCollectCustomerFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9ObWJLmX9G+E7FVNdgvdxDumIgFBAJJgARISJQ7XNxBXMUd1dR/34Mk21Xd1dPdEftp5bAl4Jy855OZPvz65nRtXNZvn96MwCkWayfLkjioF07hL/hyKOsUfJWpC/4uvLJo68Tt2rJu3j68+UHj1UnVJmUBtutd0SycRR04/seyyCawOq+yoA2KoGke5KoyS7xp4XR+0i7KECzIssBrF17XtGUOeIZB4LuOlwIiXln7zSIpFqupcPLEaxY4RS7E/23wyiIsgXiLKOmDYpEFkZMtgqJN2ukD2Nd2dZEUEeC3EEYvyBazBg/hh6SNF2URLJo4CNpFNfNLCn9e7DltEJX1tKiybtbB6PLcAZfPlWUIdA1GZ9amefv0818/vCXg99unX9+8zGnArTd2Vol/qsO/tBFfyoDNmVNEYFU1AUsX4BrwBjrk4JYfhIvX1Y9NkIUfFv/5n+ng1FHz06fPxeL1+fw2/wEGXrRxsGhLp2kDH0hdOW6SAcXfF2w2OFPz0n9WoQGOKqL3587vlMpq8V/zsx+fTN6joP3x81sJRHBmN35++2kBjPv5re7m3+8zlerHn96zcgjqH3/6Tqfp3OvsOkAMSP3+5XX9IgsWfl+ahIsvxl7gX7yAa5MqAMR/p9/8eYr+IvcyyZfn4h/L6sPizynP+vwXkPcZii6g++dkgQ3Azrf3a5kUP7541CUIIKfwgh9/+kdkvTjw0ixp2n+J7s9PwjHIAGCtl0l++vBw318X0Eu3bzT/MdsKBMy/owlY/pXdN0P9I9oPz/4N6SwBOfrNl39K7s82QP+1+Pkf6vY/bfiwCD+/rYIMZHDtuFnwafHrI0R+/sH/fvOHv/4GSP9TMkbZ1d6DwpfcKZIwaNovX37+oXnc/uGvP//QVSCKAyf/0tXZn9H8M7s++PzBgq9VP/5xL+B/LNKiHIrFtxxa/FpW/6v+7X1xcrLE/36/+bT4fSbOH2gxK/GV6dMEv8vGBsj6Ozv+9PYbQJ4CaNN5j8cAP/7jPxZK4tVlU4btwvDKrl0AB7dJHszCm3ECMLR5oEYdALs2CTDsax2I/9nDs8QAi3/5P94D7D96L7CHHzD95YXRX75i9JevGP3L+8IEZMs6iZICQLDO7vefCycCUDyzrOqgCeoewJQ7tcFHkM0f5x8zov/yTyh/eRB5r6ZfHlUjeaKezssz4jVdFrzPulkxQP+nJh4A+2AMvA7Qz0oPCBMmAKrnctCUWQ8Qc7ZDkyZZtvATgCntjPUzbWCrTzOxX375xXWa+HPxhGh88SxsDQwWfBNn8fEj0CrMkihuPxeBF5eLH3797YfFfy/+p10P4jOPPSgVL08ACTeGpi5AZnU5WDYXOgDpjv/wxK+/vWwLyBSgSgG/JWESPDeDyEwD/6uhDYn9iJHUwg2AgYFx86qs27miJe37Qg4X3+QFTOdHc2WIy6Zd+EEVFH5QgHLcxg5Q55sli7JdNCD8mhDU064JHlx/cWvnIWIOUtxpf1ko/B7UoTID/8xiPhaBzWWRAPN/C4PnfUCk/qFZcF9JvC/UORYXlVM7VVw7Lx6h8/TLXNxf2wFxZ1EEw+diLrjBbKpHYjzNAxYBy3gvl36cfT73HAAFnp1D+3WNM1dL81E1689F8wp6pw4efQYQZVpEXeLPpeAvr5Bq4rLL/If9gKQzpZcX/JdXHjHI/8MGhv997/PoDhafOwxBicX/x23SbBJ2vdaFNWsKq4Wgmvrl6aq5cZxd+uw1gQwP4R5p+b2L+YpUXwH7c5ElIO7q6S/PlQ8Hv9Y8QbCrgT90Vn/QB9E1ywroPoJ/Dua6ntPG+Vx8rQwfgNQPGAT+B0gBMmkO4K8M56dfJY0BHMzX37uEl7VnF4EAX1SdC9z03RdtPLv0q5eL2YLAd0OcePEftJqdAGwG6AMrA1HB11C8f0Pr59Ovov9h47MZmrc8GsUO5G/9IADkCGYB5+CZ3QfEa599OtDz04MIUCOv2ll3F2QQ0PR5M6iDW5c0STuj5dOuQQWA+uP8/dR0vhuMFQhAYCyQGlUHrPtIpjkkctDqABkAnoDcypMClH5glJcRHgSdfEYGgLyv3vRJ8XH7pVDwyMC5Zn3dOCsy75nbgEUIRAd3pt8DiPlnYQLo5fOKB9+/jbRv3GbaM4g2AAgBx69Pn/3C+7PkP3uKxVe6n/5uEPrx35uVHkX8+McA+LSI27ZqPsHws/B+rbvvAA/gp6zNswZ/fAHAx68A8PFr0P2B7FPjT4t/T7Q/kHilxqcF+o68I/Oj3Su0Xh9gCf4jd/lIzE8/F3rwHV8B+zIHsTX7bQJF/1sx/LoEVMSoBjAEFj+LYzPX1AGU8Uc1AE74XPw+1udcA8WmiObYbMrfYcCjKwBx//TZt6IFHhUt4O3PHWQUvM+D1yx+E7x9Kros+/AGIDL459PaXJfyOZ6becQDmQMwsE2Cx9UDHsZ2/vnH6Vd7/HCy98UqAFCUNb+PuVc1mavp71LjqSPQzQMcPix8YJlmrn5Ax5n5nFZOA+IUhOisSztVs/DPwW5uBecNXwaAzeXw9/KswMNFPVtvZvuAuWvnR3OGO8CED2Z/WRwNRQS5m5fzDWcG1xx0B8CG4gWISf8p20cp+fIsJX/Cd64/v682M+dHGH9YBO/R+4Pln9L91vb+PVEL9BwzHb/8NJffDy84A99gVPmw+DZ1ACO+5sCZQ1B0YMT+eZ54Zq8+tsw/wB7w9W3Tt//IcIO3v/6ZXA/M+zJH3jN+/lY6dcYygPWzT/+mmAKZAV+/84KX9v8koT9iCEZ9RMiPGPE+Zs34J4YCEj1AG5S+WbnvVvsue/kY3WbZga7t838afn0DIe3MXn4F9av3B8sBxn1s5q4HBmkPGILrZ4KCZ//uVPDa3sQOaEvBfo8OCSYgwpDECGZJEiEeLH0CQ2iKRHGEpCkkDAjUnxehdBAuEQ/B/IDEl4FPIQ4ZAHrPLP8yd3bJLBLJ0CHCMFhIoBji+0GIEb6/pJaUR9IY4jCuQ7ok47jft6YgR156PvWajfhtQJnt8VL31zeXIsBKiWhk9vnhYQZ1YYx2p90ZOiPLMRusrhKdpNfSfGcbboLgjc2to+lgY21z5kXd2EpCrmzt3U4OEDkuBUjfQIPJ7Ppik8dxrGean7t44azYzU7OTbW4N3BfcBldtB59tzdCfDvKW/SUr9FcrmxTl0ETN65zbNJVe8oOt41Nno+naRvC95aGtkujOso6v145mymbTo5A11F0PRrB5rwmxIO4n+zLxVsnm0Np24KR6hW0afLBcTXRTBhkGSRoCIdnidKT6c5GXUvknZ2kRhelptzK9x19uN6nWyUTuCEynrkzKVEZBdQ689hEC7U3aifH3qZHJ0Gz7Xnj7BDiuo6HdXUas/HkpsbxRHfbCMsHFma8uMGChoFhml6SYbjHYXiZTstw30Mw74e9yOxcfiUyad3cxLHgzDhCmwqtBXZajfZ4aODhtjSjbeZl8W5fbcJ1wu6tIujYybwd/CgSTwmHy8ZmgPdYCNwyGOXEuhlNEitLEHVd3Hlq4XLrfJltSy8K1NpyIiK6J9OSvd0nagyuLens24Cz2n3fK1HUTaxa2QJycwKJZI78ur1V5Wky1Synt8dU0+rWHqE11ehLY58fRKxiu04xJTOo8aBjKh+++aSbjiujlzrnsFGyXNM3p3XTraqLIBgOdpiqnR4cN7bYb+OtK622qrKCNwlTIUQXXXeiCJ9Ya9l5t1MhVKh3lY+Qex3PtlLQoxgkEUyaLMXzeT3VE39UmSIy6s1qZXP6fpJ5wXZdTUbGTjv4S1iIIgSREmPTmLvTjYSc+hgNLXeKjL2cEhW85oa2DNjcWlqH+hzrh61+dRxOvVnDqXStiN0xOXbDy0yucIGyj4ZzjzX4ZGcnXdxOIiXzMHHbqceq31yWrA7Zfhly8cXYhywMEdejYI6me1jGjbXn7PLiRJClmgSqjbum9UwjMFM+WNsVsR9JptRbSyjOaLOXwF/wbXpTdis8WrRhKRd6LlDEY6hpIcT7xHLyr0Z3CSuJpcJeMiGxW9IbfCceN6Zgs9VFyxoWVRLfwkW2IkKxEINbmfpKxFi3YRtz5X4Uw/Yc1iDAIRYVk3PMoPfVpvK2KLKm5LQ95sG+ajlk8m7IDRMCx76dDsHGsqxVxR/51jpu15KgTu6dwvZ3KExy99oixmUpOmQsM+QxEKwDiam5Tch+MO0ZqRcNIsdhjcKsxrd2aHP2qPWm88013nWJCx2dra7t8FRTrtB92p5sQsDoPIPvqV3eLnFrHVT4xIz3mqXRzFZzGFl2tHufMD5T9t10xa2RxGT6hBZ847Kw0KNiZW0NVB9ixTsUe3+vpy4hWr2R1Jg+rk7BJWPSZRoV9nqFqUeiuivlbbYLzVkN3vLKdTTzVNv4Il4t7ay7W85prxWbOiuojhVaaHnlT70k1P6JzwOMFbxq6CryumWqGledrpc3/oYFcGQj0r7X6N0wGZuD51z9+1VdhdM+QM1CEUdGiapWUsypgwVua5XSlW3vINHQy3RSsbOZJLJ74XYeYZup3Pk9WETcpeWuHvibsdJUARFRy9M35r1MNkFWk6PZ27WyhfyT3bKS2Q+whOqTL3WFTsDXSWlvsrti+lCiz1N/MVNfpkA7fJHweB3jaXXen/nzKekufuJ3vkcse8jjG0QofP7YeHiLcisuP2blpC45vE+OzvK665FoM+6T5CyCAlfqa9fWyYhBkeJcJtfL2OVVsF+bA79JStXmSk+lBPbIbvRhkpTDhK6iKGGSEq9HiAbVxZ54fcXyRSteqSni3aPe7wSJ1gmXFc95Kbe7oDHMxjhyqzLOZK+7LMttpLSyuhPqfXPMqnGd+IdaXpE7WqL8oy3fIgxvtZqS8jUnsugZl05W30g39MIda32Xn/jz1kSIy8bk7E1bRYd+Uyyp8FxNtHfeTcBPq92+EWAhnaCrcTW3hKhZdtUwfIzka/aUKTvpCl+W2yagteai5pu1eIUwbbD4ISzuk9YX+ARp5kbA1LNdbc4xZgWQk6U8IkcRdt8QS0m9TZyedpuqF+/ri32MVimNR9iSV/0zBhDtfIQFKz/4vZpZG8WqtGLVp6nkW8oBq1n4eInOlRKdyoL1Smk5bVdy3x33yKCtN6GNaQ6bm9ph2Uycp+/vmun0qGYM5JK8lJhueWSTQ5lSCGSGk+alQPHNdArwIjjxHXU6ShISrrgmKg2h8sdjxnegilOIyJjXbbLChCbYaB4Jn6Faj3oXbrlpl+91trLvU3G6308Kwt7DHWzRqZtIujAuYXvwyruwylwCi0j+TsWjZokAA8aQa2rTguKmk4aVbKQ8aPPK2+SV7JHbyCd32vLDiRw8A7mCKlue+LjJDaFr6HwQLDHiDnoob4xsc7+58hVWoS7i1pebG3CX0TJ7eat30VpZhhECwI7abbZXw1vj5eCx9802AhWXG3bIrdzFisnjaU4kG4EXVBk5WNn2wvVoBvDlkHXJ4ahsDqQf73ycC0WeS6y4jo7iGXVwzNzHPbda3mjhtLKFHTpdGBRUOWN/zKubZAN5I0cqTjtu53RBjwYJS5FuTkXt/oIjQiq3dGqd1lsRNkvNxCtDj85Ks3Z329KAzEt9xiy5nqAd2xzVI7PdYgJ2QTuhSNNmLKj9xGlsSO1uF6UnZXfDB8Bi646WkCvhEiq7O7FnvOnpg6l4HDQ6DrL0r8dGa09Xxeg2qXxiVPQk5rikjoq1FIf9DjawMBS9fH04RPbURjJkQfgZEB2K6RqJVViIHRkUGUkENOh6Dk1ueSckUVWf3XXofSTEde3uZVSRB8Mw87MsR6qBRebIoJVlWOptOAvWMbZ4pTRRtTkTqop3y1EEsMVcFH5QoPWW1ErC2SpccWZDzUspLDvT+loQ1yKadM60LwOJtUf+vt2yg64xm1i6bixfIKAzqVHClattzYx7HeIYBE5DnU/pY6tSnnPBj9JBYrlDmQ2lfsivzOGARXup3puqJQZc6KtYuISL9SluDXGlUhlWttKaZDUGNtYnG/QKkD5ABOiDc56lp0NAXPc7z72lUHbH4aAhSlQLjSyx0g3Lh3aOCcZmZSXpcEDqa0qEG0Q+n3JerqILvZXvYHAudIgIWMQ4k2M1aVfMPvDutj0IhrABs0B0lmTuKpuRk1xio/OS8preI1OuKfOypo7J4UxWzfq+hg5qLbtWRynXy4Hij8ZJw5vwhsVi72DsdXOV9/oRPtcjyR3FDsQXtEr2gQ3o8A4DBYU53XXooogBs6mQ0Tblrh0POVaNsY7sqC0JbZxsPV21IOUjUAz2aTvqwNMdNpxMbcXfDh5o0RFfJlM6XF9TxN+PSbAfCQhizGVGVeo+8XVqHWXhieGc6wVx8vp0PC1X58NJHl0oMMQsyG1sdfN9Vd1qB9Q6QB48OWhny3wDbXMTPTYRydKRKxoSlyX58aAM8l64xTKc6IagNJR1YbSw3HICcYhjgMn33XjtbqQ8CbgnyLadwXIWyJfu6Nadpq/HET7dd1AP6y42rTec290vcGMeKXvoa3LoYnyj0qpfUTuvG6VThOnO7Z7f2dbC12prXQN7uYwuYyh0QqfI1ZiKgnws2qy6XlEiH6zKyYm6co6HFoSBJF1SUZWErNCoc9m4ptBtdtNJjyVJ3CJ70eHLxmrtDCTB9YJJlrcxbwl9GVhhgLtR93IjuONteAspe8/EuMnrLdYqG2LTCAFh2GMWr6KK88LdzoI00BX25649HLONFC+XlaINwc5fp+kpWUkEOZ0E2aqONH1WNMsKqN1wbtWrVxOUKxy2nlPidwb0IWvxRO+cWKZ5W1kdVNxx3D0Si57oXWuNhMnVDuXt+hxcruthM+F54HGSdUeNm46vmkSDlNPR9UGGqMySQ7j64t4F2F2WEkzkULLiwCxiaADTdhRFZEWxvN5ynEywZNBs9SLJdLk0U4MFsFtOSJ55/Ehk2N1iVTeD+olcddpehXMjFKBtyFKb9frcMGJER8rRZ5ybQa8GARKu6Trm3RILrjjVmavwAsAGjFgdV+3Aapeijxu2n5shx7uzfHVDEq2hR4NYhgx0tcR+R3TTut9TMOxAS+poHnbOvRqTtNWpAKbZTvb9ZhsgxLjcxe4lVttyouiJOg4dnq7F1shCc2ensLRmLqkqsjtx9FukgApCuHaUsevryoK3NwLMWdeVW3STkOqqdTacAD/eHTff33SWRuAq28g0zla7NMZ9Ttap660LEXd1PJ0OOL8ri9I8mZhqbzxe5XuprcxVNyUZQJXByRTo5tIZTy3PW+3ownyz7W7j0aMSpONjf93srrpD0qCv4RmF0irzjMi44Cft/Sh5N1+6ban9cXDo1UUt10Xnx11OJletnvBxVMGgPepOp5N7NbbXPjx0mdTtMBku0CVz7iQtNvBrSIl7L2n4C5jJ0L5IAzKmrPOddAamwYUtZtdlD2xMELfDLgrKMRL3sE07nHTochq08L4E8fIWapIrCtm2e4JIMb8xvs3crLijuIb3MGMJ9es1QqM5earoZRTgh0ONN9zZNuHDLdLH7aYxIi5rV51wuERu4pawwm0xjWLrtjadcJ0V5aUXe72mzyRJY9nd9/2kr887wt9dLIdp9WKT4RoW9Io0DAzXjwe4RZWRVQLK7SECguEBh8dTmWunfID7NFz60CZLXCHH6A49ood6czBVozicl2lLOBRnL51k7NmLoQpn3DMLl0rgAwUm4sDpOEQuspV7GCVEkYhVmu7u4ZK4QJSpgMasN4mbFWg+ajYXJ4NyrGdcXufaC3tH+RKvwhhfr7XjWI5Vywzb/Q7i0LNfB/TQFruQlgllIzAHt596FCVxys82BXsqfJjVisItlNzgKUPcEKjFMftWOSsUVa1h6l7XFbnEcvcs6c063Otb7Bp6oHoVojM5UC3RiLpfXqtbc2DTSKjSyNv3sLZ2/aJaXqjLdjWgrX+JaxC/TnKomWZ0UMTdNTgWU4VocRc7uDO5JrWFd0XpzEeva3lQYNTVCjy9L81s6PaG2DWGaqXJ4eTo2zteShUNRalClVv+IPsXMg5CLdhZw9aIc6pZMYGtRTJV0gGnHM7rfIhbIm6LgYk2Z+ZqpNcEKUKcxQ7COmsJOir4NboDY3/iFdeRJvsbBB+FMZS5sFYIMKCXuFn0LJWATqw8KhpZ+0S+O6lxmOGSV+bNyj0qkNL3gRefAn+Zng5hskqobjzcPb1xtEugJVCu4/k9X+cnJse8/Sm+xPdtt0G8IcuZHOpCx1HqrL1rHV1u2OTe8ZTqrTzFW9OXY3txD0dIWhnYJqEYhMFPlxV1zduLg5EIGpl5r1rYoGG3anNPih2CWT61swudxSsvjqdVuifPHIKZKwTKLSn3G5YEQ20ckB5dgOZr4mBmxeSeeSuTwyT1hqY1CXRDsRRsTA3dYQYe71gnYLoDJl0DRnPAPFowJmhc2y2zhMbTSV1PKxhdhtjN9QiogxRT6dUbvVoSTBDcGk/QApfY35plV6w0zAluMEj+4ioSpopbLYjuG2UoBOpXTYAuCSSDiH2CsVxPaRc271kEmex8WWvLo1GcAlS6crdOO4acYqOKXw38lZxqjMJ3aOSP2Q49LvtsgyfyIacODehq5GOFxr2NjrTBXrKQzu0Wk+SygvfoGHHbe50L+2lnJFtVgEuGUAcvyKptbF5XEy9m1wpMZXyZGopPVGsSMU+d5RukIw2CPo5ySNgiSdS8CFk5hOhYs6QHP/YafsRO90teXL1iiZzuIs7XAYYoNBvc6gRVxw0nGsKwnrrhCKP7c5PsJBo0d3ul8NntHifIcqlVaXB1jf19InZGRK6xxm0aGLm7W2S17dVjgu/PcKvrPY3e3anYrZeNvc3vdu6QGFyll2p1UVA6X19kuJ8wZXAidDLXB4oWo8uaoSsFjAA37gTjG0lhyvrSiG4okgEti6Wly6S2Wqoh16d4ZI0DC+yXKI4BmyyLtqsh5QJI5GTIyGvzmIH+0kHUHQ8Jdi/tZe9AXXEvvp6uDoSaVeUyoSmdpPzK9aVDZtrSaQOp2PQSU6/GGsrv62FHXVayuhIkQ2OyVZ8IWSnezxK3hJG+3+GGcZAYQ6893kWkrCmkqNn5rU8V1tE3mWnCGBKqtwcuXfa329kZmRJ3u3RfqlQEhmMEEpE048JMQxT+3q7j26CfYUe9ITgZg7DO0bS/9MoqxV0/It1zvy0mRRF7Q5fdnL1s0yl1z0EHTYPa1k0XEKIjXRh2JUQOSZ4JQW5EKkbMqIjBDDywhL/eD+4Gapx72DOypMqad5VWVO6EAlqsaw3L6fPaZ/fRgcLH0wrfroj+xpE2YfsndO+ZZ7wqujuoXFRt9g6D6xKkOsNOCvfFnuwrFtRXlDWDfl0cumDFdftEj/ImX/k5dj7fwDCvnlQHX7tkyJwOkg+vKpnArphU3K3xmvXqupR6DnDAvbodawu62dX1nBTQBVxw5dKW966LQzSnSJpsSXYgb+3aWYXcqc3hVLc4RPE2oWyXxollncyD7nnO1yVb7tWTmG6YVMV1aqnxyb1E8dXpKg+gE+bDTOFyhD9GwZaJqSBjIdZYebRPynQs9xglHXG7anS3DWAKpRqWOAZE1dLjDe08I1QHpMiktJQc+q71odkZZLpPzvw9mIqjfhzuLFRNtxXs1lgTZAUM74ONeWUmrrlfGd2UEN3uFAQuvK2Mw7a0GWgK40uLWek7fKtAWDMwBMyapGzfSvIQsezbh7fvR2Vv/+qrXvNhzf+zM6Pn8c7X9zYeR4CB43968Pr0L0v01w9vtZcAeZ6nYk3WRa9DpL85E/v4Tw715s3T892pr6fHz+Po1onm94nfksIHe+rpS1Nmj3c2wA63a+Z3EJv5NVUPfP/+BPPBb6Ya1H3iBV/a8svrvcm3+QXB+U2MwE8AVrwuo9cJ4Yc3//WW0BecIr8EdTUr+Tr0B7rh78g79vbb/wWO86UhEy4AAA== -->
