---
name: "rar-cowork-cookbook-configure-define-posting-policies"
description: "Bulk-applies posting policy configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_posting_policies", "rar_sha256": "a7dcae15fbb065f5ad22ccb0924c74d135c46b0f740671bc4ecb0262ce190893", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
