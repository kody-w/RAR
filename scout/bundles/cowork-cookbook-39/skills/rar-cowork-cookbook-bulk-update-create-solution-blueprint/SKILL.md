---
name: "rar-cowork-cookbook-bulk-update-create-solution-blueprint"
description: "Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_solution_blueprint", "rar_sha256": "fe793c35bd95f2028fc155740838974643875b4a8e4e442e5495ef4d342147cc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_create_solution_blueprint_agent.py` and in the RCI capsule.

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

Create solution blueprint Bulk Field Update — Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (defaults to USMF).",
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
      "description": "List of solution blueprint record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 fe793c35bd95f202…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_solution_blueprint_agent.py` first:

```bash
python3 bulk_update_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_solution_blueprint_agent.py   # or on stdin
python3 bulk_update_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Bulk Field Update — Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_solution_blueprint',
    "version": '3.0.3',
    "display_name": 'Create solution blueprint Bulk Field Update',
    "description": 'Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation',
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
        "upstream_slug": 'bulk-update-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdc050c5a034c7ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (defaults to USMF).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of solution blueprint record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when create solution blueprint records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to create solution blueprint records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation', 'example_request': 'Bulk update these solution blueprint record IDs in USMF sandbox with the new owner value — show me the dry-run first.', 'inputs': [{'description': 'List of solution blueprint record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (defaults to USMF).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of solution blueprint record IDs in a D365 sandbox, with a reviewable dry-run before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCreateSolutionBlueprint(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateSolutionBlueprint'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (defaults to USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of solution blueprint record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
