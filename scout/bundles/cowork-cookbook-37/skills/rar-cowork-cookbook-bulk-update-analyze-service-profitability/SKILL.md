---
name: "rar-cowork-cookbook-bulk-update-analyze-service-profitability"
description: "Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_service_profitability", "rar_sha256": "b67b10004482ffe1fefd2f57a7c98afbbdb8ff03f35d3b10234050221074e3ce", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_service_profitability`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_service_profitability_agent.py` and in the RCI capsule.

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

Analyze service profitability Bulk Field Update — Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of service profitability record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 b67b10004482ffe1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_service_profitability_agent.py` first:

```bash
python3 bulk_update_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_service_profitability_agent.py   # or on stdin
python3 bulk_update_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Bulk Field Update — Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_service_profitability',
    "version": '3.0.3',
    "display_name": 'Analyze service profitability Bulk Field Update',
    "description": 'Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33790a7835cf3391',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of service profitability record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when analyze service profitability records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to analyze service profitability records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause', 'example_request': 'Bulk update these service profitability record IDs in USMF sandbox to the new value — show me the dry-run first.', 'inputs': [{'description': 'List of service profitability record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'Legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field across many service profitability records at once in a D365 sandbox and want a reviewable before/after preview first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAnalyzeServiceProfitability(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeServiceProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of service profitability record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
