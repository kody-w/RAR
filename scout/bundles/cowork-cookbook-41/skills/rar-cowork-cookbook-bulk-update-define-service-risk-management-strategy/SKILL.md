---
name: "rar-cowork-cookbook-bulk-update-define-service-risk-management-strategy"
description: "Applies a bulk field update to define service risk management strategy records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_service_risk_management_strategy", "rar_sha256": "6af9dc941c473b9409c7d98d4ad8bf2afcec1c4ed932dbc2c364b3de908c080d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
