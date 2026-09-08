---
name: "rar-cowork-cookbook-bulk-update-identify-workplace-hazards"
description: "Applies a bulk field update to workplace-hazard records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_identify_workplace_hazards", "rar_sha256": "d0a50dd1577f1194b6e49e9541122982950e21eae0ec3327f84c30e8c3c06a84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
