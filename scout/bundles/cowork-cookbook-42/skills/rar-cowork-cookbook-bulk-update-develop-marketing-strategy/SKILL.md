---
name: "rar-cowork-cookbook-bulk-update-develop-marketing-strategy"
description: "Applies a bulk field update to develop-marketing-strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_marketing_strategy", "rar_sha256": "81d2e41573caea26595e96163e3f10d6457b25bc3aa4172eb9edcca634a1d119", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
