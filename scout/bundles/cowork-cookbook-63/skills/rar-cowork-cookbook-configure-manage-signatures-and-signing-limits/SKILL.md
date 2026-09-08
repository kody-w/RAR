---
name: "rar-cowork-cookbook-configure-manage-signatures-and-signing-limits"
description: "Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_signatures_and_signing_limits", "rar_sha256": "610230f52d7d53f274365efefcb80fe7814af9626334129d4527a6f53b3b0823", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_signatures_and_signing_limits`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_signatures_and_signing_limits_agent.py` and in the RCI capsule.

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

Manage signatures and signing limits Configuration Bulk Setup — Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "config_excel_file": {
      "description": "Attached Excel file with one row per signature/signing-limit target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 610230f52d7d53f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_signatures_and_signing_limits_agent.py` first:

```bash
python3 configure_manage_signatures_and_signing_limits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_signatures_and_signing_limits_agent.py   # or on stdin
python3 configure_manage_signatures_and_signing_limits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage signatures and signing limits Configuration Bulk Setup — Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_signatures_and_signing_limits',
    "version": '3.0.3',
    "display_name": 'Manage signatures and signing limits Configuration Bulk Setup',
    "description": 'Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-signatures-and-signing-limits',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2938a21af65a0464',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-signatures-and-signing-limits'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-signatures-and-signing-limits', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'config_excel_file': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage signatures and signing limits, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage signatures and signing limits target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies signature and signing-limit configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a bef', 'example_request': 'Run the bulk signing limit config update in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'name': 'config_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many signature/signing-limit records at once in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageSignaturesAndSigningLimits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSignaturesAndSigningLimits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'config_excel_file': {'description': 'Attached Excel file with one row per signature/signing-limit target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageSignaturesAndSigningLimits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
