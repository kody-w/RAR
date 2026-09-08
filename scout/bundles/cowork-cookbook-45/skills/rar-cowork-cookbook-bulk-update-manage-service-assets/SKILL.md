---
name: "rar-cowork-cookbook-bulk-update-manage-service-assets"
description: "Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_service_assets", "rar_sha256": "21d9c860946217703b2934a6bd280d422532b2e43f88a73e846ac691317df2bf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Bulk Field Update — Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
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
      "description": "D365 legal entity to run against; recipe uses USMF sandbox.",
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
      "description": "List of manage service assets record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 21d9c86094621770…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_service_assets_agent.py` first:

```bash
python3 bulk_update_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_service_assets_agent.py   # or on stdin
python3 bulk_update_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Bulk Field Update — Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_service_assets',
    "version": '3.0.3',
    "display_name": 'Manage service assets Bulk Field Update',
    "description": 'Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6378f6d8a7b1d43a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of manage service assets record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage service assets records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage service assets records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to manage service assets records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, returning a dry-run preview workbook for approval', 'example_request': 'Bulk-update these service asset record IDs with the new value in USMF sandbox — show me the dry-run preview first.', 'inputs': [{'description': 'List of manage service assets record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many manage service assets records at once in a D365 sandbox and want a before/after preview to approve first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage service assets record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
