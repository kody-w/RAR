---
name: "rar-cowork-cookbook-bulk-update-analyze-service-profitability"
description: "Applies a bulk field update to service profitability records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pause"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_service_profitability", "rar_sha256": "b67b10004482ffe1fefd2f57a7c98afbbdb8ff03f35d3b10234050221074e3ce", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
