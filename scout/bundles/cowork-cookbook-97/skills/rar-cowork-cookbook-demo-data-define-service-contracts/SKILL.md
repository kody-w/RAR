---
name: "rar-cowork-cookbook-demo-data-define-service-contracts"
description: "Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_service_contracts", "rar_sha256": "3a0b9f066536e6b57238c894fc660cf5f7df5379f48b606daa5db7d49a0fdf41", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_service_contracts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_service_contracts_agent.py` and in the RCI capsule.

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

Define service contracts Demo Data Generator — Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-service-contracts
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.",
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
    },
    "record_count": {
      "description": "How many demo service contract records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-service-contracts-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 3a0b9f066536e6b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_service_contracts_agent.py` first:

```bash
python3 demo_data_define_service_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_service_contracts_agent.py   # or on stdin
python3 demo_data_define_service_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service contracts Demo Data Generator — Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-service-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_service_contracts',
    "version": '3.0.3',
    "display_name": 'Define service contracts Demo Data Generator',
    "description": "Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-service-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-service-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16fca663841fd0ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-contracts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-define-service-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'record_count': 'How many demo service contract records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-service-contracts-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define service contracts data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define service contracts. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-service-contracts-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define service contracts records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo service contracts in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo service contract records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-service-contracts-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need organic-looking service contract demo data in a D365 sandbox for training or pilot scenarios. Sandbox only — never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineServiceContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineServiceContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo service contract records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-service-contracts-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineServiceContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
