---
name: "rar-cowork-cookbook-bulk-update-analyze-project-metrics"
description: "Applies a bulk field update to analyze project metrics records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_project_metrics", "rar_sha256": "8913cdd7810a6af1329956c62c59d15fd932480c685c6b463dfa4b6ac84daea9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
