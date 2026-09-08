---
name: "rar-cowork-cookbook-configure-configure-and-manage-search"
description: "Reads an attached Excel file of search configuration changes for Dynamics 365 legal entity USMF, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_search", "rar_sha256": "92b0ced94309a48c2f76fe8e98b74ec687b9fc0658c5823561a1944d93e72528", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
