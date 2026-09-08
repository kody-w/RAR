---
name: "rar-cowork-cookbook-bulk-update-measure-adoption-and-success"
description: "Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_adoption_and_success", "rar_sha256": "35daca2cb44b6603d1a2359e3a5a0940cd338c63068e9179e921ee292f349bc5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Bulk Field Update — Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of measure adoption and success record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 35daca2cb44b6603…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_adoption_and_success_agent.py` first:

```bash
python3 bulk_update_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_adoption_and_success_agent.py   # or on stdin
python3 bulk_update_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Bulk Field Update — Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_adoption_and_success',
    "version": '3.0.3',
    "display_name": 'Measure adoption and success Bulk Field Update',
    "description": 'Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af',
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
        "upstream_slug": 'bulk-update-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c29d68b57be02966',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of measure adoption and success record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when measure adoption and success records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to measure adoption and success records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to measure adoption and success records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook af', 'example_request': 'Bulk update these measure adoption records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of measure adoption and success record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of measure adoption and success record IDs and new field values to update in bulk, and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMeasureAdoptionAndSuccess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureAdoptionAndSuccess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of measure adoption and success record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
