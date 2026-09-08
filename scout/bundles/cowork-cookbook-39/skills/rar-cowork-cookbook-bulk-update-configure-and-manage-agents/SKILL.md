---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-agents"
description: "Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_agents", "rar_sha256": "4ca2e03b8f718280e715e41173c9ce414ada1659fc84e9ddad7859b4faafeabf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_manage_agents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_manage_agents_agent.py` and in the RCI capsule.

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

Configure and manage agents Bulk Field Update — Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents
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
      "description": "Dynamics 365 legal entity, default USMF (sandbox).",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to those records.",
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
      "description": "List of record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_agents_agent.py` and embedded as the fenced Python below (sha256 4ca2e03b8f718280…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_agents_agent.py` first:

```bash
python3 bulk_update_configure_and_manage_agents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_manage_agents_agent.py   # or on stdin
python3 bulk_update_configure_and_manage_agents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage agents Bulk Field Update — Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_manage_agents',
    "version": '3.0.3',
    "display_name": 'Configure and manage agents Bulk Field Update',
    "description": 'Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b',
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
        "upstream_slug": 'bulk-update-configure-and-manage-agents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-agents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1bb469c6bcf2f23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-agents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-manage-agents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity, default USMF (sandbox).', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when configure and manage agents records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to configure and manage agents records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b', 'example_request': 'Bulk update these agent config records in USMF sandbox to the new owner value - show me the dry-run first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF (sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field across many D365 agent-configuration records at once and want a reviewable before/after preview before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConfigureAndManageAgents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManageAgents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF (sandbox).', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConfigureAndManageAgents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
