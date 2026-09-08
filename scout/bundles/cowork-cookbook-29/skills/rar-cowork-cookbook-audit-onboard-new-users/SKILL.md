---
name: "rar-cowork-cookbook-audit-onboard-new-users"
description: "Audits onboard-new-users records in a Dynamics 365 F&SCM legal entity for missing required fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returning a read-only Excel workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_users", "rar_sha256": "425d18bd08d755188fe42a75c68c713d4cd643ac12b6dbf836453b74dc42ff8c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
