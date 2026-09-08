---
name: "rar-cowork-cookbook-bulk-update-assess-product-portfolio"
description: "Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_product_portfolio", "rar_sha256": "ccfb74592f52ee89503eca93f4b7a0a271b8635fe0c59fb43aafa1f0f23788a6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_assess_product_portfolio`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_assess_product_portfolio_agent.py` and in the RCI capsule.

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

Assess product portfolio Bulk Field Update — Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio
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
    "environment": {
      "description": "Target environment \u2014 sandbox first, since this recipe writes data.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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
      "description": "List of assess product portfolio record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_product_portfolio_agent.py` and embedded as the fenced Python below (sha256 ccfb74592f52ee89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_product_portfolio_agent.py` first:

```bash
python3 bulk_update_assess_product_portfolio_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_assess_product_portfolio_agent.py   # or on stdin
python3 bulk_update_assess_product_portfolio_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess product portfolio Bulk Field Update — Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_assess_product_portfolio',
    "version": '3.0.3',
    "display_name": 'Assess product portfolio Bulk Field Update',
    "description": 'Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa',
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
        "upstream_slug": 'bulk-update-assess-product-portfolio',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-assess-product-portfolio',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bdf27f062020d9b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/assess-product-portfolio'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-assess-product-portfolio', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first, since this recipe writes data.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of assess product portfolio record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when assess product portfolio records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to assess product portfolio records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa', 'example_request': 'Bulk update these assess product portfolio record IDs in USMF sandbox with the new values — show me a dry-run first.', 'inputs': [{'description': 'List of assess product portfolio record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first, since this recipe writes data.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across many assess product portfolio records in D365 and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAssessProductPortfolio(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAssessProductPortfolio'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first, since this recipe writes data.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of assess product portfolio record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAssessProductPortfolio().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
