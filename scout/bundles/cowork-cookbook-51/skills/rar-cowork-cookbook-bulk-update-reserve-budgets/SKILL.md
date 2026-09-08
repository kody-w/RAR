---
name: "rar-cowork-cookbook-bulk-update-reserve-budgets"
description: "Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reserve_budgets", "rar_sha256": "15c643eaa70754234207b4430dbd8d27e15162a61d994160a0851600a4b73153", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reserve_budgets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reserve_budgets_agent.py` and in the RCI capsule.

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

Reserve budgets Bulk Field Update — Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
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
      "description": "D365 legal entity to run against (USMF; sandbox first).",
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
      "description": "List of reserve budgets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 15c643eaa7075423…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reserve_budgets_agent.py` first:

```bash
python3 bulk_update_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reserve_budgets_agent.py   # or on stdin
python3 bulk_update_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Bulk Field Update — Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reserve_budgets',
    "version": '3.0.3',
    "display_name": 'Reserve budgets Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c43a13d473ea2f19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (USMF; sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of reserve budgets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when reserve budgets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to reserve budgets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft', 'example_request': 'Bulk update these reserve budgets record IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of reserve budgets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (USMF; sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on a known list of reserve budgets record IDs in a D365 sandbox, with a reviewable dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReserveBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReserveBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (USMF; sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of reserve budgets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
