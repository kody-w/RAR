---
name: "rar-cowork-cookbook-bulk-update-develop-training-materials"
description: "Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_training_materials", "rar_sha256": "027e5370d37b37a5610af9d1e98e487fbdf14c18461a2cdb1955d35803787826", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_training_materials`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_training_materials_agent.py` and in the RCI capsule.

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

Develop training materials Bulk Field Update — Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox first).",
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
      "description": "List of develop training materials record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 027e5370d37b37a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_training_materials_agent.py` first:

```bash
python3 bulk_update_develop_training_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_training_materials_agent.py   # or on stdin
python3 bulk_update_develop_training_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training materials Bulk Field Update — Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-training-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_training_materials',
    "version": '3.0.3',
    "display_name": 'Develop training materials Bulk Field Update',
    "description": 'Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf',
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
        "upstream_slug": 'bulk-update-develop-training-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-training-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b0210029a45f8d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-materials'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-develop-training-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of develop training materials record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop training materials records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop training materials records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop training materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a conf', 'example_request': 'Bulk update these training materials record IDs in USMF sandbox to owner J. Lee — show me the dry-run first.', 'inputs': [{'description': 'List of develop training materials record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of develop training materials record IDs and want a reviewable preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopTrainingMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopTrainingMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop training materials record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopTrainingMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
