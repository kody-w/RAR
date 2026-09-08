---
name: "rar-cowork-cookbook-audit-identify-production-resources"
description: "Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_production_resources", "rar_sha256": "10a65483123a6db24fc42fde6cf7cbaa0f0d51a6215f98adc5f3d3ebd6c84de6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_production_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_production_resources_agent.py` and in the RCI capsule.

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

Identify production resources Completeness Audit — Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
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
      "description": "Date range used to judge stale dates; adjust for demo data eras such as FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-identify-production-resources-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 10a65483123a6db2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_production_resources_agent.py` first:

```bash
python3 audit_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_production_resources_agent.py   # or on stdin
python3 audit_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Completeness Audit — Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_production_resources',
    "version": '3.0.2',
    "display_name": 'Identify production resources Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b51462b233fd1719',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-identify-production-resources-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit identify production resources records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to identify production resources. Output an Excel workbook 'audit-identify-production-resources-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no identify production resources data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify production resources records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit production resources in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-production-resources-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants production resource records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditIdentifyProductionResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyProductionResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-production-resources-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
