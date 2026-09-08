---
name: "rar-cowork-cookbook-audit-define-service-scheduling-approach"
description: "Audits service scheduling approach records in Dynamics 365 F&SCM (legal entity USMF) read-only for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_service_scheduling_approach", "rar_sha256": "bd45a943f537dfed5577309da5aeabedae5f1fb7034f0dea605ed756ffe0e2dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
