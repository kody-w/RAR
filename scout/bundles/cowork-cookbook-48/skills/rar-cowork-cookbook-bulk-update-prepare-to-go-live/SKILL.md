---
name: "rar-cowork-cookbook-bulk-update-prepare-to-go-live"
description: "Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_prepare_to_go_live", "rar_sha256": "bc982bc421951853ce7295b4cb086ad09e5f9f6fd1edbafa03d78df2cb0a78a7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_prepare_to_go_live`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_prepare_to_go_live_agent.py` and in the RCI capsule.

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

Prepare to go live Bulk Field Update — Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
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
      "description": "D365 legal entity to run against (USMF, sandbox first).",
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
      "description": "List of prepare-to-go-live record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 bc982bc421951853…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_prepare_to_go_live_agent.py` first:

```bash
python3 bulk_update_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_prepare_to_go_live_agent.py   # or on stdin
python3 bulk_update_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Bulk Field Update — Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_prepare_to_go_live',
    "version": '3.0.3',
    "display_name": 'Prepare to go live Bulk Field Update',
    "description": 'Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv',
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
        "upstream_slug": 'bulk-update-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '11d1317d21f245e4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (USMF, sandbox first).', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of prepare-to-go-live record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when prepare to go live records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to prepare to go live records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv', 'example_request': 'Bulk update these prepare-to-go-live records in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of prepare-to-go-live record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (USMF, sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a list of prepare-to-go-live record IDs and new values to update in bulk in a D365 sandbox, and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePrepareToGoLive(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrepareToGoLive'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (USMF, sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of prepare-to-go-live record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdatePrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
