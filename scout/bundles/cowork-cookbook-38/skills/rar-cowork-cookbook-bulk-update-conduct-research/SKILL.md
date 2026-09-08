---
name: "rar-cowork-cookbook-bulk-update-conduct-research"
description: "Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_conduct_research", "rar_sha256": "7517f28a3f41c0a0d2eca1e26a940cab8549bc040e5aed7ca58c378a4a5a1ee6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_conduct_research_agent.py` and in the RCI capsule.

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

Conduct research Bulk Field Update — Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
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
      "description": "Explicit approval to commit after reviewing the dry-run preview.",
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
      "description": "List of conduct research record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_conduct_research_agent.py` and embedded as the fenced Python below (sha256 7517f28a3f41c0a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_conduct_research_agent.py` first:

```bash
python3 bulk_update_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_conduct_research_agent.py   # or on stdin
python3 bulk_update_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Bulk Field Update — Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_conduct_research',
    "version": '3.0.3',
    "display_name": 'Conduct research Bulk Field Update',
    "description": 'Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f3747fc3c2b1776',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval to commit after reviewing the dry-run preview.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of conduct research record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when conduct research records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to conduct research records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to conduct research records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, then a confirmation workbook after approval.', 'example_request': 'Bulk update these conduct research record IDs in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of conduct research record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of conduct research record IDs and new values to update in bulk in a D365 sandbox and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConductResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConductResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval to commit after reviewing the dry-run preview.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of conduct research record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
