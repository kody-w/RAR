---
name: "rar-cowork-cookbook-demo-data-develop-contractor-network"
description: "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_contractor_network", "rar_sha256": "dcee5ec87e5f64845b846eb68710127c2c0e76c2f7800fae47d34f199c4accd2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Demo Data Generator — Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 dcee5ec87e5f6484…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_contractor_network_agent.py` first:

```bash
python3 demo_data_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_contractor_network_agent.py   # or on stdin
python3 demo_data_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Demo Data Generator — Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_contractor_network',
    "version": '3.0.3',
    "display_name": 'Develop contractor network Demo Data Generator',
    "description": "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e2ade0550ab4b436',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop contractor network data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop contractor network. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-contractor-network-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop contractor network records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.", 'example_request': 'Generate 25 demo contractor network records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training/pilot data for develop contractor network in a D365 F&SCM sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopContractorNetwork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContractorNetwork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
