---
name: "rar-cowork-cookbook-demo-data-configure-and-administer-workflows"
description: "Generates 25 realistic demo workflow-configuration records for a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_administer_workflows", "rar_sha256": "d8cebf9a6e9e0a4e8484e05318a1aa654573b2ebd3af3d73ae3e717c2d148804", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
