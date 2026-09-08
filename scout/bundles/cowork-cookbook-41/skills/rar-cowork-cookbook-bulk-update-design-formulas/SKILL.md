---
name: "rar-cowork-cookbook-bulk-update-design-formulas"
description: "Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_design_formulas", "rar_sha256": "f926ab0dd3bedfbfc1e410ae1be707b93fb00b31fe8b8bd65084bb3e433e676d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_design_formulas`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_design_formulas_agent.py` and in the RCI capsule.

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

Design formulas Bulk Field Update — Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-design-formulas
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
      "description": "Explicit approval to commit after reviewing the dry-run preview.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF, sandbox).",
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
      "description": "List of design formulas record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_design_formulas_agent.py` and embedded as the fenced Python below (sha256 f926ab0dd3bedfbf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_design_formulas_agent.py` first:

```bash
python3 bulk_update_design_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_design_formulas_agent.py   # or on stdin
python3 bulk_update_design_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design formulas Bulk Field Update — Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-design-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_design_formulas',
    "version": '3.0.3',
    "display_name": 'Design formulas Bulk Field Update',
    "description": 'Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-design-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-design-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4131d335bd6d371',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-formulas'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-design-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval to commit after reviewing the dry-run preview.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of design formulas record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when design formulas records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to design formulas records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the', 'example_request': 'Bulk update these design formulas record IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of design formulas record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of design formulas record IDs and new field values to update in bulk in a D365 sandbox and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDesignFormulas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDesignFormulas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of design formulas record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDesignFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
