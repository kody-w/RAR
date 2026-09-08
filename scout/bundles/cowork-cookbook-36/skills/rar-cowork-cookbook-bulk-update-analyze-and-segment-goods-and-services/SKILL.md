---
name: "rar-cowork-cookbook-bulk-update-analyze-and-segment-goods-and-services"
description: "Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services", "rar_sha256": "786cb631081f54fdba27b9745b7f467e8258e24add7b0149b3c076ed013f9d71", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_and_segment_goods_and_services_agent.py` and in the RCI capsule.

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

Analyze and segment goods and services Bulk Field Update — Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
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
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of the record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 786cb631081f54fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Bulk Field Update — Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services',
    "version": '3.0.3',
    "display_name": 'Analyze and segment goods and services Bulk Field Update',
    "description": 'Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing',
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
        "upstream_slug": 'bulk-update-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c8440a01891fed6d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of the record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze and segment goods and services records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze and segment goods and services records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing', 'example_request': 'Bulk update these goods and services records in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'List of the record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to change a field on many analyze-and-segment goods and services records at once in a D365 sandbox, with a preview-then-approve step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeAndSegmentGoodsAndServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of the record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
