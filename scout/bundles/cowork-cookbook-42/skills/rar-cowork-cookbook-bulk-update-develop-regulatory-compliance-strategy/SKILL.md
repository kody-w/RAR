---
name: "rar-cowork-cookbook-bulk-update-develop-regulatory-compliance-strategy"
description: "Applies a bulk field update to develop regulatory compliance strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy", "rar_sha256": "24754856e78540267aa37c863d967d38a24792853d24b058f8bc998638264baa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
