---
name: "rar-cowork-cookbook-bulk-update-define-business-continuity-objectives"
description: "Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_business_continuity_objectives", "rar_sha256": "9a9d46ca6d2ba1bd1a699fe8a9b50fa670da99dcf34829e3326be2544006a218", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_business_continuity_objectives`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_business_continuity_objectives_agent.py` and in the RCI capsule.

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

Define business continuity objectives Bulk Field Update — Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
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
      "description": "D365 legal entity to run against (e.g. USMF; sandbox only).",
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
      "description": "List of business continuity objective record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 9a9d46ca6d2ba1bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_business_continuity_objectives_agent.py` first:

```bash
python3 bulk_update_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_business_continuity_objectives_agent.py   # or on stdin
python3 bulk_update_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Bulk Field Update — Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_business_continuity_objectives',
    "version": '3.0.3',
    "display_name": 'Define business continuity objectives Bulk Field Update',
    "description": 'Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '62f8bc6d460dba73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF; sandbox only).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of business continuity objective record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define business continuity objectives records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define business continuity objectives records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook.', 'example_request': 'Bulk-update these business continuity objective records in USMF sandbox to the new owner — show me a dry run first.', 'inputs': [{'description': 'List of business continuity objective record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF; sandbox only).', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of D365 business continuity objective records in a sandbox legal entity, with preview and approval.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineBusinessContinuityObjectives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBusinessContinuityObjectives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF; sandbox only).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of business continuity objective record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
