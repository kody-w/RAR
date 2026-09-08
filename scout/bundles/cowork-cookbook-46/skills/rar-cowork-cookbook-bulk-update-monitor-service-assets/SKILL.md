---
name: "rar-cowork-cookbook-bulk-update-monitor-service-assets"
description: "Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_service_assets", "rar_sha256": "06a17dd429f34b763f8b7b005ea5aec151183e282c0c6ca0968e09a660e03b72", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Bulk Field Update — Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
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
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of monitor service assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 06a17dd429f34b76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_service_assets_agent.py` first:

```bash
python3 bulk_update_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_service_assets_agent.py   # or on stdin
python3 bulk_update_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Bulk Field Update — Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_service_assets',
    "version": '3.0.3',
    "display_name": 'Monitor service assets Bulk Field Update',
    "description": 'Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b985d73d7d1e131',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of monitor service assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor service assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor service assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for', 'example_request': 'Bulk update these monitor service asset IDs in USMF sandbox with the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of monitor service assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many monitor service assets records at once and want a before/after preview and approval step before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of monitor service assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
