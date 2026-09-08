---
name: "rar-cowork-cookbook-audit-define-product-attributes"
description: "Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_product_attributes", "rar_sha256": "8af9f4ef0bac30c1a9e518f009a3e5e4dd02a51e27de81a0096680ad20af4a52", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_product_attributes`. The original RAPP
agent is preserved byte-for-byte in `audit_define_product_attributes_agent.py` and in the RCI capsule.

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

Define product attributes Completeness Audit — Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-product-attributes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 8af9f4ef0bac30c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_product_attributes_agent.py` first:

```bash
python3 audit_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_product_attributes_agent.py   # or on stdin
python3 audit_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Completeness Audit — Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_product_attributes',
    "version": '3.0.2',
    "display_name": 'Define product attributes Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a8fbd0693dd700f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-product-attributes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define product attributes records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define product attributes. Output an Excel workbook 'audit-define-product-attributes-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define product attributes data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define product attributes records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit product attributes in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-product-attributes-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants product attribute records checked for missing required fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineProductAttributes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineProductAttributes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-product-attributes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
