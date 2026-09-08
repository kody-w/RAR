---
name: "rar-cowork-cookbook-bulk-update-define-sales-channels"
description: "Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_channels", "rar_sha256": "e5f31abff4268e52f1861942c0f85d315c06f233b91ca3f44117d45d0b8bb9f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_sales_channels_agent.py` and in the RCI capsule.

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

Define sales channels Bulk Field Update — Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-channels
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
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of define sales channels record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 e5f31abff4268e52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_channels_agent.py` first:

```bash
python3 bulk_update_define_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_sales_channels_agent.py   # or on stdin
python3 bulk_update_define_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales channels Bulk Field Update — Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_sales_channels',
    "version": '3.0.3',
    "display_name": 'Define sales channels Bulk Field Update',
    "description": 'Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '009f0368ed81b4cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-channels'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-define-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of define sales channels record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define sales channels records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define sales channels records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes.', 'example_request': 'Bulk update these sales channel record IDs in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of define sales channels record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of define sales channels record IDs in a D365 sandbox, with a preview and approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineSalesChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineSalesChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define sales channels record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
