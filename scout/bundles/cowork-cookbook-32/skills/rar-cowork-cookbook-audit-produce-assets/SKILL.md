---
name: "rar-cowork-cookbook-audit-produce-assets"
description: "Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_produce_assets", "rar_sha256": "78d726c8fb32b14191d3edbda0cb52e27dafa4780a454edc0b0b873c841cff44", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_produce_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_produce_assets_agent.py` and in the RCI capsule.

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

Produce assets Completeness Audit — Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
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
      "description": "Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_produce_assets_agent.py` and embedded as the fenced Python below (sha256 78d726c8fb32b141…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_produce_assets_agent.py` first:

```bash
python3 audit_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_produce_assets_agent.py   # or on stdin
python3 audit_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Completeness Audit — Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_produce_assets',
    "version": '3.0.3',
    "display_name": 'Produce assets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4948b194beffd04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit produce assets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to produce assets. Output an Excel workbook 'audit-produce-assets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no produce assets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads produce assets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit produce assets in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants produce assets records in a D365 legal entity checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProduceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProduceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6mK/rELIHR0xCBCLkFgkEFCucLGDWMUiQDX13+cgya6qbnfPvRHzaeSwJeCc3PPJTB9+e3P7Lqmat09vx9AtF7yb52kSNgu3DBZMNVRNBr6qzAN/F35Vdk3q9V3VtG8f3oKw9Zu07tKqBNv1vmwX7qIJ3eBjVeYTWF3UediFZdi2D3J1laf+tHD7IO0WVbSomyro/XDhtm3YtWCnXzVBu0jLBTuVbpH67QInl4vt/zwy+8UtdRddEn6VidPVRZ33cVp+ABu7vinTMgZcFtzoh/liXvMQeUi7ZFGV4aJNwrBb1ECzKC2DebHvdmFcNdNMZ5b82BeFCy4fK9+BfuHozhq0b59+/uXDWwp+v3367c3PgbxAX3pWQ32qQD80AFtyt4zBs3oCNi3BNeAXVU0BbgVhtHhd/diGefRh8Z//mQ1uE7c/ffpcLl6fz2/zH2DKh65d5bZdGABJa9dL87Sb3hd0PrhT+9J5FrsFLinj9+fOPyhV9eLv87Mfn0ze47D78fNbBURwZ4d9fvtpUTWAX9PPv99nKvWPP73n1RA2P/70B5229y6h383EgNTvX17XL7Jg4R9L02jx5ahyzIsX8Gdah4D4n/SbP0/RX+ReJvnyXPxjVX9YfJ/yrM/fgbzPoPMA3e+TBTYAO9/eL1Va/vji0VS3sHRLP/zxp39F1k9CP8vTtvsv0f35STgBsQ6s9TLJTx8e7vtlAb10+0bzX7OtQcD8dzQBy7+y+2aof0X74dl/IJ2nIBu/+fK75L63Afr74ud/qdu/2/BhEX1+Y8M8vYG48/Lw0+K3R4j8/EPwx80ffvkdkP6/kjlWfeM/KHwp3DKNwrb78uXnH9rH7R9++fmHvgZRHLrFl77Jv0fze3Z98PmLBV+rfvzrXsDfKLOyGsrFtxxa/FbV/6P5/X1hunka/HG//bT4cybOH2gxK/GV6dMEf8rGFsj6Jzv+9PY7wJsSaNP7j8cAP/7jPxb71G+qtoq6xdGv+m4BHNylRTgLf0pSAJztAzWaENi1TYFhX+tA/M8eniUGqPvr//IfEPrRf8E6/ADkLy80/vJE41/fFydAq2pSALFuvtBpVf1cunFYdjOfugnbsLkBbPKmLvwIUvjj/GPG7l+/R+7LY+d7Pf36qATpE990Rpyxre3z8H3W4pyE5UtmH0B5OIZ+D4jmlQ8kiFIAxTPYt1V+A9g4a9xmaZ4vghSgRzcj+UwbWOXTTOzXX3/13Db5XD7BGF88i1ULgwXfxFl8/AhUifI0TrrPZegn1eKH337/YfG/F/9u14P4zEMF2r1sDiSUjsphAXKoL8CyuY4B8HaDh81/+/1lUECmBDUIeCiN0vC5GcRgFgZfrXsU6I/Yklx4IbAqsGhRV00316u0e1+Ic9V8yQuYzo/mGpBUbbcIwjosg7AEJbZLXKDON0uWVbdoQaC10fRh0bfhg+uvXuM+RCxAMrvdr4s9o4KKU+Xgn1nMxyKwuSpTYP5vvn/eB0SaH9rF5iuJ98VhjrpF7TZunTTui0fkPv0CKs3X7YC4uyjD4XM5F9RwNtUjBZ7mAYuAZfyXSz/OPp/7CJDvz8ag+7rGnevi6VEfm89l+wpvtwkfbQQQZVrEfRrMoP+3V0i1SdXnwcN+QNKZ0ssLwcsrjxhU/9qUMH9uYh4lf/G5xxCUWPx/1u/MutM8r3M8feLYBXc46fbTJ3PXN/vu2SiCJmQBAvOZf380Jl/B5ysGfy7zFARYM/3tufLhydeaJ671DTC8TusP+iCMZkkB3UeUz1HbNHN+uJ/Lr2D/Acj8QDbgaAAJIGXmSP3KcH76VdIE5P18/Ufhfxl7dguI5EXde8A1iygMA8/1MyDV7Mavni1n+wF/DUnqJ3/RagGoA4sB+sDGQFTwNZTv3wD4+fSr6H/Z+Oxv5i2P3q8Hido8CAA5wlnAOWBm5wHxumeTDfT89CAC1CjqbtbdA6kCNH3eDJvw2qdt2s2w+LRrWAMY/jh/PzWd74ZjDbIDGAvkQN0D6z6yZg6IAnQvQAYAHCCJirQE1RwY5WWEB0G3mCEAQOyr3XxSfNx+KRQ+Um0uQ183zorMe+bKvoiA6ODO9GekOH0vTAC9Yl7x4PuPkfaN20x7RssWIB7g+PXpswV4f1bxZ5uw+Er30z9NMT/+9wadR102/hoAnxZJ19XtJxh+1tKvpfQdYAD8lLV9ltWPr6T/+Ez6v9B6qvlp8d+T5y8kXvnwaYG+I+/I/Eh+xdPrA9RnPm7sj8T89HOph3+gJ2BfFSCgZmdNoI5/K3Vfl4B6FzdhPC9+lr52rpgDKNIPrAeW/1z+OcDnBAOlpIzngGyrPyX+o+aDYH866ltJAo/KDvAO5k4wDueZ65EObfj2qezz/MMbgMXwX81ac60p5tBt57EM2BmAXZeGj6sHEozd/POvU6ry+OHm7ws2BKiTt38Or1eFmCvkn7LgqRnQyAccPiwCYI92rmhAs5n5nEFuC0ISROOsQTfVs8jPsWxu5OYNXwYAwtXwz/Kw4OGimW02s30g2qUP4jmZXWC4B7O/LYzjfgvStKjmG+6MowWo+MByWxuIufou2xx4Lv8CDAzy6Dt850rzWLJ4Lpk5PyL2wyJ8j98fLL9L91vT+s9Ez6CPmOkE1ae5pH54IRf4BoPGh8W3mQEY8TXFPcbssgcD8s/zvDJ79bFl/gH2gK9vm779h4MXvv3yPbke8PZljrdn1PyjdIcZtgCszz79h6oJZH7l6Uv77+XuRwzByI/I8iNGvI95O37HOkCMByiD0jZr9Iep/hC4ekxbs8BAwe75nwO/vYE4dmfXviL51a6D5QDDPrZz+wKDDAcMwfUzF8Gz/1Ij/9rTJi5oKsGmFRWsMNKnIg/HPJRA12iAgyoYuIjvLbEQWwVu5BIrCnGJJREGPuIhHrXCfYpA/SgiCEDvmcVf5r4sneWYhQDqfwRAEP7xGNwKXgo8BZ6t821umBV96fHbm0cSYKVAtCL9/DDwGvVgYuVNkgBZCKyPw0ExUkm3rhQeLAU1GXEVo1uWcomRQLChoONJ9+wsTNPjNDmlTA/8xKkZE+0zyL2SBTYe0f3UHpadjF7oOA2nvrmSkYVaeCgReLgNMkM3d9wxzo+TqbQoFk7bXWGk+Whk5riLVli+gnbUVJtiwmzZnVTnqbPivOYSX7Rj6HgcYRKcypheuhoP3XKTmJm+G3cZgZHRRo5JE1Il3CJKC8bNEcodfyS4qht3DY6dtrmVoHC2yo7eWUKGrMjzsz72GX8lEqtEdg6zud6nRmx8XbHOSz43rmmX7yzROQpnX290gqWr5dFu1tlRUGSoCpqWVvEiU8fUj1T1ALnd7dSRsJIot1uJwnC1v+GFut5z/Vjru9VODhzOCVatT+z8jd1w+4k1nbu2h4fUuXZ+rrOiV7PcddghJdRvyHuqB3HMm4xA5EuOUO95SWW8z9VtzC9DKNwqjL8VOO4yKEHGuQ1pXCWIxc+Jfb3nO91RONOpA+emT+vOGnt6dc7xkcU6Y2K3qnyOU9dkVYY6Z1xjp2je0Q2zgzccXxwPdarhpJIXPBF5aElwO+5wrGjcibOOwneahlk3t7SWZXheHgaqHuWiYE4H+2S4Z10WYvIssRxfZ9L1PGg5b+gNWR355XBnIwaekJu7BmXXxkZdXR63sMzvTOD+w0mYcjVHOgc+ShikC22t9tooM0zRTM3EGId1GR8biRGcja5OIiM67koRkbFXtICCuThBECE9Su2JQ4Eh3MaIh24TxEdVzIga5jdTV4U0dqbO2s1KHG2nX1xXV6/n2KxW55iW1wV6xatcrHGOdIwjNkwN5vnXK1Fr2s1hLHVj2W6pNC7kD4lg84ZtcclqYqNU7kaaMsJBEb1DMpzDLV+pxRrDDnfqjMnCHi0plCmT1A1PpB+5tmOeDhi1K8fVtcS8OjTwXvJhVu8tuuHXSpQyMCTBg36DC7Yd4TuLZlAp45Cttqo8eKUv0rZJh1l0xPwVRsO1y6zPvuoOqXo43sNJczzW2QoSG8OcWaAOdKt8gWCNs2RnqsW3hTpccc2rEgpVHGJNIoIntY1O2bpTF7W5IXLHsZWq3nixsg61dIgh66jcnGlnkiI2bLshV5Nt5SV327Q2QgY5llNgMocjIaWLkxWyDXzu68R1zvFWFhEmz6uNdlelVFwVkVYm0bmI9JWwyzAG7jgtYtUG1XegoRUv0NTtaNw9Y+egiU+rg6usqP0hvt5lIrA7W16vJP96vKcUewzSflcbJ1VMStsiat4niQOPa2LrWYjM9ZnYT9goke3VqHfBeLxuZf3CYXa5vtn7ng+KI9eLmpavZDEZbmzWIQRwt2OsVMoeTU3O+3MbHg8DLqfBcbhAS+LiTYJpXD2rk82tpzNLnd+oGqHDYb9cn0J7dR6MK9uYanj2qoio8cD0plELT21D4/1WXcanI0L7+23B3vbiitGX0GRRrMR6NBij6bO/3bbIvaLMOlcIU4i3CMh3V7o2AOLSqRD1oAqR5o6ppe7tXQQ2tjktbC4jbKH6BB6ciKU/3vQauwlbQtmvyPM+GMLMOeuGyK6GglylWlOSZ+a4ZqhbdvEVSEiCkJBXDZKVBssaQRWMSh66emlrB/weFflhlbPpdAgzLZd1RFzysWSy+r67lye6oyvRLCVyl98pUWYk3k1aQ7lUgqFt6MERNpreXUpfuad7vFw5N/zWOvmmXYn0diNO2K5imdQJBE60NSog7w1dEfZtQ/XuiuE2BLHZ77aKXhFpum9oWszwfd+ukxYrjKOMMPEV5laN7yydasIOgUKU3RClrUsKUUUKIYu6rUmiRlLy6P4g9UF306DzZDlu5mmO6goHMrzdGpTQIz7L6Jjan2UPvikVVyETJB1zLCRprYID3eCcuzISMHlgDLm7r3Z0sF9fihLGISyC2tvtsm6Xpt+Q+/JOjEFh5KFgrZfLa3iUtThhVmKODzbeEAfuqF19yqqCBDWPqyq6D1PqaRyGRsfVZuvbVBTJSLDelxaCRVFmXIL8LLXnWlJwViRLfTtgaFam4nSasokkE5U5bxxny1bZZsczUXPa1ze3ktfDJpdS5ST1TrKu5SWKloK3mdKjfO5qYy8NK8x3qR3sL0PnfLpglXUnDtOEHsi8B0Iu00bcbNHt0Zd8C1mxO37vsVG2ZngeU4+7A6XWZwg+pf1t2vbdYKSqrrmOPPUbUU2NchfKU9SX4cnX1hIvpyQVZaJeyQbLO3tFR3r7dMp1s6uzQgvu7poLKuGaVhu0DK8NIV5pYkPb3H1U0qWhaGhiBtcuIkfNRGlzD3zhJKp/zcR9GseO5m129/J8HWDI80xmp0s2ZhZjui85zbhE9G5DwptYND1EO5p8QRwiPUbGYjqNRBnvbEsyj+fUKbb7+2HkjtJVtJsKamHjeo88WdkOGw7m6Mo+6lPHTBm+7mtpc7SSK4iZ8+G8wk6SKTPqykTFKz8BNhkOGrTT1g+T2wnhx2Afu8iNr86MX/qsZrOchN+tLTq4wakfaERfwbt2tzflsNSZ02Af15UVw6NXFH5ya2EJTWqWvKaJll/ovLGTYmgmRZG2fgoZx+S4i6EstVrnpEjYTrhwGgZk4pEL6Ni6vUgIDakIYw2e0bBdH9xQGTF3U8vGyBkUFke3ktxVNwxZtg6Dp3UyBiS2Igju6EH6tCmZtS1c4T2pE4jiY4ofd/JEdFiDIJ3Kwv75Tm6zaZXysIKgGUsKOMPERtC2+6vRnDa7pSL58ZFFePJwEPRj6tQ63uiG7jAHW6wPewMjQDsB+8KdNswjpcT07nq3/SZzyrjW7kjAr6klZJWhidqcqJmn0jkvmRZObIMJOXlf2eqGaxCcC/eZg5zTK8dPQcm6KRXAdS6uJ245VaGHLBGqqBg8jjdiVbS7iUuznaui0sWlqRCBUpfeYQxEei08wkrbsG7m8t6KbU40r2JxsIRy6nqnQXG8XDfDZJn7ULpn9JTwVxd13DbO7yco2hMN1ntavpky6bwLgvVEH4GhU47QELkICXw7OdImNgafyLgaV9zTLfJPnCvJBIFMF91z9/TONGh4n7ABQERzPNA2wxFFlYpt44lXTtoT3LTDMmXT52K2hVxvk463jC0mHm36i4hxYbzhcr0bBbKrNBKrYnGyJxaxcBSiIg3drC7y5hYTF7w475SYv0X4hVyKN9hpRYmsbpzDHovT3tuyhAkB4Fq2CMmtWR/i1iBFNtntqBuGw1+mbtTvxLZABoRAWaYq9mNLRkFOnq+K48AApQR82tlbdz3tJHIp2SS5NLfy4UrWMqZk8dXpE58rzZwp16eo7s8aw9+m8ymmTmF9cmjjolu4u6tTwT75jd2bRElr06QDhEAys4SJo6vF6bnAyroqaMRI04wXBa30wj0/WPXZuDRJs0GLlkBghLkWl2DbXaVtKOPLwB1USL0X8klstoOHStkWl3dc4KkO4VIbQvarcmvlWzxqsato8i3qoORAnJYVRp6kJI34nUgicRKPCo9kA2NQrWvYEESQzMm7Y5fl3p3kK09fV0R2bEWVaIjo2G3Zs4rWG+d4s6WUSE5DVVpGnlRXHpPDpuTbHfDMgR+v6y0YAJ2CXhGDEjKDeDKpy749CGsFL24a1tz0Pc1eGK0XW3HUJfdkhis887aiTlGGKyRLyd0LoxHz20AKWDENUobRlpapEmbtryJLgM7nkJQRqzvEWTNAhjKeslEPcYqjNsEq3NSNHibDMbOl4CytpoCIjEGQ69PRo4RweeLxM3o0SCS5DgSO8PoyRjFsOE46Eu7TQ8idDLE7emBAInS7qJYHURBZ+CrciBZyJc1Pt6eQ3pHNbrlE5ev6AlVofTmvS7MrdFxfl1tum+an3THzV8K5u1a9S26yfREkS6UI8tgVSKFUoDvPLpU2vY3BKhI6vlY0WJe0w76xEX9rcbvs4l1OOm5rtEAUPp1Qp6YYUAc3C8JbbS9lY+237SE/gD4+xF2d3rAbmWru+YmeUCOr0Ty8hrk1wBWaeG4iN5vGGW8QX9+4nMkYrN0dQU9gQJdbnWJlXBywC79WfdAd70zXXbckmDel/foc3K2bubTLg2z6RsRfBl/dXniEoANrQrEjfGcyexkglXmK0tua4JR9i8fmIYBAUytxE3kya/finMgR9Wo4LAPmLrJhSteiQEoMzfnrUaNxHvQqLmbUAQeHbFHWo+mQWREaiNiNZLZTsHHXEaDV6tv7adPjxaYjKMKvBHK7NwPzSlC037bZeVN2ZLlLfCq5ijcBzNNxEugBsiM2a8yZpNLbXHUExQfpRJV9kGTFkj4pzRF3BiaFPKo67DnQTIqtHOKEqh1xdsVQEuMR4cY+QTyGWvyQEDbaG+UqCH0bYTH7xk+wJehl1xIbZVQAYKJLa6/qpNddSy8yVmQx1HdVu7BWddKWAseTpu4WYKgadxTD+PBhZ1ZnlCF3xDZEsdVZHbYgQ1SsRkmqCLN0s0qDyAp1OFc39Hoj75siYavibmQS0SUcurHW+iEhrTTSu0O99lIovlBn9npLIzCTkM3hjvI7pDOilOskJ0fvvV9Y4SFBfVtNmlVjMknplR0cKhvXh6GVu4YHCxpzI1fALA/D+Y0Kht0lDfmCtGqUGzVvqeli2uuWD8aloD86rRvHquiIa87CsVvm7UABIe/6tTegTUgXOQjjUaAOIImyIodDqjVg8s5FF7TRieYcKSx6bCvXgRQopjzOouQzPWx3De6cErxQFF+37/VhHOGbut5WltvwKz5Yyi4hDqoE5DnBUICCzypIdmXvG4El7krcAxmnJeTpIBHmkYFvCWOl91VdwO6watFliueWxZ7aUet0Eko0v9GhcutN+fqs4pUdLQU9sLWTFG/AXyKKwlDpV6pO6MhgZOvaJcftWcuRIUvMlXNFQbNlbSuTRZVdy2gYHHtcqHrKWmhgCfRfih478BWzDjfRIhq5C0Hdj2zu2ElZVSGpb8WTquOBbNumbXCxQ4wnBoIAGHaiYbKHtSfg2RAYzj3B/NSm48MuYb0xATP6StRvOp9LwuGm2CHbatqmWY1ocuDU6+hAjYRAoXoz1xYOlJSXDN2BYWZVBjwEZszI0K6g5o3jfb+CmYGUqh0FUWS+R13L1MsxX5MSmBMxa1gby7WnyNfVlu5GfqyWCUHKpCOEds+5jgUqRrzZbFNhfx3w/Z07W6PLL9mumvozfuBXtZgxskLK1X043KFBBpUXTYLNiQh3ll00DX5atmInTNbBJRBUR6T43nd7/m6U4s3glksmu1vipejtuJvQLZupSns8CxXVn6vAv4XU3d+kjFpMEnL1BGd/nGj4IMDF3qqvjD0JMRX6ks4aoFCKcCmZzIFMzJtNI9Oqd3juoq/3LgrD5SE64WLHrinyHtzR7XhfIRSl1JZPrPtyOO1h9UpINhqs+TrxxS6Ql/3VpuzyroQu1K9vdZYJzRJzMQJhoIZDIrOVr7vVWo6JusmRHepzOzgORl236eWymLo7HGiEEV7x656XDX8POlgbr2lZKFvBS4HKvcVzUHpV29KGorLXOrrZSlO6m8r0ZPJrF2SCr8S5UHsAOqLjlEKHiN0YHt2X8VLqIKbKLitRRQZmE1rl1WH2ESEafVpRmL9JkmqJNJxX6LcgWzrb0u4LFmJEESrVVrn4kpq2uHCMJp7E+IDABk/WjKAAGXa17xu4M/37Fq/262CjxLdcI7YDlWl95WuCixNiRBYnZFxf6IA0heIau7mwXvtLh4J5HvUKkzrnG3LfiXjgRLnagTm43o+e7O+KjITA4Hkrsdw975c2bnZXbG/eGpjN0GOROY3AqcN4d3IqKNCkyYp2JHDZH/byxXLW170xwYSYug45HK4TKo1ndMAScqgum8kRxDPM3pyOXsMpo1y6rd0msJUx152Q7485IU8mkR+O29q0937eWue8Eu8QA9y0vEfKyAuNMlEurmBWipc9KYGyjvSc2FH3HEL9jl116CXoLoBOdsfuPilepMOdFo6bZcaq121OSIOkyne4i/xSSclYXR/TCe/xSpAdJTcITHZXphLSZLTK0Y6U+oukbSroRvZnUEJPuHzN1XwkE4wNELweMpQec4VSmUvNJS51tDTocPXhVRL03Bmtbja8ZzIrCqulZ93yy6hQQn8cabKIfSm7Z57Vu8J0lG5NO4UEGnH2Wkw57bxc8uJWbA/EyHmxcIN9maZXAd8MhKTc3PupW4sXdQfZE3/HODIS8bJolB6DDX7NK/GAISPKYrtydAwBvSRL1DLW4yEKseggO1BBlscbesLi29rOYzGgIBsu/Iw5wI2x6SbquGaWxIEnIKlg3Mk99J4ThLWp+aiBNr5zy2F0Swc4tc8uybVsVRXLL0Jzdg+DdNvgV8npg54A8LLzqaEZvfVhWDfxXlO56KZ49JgU9/gmA+dBgSC0Uhc30DIsxYQlFZFXmQmRmIwNptZfngLa5MRz2ceXKYMmHnT2oRUcl2Aq3TJjRlzKNimpIvYM9qodhA2xVCdOZ2sgQOi3wYBo/BpunVahRBT2btBo1RrJ8lB/jnxS93DkMoWmQiaBfOLJNS4TMmlATix2q9TScpzrWCWWq5BPKYVclsJyjVIXNcZF4ZTKyBJutRxCphPYXuFHaE+d9TtubVoXYrUBXemRq/shexvUBKkl0ss4mqb//ve3D29/HHq9/du3r+bTmf9nB0HP85yvb1g8TvBCN/j04PXp34vxy4e3xk+BEM9DrTbv49dR0T8caX383kHcvGN6vrj09Zj3eVrcufH8su5bWgZ92zXTl7bKH+9RgB1e386v+rWzTD74/vNR44PJ/O0/zu6+dNWXIG3rqp2Ps9JyfjsiDFK3+3oZv071PrwFrxd3vuDk8kvY1LNmrzN5oBD+jrzjb7//H9WFVHRkLQAA -->
