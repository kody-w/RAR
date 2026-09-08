---
name: "rar-cowork-cookbook-bulk-update-create-a-case-manually"
description: "Applies a bulk field update to case records in Dynamics 365 F&SCM via the Cowork D365 ERP plugin: produces a dry-run preview workbook of before/after changes, waits for approval, then commits and emits a confirmation wor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_a_case_manually", "rar_sha256": "d0e0886e8734e0991bb58f8dd869c795f7358b47b5bcf709098632a34373cf9c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
