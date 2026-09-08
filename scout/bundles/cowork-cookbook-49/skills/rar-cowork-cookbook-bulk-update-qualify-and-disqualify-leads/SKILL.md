---
name: "rar-cowork-cookbook-bulk-update-qualify-and-disqualify-leads"
description: "Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_qualify_and_disqualify_leads", "rar_sha256": "c67856f22586677d782493b572a0f66edf2a475f0d8aebbd1bec2e570175c3db", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_qualify_and_disqualify_leads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_qualify_and_disqualify_leads_agent.py` and in the RCI capsule.

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

Qualify and disqualify leads Bulk Field Update — Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; sandbox USMF by default.",
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
      "description": "List of qualify/disqualify leads record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 c67856f22586677d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 bulk_update_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 bulk_update_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Bulk Field Update — Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_qualify_and_disqualify_leads',
    "version": '3.0.3',
    "display_name": 'Qualify and disqualify leads Bulk Field Update',
    "description": 'Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa',
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
        "upstream_slug": 'bulk-update-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e039c26b6a0e250f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of qualify/disqualify leads record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when qualify and disqualify leads records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to qualify and disqualify leads records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa', 'example_request': 'Bulk update these lead record IDs in USMF sandbox with the new status value — show me a dry-run first.', 'inputs': [{'description': 'List of qualify/disqualify leads record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many qualify/disqualify leads records in D365 and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateQualifyAndDisqualifyLeads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQualifyAndDisqualifyLeads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; sandbox USMF by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of qualify/disqualify leads record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
