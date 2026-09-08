---
name: "rar-cowork-cookbook-bulk-update-develop-regulatory-compliance-strategy"
description: "Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy", "rar_sha256": "24754856e78540267aa37c863d967d38a24792853d24b058f8bc998638264baa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_regulatory_compliance_strategy_agent.py` and in the RCI capsule.

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

Develop regulatory compliance strategy Bulk Field Update — Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of develop regulatory compliance strategy record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 24754856e7854026…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_regulatory_compliance_strategy_agent.py` first:

```bash
python3 bulk_update_develop_regulatory_compliance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_regulatory_compliance_strategy_agent.py   # or on stdin
python3 bulk_update_develop_regulatory_compliance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop regulatory compliance strategy Bulk Field Update — Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy',
    "version": '3.0.3',
    "display_name": 'Develop regulatory compliance strategy Bulk Field Update',
    "description": 'Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-regulatory-compliance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e994e75be773c16c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-regulatory-compliance-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-develop-regulatory-compliance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of develop regulatory compliance strategy record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when develop regulatory compliance strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to develop regulatory compliance strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a', 'example_request': 'Bulk update these compliance strategy records in USMF sandbox to the new owner - show me a dry run first.', 'inputs': [{'description': 'List of develop regulatory compliance strategy record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) on many develop regulatory compliance strategy records in D365 ERP and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDevelopRegulatoryComplianceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopRegulatoryComplianceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of develop regulatory compliance strategy record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDevelopRegulatoryComplianceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
