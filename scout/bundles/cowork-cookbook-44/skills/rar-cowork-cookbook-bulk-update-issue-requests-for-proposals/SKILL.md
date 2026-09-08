---
name: "rar-cowork-cookbook-bulk-update-issue-requests-for-proposals"
description: "Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_requests_for_proposals", "rar_sha256": "d79b1c79b47e1127e6b1c914fb251942c93fe404df1bedef28fafaf54e6cc96b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_issue_requests_for_proposals`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_issue_requests_for_proposals_agent.py` and in the RCI capsule.

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

Issue requests for proposals Bulk Field Update — Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (recipe uses USMF, sandbox first).",
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
      "description": "List of issue requests for proposals record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 d79b1c79b47e1127…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_requests_for_proposals_agent.py` first:

```bash
python3 bulk_update_issue_requests_for_proposals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_issue_requests_for_proposals_agent.py   # or on stdin
python3 bulk_update_issue_requests_for_proposals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for proposals Bulk Field Update — Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_issue_requests_for_proposals',
    "version": '3.0.3',
    "display_name": 'Issue requests for proposals Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-issue-requests-for-proposals',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5ce5757066c2d02',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-proposals'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-issue-requests-for-proposals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (recipe uses USMF, sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of issue requests for proposals record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when issue requests for proposals records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to issue requests for proposals records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these issue RFP records in USMF sandbox with the new values — show me the dry-run preview first.', 'inputs': [{'description': 'List of issue requests for proposals record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (recipe uses USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many issue-RFP records at once in a D365 sandbox and want a before/after preview plus a confirmation workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateIssueRequestsForProposals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIssueRequestsForProposals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (recipe uses USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of issue requests for proposals record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateIssueRequestsForProposals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
