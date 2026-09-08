---
name: "rar-cowork-cookbook-configure-onboard-new-contractors"
description: "Validates an attached contractor-onboarding configuration Excel file row by row against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then applies approved changes and emits a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_onboard_new_contractors", "rar_sha256": "83eae2576ecad59737d1ae0ce810d5858b891671c3efe3eaa39b6dfb96b6e896", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
