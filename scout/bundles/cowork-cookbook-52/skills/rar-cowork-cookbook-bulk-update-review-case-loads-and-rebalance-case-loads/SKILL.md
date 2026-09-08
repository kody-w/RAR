---
name: "rar-cowork-cookbook-bulk-update-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk field update to review/rebalance case load records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied ID list, producing a dry-run preview workbook for approval before committing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads", "rar_sha256": "0cbc9b719276e36f50d7c1a3899891f141dfb93dec53fa197ca7ea52d7737763", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
