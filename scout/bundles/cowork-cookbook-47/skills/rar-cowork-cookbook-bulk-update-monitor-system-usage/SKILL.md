---
name: "rar-cowork-cookbook-bulk-update-monitor-system-usage"
description: "Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_system_usage", "rar_sha256": "a29ec52776dffef6d6a3b8168cc520d74f5cb9c582d5d65ab7106ec97b7469d8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_system_usage`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_system_usage_agent.py` and in the RCI capsule.

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

Monitor system usage Bulk Field Update — Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field value(s) to apply to those records.",
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
      "description": "List of monitor system usage record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 a29ec52776dffef6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_system_usage_agent.py` first:

```bash
python3 bulk_update_monitor_system_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_system_usage_agent.py   # or on stdin
python3 bulk_update_monitor_system_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system usage Bulk Field Update — Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_system_usage',
    "version": '3.0.3',
    "display_name": 'Monitor system usage Bulk Field Update',
    "description": 'Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-system-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '642159d27057a3d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-usage'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-monitor-system-usage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field value(s) to apply to those records.', 'record_ids': 'List of monitor system usage record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor system usage records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor system usage records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo', 'example_request': 'Bulk update these monitor system usage record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of monitor system usage record IDs to update.', 'name': 'record_ids'}, {'description': 'The field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many monitor system usage records at once and want a before/after dry-run preview to approve before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorSystemUsage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorSystemUsage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of monitor system usage record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorSystemUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
