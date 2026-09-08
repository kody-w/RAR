---
name: "rar-cowork-cookbook-bulk-update-develop-new-services"
description: "Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_new_services", "rar_sha256": "fb9e3787833ec800b1d82dd4989c839f05772e0c4c22891a156774bb93f3637b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_new_services`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_new_services_agent.py` and in the RCI capsule.

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

Develop new services Bulk Field Update — Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
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
    "environment": {
      "description": "Target environment; sandbox first before any production run.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF).",
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
      "description": "List of develop new services record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 fb9e3787833ec800…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_new_services_agent.py` first:

```bash
python3 bulk_update_develop_new_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_new_services_agent.py   # or on stdin
python3 bulk_update_develop_new_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new services Bulk Field Update — Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-new-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_new_services',
    "version": '3.0.3',
    "display_name": 'Develop new services Bulk Field Update',
    "description": 'Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work',
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
        "upstream_slug": 'bulk-update-develop-new-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-new-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c06dd32a8f4a518c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/develop-new-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-develop-new-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before any production run.', 'legal_entity': 'D365 legal entity to run against (default USMF).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of develop new services record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop new services records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop new services records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop new services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook and, after approval, a confirmation work', 'example_request': 'Bulk update these develop new services record IDs in USMF sandbox with the new value - show me a dry-run first.', 'inputs': [{'description': 'List of develop new services record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before any production run.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a list of develop new services record IDs and new field values to update in bulk in a D365 sandbox, and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopNewServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopNewServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before any production run.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop new services record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopNewServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
