---
name: "rar-cowork-cookbook-bulk-update-define-sales-channels"
description: "Runs a bulk field update on Dynamics 365 define sales channels records in legal entity USMF via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before writing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_channels", "rar_sha256": "e5f31abff4268e52f1861942c0f85d315c06f233b91ca3f44117d45d0b8bb9f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
