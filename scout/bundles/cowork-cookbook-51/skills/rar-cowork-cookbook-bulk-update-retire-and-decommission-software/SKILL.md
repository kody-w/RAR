---
name: "rar-cowork-cookbook-bulk-update-retire-and-decommission-software"
description: "Applies a bulk field update to retire-and-decommission software records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_retire_and_decommission_software", "rar_sha256": "c0a318a0baf3840f0717ce93b1be39b15055289f797135139ce58cce960e0b47", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
