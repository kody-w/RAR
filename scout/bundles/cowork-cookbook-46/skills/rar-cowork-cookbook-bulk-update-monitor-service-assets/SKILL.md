---
name: "rar-cowork-cookbook-bulk-update-monitor-service-assets"
description: "Applies a bulk field update to monitor service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_service_assets", "rar_sha256": "06a17dd429f34b763f8b7b005ea5aec151183e282c0c6ca0968e09a660e03b72", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
