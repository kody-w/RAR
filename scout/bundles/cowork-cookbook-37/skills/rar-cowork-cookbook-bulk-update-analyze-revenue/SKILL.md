---
name: "rar-cowork-cookbook-bulk-update-analyze-revenue"
description: "Applies a bulk field update to analyze revenue records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook, then a confirmation workbook after approval."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_revenue", "rar_sha256": "3498c0789c974963a55830b4f930316d751b6303b04a871e0b406f4c1a8540c4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
