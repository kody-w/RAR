---
name: "rar-cowork-cookbook-audit-plan-training-delivery"
description: "Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_training_delivery", "rar_sha256": "ff049183e3e67764ff8e15533d3d257d36e97f6edefb29d7c940502e2501129f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_training_delivery`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_training_delivery_agent.py` and in the RCI capsule.

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

Plan training delivery Completeness Audit — Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
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
      "description": "Name of the Excel workbook to produce, e.g. audit-plan-training-delivery-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 ff049183e3e67764…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_training_delivery_agent.py` first:

```bash
python3 audit_plan_training_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_training_delivery_agent.py   # or on stdin
python3 audit_plan_training_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan training delivery Completeness Audit — Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_training_delivery',
    "version": '3.0.3',
    "display_name": 'Plan training delivery Completeness Audit',
    "description": 'Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-plan-training-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-training-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21bcf2ccf8b93f14',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/plan-training-delivery'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-plan-training-delivery', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-plan-training-delivery-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit plan training delivery records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to plan training delivery. Output an Excel workbook 'audit-plan-training-delivery-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no plan training delivery data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads plan training delivery records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel', 'example_request': 'Audit plan training delivery records in USMF for completeness and give me the Excel workbook with a summary sheet.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-training-delivery-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of plan training delivery data in D365 ERP, delivered as a per-category Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPlanTrainingDelivery(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanTrainingDelivery'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-plan-training-delivery-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPlanTrainingDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
