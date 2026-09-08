---
name: "rar-cowork-cookbook-demo-data-review-audit-logs"
description: "Generates 25 realistic demo review audit log records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_audit_logs", "rar_sha256": "483c1a976f9381cb36644d4384e7cffa4ba8ecdec89fec5196be7b2c2e6fd4e2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
