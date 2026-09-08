---
name: "rar-cowork-cookbook-bulk-update-define-banking-policies"
description: "Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_banking_policies", "rar_sha256": "c05360197b71d925c3d7f61e82c4f197faa9d393dec97f9ad91ae8966bf4948d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Bulk Field Update — Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
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
      "description": "List of define banking policies record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 c05360197b71d925…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_banking_policies_agent.py` first:

```bash
python3 bulk_update_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_banking_policies_agent.py   # or on stdin
python3 bulk_update_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Bulk Field Update — Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_banking_policies',
    "version": '3.0.3',
    "display_name": 'Define banking policies Bulk Field Update',
    "description": 'Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work',
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
        "upstream_slug": 'bulk-update-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bc8d9e79ccc812ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of define banking policies record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define banking policies records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define banking policies records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on define banking policies records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work', 'example_request': 'Bulk update these banking policy record IDs to the new value — show me the dry-run preview first in USMF sandbox.', 'inputs': [{'description': 'List of define banking policies record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of define banking policies record IDs in a D365 sandbox, with a preview before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineBankingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBankingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define banking policies record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
