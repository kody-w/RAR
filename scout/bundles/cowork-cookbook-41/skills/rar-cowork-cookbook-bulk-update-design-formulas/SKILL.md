---
name: "rar-cowork-cookbook-bulk-update-design-formulas"
description: "Applies a bulk field update to design formulas records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_design_formulas", "rar_sha256": "f926ab0dd3bedfbfc1e410ae1be707b93fb00b31fe8b8bd65084bb3e433e676d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
