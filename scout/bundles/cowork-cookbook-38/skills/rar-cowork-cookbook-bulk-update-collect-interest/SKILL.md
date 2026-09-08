---
name: "rar-cowork-cookbook-bulk-update-collect-interest"
description: "Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_collect_interest", "rar_sha256": "0afd6b436f0a4e61e475e5a6b6cfdb45f4abc8a406fbcaff100570780a687e5f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_collect_interest`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_collect_interest_agent.py` and in the RCI capsule.

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

Collect interest Bulk Field Update — Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
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
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
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
      "description": "List of collect interest record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_collect_interest_agent.py` and embedded as the fenced Python below (sha256 0afd6b436f0a4e61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_collect_interest_agent.py` first:

```bash
python3 bulk_update_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_collect_interest_agent.py   # or on stdin
python3 bulk_update_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Bulk Field Update — Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_collect_interest',
    "version": '3.0.3',
    "display_name": 'Collect interest Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5d080f8f07eb2bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of collect interest record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when collect interest records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to collect interest records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 collect interest records in a given legal entity via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing changes and emitting a conf', 'example_request': 'Bulk update these collect interest records in USMF sandbox with the new values - show me a dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of collect interest record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field value across many collect interest records at once in a D365 sandbox, with a before/after preview and approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateCollectInterest(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCollectInterest'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of collect interest record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
