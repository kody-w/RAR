---
name: "rar-cowork-cookbook-bulk-update-manage-loyalty-programs"
description: "Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_loyalty_programs", "rar_sha256": "aaf91997eb88313bd07d81c0ed8cb4ab269ac49aa7be987bae2c7716a931e97a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; sandbox first).",
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
      "description": "List of loyalty program record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 aaf91997eb88313b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_loyalty_programs_agent.py` first:

```bash
python3 bulk_update_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_loyalty_programs_agent.py   # or on stdin
python3 bulk_update_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_loyalty_programs',
    "version": '3.0.3',
    "display_name": 'Manage loyalty programs Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b5eda514b4777c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF; sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of loyalty program record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage loyalty programs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage loyalty programs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM loyalty program records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a co', 'example_request': 'Bulk update these loyalty program record IDs in USMF sandbox to tier Gold — show me the dry-run first.', 'inputs': [{'description': 'List of loyalty program record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of loyalty program record IDs in D365 F&SCM, with a reviewed dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageLoyaltyPrograms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageLoyaltyPrograms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of loyalty program record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
