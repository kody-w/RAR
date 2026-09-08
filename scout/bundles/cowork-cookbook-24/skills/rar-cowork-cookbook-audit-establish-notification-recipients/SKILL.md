---
name: "rar-cowork-cookbook-audit-establish-notification-recipients"
description: "Runs a read-only completeness and policy audit of establish notification recipients records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_establish_notification_recipients", "rar_sha256": "9a588271fe99ecb2f134cd11bf9e25b8a640bc5501fb4c1f56bd6922d8f52a36", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
