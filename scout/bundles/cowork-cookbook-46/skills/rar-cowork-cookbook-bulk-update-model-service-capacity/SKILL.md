---
name: "rar-cowork-cookbook-bulk-update-model-service-capacity"
description: "Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_model_service_capacity", "rar_sha256": "f6a4692f47199e26e3f5d2e1594bcc675b27153d7312ff629a2e750e7e3cde30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_model_service_capacity`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_model_service_capacity_agent.py` and in the RCI capsule.

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

Model service capacity Bulk Field Update — Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-model-service-capacity
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
    "environment": {
      "description": "Target environment; sandbox first, since this modifies data.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF).",
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
      "description": "List of model service capacity record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 f6a4692f47199e26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_model_service_capacity_agent.py` first:

```bash
python3 bulk_update_model_service_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_model_service_capacity_agent.py   # or on stdin
python3 bulk_update_model_service_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Model service capacity Bulk Field Update — Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-model-service-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_model_service_capacity',
    "version": '3.0.3',
    "display_name": 'Model service capacity Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
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
        "upstream_slug": 'bulk-update-model-service-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-model-service-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b00e5e8df20fad3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/model-service-capacity'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-model-service-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first, since this modifies data.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of model service capacity record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when model service capacity records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to model service capacity records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these model service capacity record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of model service capacity record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first, since this modifies data.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change field values on many model service capacity records at once in D365 F&SCM (sandbox), with a preview-then-approve step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateModelServiceCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateModelServiceCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first, since this modifies data.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of model service capacity record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateModelServiceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
