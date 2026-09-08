---
name: "rar-cowork-cookbook-bulk-update-analyze-product-quality-data"
description: "Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_product_quality_data", "rar_sha256": "6d357e2ad62e92f5c2947a2933acf3083d6e913ada876a20fd889a9504c1ad67", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Bulk Field Update — Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
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
      "description": "Explicit approval after reviewing the dry-run preview, before changes are applied.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity / environment to run against (defaults to USMF sandbox).",
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
      "description": "List of product quality record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 6d357e2ad62e92f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_product_quality_data_agent.py` first:

```bash
python3 bulk_update_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_product_quality_data_agent.py   # or on stdin
python3 bulk_update_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Bulk Field Update — Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_product_quality_data',
    "version": '3.0.3',
    "display_name": 'Analyze product quality data Bulk Field Update',
    "description": 'Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa98d2999191b1be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of product quality record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze product quality data records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze product quality data records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to product quality records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, pauses for approval, th', 'example_request': 'Bulk update these product quality records in USMF sandbox to status Approved — show me the dry-run first.', 'inputs': [{'description': 'List of product quality record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many product quality records at once and want a reviewable dry-run preview before committing writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeProductQualityData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductQualityData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview, before changes are applied.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity / environment to run against (defaults to USMF sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of product quality record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
