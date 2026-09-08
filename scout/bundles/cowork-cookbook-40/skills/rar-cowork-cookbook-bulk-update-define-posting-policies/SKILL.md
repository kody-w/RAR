---
name: "rar-cowork-cookbook-bulk-update-define-posting-policies"
description: "Applies a bulk field update to define posting policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_posting_policies", "rar_sha256": "f4e294797a16b89bacd28d81591f92220908a502a3a8900cc0caa4d05299ffc6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
