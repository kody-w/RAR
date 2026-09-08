---
name: "rar-cowork-cookbook-configure-oversee-active-campaigns"
description: "Reads an attached configuration Excel file of campaign-oversight target rows, validates each row, emits a validation workbook, pauses for approval, then applies changes in D365 F&SCM (USMF) and emits a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_oversee_active_campaigns", "rar_sha256": "c050a80473e0dbd09fde49914b1839ae3ff6d1c52c4058a0652852b5cf3f8641", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
