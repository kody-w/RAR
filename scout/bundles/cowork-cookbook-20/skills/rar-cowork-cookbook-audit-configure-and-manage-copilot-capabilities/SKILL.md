---
name: "rar-cowork-cookbook-audit-configure-and-manage-copilot-capabilities"
description: "Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_copilot_capabilities", "rar_sha256": "12cab29628f8337326749bd247398d359f3f326e3a569a9e770ace0fd89c6c07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_copilot_capabilities`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_copilot_capabilities_agent.py` and in the RCI capsule.

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

Configure and manage copilot capabilities Completeness Audit — Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities
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
      "description": "Date range used for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Excel workbook name, e.g. audit-configure-and-manage-copilot-capabilities-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 12cab29628f83373…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_copilot_capabilities_agent.py` first:

```bash
python3 audit_configure_and_manage_copilot_capabilities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_copilot_capabilities_agent.py   # or on stdin
python3 audit_configure_and_manage_copilot_capabilities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage copilot capabilities Completeness Audit — Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_copilot_capabilities',
    "version": '3.0.2',
    "display_name": 'Configure and manage copilot capabilities Completeness Audit',
    "description": 'Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S',
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
        "upstream_slug": 'audit-configure-and-manage-copilot-capabilities',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f345730f5bc9a299',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-copilot-capabilities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-configure-and-manage-copilot-capabilities-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and manage copilot capabilities records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and manage copilot capabilities. Output an Excel workbook 'audit-configure-and-manage-copilot-capabilities-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and manage copilot capabilities data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and manage copilot capabilities records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S', 'example_request': 'Audit configure and manage copilot capabilities records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-configure-and-manage-copilot-capabilities-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need a read-only completeness and policy audit of configure and manage copilot capabilities records in D365 ERP, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndManageCopilotCapabilities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageCopilotCapabilities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-configure-and-manage-copilot-capabilities-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndManageCopilotCapabilities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
