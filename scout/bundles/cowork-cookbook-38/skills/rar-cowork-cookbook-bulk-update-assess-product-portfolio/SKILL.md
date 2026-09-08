---
name: "rar-cowork-cookbook-bulk-update-assess-product-portfolio"
description: "Applies a bulk field update to assess product portfolio records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_product_portfolio", "rar_sha256": "ccfb74592f52ee89503eca93f4b7a0a271b8635fe0c59fb43aafa1f0f23788a6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
