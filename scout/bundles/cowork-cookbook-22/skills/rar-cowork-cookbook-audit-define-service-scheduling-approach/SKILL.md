---
name: "rar-cowork-cookbook-audit-define-service-scheduling-approach"
description: "Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_service_scheduling_approach", "rar_sha256": "bd45a943f537dfed5577309da5aeabedae5f1fb7034f0dea605ed756ffe0e2dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_service_scheduling_approach`. The original RAPP
agent is preserved byte-for-byte in `audit_define_service_scheduling_approach_agent.py` and in the RCI capsule.

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

Define service scheduling approach Completeness Audit — Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
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
      "description": "Excel workbook name, e.g. audit-define-service-scheduling-approach-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 bd45a943f537dfed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_service_scheduling_approach_agent.py` first:

```bash
python3 audit_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_service_scheduling_approach_agent.py   # or on stdin
python3 audit_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Completeness Audit — Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_service_scheduling_approach',
    "version": '3.0.2',
    "display_name": 'Define service scheduling approach Completeness Audit',
    "description": 'Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook.',
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
        "upstream_slug": 'audit-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0e4a4c8d4af082e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-define-service-scheduling-approach-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define service scheduling approach records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define service scheduling approach. Output an Excel workbook 'audit-define-service-scheduling-approach-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define service scheduling approach data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service scheduling approach records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook.', 'example_request': 'Audit define service scheduling approach records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-define-service-scheduling-approach-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of define service scheduling approach records in D365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineServiceSchedulingApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineServiceSchedulingApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-define-service-scheduling-approach-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
