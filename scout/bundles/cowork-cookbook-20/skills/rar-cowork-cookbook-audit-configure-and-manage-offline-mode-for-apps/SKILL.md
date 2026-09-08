---
name: "rar-cowork-cookbook-audit-configure-and-manage-offline-mode-for-apps"
description: "Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps", "rar_sha256": "864083745d6f8a2639635c8f749c555940e56397802115b3f174edb40285db91", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_offline_mode_for_apps_agent.py` and in the RCI capsule.

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

Configure and manage offline mode for apps Completeness Audit — Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps
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
      "description": "Name of the Excel workbook to produce, e.g. audit-configure-and-manage-offline-mode-for-apps-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 864083745d6f8a26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_offline_mode_for_apps_agent.py` first:

```bash
python3 audit_configure_and_manage_offline_mode_for_apps_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_offline_mode_for_apps_agent.py   # or on stdin
python3 audit_configure_and_manage_offline_mode_for_apps_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage offline mode for apps Completeness Audit — Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps',
    "version": '3.0.2',
    "display_name": 'Configure and manage offline mode for apps Completeness Audit',
    "description": 'Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar',
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
        "upstream_slug": 'audit-configure-and-manage-offline-mode-for-apps',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '851693b60bd401a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-offline-mode-for-apps'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-offline-mode-for-apps', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-offline-mode-for-apps-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and manage offline mode for apps records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and manage offline mode for apps. Output an Excel workbook 'audit-configure-and-manage-offline-mode-for-apps-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and manage offline mode for apps data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and manage offline mode for apps records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar', 'example_request': 'Audit offline mode for apps records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-offline-mode-for-apps-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a read-only completeness and policy check of offline mode for apps records in a D365 legal entity, delivered as an Excel findings workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndManageOfflineModeForApps(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageOfflineModeForApps'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-offline-mode-for-apps-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndManageOfflineModeForApps().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
