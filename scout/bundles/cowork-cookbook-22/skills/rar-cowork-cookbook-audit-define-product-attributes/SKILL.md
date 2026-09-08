---
name: "rar-cowork-cookbook-audit-define-product-attributes"
description: "Runs a read-only completeness and policy audit of product attribute records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_product_attributes", "rar_sha256": "8af9f4ef0bac30c1a9e518f009a3e5e4dd02a51e27de81a0096680ad20af4a52", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
