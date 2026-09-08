---
name: "rar-cowork-cookbook-audit-configure-and-manage-reporting-and-analytics"
description: "Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics", "rar_sha256": "3f837a389b6dcf0e3a8e47267b609d81cc2702ab52ebe335758fb0be780502be", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
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
      "description": "Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 3f837a389b6dcf0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 audit_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 audit_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics',
    "version": '3.0.2',
    "display_name": 'Configure and manage reporting and analytics Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary',
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
        "upstream_slug": 'audit-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0351063000da1cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and manage reporting and analytics records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and manage reporting and analytics. Output an Excel workbook 'audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and manage reporting and analytics data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and manage reporting and analytics records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary', 'example_request': 'Audit the reporting and analytics setup records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change audit of D365 reporting/analytics setup records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageReportingAndAnalytics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOb2JbnV9FkR0y5GjtBYnfHixhJgCRAIBYBolzhYgexikUsNfXd5yKll6rn1zMV3X+N7ExJl3vPfn7nnITfX5yujcv65eOLFjjFYudkWRIH9cIp/MW27Ms6BW9l6oKfhVcWbZ24XVvWzcv7Fz9ovDqp2qQswHG1K5qFs6gDx/9QFtkIdudVFrRBETTNg1xVZok3LpzOT9pFGS6YsXDyxGsWKIEvuP+pbY/gdFXWbVJEH8AB8ONkYzvvAJzDJOpqZ2YGdnll7TeLsARyLqLkHhSLLIicbBEUbdKO78GOtqsLQAcwXrCDF2SLWZWHFn3SxouyCBZNHATtogLKhknhz5s9pw2ish4XVdbNymhdnjv1CHQNBmfWpnn5+Muv718S8Pnl4+8vXuY0YOllPau0fZMxWBf+EYgeBeoXbcDK+osugFjmFBE4VY3A8gX4DkQAquRgyQ/Cxdu3d02Qhe8X//7vae/UUfPzx0/F4u316WX+Bwy+aONg0ZZO0wY+EL5y3CQD+r8u1lnvjM2bGWZNGuC4Inp9nvxGqawW/5ivvXsyeY2C9t2nlxKI8LD0p5efF8DGn17qbv78OlOp3v38mpV9UL/7+RudpnOvgdfOxIDUr5/fvr+RBRu/bU3CxWftxG7feAFfJlUAiH+n3/x6iv5G7s0kn5+b35XV+8WPKc/6/API+wxNF9D9MVlgA3Dy5fVaJsW7Nx51CeLIKbzg3c//iqwXB16aJU37/0T3lyfhGGQEsNabSX5+/3DfrwvoTbevNP812woEzN/RBGz/wu6rof4V7Ydn/0I6S0DOfvXlD8n96AD0j8Uv/1K3/+zA+0X46YUJMpDIteNmwcfF748Q+eUn/9viT7/+AUj/X8loZVd7Dwqfc6dIwqBpP3/+5afmsfzTr7/81FUgigMn/9zV2Y9o/siuDz5/suDbrnd/Pgv4n4u0KPti8TWHFr+X1f+o/3hdGE6W+N/Wm4+L7zNxfkGLWYkvTJ8m+C4bGyDrd3b8+eUPgEQF0KbzHpcBfvzbvy2OiVeXTRm2C80ru3YBHNwmeTALr8dJswD/Z9SoA2DXJgGGfdsH4n/28CwxwObf/pf3AP8P3hv4ww/Y/vwFiIPPAKBnCwOY+/wVtR+LX1H7t9eFDjiVdRIlYG2hrk+nT/OBop2lqOqgCeo7QC53bIMPIME/zB8WSbH47e8z+/yg+1qNvz1qTfLERnV7mHGx6bLgdbaAGYNS8dTXA5UhGAKvAyyz0gPyhQkA+Ll2NGV2B7g6W6tJkyxb+AlAnnYuDDNtYNGPM7HffvvNdZr4U/EEcnTxLIcNDDZ8FWfx4QNQNMySKG4/FYEXl4uffv/jp8X/Xvxnpx7EZx4nUGDe/AUk5DVZWoD863KwDbgSOB+Ay8Nfv//xZm5ApgAlDXg3CZPgeRjEbxr4X2yv7dcfVjixcANgc2Dv/M2gi6R9XRzCxVd538rxXD/ismkXflAFhR8UoIi3sQPU+WrJomwXDQjSJgTFt2uCB9ff3Np5iJgDIHDa3xbH7QlUqzIDv2YxH5vA4bJIgPm/RsZzHRCpf2oWmy8kXhfSHLGLyqmdKq6dNx6h8/TL3Am8HQfEnUUR9J+KuUwHs6ke6fM0D9gELOO9ufTD7PO5UwHB5TdfeD/2OHNN1R+1tf5UNG+p4dTBo/0AooyLqEv8uWD8x1tINXHZZf7DfkDSmdKbF/w3rzxi8Guf8AimZ1R/a3wei98an+33TdSjzVh86lbIElv8f9xvzVZa73Yqu1vrLLNgJV29PL03d6Czl59NK2D9kOmRqd/any8Q9wXpPxVZAkKxHv/jufPh87c9T/QEzvABPKkP+iDgZhEB3Uc+zPFd13MmOZ+KLyXlPRD2gZ/AOgA8QHLNMf2F4Xz1i6QxQIj5+7f24s2cs4tAzC+qzgVuWoRB4LuOlwKpZpd+8XIxGw74ro8TL/6TVrPtgeUAfWBcICp464vXrzD/vPpF9D8dfHZR85FHh9mBlK4fBIAcwSzgHDyz14B47bPhB3p+fBABauRVO+vugtgAmj4Xgzq4dUmTtDOAPu0aVADOP8zvT03n1WCoQB4BY4FsqTpg3Ud+zZGQgx4JyAAgBqRbnhSgZwBGeTPCg6CTz2ABwPitqX1SfCy/KRQ8knIudl8OzorMZ+b+YREC0cHK+D2m6D8KE0Avn3c8+P410r5ym2nPuNoAbAQcv1x9Nhqvz17h2YwsvtD9+E8T1bu/N3Q9qv/5zwHwcRG3bdV8hOFnxf5SsF8BHsBPWZtn8f7wtZ4+sv2JPB/+BQT8idPTCB8Xf0/aP5F4y5aPi+Ur8orMl8S3aHt7AeNsP2wuH7D56qdCDb6hMGBf5iDcZleOoFv4WjK/bAF1M6oBIIHNzxLazJW3B8X+UTOAXz4V34f/nH6gJBXRHK5N+R0sPHoHkApPN34tbeBS0QLe/tyNRsHrPMTN4jfBy8eiy7L3LwBag78/Cc7VLJ9DvpnHSZBcAB3bJHh8eyDI0M4f/zxpy48PTva6YAKAVlnzfVi+1aC5Bn+XPU+dga4e4PB+4QNLNXPNBDrPzOfMc5r0gfCzbu1Yzco8h8a5zZwPfO4Bapf9P8vDgIuLerbmYrbww2MAj7u6ngFw9sIizICH5jxvWgdY+cn/3Vk7ciDj83JecGZIzkGbAczMXYDk5M8/FOVReD4/C88PZJlr2/e1acblR/S/XwSv0eti5vlDul/b7H8maoLuZabjlx/nQv7+DQXBOxiN3i++TjnAsG9z58whKDow0v8yT1izpx9H5g/gDHj7eujrH1Lc4OXXH8n1gMrPc3Q+Y+yv0kkzBIISMfv5L6UXyAz4+p0XvGn/93HgwwpZER8Q/MMKex2yZviB7YCQD/gHRXTW95shv6lTPqbHWR2gfvv8Y8fvLyDyndnzb7H/Nn6A7QAtPzRzSwUDtAAMwfdnXoNr/w2DyRvFJnZAGwxIoiGFkg5K0S7heyESoA4VYOSKIF0CoX1q6XkrElk5Lr4K3ABFcRKnQhdxA5JCcGQF/Pb+5YkXn+dOMpmlnEWcbQkS4rvLYMl/U++pzmy7r3PQbIY3LX9/cQkM7NxjzWH9fG1heulCGOkOrQVbCDXs+/Z8TlrVIXx+7RZQerI6+bpReMrpkFG8bK8qd03UXLDF2PbD7aVkIZWHep0WQ1mXGCbJbuLkaNWVPWpbvpiqHs9oCJ+E6SofwA4u44jxZvUpvW3Csx6OS06sj4hISOmkwIMoEcbZ2B5SVHMHVzgnWi94xsidtQKCPRpOwuNNuGgn08Iw3ZYwvufJPb8/INdI8BuxEIJMKGRMC5HmfIevNw3eE/TgFS7eLCs86l3/cpQOErRzzrwaGdU+tkEO2BdPXfojorNeh+6VxM4MGct3HGcGDo9xKy9cD7mYTxps3twqcxN+LJcHdsyFq61l407pjIzVkI5Zi9CZmCwvSca7M7HmEg1r3L2uMbhzXIqU7tcWCovLbXJpKIShrUAPLW/tOJK37LPbHrztJO1x7bLtUTIXCflSdJyVeJxhVIoyFRdFpRpP5aAycsA8mV8Om0zZ7PgglhkKsmEeyjYb+LDpjLqI9ajYBuogHhlnmztbU/QiflevjCDd6YkkXrckI7QZIaNxA0nWaip93ClYPg83nCCmrTL1J+m2VVZ8ZusxEkFdv5GqlDTd9LiNGryVuN3gQOPOVlZCxDi7rYZOHi/jEcXjq4rG7CK7681eOGt2GWG0wRpsWno4JnOJNqiJzXRxjdl2th+x6nxaeQ62h9zM1Ste6bfmUjnZGg7fbodEyM8DEgrnlaXhOX0AvmSDsYRshi0PgoMK9YFXUMKHetOB6PMpUTGlXxW9y6tssCEHku/se2mx8LU2Bu5yIm4+IWzYI7m+XFJ9FCHHHeH4YFuXTXbyO95gKnNbOshYOrgRSY65uW81y+1uxihqnq16nCnol6s1tWlSn/itclfXFsydL7dCwkQ9XZ8yMds4R3Hrh9jmPnC7PgmEvbNPpbzHJJnaHU45vVpJE2Xmoiglp6rhTsxeoZY9Bqf9YDbTZeWEu1AzydYTLELhwnbwtXWViBXM3c70Vj6q4Qndgv87GLrdliKMSZF+c+5hdYW2GrXH0YPUrsVDz9x6X7xxvs3u/JWAs4ipqMvMno69Mi2hu4et5U13rFVOwFYKCUW+f8lOytDsVv59O12gY+5cRekgBkFB2owvQOjG5g+peDY3BpLzwHNrkyR2RoysaY+ZrlJLFkVUuVGAbB3vIF3Xrj0SHnqERsE9Tj1G+IlVngrewGR4cByzuhmCdcZo60Z5W7Gi9esyqOOYNIi4uqVcMqiwIiShSQTxcqcOISkfkRay86Qaz2UWkmjqTtdLvkHqFRFKpwYlpnDSrCG4hHrBerHVeLJnOF4fydV4wNzD7VAJxmbsJYotTpwwadIS4vcZvY0vx5Gm6rM2yatwX6r8RVOP5digqyY7hqXt5BmZipeCWo0Ywo227stQzaTL5UQbp8iQaqxPyWGZczck2dk1ypx2uMiMtiWdOq42aHtzUPl1qthQglOTgff5VHHLXYRKJ1VBqQJtrXgazqG/m5A+SgKAcRHpTBtvTeZ0dDQZmeW6KfKM+ORGsbPfjZ2J9yv5crAqTsJs67BD9pQp4LUgYBWztS9XP3Pw1eVuw0cB8sw421x1DoOvxB0XVLyibJJ1EcePB7JjoM7zEpMMtWN9Ei6blmDI+yU9DNA9EZrlZDUEfgq0AE9EHaOGuwKaxKO76WOSlc95jO/CRPVocsKv9b12FINnCM1dMsehxEQMaGAdjeV55WyihpDV3T2MNxf1MApXB94gPU3bzOoocLYgcQ6vxreRcJc0RePG6JzkztFOIbvknexaTrtC0+1LqRhCv/JymYiH2l2m/rBVR91RTxzD8ONZDQi/5w4luuwSOiKR9KKR563HDQmNd2clIytyVe69AVnHAyu1DIS0IrwjWlNrDWzN+J7D7LxCdLqLGEiI7JwoJ3QtafQLdEl4rOqojLkN1/zyVCIlot3pa37T3ZNS0kZcEJVOTRiNhNueSQrzvHfdPo5wfm+hE07KSS1ihHxNRdh0Gc2/nQtZNyiKGk+80SjYmhh5o19LBEx3/JrtWu7GKYZhycSOQlfs9bbLV1eM9g7nYcKgIJzOdH+nC2nHu5kau4GoMMk4bZGpTjDFNSqEWQrOjtjG5flE9lR8FvbcDnJyhm0RIud3SluLBzPvEalYtlKiEsXobw1aKDthZcteeNwLfH9HdCmypxsaVS1kdNhIIesKljQ1DUGhEcIlFUZiF+2jDav61hm4gtkR+7WruW7peSOlKOdsHB0mOZ25w0TVELUPy426vGobW0/PWh3fdJV1Awny/aU0MEh66MS6gqN4F7UKYrI4Jl3b/nIXk6urq3JDsquuGlIWMrc8uYpt2jdP1YHMODIZAhVNN47HH7kzSRnCzinbqoo6UVelNtsYG6areiWNjbHuDh3c0g284SvTLNb2sFInbKN4F9kbg701ChMocXvSUPlGYhBMu1RKzp6Hc0eIbFRJgzemxiQNrLLerc/djWgNA2qQ/KoWISZVF4WTEkg4CqUAekRy42jdaG7kbeO5y0JLzgzF0cermRwskVGT87oVETJE0wsicSujEFPHik0x41yfUS4My6OTxRn5La/ZsViy7dYgOQEuQctC787XC0eI/GrSmss9a80alyOfK4ILPiZjWqm6ouNXk42tQ3Zaw1C04dPqUKFjguSXslHU6bJ0G1c7DXWCRNezAGsDTPPHYc1MnN1qQ37aarSk5Jck11LJp++GseuIXJqOZiMEO3xVu/U1MuXblj3sQoFe+yRbWMoOQvarEXAL4AT1C75y5J2MNdZZ5GOLP19J/axcsdADEa7mk37e6O2RbVg6HTeHQrVKBDEzAc8zMWi5eJeul7fYKbd5DnmHnOyJy3YstzFKyJx0ivI1uaI4UZYHS7vXxy1cj/fd6cBE+cXA6wJNj3smXdvMtBX2vSrTUrxvecdnMWiiCmMbRc5KR7ALAl87QyG2x00ScneJ8MgWPrtKl+4PSt4I4yXJVs5prHfIBqOqll3avsehjB/DMN3nkWtk0eDHUGePWZzvoWvrYyk1nfeirahZIrhJJGsMesAT2z2dU7ZrLByblKKTeW6CU15QTqIFpN9szkkzbm7q4HpmRnHC3mBgtJ1uyu00rtv70eeoCiIPlZ5ZrjNpcgpi5cZQWgxmlQz8Tv01i+VloiDRVj3fUqfHU8Epa3xQLas/9igTbjqWKbTdsu6yw4oN4m4LH5JJsXXVsDGdLrZ0e6jUsVr7h2WiWCGIY4i6ozWxc8WgupxAgpiwHlVlUKM0FoJWb1pJwfXQtvvAwCT9gHW9UPhJuMfKXCHb0lA5k88gq0ut8hDsrmOLqQzFuGBa88+bwTicbv32FqTUycVPxllc4qGOF/R48sK9Wtmbes/zCIhbogqWpunBoO+7j84Edbm0nLSwP3flKpb7gOjtvehMh/FyVCVQwW6YFW5Qp7xZcLrxJ/Na5ut1YiqedyPvA+JeITZPD4JfdVV9y6Is5gjWRLZ2XlMJ3iSxsM0ZD71oqdFy+6A0ojN9a1VcIASNpfiQhMuisxW2bNBNu1sFeZOU1yWFpRGkrBsxLvcqZKEnp9tpomE2kIs7EGa1/SoQ92Ny1XhMK0+Sm7u2qAM/onHipNZufRcvgYnQXUdpfjMeYCtKsoyRM3dD+GtjORiO4rCiuUU7nm1KsibO/S2wWY+8TIVb18IBMbirvYpAN7eysdo/6jZJHaUTDdkxRld4ihCo3tPZzktyR6N0fswzidOSA23Kw2VT2lSNJvFFuKXocPGWu9MFoVXBT/xkrZ5tVToP2S4biGxVgNmUI1tlswTte7JWIvMM7fYngmdZvcVkuXUFeV3Y2DaODhmGY0Tld163ru+yP6SRNXVbIsUjlopHcpKQ8UbqtH4z0U10XUNn46wtVQMD05KKZj5Ap9LS0QiuY7c5noQKRlWNv5+56GxMU21x+J7e3PVdOvBXZ8faBeVBYww6emF3zDQ7og/c2Ph1DIp3GuzSm3WgSPuOhIe737E7z7jtyNre5ZaB60xwiB0F1zfxtccvIceTxV0VDTvcT6xXllQBi1cwHHjqWeqI3VS5a1YGHSNEJ/CV0y5Uf0mGfDT2BqTThhar2NIFaN/GsF2ufSICzZWpMyhcX61EsHW8HcYTliK1TjSqa59R2kzqtZo505aWAI60WzGFEuuStE2XEt01vGHehSBFVVla9J4u6VPMTisEuWXd5q7wYT7ZhbBj9JYm5VOSIaQmSg4hBEe/VLaK2Tj0lLJaaR9VXjohcKnJ8TITTp1l3aQrFXPNWtMrI0Yhc48zKye2i5ga95NwgYHhC7p11RYMlyxVFzQitEoJ0gkkoXWR+uZa3Z14LTH9uL8jO1Yk6uyKxNbdj0MnXtXHWzXhAj6ERDq4SOxz9Dm56GOpT/kphdetSUM4ooHqu7n716qCkpzQ5APGeLcqOxK5uw9vq2iXyOFUtUfcO0VoRx4NFx0CgmJ4eIujm/7G0NMKqoP8cMqCG8dDqFUcpQi6i3hzXw6ITbpyMDV6bYV+YPTAACupLEzFqKGCj3I/JYLGNwPgkcMYVLlFxJNa32r0ItdFXfOSgvjLSIr1FWahYj+Fp3BAnPvptOVYepDvnbaBs/tS0rYrPpZvfuNIB89V2BNPiF3OjixhByV21aq2gh0Hyq6eAzPUrjnY2XJHovUR3ahIyMWBRta1TrvHrr/oQtSHVx8xye0VdaETFwhbF4NhaDnBg7Ua0oLfxTcchlmYalPJVJU6oOoVSYXc8nJh7wOW1p0gUa5slc0tEfbsdCXKFCMgrnPUy153bGmaeu+wJUyJ27NWj3igVDmKx4+DBtdHtTuZ7S7J7IZEDWEcL6GxQvbFJYkxl5dp5SbdLBDFyTU5Xo+OGxx3BzxEuCq43R2MR5SuBvlMZQnHXmES1S1Lz3I2CvVBRbz4FvorZagm0Pc57iSszeY+BGaiwzdCdiiipPAEjc8WY93xc6sQq8rzapXKsnDAaUdeYWA2Q43eVvRDpIZiBPBe7rYNKfmYxo6caa4aui9vVYkk46WBGt9ZLe9SZN3iqjAEpmKcqb3x+xZ2YgMu42zPiD07GSSZTOyesrIx3ifctU34c6almjDsNuMFLkEnfz6uD+srct1xBGIjtZuk4dJSrv6l29yU01VWUs8Bk2G7sRS+wu0dZcsQT/hpo8Vk0DM2AsvNXgzOmlNqLkqpqIHQpxEnyPq2pfYUm3DuHoCknYPJ+GLpCjF04bAcj2LI9ARfC80Ik8Y6r4rzpDIohFxT+cbc1wYmGjd7l3VIN7BisMkKKersyCG03myzvZkR91XTslS0z5fnKaPxVT64BMG06dCZsLzzO/yQMDJBRpOSoUXvtr1qZMHmSlGtPEjWlGbTaDcnqnOWQ1Uyss4UvuBI+V0ug5JfqpKRdyonedgUZInIpHujnPYbZKWLCJSbp1xt1l6dGMrSz/IBZdZNFKIqrAubwlCP7rVXZLlJoJuEpOUJqgX1tuxBnVs7emAhJDPczaIVqHAKqorWoCkIgsuuCa6XGL1BJ9ISu7OE3jQ+v7cJufKogm11FQuOh3uj1UwRh57oWsuipZFzT4USAA/iYC25VXrqi+hcL8Ur0vZ52qD9xYRjiVKrZu1QjNLS/HIi0G2+JOoV60jykpgmqkxkF+3kMQlNPpzkNsyZwNbw9H5CDjtqZDdyqrOuyRIqcXER1/OQaMdbhJ2G/rC6nO8kQSnr9pLpzh7nGz2ptfsxGBlvT1bC9sZSijfGF4w4jW18Y6S93BxSjzi59CTcL/QeifQpAaGmi1yNygxWSS1SNBUY5GpPMuWLkIWg/aW4FM6Te3mjcRJaxbueMfb+Dg+2a+V8ozZN3XAnWrVJb3+BrW2qdrl4jEHXckKLA3zcI+7FgExDxs6caNKtn19RlS4EBckhY8vfp81ocavp7ratcPTQrK1MxD2SlnwahDbj3Y1zD5WJ52jZHPL6vFuNl2kfKs11g4aEDs4v1x1kIPccKhkHSXUPr0Ip0s+ghWnyDS2FAuy3PEnikaOhBhgjacHjSxZrGaTYBJq1KQk1ECfjxoJSfHMMHtMz3KaS4drxLS6xtUPDN5Q5lcv2SAt7ScAn+Lyx71eDRChcIugmWrvwlGV2XQkbRMsTLudpjkxBU1LujGvB9PA9hCyq0G9r+hhsfDAacpnSmaN3CehulUGlF/srGD2WuHjDEaE87Q3YGFFFXga4f7aX0Oks966cgy5qdQubahlfvPuBZcxkJLhVqxdws2+RLSSBhMcj5DaQyEl0aFQJeDjyNfMgIsgmPubBlQClLXB0ifZTHZXLfnNFkgu/ccnkqGz9C86vRfJ4aqG1t41N7GhBK7Xt0LyYiuVuZ1MsZWanmAA1Y783fbcNFAY6+1LUxnW1p3RVCc0tNxFdSY4B5KWEu1tK0tLMQqcY1iGxEhkFxqkWRoACBLT0dqiIeYh7jxR/oJgdcxsdqXPBUMQbirc8L2vPbnMY9xkfhSdsjJuiOZ1WdS5b3vIW6QFTnM3Jq/2hdsjJrmIruYP+tLbkAVUSuvRgUjDAODUOpLjMdDvs3fvgX0LSMcN4uwdNP+IcY0VhzrU1NgiAqbXKUsuzqewID/X3dU8IojzUrWk2CY+REYr7R7XlV4p5K0rsxG2g81pzzmFhFcKeuh3o4L6SVrq7lcIVCTcG0bQbJtyfTp10bMmbgcvC1VOgLLr6AQkGM/oQHoetGGAZwvuDqFzL7W0fl3fQt9sDFYZWdKYYLwpk7K7tMWltuTovnEDjdA2hrR9q6dhn1yWy2d2DSsTd6dpb1BpOrj2f2Ox6vf7Hy/uXbzfpXv4LT7DN94v+225NPe8wfXn25HE/MnD8jw9eH/8rQv76/qX2EiDi8xZdk3XR262tv9yg+/D3bzrO9Mbng2NfboI/77K3TjQ/gv2SFH7XtPX4uSmzx9Mp4ITbNfNjms38JK8H3r+/6foQYX73n8+WBPXntvz8vFM5359Livmxk8BPvn2N3m5ivn/x356b+owS+OegrmbV3x5nmD30iryuXv74P7TMzFtJLwAA -->
