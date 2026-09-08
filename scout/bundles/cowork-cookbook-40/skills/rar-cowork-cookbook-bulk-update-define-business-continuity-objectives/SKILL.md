---
name: "rar-cowork-cookbook-bulk-update-define-business-continuity-objectives"
description: "Applies a bulk field update to business continuity objective records in Dynamics 365 F&SCM via the ERP plugin: returns a dry-run preview workbook, waits for approval, then commits and emits a confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_business_continuity_objectives", "rar_sha256": "9a9d46ca6d2ba1bd1a699fe8a9b50fa670da99dcf34829e3326be2544006a218", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
