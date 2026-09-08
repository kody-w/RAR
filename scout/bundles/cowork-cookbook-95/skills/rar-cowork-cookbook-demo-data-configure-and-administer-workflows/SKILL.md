---
name: "rar-cowork-cookbook-demo-data-configure-and-administer-workflows"
description: "Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_administer_workflows", "rar_sha256": "d8cebf9a6e9e0a4e8484e05318a1aa654573b2ebd3af3d73ae3e717c2d148804", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_administer_workflows`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_administer_workflows_agent.py` and in the RCI capsule.

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

Configure and administer workflows Demo Data Generator — Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows
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
      "description": "Excel staging file name, e.g. demo-data-configure-and-administer-workflows-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 d8cebf9a6e9e0a4e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_administer_workflows_agent.py` first:

```bash
python3 demo_data_configure_and_administer_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_administer_workflows_agent.py   # or on stdin
python3 demo_data_configure_and_administer_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and administer workflows Demo Data Generator — Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_administer_workflows',
    "version": '3.0.3',
    "display_name": 'Configure and administer workflows Demo Data Generator',
    "description": "Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-configure-and-administer-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a212336ea81d468b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-administer-workflows'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-administer-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-configure-and-administer-workflows-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic configure and administer workflows data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for configure and administer workflows. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-configure-and-administer-workflows-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic configure and administer workflows records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo workflow configuration records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-configure-and-administer-workflows-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for configure-and-administer workflows in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConfigureAndAdministerWorkflows(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndAdministerWorkflows'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-configure-and-administer-workflows-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConfigureAndAdministerWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
