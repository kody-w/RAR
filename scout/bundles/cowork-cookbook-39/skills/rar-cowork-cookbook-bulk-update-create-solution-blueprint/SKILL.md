---
name: "rar-cowork-cookbook-bulk-update-create-solution-blueprint"
description: "Applies a bulk field update to solution blueprint records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_solution_blueprint", "rar_sha256": "fe793c35bd95f2028fc155740838974643875b4a8e4e442e5495ef4d342147cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
