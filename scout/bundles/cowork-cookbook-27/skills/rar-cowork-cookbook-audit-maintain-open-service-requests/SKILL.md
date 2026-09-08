---
name: "rar-cowork-cookbook-audit-maintain-open-service-requests"
description: "Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_open_service_requests", "rar_sha256": "f821a9bc6527d36021eec37e7ee9b413d689823fff4eedd91e5e69aafb846091", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Completeness Audit — Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
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
      "description": "Date range used to judge stale records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-maintain-open-service-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 f821a9bc6527d360…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_open_service_requests_agent.py` first:

```bash
python3 audit_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_open_service_requests_agent.py   # or on stdin
python3 audit_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Completeness Audit — Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_open_service_requests',
    "version": '3.0.2',
    "display_name": 'Maintain open service requests Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3990891c93a655bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-maintain-open-service-requests-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit maintain open service requests records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to maintain open service requests. Output an Excel workbook 'audit-maintain-open-service-requests-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no maintain open service requests data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain open service requests records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit open service requests in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-maintain-open-service-requests-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants open service requests checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditMaintainOpenServiceRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainOpenServiceRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-maintain-open-service-requests-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
