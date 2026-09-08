---
name: "rar-cowork-cookbook-bulk-update-manage-authentication"
description: "Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_authentication", "rar_sha256": "5f485acddd83b5b3d16fb1e865c549e6c6e2addda78553bdb9b8fd1f9b7618a5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_authentication`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_authentication_agent.py` and in the RCI capsule.

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

Manage authentication Bulk Field Update — Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-authentication
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are committed.",
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
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of manage authentication record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 5f485acddd83b5b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_authentication_agent.py` first:

```bash
python3 bulk_update_manage_authentication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_authentication_agent.py   # or on stdin
python3 bulk_update_manage_authentication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage authentication Bulk Field Update — Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-authentication
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_authentication',
    "version": '3.0.3',
    "display_name": 'Manage authentication Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati',
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
        "upstream_slug": 'bulk-update-manage-authentication',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-authentication',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc159986378b08f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-authentication'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-authentication', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of manage authentication record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage authentication records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage authentication records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati', 'example_request': 'Bulk update these manage authentication records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of manage authentication record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many manage authentication records at once in D365 (USMF sandbox) and want a reviewable dry-run before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageAuthentication(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageAuthentication'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of manage authentication record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageAuthentication().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
