---
name: "rar-cowork-cookbook-bulk-update-define-service-risk-management-strategy"
description: "Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_service_risk_management_strategy", "rar_sha256": "6af9dc941c473b9409c7d98d4ad8bf2afcec1c4ed932dbc2c364b3de908c080d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_service_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_service_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define service risk management strategy Bulk Field Update — Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before any write.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The field value(s) to apply to those records.",
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
      "description": "List of define service risk management strategy record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 6af9dc941c473b94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_service_risk_management_strategy_agent.py` first:

```bash
python3 bulk_update_define_service_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_service_risk_management_strategy_agent.py   # or on stdin
python3 bulk_update_define_service_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service risk management strategy Bulk Field Update — Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_service_risk_management_strategy',
    "version": '3.0.3',
    "display_name": 'Define service risk management strategy Bulk Field Update',
    "description": 'Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval',
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
        "upstream_slug": 'bulk-update-define-service-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e401f51b2b82faea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-risk-management-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-define-service-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field value(s) to apply to those records.', 'record_ids': 'List of define service risk management strategy record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define service risk management strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define service risk management strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval', 'example_request': 'Bulk update these service risk management strategy record IDs to the new value in USMF sandbox — show me the dry run first.', 'inputs': [{'description': 'List of define service risk management strategy record IDs to update.', 'name': 'record_ids'}, {'description': 'The field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many define service risk management strategy records at once in a D365 sandbox and want a reviewable dry-run before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineServiceRiskManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineServiceRiskManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define service risk management strategy record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineServiceRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
