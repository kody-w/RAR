---
name: "rar-cowork-cookbook-bulk-update-develop-maintenance-strategy"
description: "Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_maintenance_strategy", "rar_sha256": "96adf7397d952b2aa960930e10f5f7a8fbad9e95facf67ba093b9217af0b9aae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_maintenance_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_maintenance_strategy_agent.py` and in the RCI capsule.

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

Develop maintenance strategy Bulk Field Update — Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
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
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity, default USMF; sandbox environment only.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of develop maintenance strategy record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_maintenance_strategy_agent.py` and embedded as the fenced Python below (sha256 96adf7397d952b2a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_maintenance_strategy_agent.py` first:

```bash
python3 bulk_update_develop_maintenance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_maintenance_strategy_agent.py   # or on stdin
python3 bulk_update_develop_maintenance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop maintenance strategy Bulk Field Update — Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_maintenance_strategy',
    "version": '3.0.3',
    "display_name": 'Develop maintenance strategy Bulk Field Update',
    "description": 'Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-maintenance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-maintenance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '04337cdde1fe9619',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/develop-maintenance-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-develop-maintenance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of develop maintenance strategy record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop maintenance strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop maintenance strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a', 'example_request': 'Bulk update these develop maintenance strategy records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of develop maintenance strategy record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many develop maintenance strategy records at once and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopMaintenanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMaintenanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop maintenance strategy record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopMaintenanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
