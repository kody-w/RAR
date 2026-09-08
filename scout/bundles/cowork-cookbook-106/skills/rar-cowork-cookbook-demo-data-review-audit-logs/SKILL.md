---
name: "rar-cowork-cookbook-demo-data-review-audit-logs"
description: "Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_audit_logs", "rar_sha256": "483c1a976f9381cb36644d4384e7cffa4ba8ecdec89fec5196be7b2c2e6fd4e2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_audit_logs_agent.py` and in the RCI capsule.

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

Review audit logs Demo Data Generator — Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-audit-logs
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
    "legal_entity": {
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo review audit log records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-review-audit-logs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 483c1a976f9381cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_audit_logs_agent.py` first:

```bash
python3 demo_data_review_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_audit_logs_agent.py   # or on stdin
python3 demo_data_review_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review audit logs Demo Data Generator — Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_audit_logs',
    "version": '3.0.3',
    "display_name": 'Review audit logs Demo Data Generator',
    "description": "Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1169ff9b13bb53fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-audit-logs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-review-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo review audit log records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-review-audit-logs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic review audit logs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for review audit logs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-review-audit-logs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic review audit logs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo review audit log records in sandbox USMF, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo review audit log records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-review-audit-logs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training review audit log data in a sandbox D365 F&SCM tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReviewAuditLogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo review audit log records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-review-audit-logs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReviewAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
