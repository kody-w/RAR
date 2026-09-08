---
name: "rar-cowork-cookbook-audit-configure-and-administer-workflows"
description: "Audits Dynamics 365 F&SCM workflow configuration records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_administer_workflows", "rar_sha256": "d7237e42685c003ea711442cf7f22140160715d3a6db98a4608425e44e623b0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
