---
name: "rar-cowork-cookbook-bulk-update-analyze-rebates-and-incentives"
description: "Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_rebates_and_incentives", "rar_sha256": "594bcd4370a4fec9f735a4bd9f1c99fdc970b2570d41ca5a8f064fb33127e5f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Analyze rebates and incentives Bulk Field Update — Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
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
      "description": "D365 legal entity to run against; sandbox USMF by default.",
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
      "description": "List of analyze rebates and incentives record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 594bcd4370a4fec9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 bulk_update_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 bulk_update_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Bulk Field Update — Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_rebates_and_incentives',
    "version": '3.0.3',
    "display_name": 'Analyze rebates and incentives Bulk Field Update',
    "description": 'Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro',
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
        "upstream_slug": 'bulk-update-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a17aa9907e0699f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; sandbox USMF by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of analyze rebates and incentives record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze rebates and incentives records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze rebates and incentives records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro', 'example_request': 'Bulk update these rebate record IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of analyze rebates and incentives record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many analyze rebates and incentives records in a D365 sandbox and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeRebatesAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeRebatesAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; sandbox USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of analyze rebates and incentives record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
