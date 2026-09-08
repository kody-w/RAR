---
name: "rar-cowork-cookbook-audit-configure-and-administer-workflows"
description: "Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_administer_workflows", "rar_sha256": "d7237e42685c003ea711442cf7f22140160715d3a6db98a4608425e44e623b0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_administer_workflows`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_administer_workflows_agent.py` and in the RCI capsule.

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

Configure and administer workflows Completeness Audit — Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-configure-and-administer-workflows-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 d7237e42685c003e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_administer_workflows_agent.py` first:

```bash
python3 audit_configure_and_administer_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_administer_workflows_agent.py   # or on stdin
python3 audit_configure_and_administer_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and administer workflows Completeness Audit — Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_administer_workflows',
    "version": '3.0.2',
    "display_name": 'Configure and administer workflows Completeness Audit',
    "description": 'Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary.',
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
        "upstream_slug": 'audit-configure-and-administer-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-administer-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab82e6f6afad86ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-administer-workflows'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-administer-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-configure-and-administer-workflows-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and administer workflows records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and administer workflows. Output an Excel workbook 'audit-configure-and-administer-workflows-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and administer workflows data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and administer workflows records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary.', 'example_request': 'Audit the configure and administer workflows records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-administer-workflows-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy audit of configure-and-administer-workflows records in Dynamics 365 F&SCM via the Cowork ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndAdministerWorkflows(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndAdministerWorkflows'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-administer-workflows-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndAdministerWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
