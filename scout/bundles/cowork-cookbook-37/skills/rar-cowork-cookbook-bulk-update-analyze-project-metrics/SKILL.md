---
name: "rar-cowork-cookbook-bulk-update-analyze-project-metrics"
description: "Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_project_metrics", "rar_sha256": "8913cdd7810a6af1329956c62c59d15fd932480c685c6b463dfa4b6ac84daea9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_project_metrics`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_project_metrics_agent.py` and in the RCI capsule.

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

Analyze project metrics Bulk Field Update — Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics
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
      "description": "List of analyze project metrics record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 8913cdd7810a6af1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_project_metrics_agent.py` first:

```bash
python3 bulk_update_analyze_project_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_project_metrics_agent.py   # or on stdin
python3 bulk_update_analyze_project_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze project metrics Bulk Field Update — Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_project_metrics',
    "version": '3.0.3',
    "display_name": 'Analyze project metrics Bulk Field Update',
    "description": 'Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-project-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '415a8c05991949dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/analyze-project-metrics'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-analyze-project-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of analyze project metrics record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze project metrics records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze project metrics records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a', 'example_request': 'Bulk update these project metrics record IDs to the new owner value in USMF sandbox — show me a dry-run first.', 'inputs': [{'description': 'List of analyze project metrics record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across a known list of analyze project metrics record IDs and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeProjectMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProjectMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of analyze project metrics record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeProjectMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
