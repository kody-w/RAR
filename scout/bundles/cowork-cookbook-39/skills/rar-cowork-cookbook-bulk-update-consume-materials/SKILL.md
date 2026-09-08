---
name: "rar-cowork-cookbook-bulk-update-consume-materials"
description: "Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_consume_materials", "rar_sha256": "1e43067f0a7a66d35b9f155b2be82acd769ac73d4e356e0b34f330dec4750049", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_consume_materials`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_consume_materials_agent.py` and in the RCI capsule.

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

Consume materials Bulk Field Update — Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-consume-materials
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
      "description": "List of consume materials record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_consume_materials_agent.py` and embedded as the fenced Python below (sha256 1e43067f0a7a66d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_consume_materials_agent.py` first:

```bash
python3 bulk_update_consume_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_consume_materials_agent.py   # or on stdin
python3 bulk_update_consume_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume materials Bulk Field Update — Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-consume-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_consume_materials',
    "version": '3.0.3',
    "display_name": 'Consume materials Bulk Field Update',
    "description": 'Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-consume-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-consume-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9af294454389a69c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-materials'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-consume-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of consume materials record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when consume materials records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to consume materials records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef', 'example_request': 'Bulk update these consume materials record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of consume materials record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many consume materials records in D365 and want a before/after preview and approval step before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConsumeMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConsumeMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of consume materials record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConsumeMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
