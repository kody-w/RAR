---
name: "rar-cowork-cookbook-bulk-update-monitor-employee-satisfaction"
description: "Applies a bulk field update to monitor-employee-satisfaction records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_employee_satisfaction", "rar_sha256": "57eae8d92bd5f2f90041d8a7fc64f17fde1892d27bb4b9875a4f7c45e18a91e4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
