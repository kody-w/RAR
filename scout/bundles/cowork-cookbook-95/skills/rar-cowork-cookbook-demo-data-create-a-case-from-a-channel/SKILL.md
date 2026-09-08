---
name: "rar-cowork-cookbook-demo-data-create-a-case-from-a-channel"
description: "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_a_case_from_a_channel", "rar_sha256": "e098a5645d8f82bd0129f54143556909bacc21fece2a840a1c6a0a69b98c5927", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_create_a_case_from_a_channel`. The original RAPP
agent is preserved byte-for-byte in `demo_data_create_a_case_from_a_channel_agent.py` and in the RCI capsule.

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

Create a case from a channel Demo Data Generator — Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 e098a5645d8f82bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_a_case_from_a_channel_agent.py` first:

```bash
python3 demo_data_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_a_case_from_a_channel_agent.py   # or on stdin
python3 demo_data_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Demo Data Generator — Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_a_case_from_a_channel',
    "version": '3.0.3',
    "display_name": 'Create a case from a channel Demo Data Generator',
    "description": "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6df4dc91c227fb54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic create a case from a channel data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for create a case from a channel. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-create-a-case-from-a-channel-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic create a case from a channel records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo 'create a case from a channel' records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo case-from-channel records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for case-from-channel scenarios in a sandbox D365 F&SCM tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCreateACaseFromAChannel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateACaseFromAChannel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-create-a-case-from-a-channel-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9H4fqiqi202gSTf6IgR+yIEYhGSyh0uVrHvIKCm//scpPd1VXVX3+memE8jhy0E5+SeT2b68OsHp++isvnw5YMROMWKd7IsjoJm5RT+ii4fZZOCrzJ1wd+VVxZdE7t9Vzbth48f/KD1mrjq4rIA2/mgCBqnC9oVRqyawMnitou9lR/k5eoHD9zogpWz8pw2WIVNmS/XkVMUQfYDWO2Vjd+u4gLcbQFntxxXDE4Sqyy4O9kqKLq4m1Y/+kHo9Fm3sgyF++njqu2cO2DXRUH+3Fqs2NELstUi9CLvx9WL7WvJx6dKTdD1TdGuAseLVkXweOP9Q7uqmjh3mmmVBtNnoFwwOnmVBe2HLz//9eOHGFx/+PLrBy9zWnDrAwO0YpzOoZ8M9jTQigNK7emXSmB/5hR3sLCagHUL8LsKmrBscnALaLF6+/VjG2Thx9V//mf6cJp7+9OXr8Xq7fP1w/JH74tF+FVXOm0X+MB8lePGGbDG59U+ezhT+10jYDngnOL++bXzN0pltfrL8uzHF5PP96D78euHslq8BVz39cNPq7IB/Jp+uf68UKl+/OlzVj6C5seffqPT9m4SeN1CDEj9+dvb7zeyYOFvS+Nw9c3QWPqNF7BxXAWA+O/0Wz4v0d/IvZnk22vxj2X1cfXnlBd9/gLkfYWfC+j+OVlgA7Dzw+ekjIsf33g05RAUTuEFP/70z8h6UeClS/D+S3R/fhGOAscH1nozCYjNxQV/XUFvun2n+c/ZViBg/h1NwPJ3dt8N9c9oPz37d6SzuACJ8e7LPyX3Zxugv6x+/qe6/XcbPq7CryBtsngAcedmwZfVr88Q+fkH/7ebP/z1b4D0/5GMUfaN96TwLXeKOAza7tu3n39on7d/+OvPP/QViOLAyb/1TfZnNP/Mrk8+f7Dg26of/7gX8LeKtCgfxep7Dq1+Lav/0fzt8+oMYM//7X77ZfX7TFw+0GpR4p3pywS/y8YWyPo7O/704W8AfAqgTe89HwP8+I//WCmx15RtGXYrwyv7bgUc3MV5sAhvRjEA0ifkAQWAXdsYGPZtHYj/xcOLxGW4+uV/ek+A/+S9ATy8gPU3H+DatxdyfgMXANq+LYC9XL/Q7ZfPKxNQL5v4HhcAnvW9pn0tABYX3cK5aoI2aAaAVu7UBZ9AUn9aLhaI/uVfY/DtSetzNf3yxOz4hYE6LS741/ZZ8HnR1I6C4k0vD2B/MAZeD9hkpQdkCmOA3R+BBdoyGwB+LlZp0zjLVn4MEAZUsOlVD/riy0Lsl19+cZ02+lq8ABtfvUpbC4MF38VZffoElAuz+B51X4vAi0Bl+/VvP6z+1+q/2/UkvvDQQO148wuQUDLU4wrkWZ+DZUvtAwDv+E+//Pq3NxMDMqCoroAX4zB+1bElH9LAf7e3Iew/YQS5cgNgZ2DjvCqbDlSBVdx9Xonh6ru8gOnyaKkTUdl2oC5XQeEHhTcBqg5Q57sli7IDRbiL23D6uOrb4Mn1F7dxniLmi5O6X1YKrYGqVGbgn0XM5yKwuSxiYP7v0fC6D4g0oMJS7yQ+r45LZK4qp3GqqHHeeITOyy+gGr1vB8SdpUx/LZYKHCymeqbJyzz3peVYeoynSz8tPgc9Sg4w4dVMdO9rnKV2ms8a2nwt2rcUcJrgWf6BKNPq3sf+Uhj+6y2k2qjsM/9pPyDpQunNC/6bV54xSP83fc1qaRJWS5eweuuNljLbYwi6Xv3/1CwtdtjzvM7ye5NlVuzR1K8v/yz94uLHV4u5SAWC9JWLvzUy72D1jtlfiywGwdZM//Va+fTq25oXDvYNcIK+15/0QUgB/yx0nxG/RHDTLLnifC3eiwPQZvVEQuB0AA8gfZaofWe4PH2XNAIYsPz+rVF403mxB4jqVdW7GXBUGAS+63gpkKpZsvbNrSD8gyWDH1EMLPZ7rRa3AHsB+isgRAzyEBSQz98B+/X0XfQ/bHz1Q8uWZ6/Yg6RtngSAHMEi4OKpR9wB7HK6V3sO9PzyJALUyKtu0d0FaQM0fd0MmqDu4zbuFoh82TWoAEh/Wr5fmi53g7ECmQKMBfKh6oF1nxm0gEsOuh0gA4hXkFB5XLyi980IT4JOvsABgNu3GHpRfN5+Uyh4pt1Stt43Loose5ZO4C3si+n3qGH+WZgAevmy4sn37yPtO7eF9oKcLUA/wPH96atl+Pyq+q+2YvVO98s/zD8//nsj0rOOW38MgC+rqOuq9gsMv2rve+n9DHALfsnaPsvwp6VKfnrl5CdwAaDg02KT5foFBX+g/lL8y+rfk/APJN4y5MsK/Yx8RpZHh7cIe/sAg9CfqOun9fL0a6EHv2ErYF/mIMQW902g7n8vhO9LQDW8NwCfwOJXYWyXevoAJfxZCYAvvha/D/kl5RY970uItuXvoODZEYDwf7nue8ECj4oO8PaXXvIeLCPcM0Ha4MOXos+yjx8KEHz/0ui2lKV8iex2GflADoHmrIuD568nUIzdcvnH8Vd9XjjZZwD7AJSy9vfR91ZMlmL6uyR5qQnU8wCHjyv/ib4gMIGaC/MlwZwWRCwI1kWdbqoW+V9T3tIXPvH+2wvv/1Eg45+WBoB9HWg8gu7visR/rfIedAaLOd0ndvivpvNPmX/vWP+Rsw0ahIWJX35ZauXHNxgC32DKAHXmfWAAKr+NcM+Bu+jBdPzzMqwsPnhuWS7AHvD1fdP3/3dwgw9//RO5Xkb9Bmp48SdeEsoHAC+AKs9K+15KgazvcfqbSTDipz9V/L1gfnvF099zeFXVpdouQPmM2GXhx1Xw+f559a9l9icMwchPCPEJW38es3b8EzmemgIQB6VwMdpv3vjNJuVzmltEBjbsXv/58OsHENjOIsBbaL+NA2A5wLxP7dL6wCD/AUPw+5Wp4Nn/5aDwRqWNHNCiAjIBsts6BLkm/G24xVwfQbFdSKzRNU4Q5A7ZgYrqYWgYeAHmbNeIg3qkgzjkzt1tPWKHbQC9V9Z/W7q8eJFsEQsY5BMAjuC3x+CW/6bSS4XFXt/nkkX1N81+/eCS6yUu1q24f31oGEJdEtu4huRCDRmUxIk6yMZRJy9GwZFdy/X41YzdPbEXN5qLHBOSOt3YLM6nw2043nVmr82sprLbydwU5+P5JvGxS3tzfkNuLkXt2SxDyc4gQtU3bp4/Um1A7Ni2CilhHelGox1xY7fGQokRbQmX3ThS4Z1iNbmXeIfd0YPVsxbODnyj+UCjrDvL+hx/suJK5Xpv73McqTLH/fbAGue1PURSzz7g+HYcBnxbX5sCu068qcQVfo0SOTvDXBUmI6zgB+R8tyoX5r3+zLtFVovpGqYC5qG2yJBhGanqt9o2z2myZ6MsrhuNztmdqB4N1UAvXdvp0k2wZziMrZ7YPhymRINhTolQuCBrTecLd4Y8OJgkZmyre3KqHtf5UeOySbSmSTftcER5KrEvkFI2le2dDnFcNkY9wYJn6so9zG5Yc5fLOuOvInU+0fyNTtSkJa8DtaMS9oHJCT72dzPSROhB4dBjdzuW0rU11JG7KDEUHylu5LMx9qvCnnac+4BC/jC7iLodTJko1obBoGGa2vt5GrKEQzpJnC5aQ0mXOx3dmHPuGBKnZvKF38aG0gQMmTLeXer2JydmI/hCWyZ2vzgFHuWBvVMfXqVLecwk6DmyDCOai/valg4cDzW5OrX4/rBtt3Z2zY5JlPA9BeeEjZDOOdS7OA7iaIbs9szpnKUd3Sk7Zml/G04SBulCW2n5aZRpOu+meqItBkq19DHb174TRhFuj5xBdG1p6bdDj/kxHF2dHaRdeQW7h3WNi61wMst9NN1UMRyb4YAdk/U2UwcljqyERs6Ga3Wn5oR14v7SSM0ZPss6U6tp29EuJ7e3bm07N0tgG/GyriaYTo+oVBLm9n7cVupDuRb3fm3ww4ODkHtAS9fCE/MTctBa7MDaCYQd3bXJz7ISdzmCFXv2oezmx2BszqfRTmcJn7xozfNxwUP0AWYI2suZIe7Dbp03pgezBMwV1o5RFUoLAxHajXgyBxiqQxHEeuZIbEMtVTcPr1ByVK/rU5aSeEsnBpauW58UxW18b2IyvbUDcyHHxzVShDWdsNalcRgT2qNcbPkMP2+kFooFZyOJ4mB5ReIwXU4iUaJIbGFYkb7ObvpVLce9e0ePasmED1uKLgI2sgrMzdc9ttZPlKWM+K09SLAxuQrTmZvj/VbDnnSgjgOuQ5Yf33jNmQzKydLybEwPKihvLFuXwdaJEut2sKZ4R+Ms5KCEkN44bug30bnIvfWRNS2vFp0WLQQoa3kWKY3JiTSdOOYoS+2vh/lAPMrJaK8cttFvAs+IYW8fkkOd0ooslpzFCHtpRs09W4ROfjEZ9DbnBjE5uiqypbjhLfcKIm0X3TcIie8FzvKp9rpPufmg4Ycsl7fM2r81g8NrdiE13WXqw3UHxQmtD0JDPxpd3Con5dq0wuEU3y7dYUe4unzTGV3ctycl6DfbE3WFLmHFcXSMe7B5wtcJ7hvJPLKeT4y3iBIxW4C42jsgnlzyyeZuhaTa3vpp7Vm65t4jR2DiticeCHQVLYllWz6bmE7f8HHvTLEqmycOcvV6MBBvI4V3vMgapVScft5vHztC8sKjOp8h9nqWLRoT/DAUUGtz6SoySM9WgGz3m/RYBzfVmGVVqs1QCagO2kkqEULhMdbVbcwl5Ygde0YVt2UmPRR8CLbS2Ohy35h0JFJWolaIaSd3XzOoM+3XVtRacXedBn4MNH5+0FJs8/P2IvJbAW7EMx0f2fPVUdCDdNLrKXZRAvY4k77BajpGdiacrlYb38YdwkaE7Nz7DFGqkjzsKvd896I4fJzk05bTBDFPzx6JT/QWDVrojiLF1ZjPdEmVsY8O1r26VaDECaf0KmGNflLVvgpZ9FxDdqOmdH8I7Zbxdm5W0D6VF9NUZNpRC4d5DYWXDjJq2pymmdNKtr8gztmRTKiadanDWyuIJz3hd/VY9DDH0pC9bVWsiWhqOO96rewZbTPnECOl8O56uO2gCkJlE5fqUnVuBVJjorJ3buwAMRgRQAUb0WcsQY1SZkUC2+SPMM7VsnZdjXJjJ3Z9cdS43CYsKx0NxNkq3KY9duJYnUv4ytYMEqHcTb+fDqyYQpFOeDTddLfcIts7Q+NUdrirJtXTmbsztrkKMGjYHVuCJFTFyTk6yjsm3vXbA+7d1Jt3HrBKm+FxOpE70hbSMiz3YBliZSjrIRuix/eUYzReP46b6BSPBzxeA5ArDb3eX47kOmxFWvSNjljXD9rsh+AQblzIQHiZs3iB9i6ebExyESGbeidfcR5eu+W+P9tSJxDu7nh2qiucsoe8CKgi081UutIusB3UWSJ3GkyOf9hOjDUiXYuGhSF0G92mChJdGB17WOcJi+/9UMeMWeR0T5y7EWKsyYI5ZxTIM0V1R4aoNPYiTzLrykFG2NebIddWlla9uN3vHxSXGVlNDy6JII6y2ew7l95Xrfk4jRliQWkvns1WNx7SicvMoN1Z64d5H4j7FdFp4iorjBsjg1mZgc6ckMvNppEEZmpM1rdV6D7s/b5M1KCGJTHzUFe9OmKX5U4GiZxm1jFIL6l/0M6AFIxc3QYEljIw4G7ni2rJyCjJjnxT5DaimLyw6RF0RTInkDWdYYe1zT/0axt7eoteodRnNKqmQmkL7TLIifXoPuSSORV3ZWD8Y3zgyjqaraO586oe9FUJmu0N2NpyY4eNR+F0P5K0IOfdAcOTGmLmYg9jrCXJNK7ixDa4zFHdM0eYii136TjutVwMJzcuvb6jqBo1rKNPKGLKnh8zfT1YyXUPaWdDTrPCaTOCzfe3pUUi81x0uHye8JImSvog7y5q6t1vD/9AZ4JUTOr6TG5IbK+OSoHVl1vFbSAILkYeYgVKUupZkHdFKzApTxjp7cCsxSzI1wnG1oRstnBAr60rxpSEayUJTqbXJBGtgjLmoFBJAuUv0D0hKNp+NFIs67cSPrDuSUimHDHPWXu6eEdMgGE8NqjOthkOEyaykHn5GpIBqDnSJi1Va9y2bHYe2WxtnEKCu3nGTj/051mBNYQQCVOt6BQx2Ey8dOWZIfb3Wj9LhKPUdzKRL2zJkcWmd3Frb2n8rRtU1UH38C6ju6w4Yw2JuLUFcQcKHktoLdS6SMtna5+015igRF1pGX7NPrjj7bBdN+K9N5nwIhq1pwjjBh7v0alan09JWJ/tMDbwmDPYzVU6sEJ29dLk4Z88VmXLdb0O8O2hwXjWsDZns3axKE6TU+msUyhIqpitLzEx0Hunjuh8X+W72Cjj6NwYNj7EV5vDt705ptC2SIidWhRzEV7rg0kQG3vrb84lXyeVNdmwNZJk3bs1vO3VAwvNhtplXEwXh0iqs7ugmHYgD2niEFcv9i3f2hwKXjl4+W0fxLM0H+M9tZ+iMw2LDGef7lxyuVFrNkVz53y9N52W59yJO7Fbq3/4DUKSpB2p4mF37yAZZg6TK0loFMoPbasJXs6a/CGaS0ba5JezUE/1YW0ywYN64M19OmtocnLEwqrxcyMUUN70VaoVBOL3JgfBEAERgYnhG2iLZOuJrec5bs8svLUFiqRaUMbijVvd6hxqILIG0JeawmN9bZwTCK/ufrWue5rnOYK/HgQsnaIT2vpdrRz9WgzsdYbi3tY+IAQoRenmXMSU6iZtcSvbYyoIYXI80RBaUg/txMpRhdpeUdByW+JTU4gBW1182Kd0BRZuYPoMcSzz1pujQztFVB5ulpjJMjr0hWMxUzzWyq0uoSu/O9fOrQvjuIqPWxTjD3ZlWoSFKTgI+DOf5/Xm0gZ6zvTZnKFXIq2xWKGSTTGAlK57w7mMlrYZO4gTsjFZH8qHSW7JxxzoF91FQBN+dMWMa9lhpFtvHKlJoVLeq0/VDAZjVqZZUB/P0OlIqcUlsMycNxKU2OM75bg7GpJxC/rrLmhPwfksCw1rov7JjtJNv/ENnE7sh90UmeqEWzqw62tbBxvT8m1+S5PX+G4Y7tk/Jb74GKtLHylq4vAjaDuCuonlULadLq2UmrtTg6dxaa3kIHrqjFL23swRZOcMdMh5Z9u8bGwTv5Ckbx4FphppTJRo3ciD4cDOSWjaJUJZW4hm+9ne8IJPRfpQpLPiCO4JUeokVdoJtU7+ZO/8LVmanGTQ3XBPhbYJWy6/khFu1Q6UR3BxmsV1TfveDjM6UlbSCz80ZxXPhwY3WK3SAOq7+Z6pqTuay2xVzQMol0ozbpRdDGJprWVEpgF3PpqcTpTt9nalcpbh7ge6k/DDSczKxPXdmyprm0Yp+C70JkZDYC2C9wQpOXAppx4lbAwSJc63G5IUCOpkqjYlKIMBXGeO56nUFFTNCDPCKWHcMbiBzSTJxVWwixFJMMLHhfcU9FoJJd6EJQtVlHs0LLvYQuYY2Ppw2h7r6zE50rAXoN1Mlc6GN52huF7Xs7Nrkl0/qJ6j725Co4dJMcw5wCrhmts9RG43sVxJLa2DoKhwQmtOFolY463bEuvwoWfjLA6okV8u1wHgAHNpUvTIIyZq+nGjQpcaRdyNcN/Up2Y3QDeoZJFTdpnLxKNKvJqMMqKoxAx5bQ4GoyAC3eBqqOPxE5jAC1Ij3Eh2grNboZC/BQvsWx9g4zXThi2bdY2r9j16n92xvzQztVU1yTnJ8rZ/IEK5Fnpeg7MZh+lww+ueBSZ+YQNZ8IRfOY0ZgjVzQTeMfSoP2r1A0mCnA3wjg3ictLVvHuA6HsQeLs97rWA3Q053xp6OrWNmstrpEd57Q1QUatSjTaWMvWp3apzdSgJD1dFI4TOGCKA/bgNXPoWnmqsvRDXHc6q6W+MatOqe0MZLWpYuqg/9qAjEQc9Erj7ykA0VPbSRlZuyFltiWOvX7ca/5SAWa1BNk/OV3MPZ6M1anzbzYNcZXs6873s+/yC2O65xjrvJF0jrfJAasg27E6KpYCp9xGy6R8WUGQmIXE9km2nJwWT1XWOjaKy2uVY9JHrAZq652O0whw5fe9aVy7vNHivXDuaTmt3buK1co/28s1ssVC/aaF/khyfa5EPcnTtRtyp20Kh7UAyksZ8bQZT2CZrkHIGQ69Q1UgTFrbvfmEdU3/c86bAY5RH3vY3HPDYw2D4L8Uw21IPhhwHTGqfMnotOJmajInCoFZIdtG3NWdNsbt960yl15eRmKhsWfRj9gLByu4lFz5vV4aGokEMPx0ElDCnpMM9cQ7Anrmk11pKevNSycjHwqw0Ke7efQMBf2Onoq7cZm5Imn9ENZFvB4zA7+a2GPEYLjzufsqcr3lzyvtBLY32fBvWuIQwY2njcBoPO5f5ANWFujbO3mz2ud83mnHdt4Fh0+yAKuwCtMJ0XOe0vE7SbmmZBY3jl3R83CUuVaPSBJLuwyxLi7uzrg3zvt/vZ2QaPvSYJG8JDjPKKpj5XeiKUbMSh9vWDbG4q2zIG70ERd6zFjzI/bl202Wz6ui3yW3jeVHPR5LacNFh52wwmhE6bbs8V6/h2gJ0+FrQZr8YjJzzms4SSWn9EhhrHocExew1W2wOpHpzoMaM2eblEfpBNRwSdSCuet1I4qoSTiC0TVM4VvXHrcdPYJZhqK2Q2KzYBBaCFwm3Azz7Rb7xhJq86kR2k2zYkWIS/lrI1eRF5z05DI3hJE6VsiYIJRk42iDjHwrQdkL1k674YQYHDij02wxfkNMdbT79aDzilc4QTigthPVApTYRA1XufB3BRXFo7msyRGEVtrLgaPzDnrZVDawMLrXz0W/4gqNw01BbK76dwo18QN1B2sHtirky97iUFpxSxvll7zMf2AlYru5xpwyQyStjs2FMJF8N6Ex3znXPsQbsjF1uZzpoA6WdzY+4K+YTk0JmWenMfX7gcHdyukxUPz7rKRlxlc1GFEbRjkks5Q3iaJW6n2mPeWDw2XUc+PLUJhYekKQ0zKqjQhi3yoIQdJDU9ggqPmLGWRaTNqd0xlGG/kzYbEDIGfp4mZyd5UsmuOwYpKMQFTivcObCFm2mgR7qFJRVRVd+uOnG9C+ywswkkhmwExkvlIcGmZXU+UUCcNTCbDDdhP1qjO/NWX2HfolLQr5wNdccxAwCTkkM7gYHhLFRN3GxPwi7TB09yESYrC2vdun4XkIXK+64/kZhXQpJRzdI65NIBnRGpx4+SbzfoXrGhKtY6VXZ7+djeAIApDAdCp6DReouvox0m5WM7XAeFSTHXvxPuZejwSVGEwaAkUJqvcjqm7iUI1Hl/7JoWCtacIyjBndpfNc+LIMo4MKqoC9dxi+L0Y6/iernFJ7/BtujGP52QWQOj9X4HqcV0vJX13HQDuh/qqFKOveKfdnG7ZdBLZ0NqW5NNLzXEZBKFpFv4xTnCeI+c4cZtud0wPIQwCO7zQJ73bjhI8KkPqD0uPORrMMgPe9dm2SM96/jFtLsJqANnyBEJYeYu51D4aHGnv6LBbINh78qHQXMcuwvAtCYq8iyQwyrnuy0A+5hByU4KeNLX2HYIa8VHLz18w/ULfnjoYa2KrMY+EGlfUz1hq75U3+VYpatDKW/VA5Yja0XgcAsDYGac0rWnb5CqWJP3zdW0jNQSmAcsU4QkqnODp0lvcRCukxisdBHfkz6MHnaOGembOMcHvrCJ8bDFmVNgqQaA9uFI7hh1LeenHdVruc+pZVxFCHU2QX82hE1ehhyOb5WQqk8qvreqzbaPGqJMUX6y+Tjb3nYaAwrg1WQmhm0sekYvcFI6ML0t6jlrdHY5WvnLXz58/LAch70dw/6bb4ItZzv/z46RXqdB7294PA8dA8f/8uT15d8V7K8fPzReDMR6HZu1WX9/O3r6u0OzT//a4d9CY3q9aPV+1vw6v+6c+/I28oe48Pu2a6ZvbZk93/UAO9y+XV5fbJc3XD3w/fsT1O8KLceoiyZd+e35Xtz75rhY3uII/BjI9Pbz/naaCHZPwGGx137DSeJb0FSLvm9vCgA18c/IZ/zD3/43Yo8tFEYuAAA= -->
