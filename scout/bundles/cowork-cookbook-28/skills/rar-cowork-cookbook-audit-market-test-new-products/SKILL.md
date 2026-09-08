---
name: "rar-cowork-cookbook-audit-market-test-new-products"
description: "Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_market_test_new_products", "rar_sha256": "fda4bcf9c7806ba2bc66ba2a7b2e4e783912bc2bad493d238c920efecdb4106c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `audit_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Completeness Audit — Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
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
      "description": "Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 fda4bcf9c7806ba2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_market_test_new_products_agent.py` first:

```bash
python3 audit_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_market_test_new_products_agent.py   # or on stdin
python3 audit_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Completeness Audit — Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_market_test_new_products',
    "version": '3.0.3',
    "display_name": 'Market test new products Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0244c0383750101',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit market test new products records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to market test new products. Output an Excel workbook 'audit-market-test-new-products-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no market test new products data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads market test new products records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of market test new products records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit market test new products records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants market test new products records in Dynamics 365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMarketTestNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMarketTestNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-market-test-new-products-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
