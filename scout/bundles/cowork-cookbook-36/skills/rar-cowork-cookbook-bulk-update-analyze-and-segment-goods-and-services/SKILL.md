---
name: "rar-cowork-cookbook-bulk-update-analyze-and-segment-goods-and-services"
description: "Runs a bulk field update on analyze-and-segment goods and services records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services", "rar_sha256": "786cb631081f54fdba27b9745b7f467e8258e24add7b0149b3c076ed013f9d71", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
