---
name: "rar-cowork-cookbook-bulk-update-consume-materials"
description: "Applies a bulk field update to consume materials records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_consume_materials", "rar_sha256": "1e43067f0a7a66d35b9f155b2be82acd769ac73d4e356e0b34f330dec4750049", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
