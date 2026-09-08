---
name: "rar-cowork-cookbook-bulk-update-use-similar-cases-to-find-a-solution"
description: "Runs a bulk field update on 'similar cases' records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook, pausing for approval,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution", "rar_sha256": "4b99679f90887ba9a3a9ac06c265c68f1d210e353d8c3608da6651b27407ef14", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
