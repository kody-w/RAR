---
name: "rar-cowork-cookbook-bulk-update-identify-workplace-hazards"
description: "Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_identify_workplace_hazards", "rar_sha256": "d0a50dd1577f1194b6e49e9541122982950e21eae0ec3327f84c30e8c3c06a84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_identify_workplace_hazards`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_identify_workplace_hazards_agent.py` and in the RCI capsule.

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

Identify workplace hazards Bulk Field Update — Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
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
      "description": "Dynamics 365 legal entity, default USMF (sandbox).",
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
      "description": "List of workplace-hazard record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 d0a50dd1577f1194…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_identify_workplace_hazards_agent.py` first:

```bash
python3 bulk_update_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_identify_workplace_hazards_agent.py   # or on stdin
python3 bulk_update_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Bulk Field Update — Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_identify_workplace_hazards',
    "version": '3.0.3',
    "display_name": 'Identify workplace hazards Bulk Field Update',
    "description": 'Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '743370397ed4ea19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity, default USMF (sandbox).', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of workplace-hazard record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when identify workplace hazards records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to identify workplace hazards records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval', 'example_request': 'Bulk update these workplace hazard record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of workplace-hazard record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF (sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a list of workplace-hazard record IDs and new field values to update in bulk and want a before/after dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateIdentifyWorkplaceHazards(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIdentifyWorkplaceHazards'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF (sandbox).', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of workplace-hazard record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
