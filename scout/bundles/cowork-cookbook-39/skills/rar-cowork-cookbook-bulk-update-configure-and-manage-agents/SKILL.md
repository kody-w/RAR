---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-agents"
description: "Applies a bulk field update to configure-and-manage-agents records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, producing a dry-run preview workbook for approval b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_agents", "rar_sha256": "4ca2e03b8f718280e715e41173c9ce414ada1659fc84e9ddad7859b4faafeabf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
