---
name: "rar-cowork-cookbook-demo-data-define-human-resources-policies"
description: "Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_human_resources_policies", "rar_sha256": "6968899e62738aa023c6a886ce09ec4671de14afacc260f4058f4a59527c6c7e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_human_resources_policies`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_human_resources_policies_agent.py` and in the RCI capsule.

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

Define human resources policies Demo Data Generator — Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
      "description": "Number of demo HR policy records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-human-resources-policies-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 6968899e62738aa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_human_resources_policies_agent.py` first:

```bash
python3 demo_data_define_human_resources_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_human_resources_policies_agent.py   # or on stdin
python3 demo_data_define_human_resources_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define human resources policies Demo Data Generator — Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_human_resources_policies',
    "version": '3.0.3',
    "display_name": 'Define human resources policies Demo Data Generator',
    "description": "Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-human-resources-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-human-resources-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c9aa74f82caac94',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-human-resources-policies'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-define-human-resources-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo HR policy records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-human-resources-policies-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define human resources policies data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define human resources policies. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-human-resources-policies-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define human resources policies records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo HR policy records in sandbox USMF, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo HR policy records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-human-resources-policies-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need sandbox demo/training data for D365 human resources policies. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineHumanResourcesPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineHumanResourcesPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo HR policy records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-human-resources-policies-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineHumanResourcesPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
