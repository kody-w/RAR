---
name: "rar-cowork-cookbook-demo-data-define-service-contracts"
description: "Generates 25 realistic demo service-contract records for a D365 F&SCM sandbox legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_service_contracts", "rar_sha256": "3a0b9f066536e6b57238c894fc660cf5f7df5379f48b606daa5db7d49a0fdf41", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
