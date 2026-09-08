---
name: "rar-cowork-cookbook-audit-plan-training-delivery"
description: "Read-only audit of plan training delivery records in Dynamics 365 F&SCM for a given legal entity, flagging missing fields, stale dates, blank descriptions, inactive references, and policy violations, returned as an Excel"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_training_delivery", "rar_sha256": "ff049183e3e67764ff8e15533d3d257d36e97f6edefb29d7c940502e2501129f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
