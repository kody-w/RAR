---
name: "rar-cowork-cookbook-configure-analyze-safety-achievement"
description: "Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_safety_achievement", "rar_sha256": "bd5f0e62d9379a58f789d5b6d3a3e270f8fee11fb0922fe917ddefbf8f9c23d1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_safety_achievement`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_safety_achievement_agent.py` and in the RCI capsule.

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

Analyze safety achievement Configuration Bulk Setup — Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze safety achievement target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 bd5f0e62d9379a58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_safety_achievement_agent.py` first:

```bash
python3 configure_analyze_safety_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_safety_achievement_agent.py   # or on stdin
python3 configure_analyze_safety_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze safety achievement Configuration Bulk Setup — Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-safety-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_safety_achievement',
    "version": '3.0.3',
    "display_name": 'Analyze safety achievement Configuration Bulk Setup',
    "description": 'Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor',
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
        "upstream_slug": 'configure-analyze-safety-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-safety-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85730cfa8ec3b63e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-safety-achievement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-analyze-safety-achievement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze safety achievement target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze safety achievement, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze safety achievement target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor', 'example_request': 'Run the safety achievement bulk config update in USMF sandbox from this Excel file — validate first and show me the results.', 'inputs': [{'description': 'Attached Excel file with one row per analyze safety achievement target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to update many analyze safety achievement records at once from a spreadsheet and want row-level validation plus an approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeSafetyAchievement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSafetyAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze safety achievement target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeSafetyAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
