---
name: "rar-cowork-cookbook-bulk-update-use-similar-cases-to-find-a-solution"
description: "Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution", "rar_sha256": "4b99679f90887ba9a3a9ac06c265c68f1d210e353d8c3608da6651b27407ef14", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_use_similar_cases_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use similar cases to find a solution Bulk Field Update — Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 4b99679f90887ba9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_use_similar_cases_to_find_a_solution_agent.py` first:

```bash
python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py   # or on stdin
python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use similar cases to find a solution Bulk Field Update — Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution',
    "version": '3.0.3',
    "display_name": 'Use similar cases to find a solution Bulk Field Update',
    "description": "Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,",
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
        "upstream_slug": 'bulk-update-use-similar-cases-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88aaffafa4634fc4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-similar-cases-to-find-a-solution'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-use-similar-cases-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when use similar cases to find a solution records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to use similar cases to find a solution records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,", 'example_request': 'Bulk update these case records in USMF sandbox to the new value — show me a dry-run preview first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many D365 records at once and want a before/after preview and approval gate before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateUseSimilarCasesToFindASolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUseSimilarCasesToFindASolution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateUseSimilarCasesToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
