---
name: "rar-cowork-cookbook-configure-configure-and-manage-search"
description: "Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_search", "rar_sha256": "92b0ced94309a48c2f76fe8e98b74ec687b9fc0658c5823561a1944d93e72528", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_manage_search`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_manage_search_agent.py` and in the RCI capsule.

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

Configure and manage search Configuration Bulk Setup — Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per search configuration target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (recipe default: USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_search_agent.py` and embedded as the fenced Python below (sha256 92b0ced94309a48c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_search_agent.py` first:

```bash
python3 configure_configure_and_manage_search_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_manage_search_agent.py   # or on stdin
python3 configure_configure_and_manage_search_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage search Configuration Bulk Setup — Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-search
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_manage_search',
    "version": '3.0.3',
    "display_name": 'Configure and manage search Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm',
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
        "upstream_slug": 'configure-configure-and-manage-search',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-manage-search',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2f1c8651d195cf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-search'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-manage-search', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per search configuration target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (recipe default: USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for configure and manage search, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per configure and manage search target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm', 'example_request': "Here's my search config spreadsheet — validate the rows against USMF sandbox and show me what would fail before applying.", 'inputs': [{'description': 'Attached Excel file with one row per search configuration target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-apply search configuration changes in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConfigureAndManageSearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndManageSearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per search configuration target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConfigureAndManageSearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
