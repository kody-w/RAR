---
name: "rar-cowork-cookbook-bulk-update-analyze-production-quality-results"
description: "Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_production_quality_results", "rar_sha256": "133b2e087c725d4f7532812578ca8452e9a45138b324afd483711ee8eb020d34", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_production_quality_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_production_quality_results_agent.py` and in the RCI capsule.

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

Analyze production quality results Bulk Field Update — Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
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
      "description": "Explicit approval after reviewing the dry-run preview, required before any write.",
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
      "description": "List of production quality results record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 133b2e087c725d4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_production_quality_results_agent.py` first:

```bash
python3 bulk_update_analyze_production_quality_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_production_quality_results_agent.py   # or on stdin
python3 bulk_update_analyze_production_quality_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production quality results Bulk Field Update — Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_production_quality_results',
    "version": '3.0.3',
    "display_name": 'Analyze production quality results Bulk Field Update',
    "description": 'Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-production-quality-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53f81551ad02258e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-quality-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-analyze-production-quality-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, required before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of production quality results record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze production quality results records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze production quality results records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau', 'example_request': 'Bulk update these production quality results records in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of production quality results record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, required before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many production quality results records in a D365 sandbox and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeProductionQualityResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductionQualityResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, required before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of production quality results record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeProductionQualityResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
