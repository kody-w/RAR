---
name: "rar-cowork-cookbook-bulk-update-prepare-to-go-live"
description: "Applies a bulk field update to prepare-to-go-live records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approv"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_prepare_to_go_live", "rar_sha256": "bc982bc421951853ce7295b4cb086ad09e5f9f6fd1edbafa03d78df2cb0a78a7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
