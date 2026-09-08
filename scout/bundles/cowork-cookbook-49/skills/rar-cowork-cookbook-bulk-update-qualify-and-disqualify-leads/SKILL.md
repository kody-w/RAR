---
name: "rar-cowork-cookbook-bulk-update-qualify-and-disqualify-leads"
description: "Applies a bulk field update to qualify/disqualify leads records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_qualify_and_disqualify_leads", "rar_sha256": "c67856f22586677d782493b572a0f66edf2a475f0d8aebbd1bec2e570175c3db", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
