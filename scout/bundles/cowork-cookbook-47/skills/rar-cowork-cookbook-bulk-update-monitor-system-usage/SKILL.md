---
name: "rar-cowork-cookbook-bulk-update-monitor-system-usage"
description: "Applies a bulk field update to monitor system usage records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_system_usage", "rar_sha256": "a29ec52776dffef6d6a3b8168cc520d74f5cb9c582d5d65ab7106ec97b7469d8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
