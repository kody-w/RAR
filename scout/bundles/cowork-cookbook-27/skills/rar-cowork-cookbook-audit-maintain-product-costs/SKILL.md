---
name: "rar-cowork-cookbook-audit-maintain-product-costs"
description: "Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_product_costs", "rar_sha256": "a93004a1ed18def90387398c280f40b115205a200d2b04873b881d903e2a7edf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_product_costs`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_product_costs_agent.py` and in the RCI capsule.

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

Maintain product costs Completeness Audit — Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
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
      "description": "Name of the Excel workbook to produce, e.g. audit-maintain-product-costs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 a93004a1ed18def9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_product_costs_agent.py` first:

```bash
python3 audit_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_product_costs_agent.py   # or on stdin
python3 audit_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Completeness Audit — Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_product_costs',
    "version": '3.0.3',
    "display_name": 'Maintain product costs Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a00f1b2b7319a18',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-maintain-product-costs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit maintain product costs records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to maintain product costs. Output an Excel workbook 'audit-maintain-product-costs-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no maintain product costs data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain product costs records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit maintain product costs in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-maintain-product-costs-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants maintain product costs records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMaintainProductCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainProductCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-maintain-product-costs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
