---
name: "rar-cowork-cookbook-configure-identify-continuous-improvement-opportunities"
description: "Validates an attached configuration Excel file of continuous-improvement bulk changes against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_continuous_improvement_opportunities", "rar_sha256": "6fa63c0e8a0a9425096dddfab6c215a5d9afef9ace07f277943554fa3e0f9199", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
