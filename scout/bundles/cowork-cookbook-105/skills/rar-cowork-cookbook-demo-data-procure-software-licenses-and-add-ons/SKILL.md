---
name: "rar-cowork-cookbook-demo-data-procure-software-licenses-and-add-ons"
description: "Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons", "rar_sha256": "9aec33a54cfd5f987923cef83ea1c4ad52fc775e0f9a6051f30dc572e2137db2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons`. The original RAPP
agent is preserved byte-for-byte in `demo_data_procure_software_licenses_and_add_ons_agent.py` and in the RCI capsule.

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

Procure software licenses and add-ons Demo Data Generator — Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-procure-software-licenses-and-add-ons-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 9aec33a54cfd5f98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_procure_software_licenses_and_add_ons_agent.py` first:

```bash
python3 demo_data_procure_software_licenses_and_add_ons_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_procure_software_licenses_and_add_ons_agent.py   # or on stdin
python3 demo_data_procure_software_licenses_and_add_ons_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procure software licenses and add-ons Demo Data Generator — Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons',
    "version": '3.0.3',
    "display_name": 'Procure software licenses and add-ons Demo Data Generator',
    "description": "Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-procure-software-licenses-and-add-ons',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3401aff34088404',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/procure-software-licenses-and-add-ons'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-procure-software-licenses-and-add-ons', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-procure-software-licenses-and-add-ons-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic procure software licenses and add-ons data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for procure software licenses and add-ons. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-procure-software-licenses-and-add-ons-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic procure software licenses and add-ons records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key.", 'example_request': 'Generate 25 demo software license procurement records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-procure-software-licenses-and-add-ons-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training procurement data for software licenses and add-ons in a D365 F&SCM sandbox tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataProcureSoftwareLicensesAndAddOns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcureSoftwareLicensesAndAddOns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-procure-software-licenses-and-add-ons-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataProcureSoftwareLicensesAndAddOns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
