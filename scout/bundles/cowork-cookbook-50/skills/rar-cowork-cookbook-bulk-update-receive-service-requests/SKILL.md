---
name: "rar-cowork-cookbook-bulk-update-receive-service-requests"
description: "Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_service_requests", "rar_sha256": "d341dfac80fc57eb80844db3a00ba7c4a07505ef83fc3af2bd7f517a4284eef6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_receive_service_requests`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_receive_service_requests_agent.py` and in the RCI capsule.

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

Receive service requests Bulk Field Update — Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
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
      "description": "D365 legal entity to run against; defaults to USMF (sandbox first).",
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
      "description": "List of receive service request record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_receive_service_requests_agent.py` and embedded as the fenced Python below (sha256 d341dfac80fc57eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_receive_service_requests_agent.py` first:

```bash
python3 bulk_update_receive_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_receive_service_requests_agent.py   # or on stdin
python3 bulk_update_receive_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive service requests Bulk Field Update — Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-receive-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_receive_service_requests',
    "version": '3.0.3',
    "display_name": 'Receive service requests Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a',
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
        "upstream_slug": 'bulk-update-receive-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-receive-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c58f06c6417a7fbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/receive-service-requests'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-receive-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of receive service request record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when receive service requests records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to receive service requests records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a', 'example_request': 'Bulk update these receive service request IDs in USMF sandbox to the new status - show me the dry-run first.', 'inputs': [{'description': 'List of receive service request record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of receive service request records in a D365 sandbox, with a reviewed dry-run before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReceiveServiceRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReceiveServiceRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of receive service request record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReceiveServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
