---
name: "rar-cowork-cookbook-bulk-update-determine-business-process-flow"
description: "Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_determine_business_process_flow", "rar_sha256": "189188beeabcf9d841ea75f070169b4dd5390173f0fc86a9cf41cb77b6837f22", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_determine_business_process_flow_agent.py` and in the RCI capsule.

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

Determine business process flow Bulk Field Update — Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
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
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of business process flow record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 189188beeabcf9d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_determine_business_process_flow_agent.py` first:

```bash
python3 bulk_update_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_determine_business_process_flow_agent.py   # or on stdin
python3 bulk_update_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Bulk Field Update — Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_determine_business_process_flow',
    "version": '3.0.3',
    "display_name": 'Determine business process flow Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.',
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
        "upstream_slug": 'bulk-update-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76ff0e1e6136b839',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of business process flow record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when determine business process flow records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to determine business process flow records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 business process flow records from a caller-supplied ID list, producing a dry-run preview workbook, pausing for approval, then a confirmation workbook after commit.', 'example_request': 'Bulk-update these business process flow record IDs in USMF sandbox to the new value, show me a dry run first.', 'inputs': [{'description': 'List of business process flow record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many D365 business process flow records at once and want a before/after preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDetermineBusinessProcessFlow(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDetermineBusinessProcessFlow'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of business process flow record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
