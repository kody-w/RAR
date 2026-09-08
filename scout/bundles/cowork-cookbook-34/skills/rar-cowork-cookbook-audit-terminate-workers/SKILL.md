---
name: "rar-cowork-cookbook-audit-terminate-workers"
description: "Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_terminate_workers", "rar_sha256": "250ddd93f20f28701e398da064ddb4fcd01e308ff8342ff4448323d81c2b0040", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_terminate_workers`. The original RAPP
agent is preserved byte-for-byte in `audit_terminate_workers_agent.py` and in the RCI capsule.

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

Terminate workers Completeness Audit — Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-terminate-workers
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
      "description": "Date range used to judge stale dates; adjust for demo data era (USMF is mostly FY2017).",
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
      "description": "Excel workbook name, e.g. audit-terminate-workers-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 250ddd93f20f2870…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_terminate_workers_agent.py` first:

```bash
python3 audit_terminate_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_terminate_workers_agent.py   # or on stdin
python3 audit_terminate_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Terminate workers Completeness Audit — Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-terminate-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_terminate_workers',
    "version": '3.0.3',
    "display_name": 'Terminate workers Completeness Audit',
    "description": 'Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-terminate-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-terminate-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4aedf68bd8c0b3b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/terminate-workers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-terminate-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data era (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-terminate-workers-2026-05-24.xlsx, saved to Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit terminate workers records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to terminate workers. Output an Excel workbook 'audit-terminate-workers-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no terminate workers data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads terminate workers records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts.', 'example_request': 'Audit terminate workers records in USMF for completeness and export audit-terminate-workers-2026-05-24.xlsx', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data era (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-terminate-workers-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of terminate workers records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTerminateWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTerminateWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data era (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-terminate-workers-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AuditTerminateWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
