---
name: "rar-cowork-cookbook-demo-data-define-human-resources-policies"
description: "Generates 25 realistic demo HR policy records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_human_resources_policies", "rar_sha256": "6968899e62738aa023c6a886ce09ec4671de14afacc260f4058f4a59527c6c7e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
