---
name: "rar-cowork-cookbook-bulk-update-receive-service-requests"
description: "Applies a bulk field update to Dynamics 365 receive service requests records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_receive_service_requests", "rar_sha256": "d341dfac80fc57eb80844db3a00ba7c4a07505ef83fc3af2bd7f517a4284eef6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
