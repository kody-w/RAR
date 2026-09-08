---
name: "rar-cowork-cookbook-configure-develop-code-of-conduct"
description: "Reads an attached Excel file of code-of-conduct configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation work"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_code_of_conduct", "rar_sha256": "66a000829151d2492bc0d6fa7b68b7b8bc48e447c3e316595967eaedab1d1b48", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
