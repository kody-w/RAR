---
name: "rar-cowork-cookbook-bulk-update-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads", "rar_sha256": "0cbc9b719276e36f50d7c1a3899891f141dfb93dec53fa197ca7ea52d7737763", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` and in the RCI capsule.

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

Review case loads and rebalance case loads Bulk Field Update — Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox).",
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
      "description": "List of case load record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 0cbc9b719276e36f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` first:

```bash
python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py   # or on stdin
python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review case loads and rebalance case loads Bulk Field Update — Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads',
    "version": '3.0.3',
    "display_name": 'Review case loads and rebalance case loads Bulk Field Update',
    "description": 'Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing.',
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
        "upstream_slug": 'bulk-update-review-case-loads-and-rebalance-case-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be99b02ebec1cf32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-case-loads-and-rebalance-case-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-review-case-loads-and-rebalance-case-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of case load record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when review case loads and rebalance case loads records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to review case loads and rebalance case loads records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing.', 'example_request': 'Bulk update these case load record IDs in USMF sandbox to the new owner — show me the dry-run preview first.', 'inputs': [{'description': 'List of case load record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields across many case load records at once and want a before/after preview and approval gate before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of case load record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
