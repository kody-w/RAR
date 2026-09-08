---
name: "rar-cowork-cookbook-audit-configure-and-manage-offline-mode-for-apps"
description: "Audits offline-mode-for-apps configuration records in Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for completeness and policy compliance, returning a read-only Excel workbook of findings by category plus a summar"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps", "rar_sha256": "864083745d6f8a2639635c8f749c555940e56397802115b3f174edb40285db91", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOb2JLnV9HcjpiqauzLDpJfvIhBrEJiESAJqVzhYgexikUsNfXd5yDda1e959fd1TN/jRy2EJyTe/4y04ffXpyujcv65dOLGTjFQnSyLImDeuEU/oIt+7JOwVeZuuDvwiuLtk7cri3r5uXDix80Xp1UbVIWYDvT+UnbLMowzJIi+JiXfvAxLOuPTlU1884wibramRcv6sAra79ZJMWCGwsnT7xmgVPkQvifJqssfrwnzqKNg3f23PyIN/RFlXVRUvy0AFQBwbzKgjYogqZ5yFqVWeKNz/uJU3jBB8Cm7eoiKaKFA64d/2NZZOOCH7wgW8yUHzqV4SJMCh+sahYu2O+0QVTW48wMEF40XZ47NVA2GJyZY/Py6edfPrwk4Prl028vXuY0zbvy7JuSAVP4ilM4UaA9jaEAWwhlzQBLAEqZU0RgSzUCuxfgdxXUQKMc3PKDcPH268cmyMIPi3//97R36qj56dPnYvH2+fwy/zG64mGktnSaNvCB4JXjJlnSjq8LJuudsXnT/6EFcFsRvT53fqNUVou/z89+fDJ5jYL2x88vJRDh4afPLz8tgKk/v9TdfP06U6l+/Ok1K/ug/vGnb3Sazr0GXjsTA1K/fnn7/UYWLPy2NAkXX0ydZ994gUhIqgAQ/4N+8+cp+hu5N5N8eS7+saw+LL5Pedbn70DeZ2C6gO73yQIbgJ0vr9cyKX5841GX96CY4+bHn/4VWS8OvDRLmva/RPfnJ+EYBB6w1ptJfvrwcN8vC+hNt680/zXbCgTMX9EELH9n99VQ/4r2w7P/QHqO2OarL79L7nsboL8vfv6Xuv1HGz4sws8vXJAldxB3bhZ8Wvz2CJGff/C/3fzhl98B6f+UjFl2tfeg8CV3iiQMmvbLl59/aB63f/jl5x+6CkRx4ORfujr7Hs3v2fXB508WfFv145/3Av6HIi3Kvlh8zaHFb2X1P+rfXxdHJ0v8b/ebT4s/ZuL8gRazEu9Mnyb4QzY2QNY/2PGnl98BDBVAm857PAb48W//tlASry6bMmwXpld27QI4uE3yYBbeihMAuc0DNeoA2LVJgGHf1oH4nz08SwwQ8df/5T2w96P3Bv2wMwPcl3cYD74AyJ0tDDDuyxvif5kR/wtI1C8z4v/6urAAn7JOAGQ72cJgdP3zvLxoZxmqOmiC+g5wyx3bZ52YL+aK8OtfZfXlQfW1Gn99FILkiYsGu5kxsemy4HXW/hQHxZuuHqhzwRB4HWCYlR6QLkwAss8FoymzO8DU2VJNmmTZwk8A6rRzQZhpA2t+mon9+uuvrtPEn4sniOOLZyFsYLDgqziLjx+BmkDgKG4/F4EXl4sffvv9h8X/XvxHux7EZx46qCxvvgISyqamLkDudTlYNldOAPqO//DVb7+/GRuQKUDlBp5NwiR4bgbmSgP/3fKmxHzESGrhBsB4wNp5VdbtXCCT9nWxCRdf5QVM50dz7YjLpl34QRUUflCACtvGDlDnqyWLsl00IECbcPyw6JrgwfVXt3YeIuYABJz214XC6qBSlRn4ZxbzsQhsLosEmP9rXDzvAyL1D81i/U7idaHO0bqonNqp4tp54xE6T7+ACvW+HRB3FkXQfy7m+hzMpnqkztM8YBGwjPfm0o+zz+d2AYTWsxVp39c4cz21HnW1/lw0b2nh1MGjcQGijIuoS/y5WPztLaSauOwy/2E/IOlM6c0L/ptXHjH4tUF4BNMzpt8bpsUc04/W5tEwsX/sbx7dxeJzhyEosfj/uc+ajcSIosGLjMVzC161jPPTeXPrOTv52a2CLuch3SNRv3U+7+j2DvKfiywBkViPf3uufLj8bc0TOIEvfIBNxoM+iDfgvJnuIx3m8K7rOZGcz8V7NfkAZH1AJzAvwA6QW3NIvzOcn75LGgOAmH9/6yze/DGbEYT8oupcYMpFGAS+63gpkGo23rubQW7MsbHo48SL/6TVAlAHhgP0F0CIRyz0xetXhH8+fRf9TxufDdS85dFcdiCj6wcBIEcwCzg7uE9aAGxO++z0gZ6fHkSAGnnVzrq7ILiAps+bQR3cuqRJ2hk/n3YNKoDlH+fvp6bz3WCoQBoBY4FkqTpg3Ud6zSGTg/YIyAAQBmRbnhSgXQBGeTPCg6CTz1gBsPitn31SfNx+Uyh45ORc5943zorMe+bWYREC0cGd8Y+QYn0vTAC9fF7x4PuPkfaV20x7htUGQGMefH367DFen23Csw9ZvNP99E+j1I9/bdp6FP7DnwPg0yJu26r5BMPPYv1eq19BbsJPWZtn3f74tZh+BIw+PoHn43cR5E98nib4tPhrsv6JxFuufFqgr8grMj/avcXa2weYhv24Pn8k5qefCyP4BsGAfZmDYJsdOc6g8V4v35eAohnVQTQvftbPZi67Paj0j4IBvPK5+GPwz8kH6lERzcHalH8AhUfjABLh6cSvdQ08KlrA25/b0Ch4nae3WfwmePlUdFn24QWgavAX57+5juVztDfzBAnyCnR4bRI8fj3AY2jnyz9P19rjwsleF1wAgCpr/hiRb9Vnrr5/SJynwkBRD3D4sPCBmZq5WgKFZ+Zz0jkNiGLg+lmxdqxmTZ6j4txczhu+9ACzy/6f5eHAw0U9m3Jm+wDBa+dHc/47wJ4PZn9bHExFAJmdl/MNZ4beHHQTwKDCGYhJf5dtBhyafQF2B6n3Hb5zkXosWTyXzJwfQf5hEbxGrw+W36X7tZH+Z6In0KPMdPzy01yuP7yBHfgGw8+Hxdc5BhjxbbKcOQRFB4b2n+cZavbqY8t8AfaAr6+bvv5HiRu8/PI9uR6I+GUOw2cw/aN06ox0oBLMPv2HogpkBnz9bq7CD+3/arp/xBCM+oiQHzHidcia4TuWAyI+MB5Uylnbb2b8pkz5mA5nZYDy7fM/M357ATHuzG5/i/K38QIsB5D4sZnbJhiAAmAIfj/TFzz7vx483ug1sQMaXUBwSRHIEqcJ0qfCpYNR+IrCSW8Z0sTKI0lyRSABCW7SSwRDUdLFQ5QmQEEmEGxJ+u4KBfSeoPBl7hWTWcZZQGCajwBXgm+PwS3/TbmnMrPlvs45sxHedPztxaUIsFIimg3z/LDwCnUpjHZN2YVqKijJ/aZ2DqAWSQbuZ+Flp96G4uAwphlskEktA8YUN2ljnokqbZCIjnIhkvJt4Mlkese1W3L1jXtiuR5WcBF7GqnWrDwYPHB3V22jWaqQCdS0tft0xTbhwQpHVOiyWjiYO0GNsOy0PZHLnaokFxXJl6cx3WQHMx7t89Hc3GE8q+Gb1RRarorBVjtqAT9cxzAWATjGWao5MZ/xiVUE8p1AWNkFZq5QYmXAhYzBPMXWo+GKxkmLqMmEha2LUAG80i6SSF6rzeANGyQ32VMzmVpUoZB0z+QN65+r5DrJfH3qG7/QyTE33d66kEtO3HfJnZ8sE2bqY8ab52pvmssJZ+lMWw5Iu25kNvO7tuiX4jDBy6VONzGk6BcqTGjF02l8hQ17v09EbB0fdsTFFeQldT0rJ1iQm60Ge0NoXPlVP4WOVeUVkw/NGheRSUeXK7TXbf40tLzSl8zEtMwkQJCOWyolKZKSi8OpCwSMAX6R+LpXy+2xlI+HgbmsbCXzUuwaqburSJvbe0Zt8cyDtJqzcX15N7Zyss/KvjGJPaeP4yndChczThu4Ywxd5vyTS27yy5pLglgR8tUFWrMxd94ybc9wbi/ZCRedQ0cKqSI4keoeqQ0yT1lLDqyDeYm5XUGd1ms+71K060qMmZZlk1wvhxxTMM8hJMgVXKuSzX57Wu31i0nCW1M5CkdZvXJDpmZ4V91Nu0UinQx8ZR2d+Ey+CMd0W0qoHAqnfX6almmY7jf98oYfjF3seSx9wXaQENc4sYrOWVwdrCV6ktdXh7WYNDB2gwXpK9kyl0zTEk2s3D0qOnAihrL2qWVqE1M3rE2r1bE1tkZctf62FuSWlqnbajNyo5HulnsyHMwT1Q4U0udKEaGwz9IrQ+8Z+LZR1/zy0CH6xhWuvePQYqln1glSp8bMt5aCFg3BFOvcCdgx8JyDe5y2Qa/sbGhH+ecLVXMjvcePnGkjfhcmS3/AbkaEi5uuqGOJjqUAVqRzds/XJ57KdzgExuzOjmB/vNoJKzK226u7SqgvAtS2xllYr6X8JORtGhf1KiBxWY1g3mAyATQ+Kk5wh5N8QpS8umh6fGlg0VCrW2HG3d3ym+utDchI4XNTSHfx8ShHlMWwnXVEqGS95aZJ12q8SIwwuaSs6wlmH/k84UFSymviAbtk8bAk+TsSbDI7omGBrp1Teawu9vXo1UMPVMoC5ULaSSox8HZ5iMg9ou8T+ViGkb7Wa1vvkThrXHiiN3KYHQ+3Mtvt8GQiTkti8pu7sxRz/DqpK42Ge7S/TSCzzs15b9DX8TjEPRwPymDL51t5Rwl2q6zhdjNJR6lKqVV27aGYK/lxRdQHc1KwAC8N2dgHFyNC7zcIHbWsdnir3V+oYNrpcV+ssxUy0U4zVp1OZSs2C4P0kAYB1Dd5dBx9FiKhJDAhWyY3FdZSkSLL6kZKc0bgdb0IYJk7XXY2clqvUlzidBRfOvQ23NKEo24TAbn0I7S5bk+RGhdK35JQfeYLHXPhuD67Z6HeEwiAoEAgJN7p+8LboBHS7Vc39Yyg4+lgDGYVjUO33KBSM2kc5KAGBpzIbJSigDfmlFc4VAx2at7jGLtLHaXfYGy4WM1qs2yWVSnga93NZYDW1lLIHJW8ljhyb0IgibpLkbr1NmQ8ZHmknZMkabUBlKWYpNHMwn3v0DBmVWR7ut0qBqEd9kh4W1nd+VR4AmWlND+SS0GI+WsbCiquG5yEsVIqr8vNVhyG2DuAO8MUNHrdOMo6r2RpWqsjlpecyDo+x5uEufHR6y26beRTsOwcmj2slbPobAXNjIh8qcqMsClxtWtWMYWkZ5NG2Ki+8vTVq0i3ZnHU1kir3IjZGUF0rC/DBj0mkF1LmmDuIiyy1xhSb2XMkrVs0ljLVeA7R5AQLC2vmrzf1coBQiwGsrY3Y6v3OuXLXYtdEVGzyiNMKNM9gJ39nhOXrt+ymnoy9jBs+ykWgvEJHzGfH2HdLZMQVjD5dCEFM84xH9q1CctrZXQiSpnQnKM0tjJj+aCD30bXzd33dkRYnLTy5so6hw7xpGrXagnlBhyv9omGXc7iMN4UX1WuN5W/cu7BDDc3Wd86uzrmRbJfttZWMjad42rCSgEtRLVsTolSuQYSaEmzPFotywr6cbUtnPSqSp2UsOh5hV1WBb8kezyNazLDhnEZSSKR39koudjYQJhXyL4SBLnZIpFdHC6DJbUwdj7vd3rlNxFpMX3cm6ddbIpcViVH2LNVhFkSDbkJSpbVD8x+PCviJb1ehpaqOhnaaHwsDatDu5QIRLjJMSJJnLbquLVxyN2bqyO1hw1H9cysY2ffCy6anW8Ch+x3PTsEhpuzO1FMtNRdHm5bpizkKipq69KCofLMnPgy4erK9Ch8BLDZqXafMMrQEmgskWyfVA7GZDG65Kzybm/u7g4g5Tko2L3Apn2C7SJaV1gqnYRJ2d5yK9J5ZmOkACqdvp4oBHE8bOROmLLeExknLSWoy9Zhn2/kaUSqYKeL04W4WBsZVt1TsrF36yFiGTMjFGxF8ipn+MJ+sHcO5Bhn2WoJfc3wVqELvp3VJe+cmIA/YZPKwryJV4jFL0X+7giWvsk5rz3DVXSq0R1P0srSIHAh2+0TKiqmbTEKXnJYciuK6XItpXCbFdbaYNjlNR9q+wzlUlxHCJMetrCfwY7pJ5GObaxTcW2cPKNvgmIImMNYKBySudhBBXpl7IYKRBKvz/W1PMpyIm0wr17i1wufhWsRIlLMTDlZw1e4X+xiSpM04pof3HVhRztotS52Q8o1sSrerPh2EWMkTZqTZ663+YUpMGorLrOGNrL7Oeo5j3EyQ0GG8OJimuUztrrOfHg/9XzrGvspMchgLGLLWGX49bSHaapj4A3HNik94CK9IUSRuQ/sNIpSb2xXarVbHfrWlZ2D4sCoe12vLI3gLfW2BNUqxY+3PeeVYsSOxK3qbza5mU7iqmOG1iHko9kR7nIHwTCPgFWt6FYyamnqMT+HVIC7hkznpXYc19qBsQ6H9bgPiOtdTu++uTepDtYx70Bbue6pKGdGcu+0fpgwhlx50XlzRuvtjVpno+NDdQ6r54w/97ozZV2X6vhZcDzHu7q0cV77slNq5Fa8Fc5xJzYsyawH1eCj/Z5nQHeZeOaRDychsJPOYkNVYejhdtnQWE4e6Iu5TeL90SQJOKk4NTx4sC4nm8LzYMmCLq3Na3tMCKZa0eT2dkvaZVAXFeLrcKXIwxiP50o3cm5zEablAUokg7z1NO/LfocMh4SUM1rmb1vluifXy4ps2MnZBD4bD4eNduoreetTVo+lyBJ19aqD7oa7wjUA+N3B3uJ1al0QzKFRLKm90wk9YjaeDeNhglDCVJFyOtSe1CnYfhybUUZMjlrucwvUbpxD9xeXHhmMvBhpNdw2cSpx22SFafUJ77NDxZirq4Je9932EJshL4Bp7w55VO8fD9s6QRM7bTclhIxdmjm7y3E0LxiyWyPLHbyebqZ1Kfi+QuR0hdWHMOjDmugllbCYdYBuKQ2CiOy4pwznNtk5dGq7dR2qRTDQ57JPAimSJtuhuxype7ZfgjkoguD+tmrDaSwuij3ajbgW6SW/b8pLtUNOV3YbVERtcnos9jYab7KYhe7Vjt0f2sZX3U5FjqjgOMPVzpFjrl/7yS1Ycn0gjl7QxihcD6nWelYdHtZNxZKSEZ1bbLhVukqLaleoHarhykEm5J6/nk0w48QAaZenBCUg1EIkXXAGTGO7kl4aqRJfUbE5GNnmeolSXilQ90iWLs8Lq4uQ11my4kWrWtEsvKOILeWy3ATF7JqnA+5Sn7rr3koJhl9KJ4JE6Kq5eUFvNUq+nPJjxJdSo2OM3NMCIlr3iLSd1XU0kTsWb++JdNsECd0M0BJA8YFlGcm5wrdd1yOw01hdghhBiRv7bJrquztuKa7LUZdP28PZxO7o4MdK6iUZJ56qpuRO6+Wd2Toyzg742kQnMVgeMureHDucXWvjivOPsZjb1mBlAb8WSq9aD25PnsMbuxqwMmtK/U7zXlR6FpyANgKAwoV11eP9FinKUd2uizu9g86yYnLrmD7Zsrh2iDuxX1fHW135Sx10aPalDIjbUSFWsILiGJsLkGumBi7oTmrXZ2ikibHGRpE+jrDpEO3qlOOSYDiIRVc7TpUPHWU1bDhdk8Zii/iSE4MGmbAEcRfcleU7XZ9g6Z7QvXOVjgbBYqTGY3qAYeHpHiMlIw6I3oWZaviht8+4eNPyU1sWjKU5bojnZX9f1Xu6OScbIVNRs+sGEZYzwUHWFIKhvbie7MzbgSGUrHVE3NCHW0YuGZXGz/ZQoVS5LbyB7Ih7YIIRdbvtbjolnkUNv6CclHuxCJ8nlby1LrZGI1a73sTp4OOYskOUARcYE/dPcnbU+wooCFdI1eq+d8+jtvYrJE9Mdd2kfe9NmtF71E3yWq5sVo2Jn3LbDFuErDAs2GYQYo8UpaCd1Fww+WqHfnAcJ6Q+bFGrTm8taW0IRWsE/dRO+kVChLOtOYLeqfWxJuk0uNp1abQIcsQdP5awpT3UQ6IGK7dDlVWYHlEqEUI/uYKefdxs2FyOtSRElFuu50dmsnjr2F+iDUbDe/lkmG4NIauVJBEZYRNrKMxBBuD387llMRpSEiotdNsbysnF7vfdJCxV6eIihwMdXJvxygT5McTwO0wId2wD2qxBORXwKoPjdhC2FnfoOei+c6ZVcOOPCihE01Y6gV7zpItlKQ+iVBhrHO96GTZ3zM2zWs2Bpu2mOnKOuVZxxe75NFe2awLMUWkeYqerl8dOu1ImsihLdA7uNYlJtWkOTMAy+/sJ4jQPTARXmj/pFOd5OYmv9oZKl1WxLyyT7MYDwxS5TdwREscvx6uMS6ytTqxtXx33osQ8iuimcbt7uXUTIDlBTH+FjLUdHqpCCaBtQjirgOVvUoDurq2jp9kO6u61geFcPIDGySAZxZT5ZaAnrQLRW6tc3UHtSo7Htta9bZIq4nhuoMYXMeSuRvYtJovjiSs5o3YRU3ehlVjDa3qniVYk4zWGC/kGJ7pdZuo8Z7u8WW3TTYomihX1sIH52Oa8CUdurxBuZbhB17GS4gSxCF2J9QEJ+AvF4MrNZZC1GVvWULnrCAxybXeKt1JbK6Em3fc9GD0M7KqnUj2Q8K6ktMxCcRtd9/VojkYRnkcTc9FBig2No8Wbadub3u81jui6m8XB1jkYRQcUIwUnWMgjSuEW0JB1U0iAFAnN79ueNxpy3S9txBSDwVlXme8dKw63csYba86vlcnRhXudath1Szoe4qoZnxiXyTieAqY7OpwPaVqzK7chl2xpfvA0M0R3pwY6Vq0t3jp9WLIeQqbYLYWkW5SrDKVgI30sqVRv23hPctxJ87jUs929crfryxk6Y4wgkns7KEkC8ft+t5FWqO5cTGWb7K7LgAmMVWqjQZNm8kplHNXuNvyq31n1FtudIZVCVhUeBtapDY73eioKjL/BJbbxofsVzOV0xrVkmVwyurUdvDj0yg0Ji02kwQbV6SeSmFCsuN3rYpQhaOXk2L2Jrre1zwZhkA9dNlA2Zpl2nW92oEGHSzJiHdD2H+VshxMIlwlUjZXLs3Ac6kIgJV++Oh7OrBx/ZOnV4OoEQAD9dB5Gn0wQAEz1dlOzvrw6u6jbOGiErQ9QpkzURBwO4TQR+831LOBnCaC0lYlp6GSR3l8LgaDy/VWCGGFX3nStZnhNkLa5YHYXUYDWmd2dEspCCCLlKGXsMTc7Lg8nijIxy84H405h7IWi4mbKjdbSzjB9tJVL0K10e2+VO6rVjBCX+d1tm64xFWIl7LZfKfYZloLMINtyWxmwDeuwCKtkiS3rpXILkfPWaGmWViXQ+muH5NKiNx5UonXW7VTX1zCkHIf7TjLbEr+culBPjsJ2xFg1GK75uCM8tdZP5daVr4q/YkEYaziWT9YVLeapoC6Ckj4jvBWSho2VV2Vbbi4at9wF69C/M+q0ZILiLpzTGM73zM2Rsg3bkDvWIDKfvk5pR919SszikFHwa5GqG3qXk5JUi8PyBhCtFFp9hZiXw1Rlle3SkgrdSFPC6frAYnpy31q6e5jKSEmxhnEsXIn85b7pIu8y9DBM2lMFl7eNBGnEslNaihlBXd6L8h1bYpnW+Sd/hHCvpI/VmR8DabjsfG8Fu9Vk2mi52nPC/eZMSy7JjaRwRePSiescZPh+ULcERo6wyrU4C+DDlUDUUAOF3PWLn5eeHKaBiSkb5ACshgURpeKbwJHU1SoycS0eOali+pHF8c3AyOg1TaPOXS9XCBvxGr5OYGy03JasEAgbsixUa06eSv/eXKbpWNi0XXKgT98jp344cth26O1jgLpEV9aU221A1TMh9GjYhYfU8T0saxx0hhYZwjeNLAQ2BiWIoc+Nct83wVVudPYS58tb7GLjyWaNo3T0VQffWpc7ZO9xA15pTF2TMDup7aU61qpI6Mfogop3XEQ9atmhYnA+EhmUn0FjnjNCcofvvhT1k0EMAk2iRZfEOB1AB9j2r12jM0OfLfs8lg8MdzteKRXpDZ85CsStLCMVoe5UCMD6cPSVFYWeWZ4bcP5OcsqlZdCNiIIWXmfTkFnzaq1OO4AbnZjodrG6tjEeU3fSh7HNaqvv9/iqn+jC3AVYGlhJhR+46kzAdnex1/ZYDJtYuHumw9/ObXk5yD7XL4+QHWo9rN91/rIUSYbyhiCDG4e/Y7l5CGTSEO9LMBdeY2HgxLpEbPSyubdaoK3hpYSnHp05KscwzN9fPrx8O5h7+W+/mTafEv0/O5B6niu9v1TyOIEMHP/Tg9en/76Iv3x4qb0ECPg8lGuyLno7zvqHI7mPf/WQcaY2Pl8Gez/efh6et040v0/9khR+17T1+KUps8crJ2CH2zXza5fN/GauB77/eMT6EGD+9p8vjAT1l7b88jyZnE/kkmJ+lyTwk28/o7dDyw8v/tubUF9wivwS1NWs+NtbCkBf/BV5xV5+/z+yzpNCFy8AAA== -->
