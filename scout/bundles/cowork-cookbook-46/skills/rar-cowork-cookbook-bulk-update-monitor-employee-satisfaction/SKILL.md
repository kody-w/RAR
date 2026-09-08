---
name: "rar-cowork-cookbook-bulk-update-monitor-employee-satisfaction"
description: "Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_employee_satisfaction", "rar_sha256": "57eae8d92bd5f2f90041d8a7fc64f17fde1892d27bb4b9875a4f7c45e18a91e4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_employee_satisfaction`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_employee_satisfaction_agent.py` and in the RCI capsule.

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

Monitor employee satisfaction Bulk Field Update — Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction
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
    "approval": {
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF, sandbox first).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    "record_ids": {
      "description": "List of monitor employee satisfaction record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 57eae8d92bd5f2f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_employee_satisfaction_agent.py` first:

```bash
python3 bulk_update_monitor_employee_satisfaction_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_employee_satisfaction_agent.py   # or on stdin
python3 bulk_update_monitor_employee_satisfaction_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor employee satisfaction Bulk Field Update — Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_employee_satisfaction',
    "version": '3.0.3',
    "display_name": 'Monitor employee satisfaction Bulk Field Update',
    "description": 'Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-employee-satisfaction',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-employee-satisfaction',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e9363764c21b94fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-employee-satisfaction'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-monitor-employee-satisfaction', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of monitor employee satisfaction record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor employee satisfaction records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor employee satisfaction records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c', 'example_request': 'Bulk update these employee satisfaction record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of monitor employee satisfaction record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many monitor employee satisfaction records at once in a D365 sandbox, with a reviewable preview before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorEmployeeSatisfaction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorEmployeeSatisfaction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of monitor employee satisfaction record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorEmployeeSatisfaction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
