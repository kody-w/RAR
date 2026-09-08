---
name: "rar-cowork-cookbook-configure-implement-new-features"
description: "Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_new_features", "rar_sha256": "66ceefd2efe8f23ac68a99b5bcfc0280d657e1094c8ffb6195aff1a97aaf1119", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_implement_new_features`. The original RAPP
agent is preserved byte-for-byte in `configure_implement_new_features_agent.py` and in the RCI capsule.

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

Implement new features Configuration Bulk Setup — Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
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
    "config_workbook": {
      "description": "Excel file with one row per implement-new-features target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF; sandbox first).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 66ceefd2efe8f23a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_implement_new_features_agent.py` first:

```bash
python3 configure_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_implement_new_features_agent.py   # or on stdin
python3 configure_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Configuration Bulk Setup — Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_implement_new_features',
    "version": '3.0.3',
    "display_name": 'Implement new features Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef',
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
        "upstream_slug": 'configure-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7fd450572eecf62',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'config_workbook': 'Excel file with one row per implement-new-features target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (default USMF; sandbox first).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for implement new features, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per implement new features target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef', 'example_request': 'Run the bulk feature config setup on USMF sandbox using my attached config spreadsheet — validate first.', 'inputs': [{'description': 'Excel file with one row per implement-new-features target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply new feature configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureImplementNewFeatures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureImplementNewFeatures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per implement-new-features target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF; sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
