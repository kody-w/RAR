---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-surveys"
description: "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_surveys", "rar_sha256": "0885b851cf8f0a4b16753393b41cbc213db5bb1ab1b3fe0f67cb79bd5f0459ea", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Demo Data Generator — Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
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
      "description": "Sandbox D365 legal entity to write to (default USMF); production is not allowed.",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 0885b851cf8f0a4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_surveys_agent.py` first:

```bash
python3 demo_data_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_surveys_agent.py   # or on stdin
python3 demo_data_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Demo Data Generator — Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_surveys',
    "version": '3.0.3',
    "display_name": 'Configure and manage surveys Demo Data Generator',
    "description": "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3a3db1fa7af449f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic configure and manage surveys data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for configure and manage surveys. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-configure-and-manage-surveys-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic configure and manage surveys records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo survey-configuration records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo survey config records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for configure-and-manage-surveys in a D365 sandbox tenant; never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConfigureAndManageSurveys(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageSurveys'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); production is not allowed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-configure-and-manage-surveys-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
