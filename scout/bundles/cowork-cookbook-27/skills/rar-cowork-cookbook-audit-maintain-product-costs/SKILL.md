---
name: "rar-cowork-cookbook-audit-maintain-product-costs"
description: "Runs a read-only completeness and policy audit of maintain product costs records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_product_costs", "rar_sha256": "a93004a1ed18def90387398c280f40b115205a200d2b04873b881d903e2a7edf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
