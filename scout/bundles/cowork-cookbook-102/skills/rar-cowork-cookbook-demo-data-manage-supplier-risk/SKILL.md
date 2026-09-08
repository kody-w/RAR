---
name: "rar-cowork-cookbook-demo-data-manage-supplier-risk"
description: "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_supplier_risk", "rar_sha256": "6d5446811ffe9f6554ba41678c28e20940746adf160a068f8d81c2ee9e08f9d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_supplier_risk`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_supplier_risk_agent.py` and in the RCI capsule.

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

Manage supplier risk Demo Data Generator — Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); production is not permitted.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 6d5446811ffe9f65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_supplier_risk_agent.py` first:

```bash
python3 demo_data_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_supplier_risk_agent.py   # or on stdin
python3 demo_data_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Demo Data Generator — Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_supplier_risk',
    "version": '3.0.3',
    "display_name": 'Manage supplier risk Demo Data Generator',
    "description": "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07be064bf07ba675',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage supplier risk data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage supplier risk. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-supplier-risk-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage supplier risk records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo supplier risk records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo supplier risk data in a D365 sandbox legal entity for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageSupplierRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSupplierRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZV/ZhEpMrKqIBMQkhQAIJlK5wMoMYxSBA2fnfeyOdYzurXHWrIvqp5bCFYO81r2+t5c3vL27fJVXz8unlELrlQnTzPE3CZuGWwYKrhqrJwFeVeeDvwq/Krkm9vqua9uXDSxC2fpPWXVqVYLsYlmHjdmG7QPFFE7p52napvwjColq0fV3nadh8bNI2Aw/9qgnaxS11F10SLtZT6Rap3y4wAl/we31R532clh8WbefGgB5YUyzSEoi04Ec/zBezVLNAHxY+YNR9v2TRAsG9alzkYezmi7Ds0m768NCmCbu+KdtF6PrJogyHNzl+ahd1kxZuMy2ycHoFeoWjW9R52L58+vVvH15ScP3y6fcXP3dbcOtlDRRau52ruiWQ7vCm2R4oBrbmbhmDNfUEbFqC33XYRFVTgFtBGC3efv3chnn0YfHf/50NbhO3v3z6XC7ePp9f5j/7vnwYpqvctguDhe/WrpfmQJPXBZMP7tR+VQYoDFxSxq/Pnd8oVfXir/Ozn59MXuOw+/nzS1XPPgIO+/zyy6JqAL+mn69fZyr1z7+85tUQNj//8o1O23uX0O9mYkDq1y9vv9/IgoXflqbR4stB57k3XsC8aR0C4t/pN3+eor+RezPJl+fin6v6w+LHlGd9/grkfQadB+j+mCywAdj58nqp0vLnNx5NdQtLt/TDn3/5Z2T9JPSzOWT/Lbq/PgknoRsAa72Z5JcPD/f9bbF80+0rzX/OtgYB859oApa/s/tqqH9G++HZvyOdpyXIlndf/pDcjzYs/7r49Z/q9q82fFhEn0HG5OkNxJ2Xh58Wvz9C5Nefgm83f/rbH4D0/0jmUPWN/6DwpXDLNArb7suXX39qH7d/+tuvP/U1iOLQLb70Tf4jmj+y64PPnyz4turnP+8F/K0yK6uhXHzNocXvVf2/mj9eF0cAdsG3++2nxfeZOH+Wi1mJd6ZPE3yXjS2Q9Ts7/vLyB8CdEmjT+4/HAD/+678Wauo3VVtF3eLgV323AA7u0iKchTeTtF2kDxwECgC7tikw7Ns6EP+zh2eJq2jx2//2H7D+0X+DdWiG6C8BgLTZrgDTvrzD9ZcZrn97XZiAatWkAJMBpO4ZXf88Lyu7mWPdhG3Y3ABKeVMXfgTJ/HG+mMH4t39N+MuDxms9/faA5/SJeXtOnvGu7fPwddbslITlmx4+KADhGPo9IJ9XPpAlSgFMfwAat1V+A3g5W6HN0jxfBClAFFCnpif09+Wnmdhvv/3muW3yuXwCNLZ4FrAWAgu+irP4+BEoFeVpnHSfy9BPqsVPv//x0+L/LP7VrgfxmYcOysSbH4CEm4O2W4C86guwDLgIOBWAxsMPv//xZlpABpTOBfBaGqXPYjbHfxYG73Y+SMxHFCcWXgjsC2xb1FXTAdRfpN3rQo4WX+UFTOdHc11IqrYD1bcOyyAs/QlQdYE6Xy1ZVh2olV3aRqA89m344Pqb17gPEQuQ4G7320LldFCFqhz8M4v5WAQ2V2UKzP81Cp73AZEGFFP2ncTrYjdH4qJ2G7dOGveNR+Q+/QKqz/t2QNydK/Lnci624WyqR1o8zRPPjcXcSTxc+nH2OehEChBSQfvOO35rPoKF+aiZzeeyfQt5twkflR6IMi3iPg3mQvCXt5Bqk6rPg4f9gKQzpTcvBG9eecTgs9R/7WIWjy5m7gMWcyOweOt85nLaozCyWvx/0grNqjOiuOdFxuTXC35n7p2nS+ZGcHbds3cEZBcgLp/p961Xecejd1j+XOYpiK9m+stz5cORb2ueUNc3wO57Zv+gD6IImHqm+wjyOWibZk4P93P5jv9Am8UD7ICfASKAjJkD9Z3h/PRd0gSk/fz7Wy/wpvNsDxDIi7r3cuCjKAwDz/UzIFUzJ+qbR0HEh3PSDkkKLPa9VrNdgb0A/QUQIgWpB2rE61dMfj59F/1PG58tz7zl0Q72IE+bBwEgRzgLOHtqSDsAV2737LuBnp8eRIAaRd3NunsgU4Cmz5thE177tE27GRWfdg1rgMcf5++npvPdcKxBcgBjgRSoe2DdR9LMeFKAhgbIAEIV5FCRls/AfTPCg6BbzAgAEPYthp4UH7ffFAofmTZXpveNsyLznrnYLyIgOrgzfQ8U5o/CBNAr5hUPvn8faV+5zbRnsGwB4AGO70+fXcHrs7A/O4fFO91P/zDY/PyfzT6PUm39OQA+LZKuq9tPEPQsr+/V9RVAFfSUtX1U2o9zQfz4LIgf/4QGf6L6VPjT4j+T7E8k3jLj0wJ5hV/h+dH2LbLePsAQ3EfW+bian34u9+E3GAXsqwKE1uy2CZT2rzXvfQkofHEDgAUsftbAdi6dA6jWD9AHPvhcfh/qc6qBmlLGc2i21XcQ8Cj+IOyfLvtam8CjsgO8g7lNjMN5MHskRhu+fCr7PP/wAqAy/J8Gsrn4FHMwt/MMB9IGtFxdGj5+PbBh7ObLP4+y2uPCzV8ByAMcytvvA+6tZMwl87u8eGoINPMBhw+L4AHFIBaBhjPzOafcFgQpiM9Zk26qZ9Gfs9vc7T0w+ssTo/9RoMMbkq/nsvA9nM9w9wT+r6UEQP/PYNh0+7xbWAdV+OUvM1oEz05yxtvZuvWc3R3w3Q+F+dqX/qMkJ9AWzEyD6tNcIT+8IRH4BrMEKELvYwEwwdug9pioyx7MwL/OI8nsk8eW+QLsAV9fN339PwUvfPnbD+R6qvgFVO7yB17b9YUHIg+g9KPQvtsDCPses98Mg+K//FDz93L65Rlbf8/iWXPnWjyD5SN654UfFuFr/Lr419n9EYVR4iOMf0RXr2Pejj/g/1ARADgog7O1vrnhmzGqx7A2iwqM1z3/b+H3FxDh7sz4Lcbfun2wHODdx3budCCAAYAh+P3MVvDsP5wD3na3iQs6UbCdCPDViqAQJIpCOiJwfOW5K4QgKR+lQhSmVzC5ItwgQgjYhQkqogIK8dEwpEOYiugABfSeGf9lbubSWSKcJiOYptFohaBwAHyFroKAIijCx0kUdmnPxT2cdr1vW7O0DN7UfKo12/DrSDKb403b3188YgVWSqtWZp4fDloiXohC3rS1IRun023c+Qc352u63Ak5228v7lgeWIZacQEZEIIyxZZ23hTmWfDXRS6pzB02IMOka93H7tl9wP0KhQvydkLGeOAO0ya7nynyEoyrO30Zb9T6LMeNZfXtNJ3U3Mf5OkoTDTf948ZizLSzxkxK9vX2RhI4uVzZiLLdwLSwrXYOYSmCfN0ml1axlNCYTH0np1N7TEX5MvpZz3nOFdEUj8QJBSZVXa5u286qCiMJHLvTnObIbTh2My4vhdV6iUZRXV7kuLaXUyHtHaNy1Ox0daP94W4bhzGzrkm6oySLU9vT+YxXsrMb5HGDe1HmuLWUu8kt0zC+DiA8prQt8LtuIhO1LGtChjE/umPkNFr+ILrnDXOqUkXudkWlVSdRuozWueaN87kVjFE/6mqaxnfb4e7kgT1N42SVeMEq43G7G4z1lDDqZKX+zUwuVCUCFYpWKe9jHa8TXYgc21w7bJW7hyMSb5YbBc+veepcTIpV7im5dy/ditAvIYt169uWX97OrJxVnklujplKbUd/zNf6oa0r0TnYKyaz5O6cZen5UHPdeDuKxlFSoQ0PyZxnCKLACPp1ZabacCF9gvLvE1YXQp5bhStr+nG/2W82khauEydrLY/oj55wThhr7xKns8Pv7nUsLnd0wZ4QQtwbyulu6OcDDinn48nSSX7KdwW8PPaHeknt7arSUX/aclzWcdPEZ1u6YNxhKoyuywQeUhmKw/Pb8aSoue3powwMzJJ8a2quEdmWl5246gwzBi6XfETBep5ww9QPF84nKVORDq1kIHViIFPNuHC7DtWit49Ww4e5szkHricoLd6R104d11yQbX0fjxJXJXjKr0MjXlqlY6rm1aY2mL3i6U6W0hRlEe7capyJqTTbwhGaXKPUQvZnqUYD1pzG3RrE3Q4OUcNBrCgjOlWe1utALVn1hJLRRqxQbdxFYx6acXniiigNIDqBLusAajfnDIJ5eaQ1W4dRaPRvbHEcPV+uK8I2tiDZOtLfTxvs4FyJu7FHSVnO05u/YiS2V5vuCtEeE0SD2LaHRo52GurqXOOzauGuBbFcW2FJnrmdCGOsvpGzrWOKV8Jk4JrnetOCCUao2VUv+JAkGJfB3g26myjBeiU08R3EDotk6Nl2tVbc3Zxutd5NdrhuKOxUAzU95ipcD0pylIQBhKfhVg7a56eUNxNxdRlFyKesy3Ub0xiX2XQlKZfiMO0sg76Ru1Wmmv1FDPmst1F3aV7q2D7p6HhkcsvI12iKwOJFT9eHIO25ARmq9Ykb2CjlaeJ84YxbfiTqPSS27Fno25STTMTgHPF8YYGFSuIm2/lWa7YHm+dcEE/lQJa5opqr4NzcXH650/a2dMMNdu8FAmPZe3F9oTsAdSODxKpK5HZ7ydLGQZthSDJqTWz4PV9poCKgprSnOuZKM6scDSUoO1NXRjlu7+RZ2bqysNv7kbxZD74wuYze92zgVkpdkgo77OCu5ZDKF9l6vyPoPcN1ag1xHcjpjBktr2i7w7jnhS5N7CulYNs24dibLm4cWDgyKYuP0N3KyGuAOLVyUTi3KXNfWvo+KWqr6KBudc1hO4IdKGRjXlbbtbNMQuAufwlZSySgRH2L8QUdr+Hdyh/Zkg0aeXSF1R3r0+roXs2hlQlif7K6m3ExPGJKpZhQ7/zxDCqqqWgXyt6Wg3HiDxrN2fIas3hL1pYxAD04q5WRi471yHkI3SISRuxvO9Dqs2vh4ERGfMMRGB6PimWaJhEa5fHs3jti2G3327OUyA5X6JnOyTcvOjNXsbEjwyHN68YpEosZWYXECMNK5To+3jNtxY9WVYlFMiC7hhSI/mTsXHjto+nWh21py1TEyfcqqorvBcHQt0sGReWZOkyaMR1IQa/U0rYOlruPGNwMtp1UWSE3HS4atr1AZwrJNAJ1jKCTOHEd3u5kbd8pzIu2grfiMQhbXj2r0aiiUTd5GaWkE8fsJeMwXCMTXPD3Ll9fr4h1Fc7GYJUasvaGATlGLs4I/p0y8HoX4O20krkMFkaXTJmQwdu9WiQ0a1T64WTtYpFxWj41CUmSfUtjhsaUa/hAt5TnTClFMhSOljtV3PcGRiSqBJ0I8nw/HkwX8VkhRfkDsDm6REU7O60Q+WjmhJAYXtgdC/xO8gzD7+Qw3wp+CJfnLuG2aIZOgiTcRV7euNRhRZL7mNUS1seGaZ1VfORbySYDF8KITSsiYvs4gDTvLjEKR2fyAYu17FSHthE2TF06JJTcWAK3KhGOlBvpXq3U2CiSJCiU1WR9nfLqgF2K7WRdOaWyN2m6snejm1fcPtXl40HYbgsnj5fSkuaMOttWxztNWqkyWEnkYNaw1G2Ar4I48tJ5v+m3a9Q5O9c4u2bONQxwy3KuguX3h3t2wCeRYWE2Vi6IVxzxG1zHe9YnePYw5GxyVxKtUwKjSJyUTg/n9aZoNmSdVDmr0wSR7de4quzWbnG8reNteO0qd1tdNTW/39jqpFgaLhmDKK+bS++6sJrnuLxqDbfu8/AghPBVtWnRiB0QaCQZ1EfVm+zjlTpUolJjhdZWai1atsWjztHlAcbvnW0u7+XRCgtHsSp9L3gsa001xtP5jdzzG1qUxWV5gVDbS2WxVyAnX/Mhu0wQHuVToqgE2i+xHC3gAllFrcPY5zLpux7dCtSGC5n91FwOdDcQt6EdK52canZjnHBQfC4TRan05Okr7SCFurnjpRHOV2veXsuNwbidlV1OhMltWEFTh4IDDBm9BNVuszmjzSbcbw6iI8OKXzepGOMtdSOY3mVTF6TGYef4Y3cZuCTK1yrBYE4gphsUIVZnG8LyJSQ4vOyKF84dfQ+NBpU7WPxWl52I5RsY48M23/SQxyBtXstjA2HZvss3erxXl9d7UIT74+kqU7GZq9zkpA3h6rh8IXg65KfOpWpzFwyYE0FQsFFE/OyomOHJMq5eJAlNuyVlhmdlnbeQzOKBr1jX+8Ek5bpJDAA/rn+1p8syVK311WxqI94chMA9+3dDVjIrPRwT1xOrsB4VA61YrBg6Q2L2ouney77fOrqzH4/uUS/I7rTKtMmeQvWgX2v6ksZGZh34VVGlsgLrMsP2axXNryxjE1a98wuR6nkLXa02LOZlndRVxwKyLsFu3PkgDI9qErNAmoztFYkiw9vY0jKRSxveyYa8qRjRPAXcteY9AMBHxfDP/tYLkaDPKdbWGMye5NWElDJxPQcrqjTVnXDPQWMr8CYvqHtbIQXcYtnMySDSFbBIwpaFOcLLZXHHl1qJTU1E4UgN0asTfCSQzK5jBz0VyHFwJ/hauTTXKwd/SZonETmu4npSrfEwOJy8jfjTdEAlp806M1C5rS1rapbacYiOG6m7HEZlSFWFkqUWhg2Zs2st4AW8cI/ng1vtdggJi9XmZvTDvoEJurPvy/XSkaZB9Dc6APrgVuJDfllBBF/252QDmu2zGhSQ2FvidRk3VMSE7OZu3+LhCBHsBpcC2NtzWL9HFUfaLlcdtpmgCIIxN++6yLI8rnSXBhVfzaiGxwhSGHy7UhMrC09kwKi7FeKhJBMnfuwMEiuYezItXZjp9o4hOw7GW9c2hg/C2F1XpH1YEdg+ygMEuRLCKoyaKxQUAJE4+QLd+NTSLLHJnKMV71rFP/Jqp1XbxjhWpL8UlnUk9n4i7/NA6jATvlFLbdti5w5rUDR195JF+7gjCtpVLXIauS8vrMrJA7bnXdJCfYWoT7aTb8vmLO7oElVkZHvcqepyhxUxkQPIIiTr1t9xJgymuMwEpHYB4ibYFI/KJS9qo4kuMgSJGDwdzDVj9Bdmd7836x1ehzFWd8eQKEwFzDuRZYfOIPNO7GdTe73QxE7YchbREsi0p4+6Cd2vEjrkZswPMezUy1xbFhu1UXVdjfSTrCvXS31011xfbY3JQ6VjJLHSKT41ZaeF0YpLT2DWK3ydoN3rzmGRKWBAs3blEYU0OeymDUJs3s94jTi7DvRRQpzYhnasWs0c0nxaXTTDHoi+NJ3o5GYiUhF9eJXudypYVpK1YmRlXXUcv8ysQG/YYkK67nDaIXFcSjvfXDeO0yWR5WMyjnQ7a5ecXJFzb1v26PlN2F1ZiPRM4by/gva4PLV+JCFL434p42a3rICbo50/Vk13164naHM8cvBENseVe6HNzYifNyRaUqoauD5jObAbKV6qyndGIRpd0pJTeg9FMo0sd3dcGlfEJFcJclE1URmWguv5Z7s7Vpej55w1RqcalWSaA2jgbjC0Z5eMK8B9BDthL6fr+niCFMsi9qR16pXstjPH9dXSAo4G4+xWnbS0urNoWSJxoznM4dLHuwQdriGOo+PuJlRWY0nkppgA8IZaBRflitqHUGtfbFxoEX/U1fvRl7gqwiSTKIgVQ6UKqZh0X2oGur5nNzGFSikou2plaKPqkWRz7wUiUzEs0BpQHnPVjP1VZtEg6+ksMk7FcGe6u9OdWu0WGjgd9kaOrUF8y+jGJ5Mwg8SbQGpKrUBrHI2uRsjvjivCGWI3V6JUYXgjG9GzueSBA5d25qQhVLpJxuspjk3LnjqU5fVEHL34hhEZcdmMKKprTbdNVnSgnI4o5PoT1dhgRtPXe1Rcsqkt3XcpobLkeQPtQghiSwi08aK4B+NulN0oj2LLvdd54Q2jLo2MkBVbOSZ+0CEnMgdSuBbxiGXgmg8iiBDhyx3WeiRtshNbC2t3YteYag98VqgcQ1HekjB1b73vzSNIFkxDa1Qxm/MViylyfczuzsRxnNGiy63m7/BLSvAnvVgfNJNG6I1S4KpGxibbh9i2RjdQd2ua5jZhnKGl+s7rmZ3eo/B03kpIppijkvlUNK16vMQOHYxc4UmC8Ubre/HiUMswhTtxiYsJnZ/NCaHB4Oa4usAbBWykB+ZQHNhhCdH+OUDP5bg2+T2xPSFIqrXFuu433A298419bG/3yBVd31oJeUfE7R6+tw0ctVR9a51RYku8PbdLqo/SrhcS3OjGeE94upFW00Zz1wytQvBGyI+ac2ClRlTXCOgpWm/Khs4+2dodz4ghNtcUlbpMGg7x2ht7yhXbvbYMUCvzTzG5pNbnbOzbG7O07sf8cIdoSy9JCpfL23LpbFlnyo1sqzRnUyUtZNj3N4RXOiKpfP+uQYOqLV3upkcBF9tC0+HliEArD5aJY6o2K82FcQ0kLMnbu4k/tngyULZ6EKmlN9Z5cETKLRWpBp7YGnq6d+ilADwJV71l9eV4Q9Vhz9mCeMRhlk6qDVbB5NBXV0rj8bMYpdMF9BjQZYoDt4XzhFYZu7ipBGzZcG/BSCXtTvDJxQVrpMqOsGV1Z6x00Vr1RXwOb6dppIaAEQTECALsvIKDYdjKEoRGFn5SlXR7oUIm3NOZjZzbLKvp7nbanHqZp3u1lc2KJmG6sc1TdOy0c1Cvb2W/7/OqUCP8Vi4RjixBmUotkDNYczveQ4QIhmuyPCqlFibUWOb0aQkdhUMAptpjFK52rrVDw4IyvI2NSlISXXaboGecLuY86t4f8gMBo1fSxi5jjcX29ebuV8PVPvW+OLXE2A+4Wq/gbcFiTTZEd0X3kTN/W0Nyz2ACOxXHTActgEC7JB/4uzgXzx6FVmDCUFc1dduSDLfr7L0clQUYiLoVNNK8urrpvCaoOs7UHbvH6aWlCoezPGJO5oHMPk3nIylUYUaF/mFNnfaOR4/FUrl4wcbbNqZzxXbHS8HWdhe6l/VZx6sG3dzWIdRV+5a5h2Ac9+KSFzY64ykkY0KWoGEsqiPDmffOHOiaohLMn4N2D2kRFaI8N3uJPXQ31z7XdBViuSzakZhIp/NwFtNLiJlBp6gUmTfnE+r596NW0kojbFy2uAXDfSPR/WksPEvcWUiha7gnrosVgkZuqYQhtUI0tQtIBIzdq9SFrjx9t/YxcpbkATph2a3H+N19adC6q4zn7VKLBesaWolipyhiVYF3X43b7bWurVui2Xk5iYVv3cP9SOBt5HZ3brfsaqwz8MpcxnLpknedutauhG1BwHjr0UZ2RXMB8SgexBOn7bGq9Skmu8SUNw43DLg+g+COX0Mn3rFBEjHn0xaJJQFrXO+AnbROw0OvP9HwxkdzX7pM6BUnW8kprd6ViUFSdGcnnRpJ9Y4b1CcGX9Vlfm1bY8ARaDVCu3U3+MtA8CQ8hq+g09S3Lo3E4eYWB4eTvIVhNlEL7ULQkxi66x0dZCamVQN7gWNnw3pkqhpc4JAbeVvEkR4wFQsoejpNZSgJNmgG757toRg1fyl5pKhSuzOyRAgmQgy4E1r1aNBpSq0Ruzstd+2VaPpNQ07m8lLvbdtCt1AUVCR0Ip0tGemFTndnNo9gj0HJyNKSgOLYXo+NgQz3+448b7eJer1cr0XnJZsWguTKayG2ERWij4YWc3uYGIvGXzdDQFB2U3r92rNPFx103wfIVHUXL1SUt2+wy1G7dgqVfUh3DnlNggRrA8mu5f260GReF1h4w1zZHg/UlWkyoG8VzKNh4r5d7+rB17f91Q13gcLd81HSwyJau1yX6Id9WhGhlBh6zfK76+6+JfN1GPDhLSJFj70lxA0PIFSmT2Gc3Jq8xLTsRNMyJQlmX0mHYexvwbTk+kzPjGRziw4uf3VAZsGb/XqA8qUdacNSv+mxRa39ONRWt4MEEM/2jnKero5H8UbvcC3VuOF8wQaB7/zzfUU0lyGiODkmOCg8sgzD/PXlw8t8JPZ2LPtvvvw1n+X8PztSep7+vL/h8ThxDN3g04PXp39XoL99eGn8FIjzPDJr8z5+O2L6uwOzj//6wG/eOz3fpXo/aH6eW3duPL9b/JKWQd92zfSlrfLHux1gh9e38xuJ7fzSqg++vz8u/arAt/OvrvpSu7MN03J+YSMMUrcL337Gb4eHYOPbW0VfMAL/Ejb1rOLbywFAM+wVfsVe/vi/BLYq4QouAAA= -->
