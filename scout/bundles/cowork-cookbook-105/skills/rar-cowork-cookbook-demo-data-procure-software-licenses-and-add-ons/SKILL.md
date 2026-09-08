---
name: "rar-cowork-cookbook-demo-data-procure-software-licenses-and-add-ons"
description: "Generates 25 realistic demo software-license-and-add-on procurement records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons", "rar_sha256": "9aec33a54cfd5f987923cef83ea1c4ad52fc775e0f9a6051f30dc572e2137db2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
