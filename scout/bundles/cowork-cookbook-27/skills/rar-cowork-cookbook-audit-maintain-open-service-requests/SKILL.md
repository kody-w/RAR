---
name: "rar-cowork-cookbook-audit-maintain-open-service-requests"
description: "Runs a read-only completeness and policy audit of open service request records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_open_service_requests", "rar_sha256": "f821a9bc6527d36021eec37e7ee9b413d689823fff4eedd91e5e69aafb846091", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
