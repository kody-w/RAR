---
name: "rar-cowork-cookbook-bulk-update-analyze-revenue"
description: "Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_revenue", "rar_sha256": "3498c0789c974963a55830b4f930316d751b6303b04a871e0b406f4c1a8540c4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_revenue`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_revenue_agent.py` and in the RCI capsule.

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

Analyze revenue Bulk Field Update — Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-revenue
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
      "description": "Explicit approval to commit after reviewing the dry-run preview workbook.",
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
      "description": "List of analyze revenue record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 3498c0789c974963…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_revenue_agent.py` first:

```bash
python3 bulk_update_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_revenue_agent.py   # or on stdin
python3 bulk_update_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Bulk Field Update — Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_revenue',
    "version": '3.0.3',
    "display_name": 'Analyze revenue Bulk Field Update',
    "description": 'Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.',
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
        "upstream_slug": 'bulk-update-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82076d515dc992db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval to commit after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of analyze revenue record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze revenue records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze revenue records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval.', 'example_request': 'Bulk update these analyze revenue record IDs in USMF sandbox with the new value - show me a dry run first.', 'inputs': [{'description': 'List of analyze revenue record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval to commit after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across a known list of analyze revenue record IDs in D365 and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval to commit after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of analyze revenue record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
