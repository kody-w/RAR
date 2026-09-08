---
name: "rar-cowork-cookbook-bulk-update-model-service-capacity"
description: "Applies a bulk field update to Dynamics 365 model service capacity records from a caller-supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_model_service_capacity", "rar_sha256": "f6a4692f47199e26e3f5d2e1594bcc675b27153d7312ff629a2e750e7e3cde30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
