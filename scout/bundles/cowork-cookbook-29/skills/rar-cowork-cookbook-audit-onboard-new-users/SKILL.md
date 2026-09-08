---
name: "rar-cowork-cookbook-audit-onboard-new-users"
description: "Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_users", "rar_sha256": "425d18bd08d755188fe42a75c68c713d4cd643ac12b6dbf836453b74dc42ff8c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_users`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_users_agent.py` and in the RCI capsule.

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

Onboard new users Completeness Audit — Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
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
      "description": "Date range treated as current for stale-date checks (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-onboard-new-users-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 425d18bd08d75518…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_users_agent.py` first:

```bash
python3 audit_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_users_agent.py   # or on stdin
python3 audit_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Completeness Audit — Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_users',
    "version": '3.0.3',
    "display_name": 'Onboard new users Completeness Audit',
    "description": 'Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook',
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
        "upstream_slug": 'audit-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '349455903b3d0ea3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current for stale-date checks (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-users-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit onboard new users records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to onboard new users. Output an Excel workbook 'audit-onboard-new-users-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no onboard new users data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-04', 'what_it_does': 'Reads onboard new users records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook', 'example_request': 'Audit onboard new users records in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current for stale-date checks (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-users-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of onboard-new-users records in D365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditOnboardNewUsers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewUsers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current for stale-date checks (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-onboard-new-users-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
