---
name: "rar-cowork-cookbook-bulk-update-develop-marketing-strategy"
description: "Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_marketing_strategy", "rar_sha256": "81d2e41573caea26595e96163e3f10d6457b25bc3aa4172eb9edcca634a1d119", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_marketing_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_marketing_strategy_agent.py` and in the RCI capsule.

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

Develop marketing strategy Bulk Field Update — Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity, default USMF; sandbox environment only.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 81d2e41573caea26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_marketing_strategy_agent.py` first:

```bash
python3 bulk_update_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_marketing_strategy_agent.py   # or on stdin
python3 bulk_update_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Bulk Field Update — Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_marketing_strategy',
    "version": '3.0.3',
    "display_name": 'Develop marketing strategy Bulk Field Update',
    "description": 'Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61fa441a1aaedcde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'new_values': 'The new field value(s) to apply to those records.', 'record_ids': 'List of record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop marketing strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop marketing strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and', 'example_request': 'Bulk update these marketing strategy record IDs in USMF sandbox with the new owner value - show me the dry run first.', 'inputs': [{'description': 'List of record IDs to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of record IDs and new field values to update in bulk in D365 and want a reviewable dry-run before the write is committed.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopMarketingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMarketingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity, default USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
