---
name: "rar-cowork-cookbook-bulk-update-develop-new-services"
description: "Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_new_services", "rar_sha256": "fb9e3787833ec800b1d82dd4989c839f05772e0c4c22891a156774bb93f3637b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_new_services`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_new_services_agent.py` and in the RCI capsule.

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

Develop new services Bulk Field Update — Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
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
      "description": "Target environment; sandbox first before any production run.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF).",
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
      "description": "List of develop new services record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 fb9e3787833ec800…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_new_services_agent.py` first:

```bash
python3 bulk_update_develop_new_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_new_services_agent.py   # or on stdin
python3 bulk_update_develop_new_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new services Bulk Field Update — Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_new_services',
    "version": '3.0.3',
    "display_name": 'Develop new services Bulk Field Update',
    "description": 'Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-new-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-new-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c06dd32a8f4a518c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/develop-new-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-develop-new-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before any production run.', 'legal_entity': 'D365 legal entity to run against (default USMF).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of develop new services record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop new services records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop new services records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work', 'example_request': 'Bulk update these develop new services record IDs in USMF sandbox with the new value - show me a dry-run first.', 'inputs': [{'description': 'List of develop new services record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before any production run.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a list of develop new services record IDs and new field values to update in bulk in a D365 sandbox, and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopNewServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopNewServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before any production run.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop new services record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopNewServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
