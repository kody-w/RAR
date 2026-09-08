---
name: "rar-cowork-cookbook-bulk-update-define-posting-policies"
description: "Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_posting_policies", "rar_sha256": "f4e294797a16b89bacd28d81591f92220908a502a3a8900cc0caa4d05299ffc6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_posting_policies_agent.py` and in the RCI capsule.

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

Define posting policies Bulk Field Update — Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
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
      "description": "The new field value(s) to apply to each record.",
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
      "description": "List of define posting policies record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 f4e294797a16b89b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_posting_policies_agent.py` first:

```bash
python3 bulk_update_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_posting_policies_agent.py   # or on stdin
python3 bulk_update_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Bulk Field Update — Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_posting_policies',
    "version": '3.0.3',
    "display_name": 'Define posting policies Bulk Field Update',
    "description": 'Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a',
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
        "upstream_slug": 'bulk-update-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '094ef9b426d4a6f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to each record.', 'record_ids': 'List of define posting policies record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define posting policies records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define posting policies records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a', 'example_request': 'Bulk update these posting policy record IDs to the new value in USMF sandbox - show me the dry-run first.', 'inputs': [{'description': 'List of define posting policies record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of define posting policies record IDs and new values to update in bulk in a D365 sandbox, and want a reviewed dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefinePostingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefinePostingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define posting policies record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
