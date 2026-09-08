---
name: "rar-cowork-cookbook-bulk-update-reserve-budgets"
description: "Applies a bulk field update to Dynamics 365 reserve budgets records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reserve_budgets", "rar_sha256": "15c643eaa70754234207b4430dbd8d27e15162a61d994160a0851600a4b73153", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
