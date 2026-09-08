---
name: "rar-cowork-cookbook-bulk-update-develop-maintenance-strategy"
description: "Applies a bulk field update to develop maintenance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_maintenance_strategy", "rar_sha256": "96adf7397d952b2aa960930e10f5f7a8fbad9e95facf67ba093b9217af0b9aae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
