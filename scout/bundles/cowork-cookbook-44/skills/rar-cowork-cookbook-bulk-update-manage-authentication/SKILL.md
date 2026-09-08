---
name: "rar-cowork-cookbook-bulk-update-manage-authentication"
description: "Applies a bulk field update to Dynamics 365 manage authentication records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and emits a confirmati"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_authentication", "rar_sha256": "5f485acddd83b5b3d16fb1e865c549e6c6e2addda78553bdb9b8fd1f9b7618a5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
