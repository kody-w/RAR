---
name: "rar-cowork-cookbook-configure-analyze-safety-achievement"
description: "Bulk-applies analyze safety achievement configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_safety_achievement", "rar_sha256": "bd5f0e62d9379a58f789d5b6d3a3e270f8fee11fb0922fe917ddefbf8f9c23d1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
