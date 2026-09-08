---
name: "rar-cowork-cookbook-bulk-update-retire-and-decommission-software"
description: "Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_and_decommission_software", "rar_sha256": "c0a318a0baf3840f0717ce93b1be39b15055289f797135139ce58cce960e0b47", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_retire_and_decommission_software_agent.py` and in the RCI capsule.

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

Retire and decommission software Bulk Field Update — Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The new value(s) to write to the target field(s) on those records.",
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
      "description": "List of retire and decommission software record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 c0a318a0baf3840f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_retire_and_decommission_software_agent.py` first:

```bash
python3 bulk_update_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_retire_and_decommission_software_agent.py   # or on stdin
python3 bulk_update_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Bulk Field Update — Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_retire_and_decommission_software',
    "version": '3.0.3',
    "display_name": 'Retire and decommission software Bulk Field Update',
    "description": 'Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then',
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
        "upstream_slug": 'bulk-update-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32a1cd5e7e00d4cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The new value(s) to write to the target field(s) on those records.', 'record_ids': 'List of retire and decommission software record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when retire and decommission software records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to retire and decommission software records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then', 'example_request': 'Bulk update these retire/decommission software records in USMF sandbox - show me a dry-run preview first.', 'inputs': [{'description': 'List of retire and decommission software record IDs to update.', 'name': 'record_ids'}, {'description': 'The new value(s) to write to the target field(s) on those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of retire/decommission software record IDs and new field values to update in bulk in a D365 sandbox, with a preview-and-approve step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRetireAndDecommissionSoftware(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRetireAndDecommissionSoftware'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The new value(s) to write to the target field(s) on those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of retire and decommission software record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
