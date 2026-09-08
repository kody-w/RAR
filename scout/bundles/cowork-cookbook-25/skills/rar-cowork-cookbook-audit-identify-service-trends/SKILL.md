---
name: "rar-cowork-cookbook-audit-identify-service-trends"
description: "Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_service_trends", "rar_sha256": "14111087b4e790db1f707835890d54d76d758c37cabb4d85cea71f7698100371", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_identify_service_trends`. The original RAPP
agent is preserved byte-for-byte in `audit_identify_service_trends_agent.py` and in the RCI capsule.

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

Identify service trends Completeness Audit — Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-service-trends
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
      "description": "Name of the Excel workbook to produce, e.g. audit-identify-service-trends-2026-05-24.xlsx.",
      "type": "string"
    },
    "record_scope": {
      "description": "The record type/area to audit, here identify service trends records.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_identify_service_trends_agent.py` and embedded as the fenced Python below (sha256 14111087b4e790db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_identify_service_trends_agent.py` first:

```bash
python3 audit_identify_service_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_identify_service_trends_agent.py   # or on stdin
python3 audit_identify_service_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify service trends Completeness Audit — Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-identify-service-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_identify_service_trends',
    "version": '3.0.2',
    "display_name": 'Identify service trends Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-identify-service-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-identify-service-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9876f1a4e6377cc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/identify-service-trends'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-identify-service-trends', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-identify-service-trends-2026-05-24.xlsx.', 'record_scope': 'The record type/area to audit, here identify service trends records.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit identify service trends records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to identify service trends. Output an Excel workbook 'audit-identify-service-trends-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no identify service trends data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify service trends records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit USMF service trends records for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The record type/area to audit, here identify service trends records.', 'name': 'record_scope'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-service-trends-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check D365 ERP service-trend records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditIdentifyServiceTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditIdentifyServiceTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-identify-service-trends-2026-05-24.xlsx.', 'type': 'string'}, 'record_scope': {'description': 'The record type/area to audit, here identify service trends records.', 'type': 'string'}},
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
    print(AuditIdentifyServiceTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
