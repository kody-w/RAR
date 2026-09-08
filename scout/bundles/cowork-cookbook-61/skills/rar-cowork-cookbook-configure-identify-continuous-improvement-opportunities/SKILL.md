---
name: "rar-cowork-cookbook-configure-identify-continuous-improvement-opportunities"
description: "Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_continuous_improvement_opportunities", "rar_sha256": "6fa63c0e8a0a9425096dddfab6c215a5d9afef9ace07f277943554fa3e0f9199", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_continuous_improvement_opportunities`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_continuous_improvement_opportunities_agent.py` and in the RCI capsule.

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

Identify continuous improvement opportunities Configuration Bulk Setup — Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are written.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per target record and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 6fa63c0e8a0a9425…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_continuous_improvement_opportunities_agent.py` first:

```bash
python3 configure_identify_continuous_improvement_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_continuous_improvement_opportunities_agent.py   # or on stdin
python3 configure_identify_continuous_improvement_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify continuous improvement opportunities Configuration Bulk Setup — Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_continuous_improvement_opportunities',
    "version": '3.0.3',
    "display_name": 'Identify continuous improvement opportunities Configuration Bulk Setup',
    "description": 'Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-identify-continuous-improvement-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-continuous-improvement-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2e35b53aa994aac3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/identify-continuous-improvement-opportunities'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-identify-continuous-improvement-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are written.', 'configuration_excel': 'Attached Excel file with one row per target record and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for identify continuous improvement opportunities, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per identify continuous improvement opportunities target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a', 'example_request': "Here's my config spreadsheet — validate these continuous improvement changes in USMF sandbox and show me what would fail.", 'inputs': [{'description': 'Attached Excel file with one row per target record and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply a configuration change from a spreadsheet in D365 F&SCM with row-level validation, an approval pause, and before/after evidence.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureIdentifyContinuousImprovementOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyContinuousImprovementOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are written.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per target record and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureIdentifyContinuousImprovementOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
