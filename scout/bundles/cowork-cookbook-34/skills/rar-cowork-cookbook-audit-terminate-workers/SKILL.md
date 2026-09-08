---
name: "rar-cowork-cookbook-audit-terminate-workers"
description: "Audits Dynamics 365 F&SCM terminate-workers records in a given legal entity for completeness and policy compliance, returning a read-only Excel workbook with a sheet per finding category and a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_terminate_workers", "rar_sha256": "250ddd93f20f28701e398da064ddb4fcd01e308ff8342ff4448323d81c2b0040", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
