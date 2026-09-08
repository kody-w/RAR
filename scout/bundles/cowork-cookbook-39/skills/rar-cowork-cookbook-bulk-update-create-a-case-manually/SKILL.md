---
name: "rar-cowork-cookbook-bulk-update-create-a-case-manually"
description: "Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_a_case_manually", "rar_sha256": "d0e0886e8734e0991bb58f8dd869c795f7358b47b5bcf709098632a34373cf9c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_create_a_case_manually`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_create_a_case_manually_agent.py` and in the RCI capsule.

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

Create a case manually Bulk Field Update — Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
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
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment first.",
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
      "description": "List of case record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 d0e0886e8734e099…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_a_case_manually_agent.py` first:

```bash
python3 bulk_update_create_a_case_manually_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_a_case_manually_agent.py   # or on stdin
python3 bulk_update_create_a_case_manually_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case manually Bulk Field Update — Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_a_case_manually',
    "version": '3.0.3',
    "display_name": 'Create a case manually Bulk Field Update',
    "description": 'Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-create-a-case-manually',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f9579e0f23acb99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-manually'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-create-a-case-manually', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of case record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when create a case manually records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to create a case manually records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor', 'example_request': 'Bulk update these case IDs in USMF sandbox to priority High — show me the dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'name': 'legal_entity'}, {'description': 'List of case record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many D365 case records from a supplied ID list, with a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCreateACaseManually(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateACaseManually'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of case record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCreateACaseManually().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
