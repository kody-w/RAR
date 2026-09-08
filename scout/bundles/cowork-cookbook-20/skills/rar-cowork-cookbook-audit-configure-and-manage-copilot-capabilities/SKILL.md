---
name: "rar-cowork-cookbook-audit-configure-and-manage-copilot-capabilities"
description: "Audits configure and manage copilot capabilities records in Dynamics 365 F&SCM (legal entity USMF) for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a S"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_copilot_capabilities", "rar_sha256": "12cab29628f8337326749bd247398d359f3f326e3a569a9e770ace0fd89c6c07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
