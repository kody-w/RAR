---
name: "rar-cowork-cookbook-configure-oversee-active-campaigns"
description: "Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_oversee_active_campaigns", "rar_sha256": "c050a80473e0dbd09fde49914b1839ae3ff6d1c52c4058a0652852b5cf3f8641", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_oversee_active_campaigns`. The original RAPP
agent is preserved byte-for-byte in `configure_oversee_active_campaigns_agent.py` and in the RCI capsule.

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

Oversee active campaigns Configuration Bulk Setup — Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-oversee-active-campaigns
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
      "description": "Explicit user approval after reviewing the validation workbook, before any writes.",
      "type": "string"
    },
    "config_workbook": {
      "description": "Excel file with one row per oversee-active-campaigns target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 c050a80473e0dbd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_oversee_active_campaigns_agent.py` first:

```bash
python3 configure_oversee_active_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_oversee_active_campaigns_agent.py   # or on stdin
python3 configure_oversee_active_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Oversee active campaigns Configuration Bulk Setup — Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-oversee-active-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_oversee_active_campaigns',
    "version": '3.0.3',
    "display_name": 'Oversee active campaigns Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-oversee-active-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-oversee-active-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cc739e1dbf56787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-oversee-active-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any writes.', 'config_workbook': 'Excel file with one row per oversee-active-campaigns target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for oversee active campaigns, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per oversee active campaigns target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi', 'example_request': 'Bulk-update our active campaign config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per oversee-active-campaigns target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any writes.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply configuration changes to active campaign records in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureOverseeActiveCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureOverseeActiveCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any writes.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per oversee-active-campaigns target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureOverseeActiveCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
