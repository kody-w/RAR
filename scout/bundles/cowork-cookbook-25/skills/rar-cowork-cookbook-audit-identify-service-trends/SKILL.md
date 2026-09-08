---
name: "rar-cowork-cookbook-audit-identify-service-trends"
description: "Runs a read-only completeness and policy audit of service-trend records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_identify_service_trends", "rar_sha256": "14111087b4e790db1f707835890d54d76d758c37cabb4d85cea71f7698100371", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
