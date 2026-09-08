---
name: "rar-cowork-cookbook-configure-develop-code-of-conduct"
description: "Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_code_of_conduct", "rar_sha256": "66a000829151d2492bc0d6fa7b68b7b8bc48e447c3e316595967eaedab1d1b48", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_code_of_conduct`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_code_of_conduct_agent.py` and in the RCI capsule.

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

Develop code of conduct Configuration Bulk Setup — Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
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
      "description": "Explicit approval after reviewing the validation/dry-run workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per code of conduct target and the new field values.",
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 66a000829151d249…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_code_of_conduct_agent.py` first:

```bash
python3 configure_develop_code_of_conduct_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_code_of_conduct_agent.py   # or on stdin
python3 configure_develop_code_of_conduct_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop code of conduct Configuration Bulk Setup — Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-code-of-conduct
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_code_of_conduct',
    "version": '3.0.3',
    "display_name": 'Develop code of conduct Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work',
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
        "upstream_slug": 'configure-develop-code-of-conduct',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-code-of-conduct',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0db89f15fa10cfe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-code-of-conduct'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-develop-code-of-conduct', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the validation/dry-run workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per code of conduct target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop code of conduct, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop code of conduct target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work', 'example_request': "Here's my config spreadsheet - bulk update the code of conduct records in USMF sandbox, validate rows first and show me a preview.", 'inputs': [{'description': 'Attached Excel file with one row per code of conduct target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the validation/dry-run workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply code of conduct configuration changes in Dynamics 365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopCodeOfConduct(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopCodeOfConduct'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the validation/dry-run workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per code of conduct target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopCodeOfConduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
