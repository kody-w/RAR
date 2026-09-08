---
name: "rar-cowork-cookbook-configure-implement-new-features"
description: "Reads an attached configuration Excel file of new-feature rows for Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a bef"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_implement_new_features", "rar_sha256": "66ceefd2efe8f23ac68a99b5bcfc0280d657e1094c8ffb6195aff1a97aaf1119", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
