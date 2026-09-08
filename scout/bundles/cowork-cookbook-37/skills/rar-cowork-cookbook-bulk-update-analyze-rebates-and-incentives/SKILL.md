---
name: "rar-cowork-cookbook-bulk-update-analyze-rebates-and-incentives"
description: "Applies a bulk field update to analyze rebates and incentives records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_rebates_and_incentives", "rar_sha256": "594bcd4370a4fec9f735a4bd9f1c99fdc970b2570d41ca5a8f064fb33127e5f9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
