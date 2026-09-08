---
name: "rar-cowork-cookbook-bulk-update-follow-up-on-a-case"
description: "Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_follow_up_on_a_case", "rar_sha256": "b9e22aea0b5e12eccac74303d98b9633cc6a3a7962465f630a96558fc60a4a66", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_follow_up_on_a_case`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_follow_up_on_a_case_agent.py` and in the RCI capsule.

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

Follow up on a case Bulk Field Update — Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are written.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of follow-up-on-a-case record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 b9e22aea0b5e12ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_follow_up_on_a_case_agent.py` first:

```bash
python3 bulk_update_follow_up_on_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_follow_up_on_a_case_agent.py   # or on stdin
python3 bulk_update_follow_up_on_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Follow up on a case Bulk Field Update — Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_follow_up_on_a_case',
    "version": '3.0.3',
    "display_name": 'Follow up on a case Bulk Field Update',
    "description": 'Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-follow-up-on-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8853817adc4f2f13',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/follow-up-on-a-case'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-follow-up-on-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of follow-up-on-a-case record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when follow up on a case records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to follow up on a case records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to follow-up-on-a-case records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after appro', 'example_request': 'Bulk update these follow-up case records in USMF sandbox with the new owner — show me a dry-run first.', 'inputs': [{'description': 'List of follow-up-on-a-case record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of follow-up-on-a-case record IDs and new field values to update in bulk in a D365 sandbox, and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateFollowUpOnACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateFollowUpOnACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of follow-up-on-a-case record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateFollowUpOnACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
