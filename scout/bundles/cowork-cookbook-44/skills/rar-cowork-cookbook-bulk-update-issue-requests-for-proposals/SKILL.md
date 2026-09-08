---
name: "rar-cowork-cookbook-bulk-update-issue-requests-for-proposals"
description: "Applies a bulk field update to Dynamics 365 issue requests for proposals records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_requests_for_proposals", "rar_sha256": "d79b1c79b47e1127e6b1c914fb251942c93fe404df1bedef28fafaf54e6cc96b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
