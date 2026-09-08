---
name: "rar-cowork-cookbook-configure-define-posting-policies"
description: "Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_posting_policies", "rar_sha256": "a7dcae15fbb065f5ad22ccb0924c74d135c46b0f740671bc4ecb0262ce190893", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_define_posting_policies_agent.py` and in the RCI capsule.

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

Define posting policies Configuration Bulk Setup — Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per posting policy target and the new field values.",
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
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 a7dcae15fbb065f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_posting_policies_agent.py` first:

```bash
python3 configure_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_posting_policies_agent.py   # or on stdin
python3 configure_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Configuration Bulk Setup — Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_posting_policies',
    "version": '3.0.3',
    "display_name": 'Define posting policies Configuration Bulk Setup',
    "description": 'Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '38f25fd54ff67665',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per posting policy target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define posting policies, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define posting policies target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c', 'example_request': 'Use my attached Excel to bulk-set posting policies in USMF sandbox — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per posting policy target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to define or update posting policies in bulk in D365 F&SCM from an Excel file, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefinePostingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefinePostingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per posting policy target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
