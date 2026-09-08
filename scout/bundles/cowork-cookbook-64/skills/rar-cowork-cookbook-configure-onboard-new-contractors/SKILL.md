---
name: "rar-cowork-cookbook-configure-onboard-new-contractors"
description: "Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_onboard_new_contractors", "rar_sha256": "83eae2576ecad59737d1ae0ce810d5858b891671c3efe3eaa39b6dfb96b6e896", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_onboard_new_contractors`. The original RAPP
agent is preserved byte-for-byte in `configure_onboard_new_contractors_agent.py` and in the RCI capsule.

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

Onboard new contractors Configuration Bulk Setup — Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
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
      "description": "Explicit go-ahead after reviewing the validation workbook, required before any changes are applied.",
      "type": "string"
    },
    "config_workbook": {
      "description": "Excel file with one row per contractor onboarding target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 83eae2576ecad597…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_onboard_new_contractors_agent.py` first:

```bash
python3 configure_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_onboard_new_contractors_agent.py   # or on stdin
python3 configure_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Configuration Bulk Setup — Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_onboard_new_contractors',
    "version": '3.0.3',
    "display_name": 'Onboard new contractors Configuration Bulk Setup',
    "description": 'Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cc2151a560159a51',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, required before any changes are applied.', 'config_workbook': 'Excel file with one row per contractor onboarding target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for onboard new contractors, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per onboard new contractors target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir', 'example_request': 'Onboard these contractors in bulk from my attached config sheet in USMF sandbox — validate first, then wait for my approval.', 'inputs': [{'description': 'Excel file with one row per contractor onboarding target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, required before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when onboarding new contractors in bulk from a spreadsheet into D365 F&SCM and you need a validated, approval-gated write with before/after evidence.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureOnboardNewContractors(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureOnboardNewContractors'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, required before any changes are applied.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per contractor onboarding target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
