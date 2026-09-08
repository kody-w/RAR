---
name: "rar-cowork-cookbook-audit-collect-customer-feedback"
description: "Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_collect_customer_feedback", "rar_sha256": "c7f49e4ff5249854f3e8d4207651305760fe41df49e17ef80c02de538ed60a5e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `audit_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Completeness Audit — Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
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
      "description": "Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 c7f49e4ff5249854…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_collect_customer_feedback_agent.py` first:

```bash
python3 audit_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_collect_customer_feedback_agent.py   # or on stdin
python3 audit_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Completeness Audit — Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_collect_customer_feedback',
    "version": '3.0.2',
    "display_name": 'Collect customer feedback Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of',
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
        "upstream_slug": 'audit-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '18abbf505d465066',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit collect customer feedback records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to collect customer feedback. Output an Excel workbook 'audit-collect-customer-feedback-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no collect customer feedback data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads collect customer feedback records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of collect customer feedback records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of', 'example_request': 'Audit collect customer feedback records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants collect customer feedback records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCollectCustomerFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCollectCustomerFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-collect-customer-feedback-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
