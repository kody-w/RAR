---
name: "rar-cowork-cookbook-demo-data-audit-financial-transactions"
description: "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_transactions", "rar_sha256": "46185e1cbd4a4f155f6adee02ae8570068a7a1ed2b3a7c8d7a7f34e77cca2f14", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Demo Data Generator — Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 46185e1cbd4a4f15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_transactions_agent.py` first:

```bash
python3 demo_data_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_transactions_agent.py   # or on stdin
python3 demo_data_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Demo Data Generator — Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_transactions',
    "version": '3.0.3',
    "display_name": 'Audit financial transactions Demo Data Generator',
    "description": "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e5e5780c8805b5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic audit financial transactions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for audit financial transactions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-audit-financial-transactions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic audit financial transactions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo audit financial transactions in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo audit financial transaction data in a D365 sandbox legal entity for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAuditFinancialTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZF/swD/KNimgJCQECCcQgUDrDyQxiniQgO/97b6RzbGeV63ZVRz+1HA4J2HvN61trnc0fL07fxWXz8ulFC5xisXOyLImDZuEU/oIt72WTgq8ydcH/hVcWXZO4fVc27cuHFz9ovSapuqQswPZdUASN0wXtAiMXTeBkSdsl3sIP8nLh9H7SLcKkcAovcbJF1zhF63jzTrDUKxu/XdwSZ9HFwWIzFk6eeO0Cp8jF9qQsqqyPkuLDou2cCFAHa/JFUgABF9vBC7LFLOMs3oeFB9h23y9ZtEANtxwWWRABtkHRJd344aFbE3R9U7SLwPHiRRHc3+T4qV1UTZI7zbhIg/EVaBkMTl5lQfvy6dffPrwk4PfLpz9evMxpwa2XDVBv43TOataQe1dQ/6bfbKjMKSKwthqBpQtwXQVNWDY5uOUH4eLt6uc2yMIPi//8z/TuNFH7y6fPxeLt8/ll/nfqi4eButJpu8BfeE7luEkGNHpdrLK7M7ZflQKKA0cV0etz5zdKZbX42/zs5yeT1yjofv78Ulaz54Cwn19+WZQN4Nf08+/XmUr18y+vWXkPmp9/+Uan7d1r4HUzMSD165e36zeyYOG3pUm4+KIpW/aNFzBzUgWA+Hf6zZ+n6G/k3kzy5bn457L6sPgx5VmfvwF5n6HoAro/JgtsAHa+vF7LpPj5jUdT3oLZX8HPv/wzsl4ceOkcyP8S3V+fhOPA8YG13kzyy4eH+35bQG+6faX5z9lWIGD+HU3A8nd2Xw31z2g/PPt3pLOkAFnz7ssfkvvRBuhvi1//qW7/3YYPi/AzyJwsuYG4c7Pg0+KPR4j8+pP/7eZPv/0JSP8fyWhl33gPCl9yp0jCoO2+fPn1p/Zx+6fffv2pr0AUB07+pW+yH9H8kV0ffP5iwbdVP/91L+BvFGlR3ovF1xxa/FFW/6P583VhAgj0v91vPy2+z8T5Ay1mJd6ZPk3wXTa2QNbv7PjLy58AfwqgTf+GLJ9e/uM/FnLiNWVbht1C88q+WwAHd0kezMLrcdIukgceAgWAXdsEGPZtHYj/2cOzxGW4+P1/eg+w/+i9gT08A/cXH0Dblwd6f/mK3l++Q+/299eFDqiXTQIwGkDsaaUonwsA1EU3c66aoA2aG0Ard+yCjyCpP84/ZnD+/V9j8OVB67Uaf3/AdvLEwBMrzPjX9lnwOmt6joPiTS8PFIZgCLwesMlKD8gUJgC+PwALtGV2A/g5W6VNkyxb+AlAGFDNxmdJ6ItPM7Hff//dddr4c/EEbHzxLHMtDBZ8FWfx8SNQLsySKO4+F4EXl4uf/vjzp8X/Wvx3ux7EZx4KKB9vfgESitrxsAB51udgGXAZcDIAkYdf/vjzzcSADCiwC+DFJEyeRW7OhzTw3+2t8auPGEkt3ADYGdg4r8qmA1VgkXSvCyFcfJUXMJ0fzXUiLtsO1OgqKPyg8EZA1QHqfLVkUXaghnZJG4Ky2bfBg+vvbuM8RMxBwjvd7wuZVUBVKkFdL2cxH4vA5rJIgPm/RsPzPiDSgCK7fifxujjMkbmonMap4sZ54xE6T7+AavS+HRB35kr9uZiLcDCb6pEmT/NEc/sx9xsPl36cfQ76lRxggt++847eWhR/oT9qaPO5aN9SwGmCRwcARBkXUZ/4c2H4r7eQauOyz/yH/YCkM6U3L/hvXnnE4OqfNzntYu4TFnOjsHjrk+Yy22MISiz+v2ycHgbZ7U7b3Urfbhbbg36yn46am8jZoc++E5BdgGh9JuW3juYdtd7B+3ORJSDqmvG/nisf7n1b8wTEvgHeOK1OD/ogtoCjZrqP0J9DuWnmpHE+F+9VAmizeEAiMCXACZBHc/i+M5yfvksaAzCYr791DG86z/YA4b2oejcDHguDwHcdLwVSNXP6vvkX5EEwp/I9ToDFvtdqtiuwF6C/AEIkICFBJXn9itzPp++i/2XjszGatzyaxh5kb/MgAOQIZgFnT92TDoCY0z17dqDnpwcRoEZedbPuLsgfoOnzZtAEdZ+0STdj5dOuQQXQ+uP8/dR0vhsMFUgZYCyQGFUPrPtIpRllctD2ABlA4ILMypPiGcZvRngQdPIZFwDuvsXQk+Lj9ptCwSP/5vr1vnFWZN4ztwSLEIgO7ozfw4f+ozAB9PJ5xYPv30faV24z7RlCWwCDgOP702fv8Pos/8/+YvFO99M/DEU//3tz06OgG38NgE+LuOuq9hMMP4vwew1+BQAGP2VtH/X441wuPz5A4eNXUPj4PdD8hfpT8U+Lf0/Cv5B4y5BPC/QVeUXmR9JbhL19gEHYj2v7IzE//Vycgm8gC9iXOQix2X0jaAC+VsT3JaAsRg0AGLD4WSHbubDeQS1/lATgi8/F9yE/pxyoOEU0h2hbfgcFj9YAhP/TdV8rF3hUdIC3PzeVUTCPc48EaYOXT0WfZR9eAGQG/+oYN5eofA7udp4AQRqBRq1LgsfVAyuGbv7517H4+PjhZK+gBABcytrvA/CtsMyF9bs8eWoKNPQAhw8L/wHNIDaBpjPzOcecFgQtiNdZo26sZhWeE9/cIz4w+8sTs/9RIO0N2Tdzmfge3mf4exaCr6UFlIKfwYjq9Fm3MDSZ++W/FnkPGobZuO4DSfxnL/pDOb42sv8oxBn0DTM/v/w0l9APb6AEvsHwAerR+xwBtH+b7B6jeNGDofnXeYaZ3fHYMv8Ae8DX101f/zThBi+//UCup3ZfQGkvfuCwQ5+7IPgAYD8q8LspgLDvYfvNJhj5yw81f6+sX57h9fcsnuV3Lsszbj4CeF74YRG8Rq+Lfy3RP2IIRn1EyI8Y8Tpk7fADOR6qAkwHlXG22jd3fDNK+ZjyZpGBEbvnHyX+eAFB7swCvIX525gAlgMI/NjOLREM4AAwBNfPxAXP/i8HiDcqbeyA1hWQISiUIQPUc33CIUKUJEMK1JUAwZyAIWkEoRiHdtDAx1zcoT3Gpx06xImApj3PwUKUAPSeIPBl7v6SWTJySYfIcomFBIohPvAdRvg+QzGUR9IY4ixdh3TJpeN+25omhf+m7lO92ZZfZ5nZLG9a//HiUgRYyROtsHp+WBhCXQqjXU10oYYKSlJdNXvtcMpDjegoruV63NbjdUREJywoSpdPd/EoSttDeh4Dd3eV1UlWmbs+VUrrI6SZGud9WuFyVfh5u92utLNu1qZSMBUqZSecp06YpZqJcDnFdHtaUqkWjRJDLG/3RD+uAVZXR8Gg4Puway8jc2/SdGJobQkf3GUqVYSfGANlXCKr1Bh219OdSCRxWAlc70aiYu7aSr/6Q0fkS14ZJtfniX5KbkZy9WJrJ5BbC48aQz7b13sWE61+pUm5E3DWvSw1UWzSkB3oPacYemrF9zZNmSRN2nYPyYkk2Vd9hd1djssxgUZg6SyQDp6XJCQdVi1uNbaJ4lKzLBq+QZdhISEQXKyxfUsfFXRiSKFU7IOoEJFktBIA7bMa7StbVent0YM4unY9QcDLs5z0ia7IbLFDKcO9CqqSk7smkgUs39nbTRWN20si3K7s6N7iy6pI74hk0vdK3VwltZ+OFIYxR27a3+T1cRBw2YvFa6ZcrZxDUtSSEPTGksubgMIGNZFbR+NqPZCYPImhMBPK/Zhlwo5lIHidQtFWWgfEqJ2FLN9juCFofkELVsbq9aq7b9c2cZSxuI0g5EgbR+Yw2UN13mQHcYtpCC+k4ybXdwizY8XDRVBoP24DkjxddlxCSu1FLpG7wuTS+aqzFCO0hoUaO3fMJklWxxiujkaFwFxypC4KngjLTFxq1MlTjUw4O2oeh2nEYLuE2cbtTeDJqBEs+ZDvWl30sYnRmI2u96fLdsgzGjV3Sy6qd91qe9TEgYcPB9JV5YPUCvfiDG/HCGnWyNa5GIe2VnfdZoVfxS5Dzf3AV3thvHk0d2zFisxHPyPTm2CVsQQnpYw6KaF58YYRd/ecuK4rW7/dVheYONWsSDSdcFYxSYnSkQgiyDjoBHocpLJECoTIlRRGlvpk6ZOtD+cIEjwvXDOsKFs3uFckqFWR4jAHgVMQikK2bFdeql7E6UzB9z7NqGZvwJEfF8IQwlcdUkwak/rTXkUvK2303PP6VLlaez6TPH2+RGfIU+Xc6htTtdX7ec3Ep3g8LHFWhFdOQgrHoLksUywknXEZpAafJ4F179bY6DvGkG9TTyQsgQHtZcuratTd93mhre40TuLSlQpZMkikNnA9SQwD1iWRkUvxrDrmF0zskkFGpVt0YTQXvoV7CJOvVmWL1kEbL4Mp10tDbnwT6fy027AicvVUcgrz4LTJneDUkZhzmQjkzJ2wKt5PZ08hMoLwT4kudmnnFjs3OHHmVZHDvuaZy5rVFXe6yamdTe0VOcFGYAtckULraaKg/algk6I6UyYK1TuiWIeiIh6q9LZbyaxrpMhOmC5ARipmjTuEqEdPpbghdywoz0Ng6MpMz8v6fHD8BKpCrZxWhIRI4vnuUa5c2jpzX516VCYL+YIvN/2lMrNqLa5Xbn2+7W5FMEnI6EmSii7JgjrycOowzbh39hNdextPUfOEgrbRub1L/M69uldjp95xBbOV5Co29lqyicgsrkenuq7YXh4KGeRpnt6ua/1wOmW7lWGthFVvgXZlmR0Qd2L70DQuqqomQcjE+6PThHXITzLHss4t7kI88BgXO9OWJkvSUVjHxMrley31GCZeKupNDuKADcQYDaEbtzn1dsQZ5UQuk/VRxIVMvCs0H0DiCeBTT2tsKGwMfde0+XK3cpYpb2VYGe3uo8Rd96OdEdBFWQn5Xm1oVLZdxAq2sb0X25N5tSdzk7HbhhVvFj7dTZMsEMracZrhr2N1FE2e1kfeq3pgaFXLx3KJZdl5GPfiYb27bBhjCUr1CbTAnXC4mtRE8Zbnr8WDsVd3tYg7jJ5kI9dRiMeqUbHvuBWBoxIx9q2VkDYyZapLmWsXl7RW0EUhLc9bpFqKxZLwcBELizz32OrQbqFoJP2TeKq55ZiLKYMcY5WUxOPRzRW+n6ZcpZfUGI1On2655Z6AU8RaMsulDtOgDTwR/TV27UbxcpAAVREmjR1F6yZlcVKhY5I0zqTIq4eMuanSeIyIQrWS5FjWrqQc3QSMiEpK4Mm0V/u9qTZ2F2zZpV6ct9p5g+XHaFnF6pkxtmwET5KwDaDhdORW4zHBtPbO8PIuvawrXDEGoV86Slc4elbvr0paxjeW8LK1SFKVsFKlnLwRiOsPVQbBEm1XwaU0x6TGdRpNdGeJHfm2zYT1edMXGYptDURzb9CVMLIcGF64bPlBdJgDQZ7QdSK7+2Xft82xvRMVyHbvEk9htIHpE3weFLzlo6NhFsgxtxTC5Phc2TRTVhrDrVveK3vd1uMmJjPcNKFtbBkqts8o7mxScmgmstdlodapqSnsZEPeX1aSV0YasyZ1W3USCvhZj2EId/bkJuNWNm8mu4t0v2YdEus8Tx0s7sxsL5w13EgHIY5LsYwg5xTFiYu0giJu9e2wk4edpcQrkd1z9QnFG7ym9GS/3VmlzR1Ycye0dUUtK3zlcImEieuzXDsI6Pzr1uNhuLATwRWgc+sHY0d6noscai0eXSmKD5t7nSWpeXQgFOrXlKgXdS4eyNA/9wnPbswc5EeuXPtM1BmhXx2HW0qxMsln2m1brjLMv8TRfrfXMg5dH3PuUm69pMi9Qbtox5KvIy33NoS2Q1RXrv1YubgQcmKtU71iSwH2M8xO1lVyw0R15EsF8c0uEY81tSat43Lpi+0aD/XsuvImA2RXhw0ur2JralWwGcZTU1vD0YQJKG2rw55hbvhl9K1r3PSTSG5G2x280/662dV95G9sErLZq1kWkUbS9mUvtFS6VYNKUUWmd9JQlHaoLY2iEErrnaiTB1lD5EOR4wM6qGffwuUcRFJOIrhwlry6LgSFXXJWX0yn5oq6oNdq7iaAeLvWhN6EV5WyGi8io7ZyHDHIudUQkxyxetBb3hyxcrO7oUrMC0Z1lPMCDS4IR6k1HPNL1qii82lnXqcTnK6gWLFiuTl3e4c/Ei4zQTC8RRivPezc+lisj6ayBUWi6/BWnw6q3GWkcJCkVNkPSApp0pGo98mZKg4mA3XTKUl8LTtMnnivCcytVqMm7BFTU52iFpyS5tD9uq98cjcgK3Of5LQ7XetOk0CZvJ0uVulA3Y7L1IQwQqbeVNt9dI97WFojRrS1tia77iK7YIE+1d6yIC/lIMcdkdSUrlfKCsoxxfB1cz1XBRWwGmoVamRvVCHhsy3PeEqBoaCIYyxog7xoIxvpRvWK0+hatRKs79OmpaXJk1T2xsRq16iDLu14y0BFxt9c8t3+wpJUskrqnMqDqlwm9zKLzxvNcovE0zgCPk5Vi8G8TsC7CadvYHIbdYyGb2XDNCvSlJMbdyirHM06k+lIwvAKEuJSw21YremWnIIQW3vcY2ByzCZolNahLwJAQMfN9SiIxu62DTRdoA6atyrZ25nVOYHbyDF6ci5sKqa5Y6e2Sva33WCsjiJ3s6nhcKOHjX7icxYvt7fRAmA1OaSyni7BBMcImd2TYPA2a6Ktu4uo5g0V9TGjbu/Anf3GtOBUVMrNdKK38p5EiZrwiowJb82IWwx+c5pK5c0VvYuWO5WJqdNSq5MOGjeZGWGchpFhZ6Sojp95n2Y33LiKbc+Ql0JXbs53pZYr9kjsjC3PtrdNgWahP6JYByFBPnJ44eC3IiaXfeMPl4zliETPl/thdWkddB3fNRa7N6O10kGtOmeilePTvl2N09USgm0FJqmAPwNUGaCjxExh1hT2AfQeRndcu/ucrfQz4ENoEW7sxJPr+86kW+1B1w9Ne+bk+Fb0w8lF907OFusc3q8qw3echnNO5JpQKOvoZutUa6Y7Lih94NXOrkYFBzL5pbcJ1yfSKIJxlFfVbnVBcSEn15CNNl1nODm+KYjcYn373rBrAJDqymaWXq5nw95zuIASzmAeIVx3syPKTL7MYyinMAlmD2IGEJjUSep+GizjyHZqvERX1FHvYafsCd3G2aXHVIMYXas7qh1As4yfYTO+repcLbfF1rTzyjpGCT90a1vAbanLm+qQmYkaWULkIdwJZVMMM6LhvslB+2Q0KKETN9OkTQTNYdCvt2jOJnIwuAJZ2qgxFl0X+d1mh51uFYGcZM6W6WCvYu2oaSlpdfYQd25eXy99Apc1eTUyfteloHc68rG2FINoGk6RZJ7CqRG3MujWcYQiCY9bng/XTXMobs0FPaC8nza3vXYZkqG3B3UztkLukvJJ3/XtOF4rukzwa4+Ukpdpeyu280Swio3MbI+gOro+doIgN2ajDENNhl2mcHPjcPpQKgZMKTh/048jYynauihSN1SHerXPD86p9S4IlbuohK4iw11uDlpYugJ1JG/RiiaNIY6gs6XSNVyavXZNjh7DOYNzOKHmpF6WY6L0XNk5mae0dEvzpI2rFI0sOTiXOshFGYvc0ydh2vJlbJFGeEApZKMrhbZ0Gsrrzh52va7dLYXitJV5vi/6ET0MaqYtK9TeFnaaNzuu6DY9K+fJhQvq1bQnfR/eVM4yGKscS6BkajEKH5eZJ7MnXDY3GCulJFSxtmbaVzE7rGtThNCSX7PXzWW5YuK1f0eJnZ16JNLSmxhpu7JBYNIiUJeTe4KGl4Z4ycmC3pQttjxtQ4i77B26Px7CI+TfGO1+9zcdsW3G7ugim01LnekJh2mKg++WAybUy0GpyQnmwnvH+epGVQK9OY9Llzw5jhHHq3MbBeQxGbT11p86q0ymkiJ2TEnzWIFaYc7Gl4itjQPHb6373YuOmsp44hhrcCWvGWXX8Wx1SUnc3I/jWTljoI2x2dWyoVRTrQ+1RXZDco3kQHbcQN5EJDykBZHSaGb2J8+6KOtK3NW7Ahqx/NbjuiwK1KnFe2JtQHQ3FBojVQpSJKbgafCWA1NOXzRu49cHvZ4cs/MOx4ljUb5yOH/seMLOYKmhUr+7I+ZZ6A/RSs5XnJxv4iVD32m3RflY0lcnSHdQlGX75BbjYnLFJqSxzkw+WPWu9gx7l6P0ESsRG1tShzOkYWfPu670pd7WuqzfBtPSkEA4QoPgn33hZDfbRvILqGiprYrvdUFcDUOSc0uKJkpKMw0EN9kQ0dd4HOUcVW6xtYdWqxxO/O7Mt/EeYvdG0WIM0Xu8k66RW6FoJpGDGq2QplJMJE02dQ+l+7U9bJMTZO00rMHE61X09VowTzgfqnTeFYndGRgHuZ4/ljrvR3U5oAw5TJTfwNzBtAzZhopea6dt4cAZzbV9ldpUS2ZddjC48oIiMnyIrRZrdR928wBzHIqpUhpMmBLli7GUbHaks4JPHOfe3a7UTVCxrghzPQ97czI6ZklWx8FxzgNUqtK0yTvHVqhoHzi2iJMHLu9P5jHUpiAbN+u08ISR5xB0I6EUdubzdcmWyJ51B/PQDPRqxaQhTo6avB7OJ8Ld4NFeaZO+OvByrICJ57RfTms+3zhL1WhcfijONzmnJc25dEvqeL0qFi+YUtipEx4U3TXDKZFUR3kqjkN47P3sNl3F8ZYHtZ6OoYc1Icp3aGKUTLg6XCyIOJtyVVRBRnRQPIQGOVH2fmTW7v1Inq9CawYinUNsjvomRCF1hm/rg4BS9xVVKYp6bZQitQz8xp/dAGOCi0NdQ55SD0MusKaQC1ALukTsjoN0u8SsrBXYVELkVSYq+CYNKxaNTS28pfmw2x+ODEcL4t3vjXJf6kMw7bns2sBNCfr9eKowAZavGiWM1Lg/BTLPlNGSMKDJ4TAZ2ku2v43TDmq3Ltbfp7VaU+jBjJiCQcyBs1ArwAyZXu0b+ooqg8qyaReJqX/3oZq/OZG7owkjOSBXX9krIwHVjFNFUOJqylhPXXXuGoeuJETGkNtqLJZmmd+VLAMeGekOQxpNzy0UdZ1uw+kUfK/QtKp2+wHbMIiHXcLNpbPti3iTvUOCyrx4r5geORrQktz018ueUGoWEwcTxcwLw5UTO14kAYddc8QxN8khVAyuN65MMzhX2Rrl9yG3nvzQOZ+PInPjetxAav1eSPeJ5JIC37gjJZ5Rlz4fmcMN9VfhvjhIoZlxcFhWIRru1QBusdVuYhymkQ/7K5Zs76d2kKrCi9YFuhpbmQj5joaRW36aErd0l24p9YJfc3dUv66xLkduqN7Ux2bykGtxbHCjjpgQmFnqVvRxo1HVdT7XXEaIHxneyTeay9Sw98tZE3Y9Z1r0zcl42C7c5MJoAqZM6wrt0CbwcFcWGB0W7bS1uarcsJe226F0pzJI71D0Kuu7E7Th4+19ZFF8a0dbCrrrkYUwoRmtvON1RxzS/ux3PV53m9LgwSxxYriDnjhTbBaS5Texoi5Hw/fLPqYyjgGDHtTKwD7oNhQbEtH7m6Txlun4jBZu1/DVbYUNXIw8bPix1tDm3fVuMqz2wTrA+btsHxsxwi8dh8K8uR5M0AAOGaXDWcrhIawl8j4J7wzk9DbpT+d6jRJH/+yiY4/vOroN8pwLhJCsd51H8z4rYaScHXe1rXDE7egwHXIDzRYGueZFjZX6KG+VrEXEVbLCqrPiX+pon7BsRZWCVytplhIKn+EGZl0tbdWS3mnAquJORVdbN5LWpHUE2oMxXejxEt9mvQW6A5WCaNnvtr1UwSiN2qcBJDEG9zs3oIYLgizvgbkidQwtEj+AUp+tckV1rxdVrcytf5SjfelR7RKjyIYf/CW84ac61bs7tw9g03YgRzzEirhsqpALbZUIvMCPqHUd1YcLVZoDhiltyJ+HK3sh2dVq9beXDy/zEdnbSe2/+dbYfKbz/+xo6XkK9P4SyOMkMnD8Tw9en/5dwX778NJ4CRDreZTWZn30duT0dwdpH/+1A8GZxvh8Kev9LPp5xN050fzy8ktS+H3bNeOXtswer4OAHW7fzq86tvPbsB74/v5Y9atCL1+PTLvyy/PVsZf5TcT5NY/AT5wueLuM3s4Xwd63d5G+4BT5JWiqWdu3VwmAkvgr8oq//Pm/AbbZ+tF8LgAA -->
