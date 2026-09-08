---
name: "rar-cowork-cookbook-audit-establish-notification-recipients"
description: "Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_establish_notification_recipients", "rar_sha256": "9a588271fe99ecb2f134cd11bf9e25b8a640bc5501fb4c1f56bd6922d8f52a36", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_establish_notification_recipients`. The original RAPP
agent is preserved byte-for-byte in `audit_establish_notification_recipients_agent.py` and in the RCI capsule.

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

Establish notification recipients Completeness Audit — Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-establish-notification-recipients
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
      "description": "Name of the Excel workbook to produce, e.g. audit-establish-notification-recipients-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 9a588271fe99ecb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_establish_notification_recipients_agent.py` first:

```bash
python3 audit_establish_notification_recipients_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_establish_notification_recipients_agent.py   # or on stdin
python3 audit_establish_notification_recipients_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish notification recipients Completeness Audit — Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-establish-notification-recipients
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_establish_notification_recipients',
    "version": '3.0.2',
    "display_name": 'Establish notification recipients Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s',
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
        "upstream_slug": 'audit-establish-notification-recipients',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-establish-notification-recipients',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93f4258c747f8ee0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/establish-notification-recipients'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-establish-notification-recipients', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-establish-notification-recipients-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit establish notification recipients records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to establish notification recipients. Output an Excel workbook 'audit-establish-notification-recipients-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no establish notification recipients data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads establish notification recipients records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s', 'example_request': 'Audit establish notification recipients in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-establish-notification-recipients-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check establish notification recipients records in D365 for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditEstablishNotificationRecipients(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEstablishNotificationRecipients'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-establish-notification-recipients-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditEstablishNotificationRecipients().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
