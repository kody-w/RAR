---
name: "rar-cowork-cookbook-bulk-update-analyze-production-quality-results"
description: "Applies a bulk field update to production quality results records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, approval pau"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_production_quality_results", "rar_sha256": "133b2e087c725d4f7532812578ca8452e9a45138b324afd483711ee8eb020d34", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916efPa1prmV2F+XTVJGtvakJDcdasGgfZdIJCIU45WJLSiXaTz3ecIsJ3c63t70jN/DbYLkM559/d53mPx25vbtXFZv31824duseDcLEvisF64RbDYlkNZp+CtTD3wb+GXRVsnXteWdfP27i0IG79OqjYpC7B9U1VZEjYLd+F1WbqIkjALFl0VuG24aMtFVZdB589rF7fOzZJ2WtRh02VtA979sg6aRVIsdlPh5onfLDACX7D/c79VFj9m4cXNFmHRznusvcK+WzTAOq8cf1pEdZkDjT6wOqzfN93DhmCRJU27KKOX5IWwax7+FOGw6N2sC5t3iyFpY7AzqKf3dVcA88I+Abdnh2df3y3cCpgMVi8qtwPOhqObV1nYvH38+Zd3bwn4/Pbxtzc/cxtw6Y0GLlsPXzeFm033UP/qrvH01nw6CyRlbnEBW6oJxL0A36uwjso6B5eCMFq8vv3YhFn0bvHv/54Obn1pfvr4qVi8Xp/e5j8mMLqN59C6TQtc9t3K9ZJZ04fFJhvcaY5r29XFnJEGpK24fHju/CaprBZ/m+/9+FTy4RK2P356K4EJ7mz5p7efFmUN9IEAgc8fZinVjz99yMohrH/86ZucpvOuod/OwoDVHz6/vr/EgoXflibR4vNeZ7YvXSBBSRUC4X/wb349TX+Je4Xk83Pxj2X1bvF9ybM/fwP2PgvTA3K/LxbEAOx8+3Atk+LHlw6Q67BwCz/88ad/JtaPQz+dS+v/SO7PT8Fx6AYgWq+Q/PTukb5fFsuXb19l/nO1FSiYv+IJWP5F3ddA/TPZj8z+negsKUAbf8nld8V9b8Pyb4uf/6lv/2rDu0X06W0XZkkP6s7Lwo+L3x4l8vMPwbeLP/zyOxD9X4rZl13tPyR8zt0iicKm/fz55x+ax+Uffvn5h64CVRy6+eeuzr4n83txfej5UwRfq378816g3yrSohyKxdceWvxWVv+j/v3D4ghQIPh2vfm4+GMnzq/lYnbii9JnCP7QjQ2w9Q9x/OntdwBDBfDmCTMzCv3bvy2UxK/Lpozaxd4vu3YBEtwmeTgbf4gTgLHNAzUA2oV1k4DAvtaB+p8zPFsMcPPX/+U/oP+9/4J+aMb0z080/+w+Ie7zN0j//IL0zy9I//XD4gC0lHVyScDihbnR9U+FewEgPlsAwLYJ6x6glje14XvQ3O/nDzMB/PrXFH1+yPxQTb8+AD55YqK5FWY8BCvCD7PnpzgsXn76gOPCMfQ7oC4rAW8AospmPgACy6wHeDpHqUmTLFsECUAcwHXTQzaI5MdZ2K+//uq5TfypeAI4tniSYAOBBV/NWbx/D5yMsuQSt5+K0I/LxQ+//f7D4j8X/2rXQ/isQwes8soTsFDca+oC9F2Xg2UzTQLAd4NHnn77/RVqIKYArA2ymkQzC8+bQd2mYfAl7nt+8x7FiYUXgniDWOdVWbeAFRZJ+2EhRIuv9gKl862ZN+IS8GgQVmERhIU/AakucOdrJIuyBVTcJk00vVt0TfjQ+qtXuw8TcwAAbvvrQtnqgKXKbJ4C6hdrgc1lkYDwf62K53UgpP6hWdBfRHxYqHOlAg6u3Squ3ZeOyH3mBbDTl+1AuDsT/Kdi5uZwDtWjbZ7hAYtAZPxXSt/POQfTTA4w4jl3tF/WuDOXHh6cWn8qmldLuHX4mCWAKdPi0iXBTBT/8SqpJi47MOrM8QOWzpJeWQheWXnU4Gsu+Fdz0DxELNjH3PScJRafOhRGVov/n0erR2w4zmS4zYHZLRj1YDrPnM3T5pzb54A6WwgK99mf34adL4D2Bdc/FVkCCrCe/uO58pHp15onVnY18MLcmA/5oMxAzma5jy6Yq7quH6H+VHwhEGDv4oGWIL4AMkBLzUH/onC++8XSGODC/P3bMPElTCBEoNIXVedloAqjMAw810+BVfXcya80g5YI59AOceLHf/JqThGoPCB/AYxIQGIByXz4CurPu19M/9PG58w0b3nMkx1o5PohANgRzgbOyZsTBsxrn8M98PPjQwhwI6/a2XcPtBLw9HkxrMNblzRJO+f6GdewAgD+fn5/ejpfDccKdA8IFuiRqgPRfXTVDDg5mIiADQBYQJPlSQEqCgTlFYSHQDcPH4X3ZYR9SnxcfjkUPlpxprYvG2dH5j3ztPAq3mL6I5IcvlcmQF4+r3jo/ftK+6ptlj2jaQMQEWj8cvc5Vnx4TgbP0WPxRe7Hfzg9/fjXDlgPrrf+XAAfF3HbVs1HCHry8xd6/gCwDHra2jyo+v0THd6/GPT9N4h4/4KI9y+I+JOWZwA+Lv6apX8S8eqUjwvkA/wBnm/Jr0p7vUBgtu9p5/1qvvupMMNvuAvUlzkotTmNE5gNvpLklyWAKS81wCyw+Emazcy1A6D3B0uAnHwq/lj6c+sBEiouc6k25R8g4TEtgDZ4pvArmYFbRQt0B/PceQk/zMe12fwmfPtYdFn27g2AaPgXD3wzeeVzrTfzkRGkAox0bRI+vn2Bwvnzn8/TzAgA1wdt8hUt3QjIWDzRdO6juQT/DmTnOQY05wxxL56fm2AANf3wpZ2q2fjncXAeIB/INbb/qF17fHCzD4tdCFAya/7YDi/Gmxn/D137jDeIsw8cfLeYY9PMDA3iPfs+d7zbgBYCZn3XlgcZfX6S0T8atJtp60989Ron3Mujw/8DwEnkPkgP3Ji57AuVfVcZ4KvPT776R1UzUDw49sfmpz+T23xhHjQAFz70hy4A6qff39XydXj/RyUnMBvNIoLy4+zGuxfagndw4Hq3+Hp2AoF8nWZnDWHR5W8ff57PbXNhPbbMH8Ae8PZ109f/nPHCt1++Y9fT5M9J8B3v5RfB/5dTxYP7H0w4p/o7/j8UPatxtvlbML6ZVD7OlbNJwIX2+d8gv72BZnGBTPfVLq+DCVgOkPV9Mw9dEEAXoBB8f+IAuPd/eWR5SWtiFwzJQByCYR4awuTaX6N4sIrWOIaSCIqvSd8lVzgaUu4KRzDSw9CVGwUrElsjSBiSoQejcICtgLwntnye58xkthCn1hFMUWi0QsASUK7oKghIgiR8fI3CLuW5uIdTrvdta5oUwcvtp5tzTL+enh748fT+tzePWIGV/KoRNs/XFloiHoGuPBP3lnciLAmDO1VC0GhNRijuzk7IZPI2scBLUHOg6XIr1469N9Zucca6umz9waLJcXePdSVd4sjhaCNXC5eCM3/OG8GhLXe6WUSk4YfOloo8VO+xeJbvED+dJn2DyaVw3Zv66E/Xy41KRLsrB1k+EzZ5Pq44N12xKlWU+8laqm0EJZXWJJOW0ed9zcXkPdQybg/tu+U1k9Lr3RKaktlDaBKM7MU8R5DvH8hIjrAKX0qwO6JN7Nyk/UUNlhAUeZnJJedY6uEVkjQktud5QzmP0y0iKhHfMpZPWFLqwu25kMnNCU5LprBavUlWR75M6puaJPgx7isoPxsyigi+MFBBFdVHCSY6MaUzZ8wnc7KFQeMLhOjkBvHzdTNGyVo/rZORosgTUZviJqfNywH4hbrWmqwD1WfVVrgQR6VOhKWIrWpFLpRAZOrO7Bl4f7OXwMLcSzSnO+XORkyPmrMaGlukz5ptueIkxs2xv156Y3fVTz6xK6wpaQOBDWkrOkq42BaMa3MMQmsEWiI8jyPeTY4QTQR/Dxs5MzeHcafTVOfcroY0HbeZP3UbUS/p7RRWCmztD3sChS2P7QshsNOQENqB2TCx69nJgXR6ST/kB5730eYclKvJNFqrFwlBuWTHe9PTl0Q+7blTWpVMk1xHNzsZpE84NFQEZ8MJwmkvbxkftaXMhzKc07aZNKRuJFW3nsr49cSEmUwd2INhMHF1OpmZubt1yOEmpCXqJMFulYbMLdvhclqBMthwxZkQpzOS7Ae9gFkuoakTRiUXaaeBbzshNKL7IZLzbVyimVj0oy4E0hDstJzd2VJK1+aoriYCD46HxiQOsVTXB6dqr+o1vMH3jcKiRj9mV1IyMas7ZNrkRaOA+juWkNB9Yl9Y6Ca0NENaHaILHnsdXHfNl3pGnZbqvdmj0kGhima1senCDXhiv85PrHUfLkp1cbiqFS/T+sBdbgX7+Nc5Od7Td/KUkWqSORWeyDJ056FcUyJOaSeI2FkMUdyxpQ9dG44eg1u5pG9pMuxOhL8+0efKm6hTSHA7XSkl3VYPWSHdJ4eVc2HSGSFCmztCbkjdyXhjdNUSD4/JkPk5t2O1YgfmnBW+UzkSo21RSGXnwFmseCHum21nwDBx4Vya7EDmisy6Dgd1UIhYCneydefyASQfPav5GT4fulG97y7G8cTCS9k24XZfJcfTXZWq86m1Gpeymvp0Ox2vx92eXEnZPl7SHrvEvZUu4Bjr1xSMYogmSFkp7dWhI5eQn8ejefdOh1tEqXyLEUOHw8eY0pxp3wiHbH32iauZTvGojLZoub5l1nC+3BTQPtgcmfspTrc70phOplu1hr2U0lJgjpaD7gt4Obiao+T8sT7LE+9WZD6tGnZgc5kSyTsa3NZcvmrr84lmKv3aGQ5o9qVyVh1mz6uVf1taO/6EGKc0SZnrdr+xgx2GtUEKydoRYdmLrkp3CyN7LDuY9zjqvX3sxzHnN/ZFd1aijWeptr6sr8z9QGYy7Or5TVxbW7mEm2ug+UjAbXnCNDTuONGtMCYGph7NmnZQLnTMZb9tsbUsX6D8apKeRMQXGmDgBDfIzY8UiLMsLuWQiM9WmgLhjh+swIHnFFrDYT3s7ngiFAVx0qYBbZf3PbOejog+hBEL44SKNhtOCVk8MTXd25sgx6oeqowwCAp1uoidoVVFYBCBrNDEqRQieTUMQZs5660PI/oIMSF98E3BQ4/dqmQU8Sx4l0lE8KuCLi3DbZqMCqG1pt7z5OCilslWebU7WGrKgWZRkqlUFLs47cvt7ai119OYNNtTboos3QPd+80h6BhTOaMYEQ7ktFeyIKW3Ej4scwRQAmosydsYbZbCyjJ2d4P08pa6UJjMcmBmHxyEHYKsmiYxv93j4L6P1bxA7lFRo8sOPl+O266JDwWtViSfnRLLT3T3LHe75AqftqZiKWs/0slit9+TXhDTHBoJpYiTbbS+gqoPoy2/GxFquQz3utxez+aRYNE1aEWSOdFisvM2qT4oiMydWtaluxZBmM2SWun4KjJ4RlUzG+6G4Oj3jNddKzY4nbaaHcuFgXarWPcy8SaeWafSL6F4MArmIG7jUNYVK4zHfSTxpbLF9jen0RLSabapSKWoQ9VVlU8Xd4caih/6jCQmrddVl8njdL0RcXO906cWdpkbPkApeTrF91KJklt3kfacpB+PrBLAgGHijYZm3cTz0o5jOtZpEk/TL85NTcXpIqNLLm3yCZY4RXREo9uZVcLxS6/G/ENj0Ntzzysmfxls2GJvm1FlnX1DuydS5RJkN6wzUM9cpPeddaO7TWlxhz44QumRSdKbkm9Tv06ByUwDM7vNfbJvglstxeQS2QYdZAeASyaTmbfs5I+qREYUIQ2NeSPleEoAewybOHJgctLUGAee2cp+OghSWxnR+jDyQZPE3KqfUElRSvag2UqDMeiwEWjSGANwNG2IJeb6d4N2IZaunL0w9hlp20F/lKaVPB0aMT96PqWwR38D9baVOJ5AHxsPnVrct2rUs8wDjNl050ZXxKOFWyC3zm6zgQ95r9p5cdunLuFMQpDlLrsU8Mg+brFhsA6bjl5lreO6Y1iRtszq9DrrwFRZJXvL2lMOS8QWcT05dcZcnHbr5AfJg0tbzCWeYOxcldYFfF26q1ZRjjQGr7CdIfsGQ40crzTeVUijgKlyoWvP2yCyEQAuXUX5d7bf7Q8KpDY2Mgr51GwZXmODGgvi0y3cOcRVUs1NWsstCmmHhKQUCvF04bTnQ/2gMnyFBKtdaXvC1UDd1kJ2J0zeiTSHKcNpi9AdrReYdVtVZ7RmQ1O8cI6Audv1gWktyMF1mPZhLsPYXT7RZeCr6WoXR9lRBXxUtZwsQgBOlUmgNyhzntY0YuaCrGVKkvODqVFqzNfifimMbcFyKGNsYL+oBqSCCj/Xrc24Y9Zwv7v5a5+2rkaQMoORNdLk7LOzq1Pi1d2QobXsXCZ3VArGHIhaQntBnczVuRMgXhG32p26HwjbFUNc2mUKdt2KgW/iUZMCsG7ZjVfXztlXe4zS9tqlJgVHGjLc8jq0TOmDdJYkkyDsTsYDNNxU/jq9K75xjIt92KzIUhO08ia1bLkTLtNxfzgzFNwzhKmZHOoIYiQ58cb3+0orQzQ/dt5p3FHrdUJmNdPbVWK1QRYZbXWySrQ9BvZS6SwDbpiNia+E5HoeEnFI6bUDUz6a9q2QhiohuWjjIdwFUmvxNBiYL7ZeFsdtchjyo8hGLSfRCaaCMXCzYqlWsFBmrziC7W1YOusgIpfXm9AoW5zGffuCRVF1ua6S7U0i7PF6g7L1aYh9glftzFh31hCjdnOTVss6yJltHeW+eqQszIev66IYhcHgZdXZnmoiFidzeYF3sm/R7WgqkSRgCAsxlqhKES3vxot+d7KbN0FDKLv8Kk9GGhl3HsVuzY50rVCUrK4fcWkTaQB/yyDATWt5EvQtJmOO0faNbffdWRQvtnUCqLGeomWyl/vLfouFnF2Ari15huhbxZFhHlA3IkkbA2JXawjFWiSLi8IS/ECKDYm+9Rd+MrwI6XQZMMLNwKliU5P+ETeyWC8rnbXFQS8NYst3m+5GU1WkMnHerAtr3bFWV661fMPIq/FS5aw2pEZ+Uot0Ymv3vpXDg3j1My6WL4nRpR3jnNmNxp8YStcLP7ppvq1e+YMGHY/yam0kNb1xLG0fi+NVL5IY12RkGfY2lTeIJMTCNTtaSDXEVxXptkZ5wC8D7GKksQk5xTdJ35LKO5h5j9TYHCkqI9msFl13fx68rt2I0pHSVTHzfF2Sr+tWmUzSzW6OTo89waW30ylD+OVSXZOrDtpS05nOblO6yeTr0Qw4wds3wfXqba+bNhEp4x4nTUxczoZo0DAT6kXbC0Mh5OrRGQF7JGdO2h3pZbcUyLA5KBYCzkuWMlKGUKnF9dZsY7m7eTreLcmKQsjkZCCHDUTawHfCbzFTVS7QhhVg8w5d6dvq6kLRKTC1pbPZI9HJJptaQ6u6MhGYofbXw9CGohE3e2JHWzeUFfVimGrHkorSLdwb5CEku1xGFibIWHCuRYeplLK8Hvr1ukwEAWS1QicuOovqFoFX7J4vjc06VBKEM1oIrk48jbYHh98jZHBLCnyjIFcSk+1I3qh2XCQkpO/bgbvup8JbqVGe6mf7eKtOAbns4aIDgNOn7egNF3BkWFXrwrntefnGbTT5sNwWQc/LyWYYYM7ANJdRucBUvQRf1v5odFNE0G0SqCQP4GId6WmyxtYej4N5KEDPhLFOuuSSEPrOWpeuoK5cuKF38frexXsw8ckDBVHjyop9WLNv4nJvTkjS1SzqpLfjfYMS1xGcKTensnNvvBNdwstIDTka94KK2yhENSVEymWUmZiZT+sB0sgt5uTR7lShsYfi2doK7lpAV1c9W2tUdD5yPGGfjTFd5koRr9jEw13vGPMc1qtWl0LnAcdcNDyrJGrifsCG6DoX1tuxvWL20UdacbdtUWJ1q7lbENAZ5VQE1Xm8Qlx6dpfFXhG7o81HI7TxW9iB13gMEesaH5RT1LVEV4beoSwodxXKRYx4xyjpOZ0i2lvpShi8hqxtoFIbEb6ngcuKUbjlx6JMbuhBMOv2mLjtPsV4pMsJlx+PTr86Bqom3zwsclfxXQ37nugq1UYGMLKjYyXv0yG6RvAJEIDjaroScvR6hUFrAoEGGx2PhciOeQZBUrTCUrXg2LYf+7riIHfjbRnYxNO6lUzfCW2nc6+JnsI14WxKDarM3ApppOuMfG8jXA3FXFwnOrHXDF4Ex1xq7YgYkpcYW588A5WWPi9dvf6u3MtSVzNpaTaWQdFlePazXuH8cZSTA3MfkusVOoX7JO4PdEgymH9qfd3eRlgRREEYnshDHGCMPC2DrIVRTmZWYXrfc35u6HfykJUpRLTXoOdueui0qyMLI2sqHS3terN4DY5E1ya86Hi9dswOORr7a7I5p1swYOum51HTsTgXEUNr8SFra92XpJsdCE0u6zVvtq03rFjpdsYR80IYsDvemTu69McOGmgUi9OVFORUMHqllCxtvt1iGs3UW5OVwCTElsp1oiAjtmkHv5RM2DlDH15P7D20QBSJ1M6jQd3TMD6S19tQ+XKpuLQaqRtCSSH6CrhedEgfpxUitDm97V3eh88iKL1oIkOl7yGTwrDh4rM4i2mTtORQVjNbXtV4hJEaolB8/65BA5jc3W2vR8H2YmfrqqrOCEScYSage8HDarU6srsADxLhtNpKy/CyOol5VQeOKqBTmOBIqsj5xp/qwpDdIzzJBqYELThAwkiJeZrrx+Ags8NhkapSbWycwLGt41Lf+q2sDuszdqrXB5zPqdB1p+V1UO/A7fNNJrRb7MDe7erKapjcTpCJImLKcbXPHRTf9hylN+tGsRXeYPckTPdNGOpMs9lNJrQsVKbi2DM/hvxWL8dJIq6DiFiBt6vSwMs3uqJhRGemWlRvG+h0XtkJUvc9Svg4sqaTgaBybqkjdxcPpusREUyFIPWi8+64ISCgrvPLEUryvg8qfLq20DHU98yBWkPH+fkR7drnzi+WrbrMRsKCavdUYIzUrfiQkYKDRW+Rll/BGF942Km1Yic7VKdOIwC/AXAiPDItrqyNFVjUm7pSUqNewIJGTgwdpjbjncBoRjge7PkBnHLgSI8IE7Ej4RLq+WmTtBcLX/kpSmmSKi5HeyMMfZ6diYsxxpDI7urbPM8YuIXDdaP1RR3ThXFMCA/DaZYfKiprIk5ZrdUERuCko4ickzBauYalx1Eov/fuV8jpqM5GBzMnNsGWhKpJDgchpgz/0o39YBDYmS8HascEeVbAhbHk+RaDIMUjbe/YmfbSsvjbBNcBmqH7yLUv+D5o90IjrwLlKJHdCXOPVTXK+bJtOeRatx7uo9IRvooOMRInzRP6K4k2qptVSqeOGOkJgwcv4aVDUnsUyrfHe28F7U3De7LpiXWcs5al5CalR2a39g7F/S7AWV8jl4bwyYMhHl2+0rbnsVsjfFisM9YKWFXOSPFONqCr1/HRmyQdCwri2EWiIYfhOuXOLGTaLm+IihL0SOQaIRQhm9OdbPH9mRiGgDmnMZIm6W4S+EiRhZLnZT+CcAScvYMNu+33IqHZ6U6qwnYe7J17iBHt/YB5WIBeu1FdjubFXfa3DiVaDMG8vOhWI3FBeZUg6TUfSYgelK7KwS53o9lgd0Pre5Tb51ptV94k3A1K6QpUP2Xrtemvd7RMgol/vHBJrOD5CBe2T+3WexwU9vY0Yny58ZkdL8vGYCSDDdBN3ZLWmvI2/K5EugMrBHmOecNIwej1yi0vS9GtBipYeddr3WVwX9KUrFVlG98qnjzll7AhtZ6Ykr7qV2jRmjpG3G7kOs/J85pSA8LguUiGIFG/TWVTUNdBQ3hOhj2+sdV42Ob24X5DCk88WjJIyAlmr0FF1Y3f9d3hKmkDFONLpMGRvD01rH2h0GNvaZjvIUsH8VZnJI6Swj1evUgZcqckQ941YwocvAgeSQ8hVNXdMezulM1mkkMM+2WNGelW2BKZBV3VhrWMjakfTT4dlymCmSuyk+J6lcE1mI4ZP5g8sk0FNMUFjijKlcbSS+uyR5271od7DQclTuml16Aoc4NA9Z975Czx/FJzQ98NPIzp7yG7xS+UbHI3CJMFbW105x3D4aO4Ot0SLgO4pmg7M+QDH9utOhIg/kqdaHiVtGrkw2oUKJfytCdauI97K/X1iFwNVIyER7ZZKvhqzfeg8zntNAYVOPlv/vb27m1+HP16qPzf/O3b/Lzo/9ljq+cTpi+/X3k8awzd4OND18f/roG/vHur/WQ27/HYrsm6y+ux1t89tHv/1368MMuanj81+/Ig+/mUvnUv8y+135Ii6Jq2nj43Zfb4ZQvY4XXN/IPOZrbcB+9/fJD6Bwdfj1U/t+XLxflKUsw/WQmD5Llg/np5PdR89xa8fmH1GSPwz2FdzW6/fg4BvMU+wB+wt9//N4Jxa8xxLwAA -->
