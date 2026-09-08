---
name: "rar-cowork-cookbook-audit-identify-production-resources"
description: "Runs a read-only completeness and policy audit of production resource records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_production_resources", "rar_sha256": "10a65483123a6db24fc42fde6cf7cbaa0f0d51a6215f98adc5f3d3ebd6c84de6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
