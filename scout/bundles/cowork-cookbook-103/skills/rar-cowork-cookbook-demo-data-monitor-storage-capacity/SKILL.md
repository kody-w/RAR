---
name: "rar-cowork-cookbook-demo-data-monitor-storage-capacity"
description: "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_storage_capacity", "rar_sha256": "b79d1efea201874628df88fe8e34020ec094e92f41d522db2e4c1f06ec63ef7a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_storage_capacity`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_storage_capacity_agent.py` and in the RCI capsule.

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

Monitor storage capacity Demo Data Generator — Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 b79d1efea2018746…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_storage_capacity_agent.py` first:

```bash
python3 demo_data_monitor_storage_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_storage_capacity_agent.py   # or on stdin
python3 demo_data_monitor_storage_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor storage capacity Demo Data Generator — Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_storage_capacity',
    "version": '3.0.3',
    "display_name": 'Monitor storage capacity Demo Data Generator',
    "description": "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-monitor-storage-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4fab619c4533bea3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-storage-capacity'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-storage-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor storage capacity data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor storage capacity. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-storage-capacity-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor storage capacity records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo monitor storage capacity records in USMF sandbox, stage to Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox demo/training data for monitor storage capacity in Dynamics 365 F&SCM. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorStorageCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorStorageCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorStorageCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOb2JLmX9G8HTFV1bJfdiTc0REDAiQ2gQCBULnCxb7voIWa+u9zkGS76t66fftOzKeRw5aAc3LPJzN9+O3NHYek7t4+vRmhWy22blGkSdgt3CpYbOpr3eXgq8498Hfh19XQpd441F3/9uEtCHu/S5shrSuwfRtWYecOYb9AiUUXukXaD6m/CMKyBpd+3QX9Iqq7RVlXKSCw6ME/bhwufLdx/XS4L9Jq4S56wNerbwsWI4kF/z+NjbIowtgtFmE1zIt+DMLIHYthcTQU/qcPgAqg0S+GJCwfBKoFd/PDYjELPsv8YeEDWYbXkg8PtbpwGLuqX4Sunyyq8PoS74d+0XRp6Xb3RR7e34GC4c0tmyLs3z79/MuHtxT8fvv025tfuD249cYCzVh3cJWnQsZTn81LHbC9cKsYrGvuwMAVuG7CDhigBLeAEovX1Y99WEQfFv/+7/nV7eL+p0+fq8Xr8/lt/qOP1Sz7YqjdfgiDh728tAAs3hd0cXXv/TeFgPmAf6r4/bnzO6W6Wfzn/OzHJ5P3OBx+/PxWN7PDgPc+v/20AB75/NaN8+/3mUrz40/vRX0Nux9/+k6nH70s9IeZGJD6/cvr+kUWLPy+NI0WXwyN27x4AROnTQiI/0G/+fMU/UXuZZIvz8U/1s2HxV9TnvX5TyDvMwI9QPevyQIbgJ1v71mdVj++eHT1Jazcyg9//OkfkfWT0M/n+P1v0f35STgJ3QBY62USEJqzC35ZLF+6faP5j9k2IGD+FU3A8q/svhnqH9F+ePZvSBdpBfLiqy//ktxfbVj+5+Lnf6jbf7XhwyL6DLKmSC8g7rwi/LT47REiP/8QfL/5wy+/A9L/lIxRj53/oPCldKs0Cvvhy5eff+gft3/45ecfxgZEceiWX8au+Cuaf2XXB58/WfC16sc/7wX8j1Ve1ddq8S2HFr/Vzf/ofn9fWAD5gu/3+0+LP2bi/FkuZiW+Mn2a4A/Z2ANZ/2DHn95+B9hTAW1G//EY4Me//dtCSf2u7utoWBh+PQ4L4OAhLcNZeDNJ+0X6QDygALBrnwLDvtaB+J89PEtcR4tf/5f/wPiP/gvjoRmvvwQA1r68gPrLC6i/fAXqX98XJqBcd2mcVgCZdVrTPldgRTXMXJsu7MPuApDKuw/hR5DQH+cfMzr/+s+Jf3nQeW/uvz6gOn1in74RZtzrxyJ8nzW0k7B66eMDyA9voT8CFkXtA3miFED2B6B5XxcXgJuzNfo8LYpFkAJkAQzvzzIwVp9mYr/++qvn9snn6gnU2OJZ1XoILPgmzuLjR6BYVKRxMnyuQj+pFz/89vsPi/+9+K92PYjPPDRQMl7+ABKKhrpfgPwaS7AMuAo4F4DHwx+//f4yLyAD6ukCeC+N0mf5mvMgD4OvtjZ29EeUIBdeCGwM7Fs2dTcA9F+kw/tCiBbf5AVM50dzfUjqfgAluQmrIKz8O6DqAnW+WbKqB1CBh7SP7h8WYx8+uP7qde5DxBIkujv8ulA2GqhGdQH+mcV8LAKbgUeB+b9FwvM+INKBwsp8JfG+2M8RuWjczm2Szn3xiNynX0AV+rodEHfn6vy5mgtvOJvqkR5P88RztzG3Fw+Xfpx9DtqTEmBB0H/lHb86kmBhPmpn97nqX6HvduGj6gNR7ot4TIO5IPzHK6T6pB6L4GE/IOlM6eWF4OWVRwwq/6iPmfuCxdwYLF4t0VxaRxRG8MX/bz3SbAd6u9W5LW1y7ILbm7rz9M/cKs5+fHaXs1SzXo9c/N7AfAWpr1j9uSpSEGzd/T+eKx9efa154t/YASfotP6gD0IK+Gem+4j4OYK7bs4V93P1tSgAbRYPBAROB/AA0meO2q8M56dfJU0ABszX3xuEl86zPUBUL5rRK4CzojAMPNfPgVTdnLUv14LwD+cMviYpsNgftZrdAuwF6C+AECnIQ1A43r8B9fPpV9H/tPHZB81bHj3iCJK2exAAcoSzgLOnrukAsMsdnp050PPTgwhQo2yGWXcPpA3Q9Hkz7MJ2TPt0mCHyadewAQD9cf5+ajrfDW8NyBRgLJAPzQis+8igGVxK0OUAGUDMgoQq0+oZwS8jPAi65RywAG5fMfSk+Lj9Uih8pN1crr5unBWZ98wdwCICooM79z+ihvlXYQLolfOKB9+/jbRv3GbaM3L2AP0Ax69Pn63C+7PaP9uJxVe6n/5u9PnxX5uOHvX7+OcA+LRIhqHpP0HQs+Z+LbnvALegp6z9o/x+nCvkxxcGfHxhwMevGPAnyk+lPy3+Nen+ROKVHZ8WyDv8Ds+P5Fd0vT7AGJuPjPMRn59+rvTwO64C9nUJwmt23R3U+29F8OsSUAnjDmATWPwsiv1cS6+gfD+qAPDD5+qP4T6nGygyVTyHZ1//AQYe3QAI/afbvhUr8KgaAO9g7h/jcJ7aHsnRh2+fqrEoPrxVIPD+O9PaXJHKOaj7ecgD6QP6sSENH1cPjLgN888/D73q44dbvAPUB3hU9H8MvFcdmevoH/LjqSXQzgccPiyCB/CCmARazszn3HL7/FEHZm2GezOL/xzs5lbwAfVfnlD/9wIZf6wNf6oKAPaeMP+t0oBa8OdS8Zf8vvWlf8/MBu3ATDeoP82V8cMLdMA3mCVAVfk6FgAtX4PaY6quRjAD/zyPJLPZH1vmH2AP+Pq26dt/MHjh2y9/IddTiy+gYld/4Zj9WHogwAAg/6m4AmG/huZ33VHirzX/Wh+/PEPob1k8i+hcXGdcfATpvPDDInyP3xf/PJE/ojBKfoSJjyj+fiv621/I8FAT4DWoerPFvrviu0Hqx8A2iwsMODz/f+G3NxDI7sz8Fcqvjh8sB/D2sZ+7HAikO2AIrp+JCZ79X8wCLwp94oJOFJDwVlSAgLbJBeG+XuEkug6i9ToK1yGGwygc+jCFhxQa4UhAoGjgoSHuIxFMhj6JhdHKBfSeCf5lbubSWapZJGCMjwAjwu+Pwa3gpc5T/NlW30aPWe2XVr+9eSQOVu7wXqCfnw20RDwSXXmG6C07MqyJAyNLxl4nXdO8blpPN0KUuxqOKmyDaiC3OkLXfWrczDPfn8arkNQ8ke6qTXiWianN2z5P9KHRmqqBz95mX9tk2x7JSCXM8SRlo6pg6UkstmeilWkIuiO8sI2WR/646o0bJnkpuqGo9dEplUvQwAUEQUw0GbqX3k1VN6almmaCpHOZ6d/KPLRSgQ/PI3vbqty4la85tDlHzXnHQtSqKXDoDFX6kuLkfbCUt7oBt3oi8cGSP0dpAu2xDg6yI73dH5qDN9rHTWpmxE5JnJMUEYQp7uW1n9KbZVFl8jZhWL/g7ZDnZPJ6dPJ10U7EzUnvpDpUS4hrghsRr3fyHoVUcyDX0C65yxyhasSKIoRS20IbT0xthzsRljdIfiiJZnEea1xS+pqItettlKR0kFbyOrjtuTuzPFXuKLRpa5/juLBo4ZxLChFWGU9ouFCX9u0YjuKw8UViN3IKVLKdSPESn1qq0BL5KdcbYRTgUTFbpUWxGtmxxNq57C8H4k4pXRkloqBZhKE7bMSvB2eZNKJt45QA1KYPkuD2sKErDdzYOJYbh2IHh8c4ypl9vWG5QxEV14rbFzu1gV1lumNFuaskUYUPitv1bmocVXe929wEp8Zg/4ZaJc5HRVXCHVf7vuLAV22NSsvqYKyWis+ZSONPhYxYR51nb7YymOdGK7xcgJZOBjfR3b+7Gy7fS+20qQXK1trrdDeHICOFiGPVO1Jcatg4exYcpl7prYsNTsXO5LJLK6H4uN0GNKca/G0H7fdUdOiVrhdul2AULbaxN7UL32uXsOK9a4uXjX3yxja4y4Z/1n2+lEwn8ye71a1dngmnOpmg4ui02f5WiEKEc5E0pZstcRPCdeytdb0XqjRBG4I99yprXpiUIWJqyHwQI+l9cjI3YLrrFVbHtbBHVN7V+GJ3W3KxkIpDdxYp8HftnT1fbq+sdjt705mXD9mkHDCs1C7K0VvWEiJC14DZcUgImSbB1yqrrCrbYE4GMuY2kh9cFK8KM9GZXWkVimmZ/IUgq8MeUpgSOsQGXyyxmL1l2yY1odjGPII/Mbccss/CjXezfLVzov60zWWxEXLXyCV2cyyGGM9yfmDTKxkHK8bZskEkKwfZN9X4MCU8TZtTdS6ufgbJYj+p/CZAb2W9ji0rRTQkdO1zailaa4s0yRd1sCFRNbG2uxYu6oMuWc2NLY7Qntoy1nmlru1z3V82Bxxh3ZJrl/EKQlfJtUwY21RE0r/0qBOLLHN2opDfGlbG9JUrCzV8Zgb05ouBFQfJgafH2HE2ESXCG/3SDlamU2tO5c+ZGBVqnk5W5u4Zukh2h3smTZp7nVrZF4KBufK3g5Ce/HjtL0O3v7ITgpbLerU/u2inRmSx3lSorDTiOkrZzZDXPYlK+QQSM1dya3fiQxt2Su6QGrS63VyqcCle1Ui+wOmmMU/qqWtXa2On1g2BN4rqO/01LmTZhGg45HG18xmNWgqqpbm+pgfLViiGgzNmSWIb66sT9so+p1tflvOdm6Ei7yMF7x8TXV7fMyssGgw1MOaiSRZxLJD9hllNUFnoV8xBu6UQt1bNd0tyXGkKtjop7iYsrWMIrw+rw74Jz6oxSarYmuFl1JerkIiiy/LCHmB5ZJjjXVlHTm4msCTqa3Y9YZm+2bv6CXMP6rWizjJ5YhVvvbkF+N44bzq8LHGJ3zGoaE1r0dtI25vvabznrWoHyhNWODn2cRSIo9Zsth7SjdhuQi18WR1ThucNx9MT7YZjCtJIwropObxK3cKsPWQIwrtu0KVOWBtfuPug8bdMVhC9S0hN6E4xboU80IJhqxpcNsfEWnYXNz4wlzpx9oOKuGhBZBTaiXaK06E97sO9mhWJpRTYlqx4yVUgjEVJ1YQhxaSbwT+XBXPu2JXaNlwNHaAGLknM1Q4ObuUhr0wYNBK0Kgd25R1uiXJvt9QJukgrD8K7peadYTKQyfNIt4xP7I/edO/XhX1jY1YWisvVxzoIxXPBaGG7thgn4VQsRNk1d0N40yOuoj/5h8Yvl4onjca1Adllo3i8u+MubExuZ4S0BFfJ3mkFnult9dBQamLI2yK9uroi3h17klCC3zmqSWD21LWZLLsOrWwzjUPRguH3DlsiFIxr48X2kSOMDtNGv8lH/YZi2zuCbC9lwIMZS1A6yId5GiqvFMPf6E7Ys6lSN5l6kfZbeLMjA69IN7q/2WJiPrLKga7EVLukt8uRZRuTU23rKBWI48s1U2DexepXA8Q4ZiEJbNYQwi2636UqQVctJTn4EsJhgTGsUBS3iUcxVtQ4S4U7lE3IYIVu5qLDmVKKLZujKB5oU9wydpBinrAhBONIcZs2Od+bVggg5DZC+l48bsvE0VFTF3jdF1DkFjJZ01Zx53SUFNdoydz2KgdKu8Q5YYgQtnM2pNYvrs0orGkuZva82bTcJSBhUPugjl57G6bpzVjfFsgR6jaIv9FkwuE68tpEtidtaO16gu+KKyR+v+eTUXROZ4S9CE3rdnnDoO4usTxesH1scFiahvXyYnm2a1y2w8TtOfQ+7Q1oK12qRsSu13xFiw50x/ctkobNeOp4OiHzMaydM6i7uTE5vMOyoqj3VkZ7ze7EIkfeFHlKlh3hsNXVGnVG6BiYmtgyQs0sV/TSTc5JHPV2Umics94uSa7U9ILF66AjIVPRAmLXSXRB1qSXk0MahJsYwwQ/PduXKLx2uGr4GnVk4qKWDziEMfdA3dakv1qrZ73fist8Y7QJlZBCka4wvsxsMUYQ5DCauprtRToxwqtMUjy9NMpzc8dq3dFbeu92V9epGkdmxfCqlXFad8h6qeNMuYZdzpH75lxdZY5FHLyqi2wVSKlkZusYoBRjcyPO7vEtiImUr3Jll6bI3U0vjiEXjTqxsJAwNaGaycWANL+9tgrKGBHfsaTv1fJxMNcGXQPw4M8KbxjD7gYqN70O4WXq+kO/WTXjFcLWpFmrUm71O5gE7Q/pRq6mU0JNTbAmOMsQaI0nhk8ImpKuR2Vsh5NE3KHL1ueO9YRXGnE4Nht3UMbEoTnDRUDDh1jR8VCQvLjTMggbpppu1WR/wyqNcesovCfFfeoqhHL3NynZrGoIP5qhYG23TLLpaR1VdH+EhW3IxL7kbtR8WPp+WciatkfcXOJv03Ia4c1Q2CRdEJYvVbLjp/HJp0i1PKc8UwhFRItmexm4hJYuaGbBKVPd9sQhjEQFNtlCvvmuzunWzToM/TXQPdc4GFXTmdQ1OqeBtssgwrvIOBqa4kCtqlHL+tEDw9A21NtJPEsuZUnyfiQzGbvX687s9xoexwyGmOU1R4yrl+4ciLvdo8HvQ91ut21QZNWOK81DrDFOXpS36yGuL8WBPe+cVlKYK1IeVEYYAETbgoCZ1yZdMxyj8XK/Cym1iI+4SMTNinavVqjaMOpGw2YbaVAdqM6ai3uMyX30bPdSbVqUeDoEV8iZ9BFLzg0kcVmvSy1SrkDZxpSOPwEN1VOzdi8Y8BB2JUN06UKdUoHOD5dNhYnz4GSed8PRQKLM0g6IkdZ3hkaiI3uXl6guHpKYo50qtmNfdk1SpG0dw+oDCSKfMNJdEEyMfTELEtKmAWQCmK/bNaEYrBEzR3bj5mzQHTeGmvMW67XXRriwyFm/FEf1AIum2pErxjgvo12BLi8enPn4sLdTN0lq+cyJvKQil23lH9eEJVhciByNpSK0183N2RTOyQFDcnWW9lSlSgKqWFanLPcYaLuKelmQu+Mw4gQ9BmjOY7567PVhdY8jKbHq0RirRIRODIq7kaWtun5iAKLfL2qzP3EnbNv3Zy873gkjoicjhi3pRts9n26V0SiyG0nlI8ONFG2FBz7Y8VPls8vErfGbyHcmC2lBwhnnNlyudRxychgUsPOx7iU8DnbiNJA4Ngra/pqdoiPaQocN7jbjlHiDaiAH99oloCLx0q5QXJ7NpVgxZTsZLIW3Qr2jTMOqfZE1xjjwEscvdG5ToDxXWoF1vIdjdLzW53tnjHeyWE5LG3INye5wXnZshmUMMrzvE9taD9WA0LIr2CcV7v1tYMkqWfet3q2RvtonZJvCSn8HlTUYbYpcHgYxXtfEUb0eVuhwaV1PcQ4eam0jX4cgY9qhHRocKdQISAHOT9tLZO2jcuhgY4M0kJCMO7k4sbaelmBwzFcAl0qC1Vi1xsrIXeI7jyNDZagPMXVXRhWN9e7M2SR69/ITZp/3Fze8lRsoWXosykwgUiE9lfBUQ0GfL1pBZY6haaXHKyRpx/35gMASYknxfbJJm1IxbxlIyDFw4bVa4iTrbYRVVsnbzTqwcS+OagOt9BNHwdu8DzF4h1Lp2EO1GZQYeyEAaIDB8YzJB3I7Otv+7lBeTGEg7QebkmRq3KzHlYhQVHJ2BVAnsO3eoNdsOniWmSFqdlDJibud+zWBR1evuE7CBfFR+2RXwIH85XQqXbGO2rRjtADvdOzKVuHkDhIULnenZY7EKytQS+UKkuAktDHG8fQ+OK6ndujCgNgKuUagGUGz+Bjkl+a0OdYUihndqqKUSK3v/jBkg+u2eHBx7JIPqBVjY5kznsod6YNw87k94VMXSr9qAQRh3QkilQgVMhyfeqvC1gWUVLV72AYUZl28CV1jVlIbFqOxwopKxN0E2zaBbQwdjHrnbAUlhbD22TZwJHxFn5MDWtA6NTHURhSydVXttqcyn9Ar7qaobJVd4XEQLyW8VeOaWtwxHINjKOFkazTNiq8UfxLi294XaEK7YXkNOumwGnQZI2S9EPhWcZf6shqXkKQ4PQ71yAXXpTUYe0qD02rhWGQSF+FRyo1EhYGoQSokuk1Ep47jNnPTW5giw3ZJbDNIkqrcI/soOFy1rRMo15TLaUTIWYJYkvid7Attkk1OX8s2gqRqX8pNL24u6MR3J7u/TJG7bcOjw5fDilZr0kVNUkPHE4YqTkJPlNGikXrSbuFJuvqCTVyFwTIF/dhwF42Jw2NEKs692wkinSFTyRMwieeekR8Q7JgE9bRHErrdkhKHgnb8RNtYul1eaJUuoQmRDHVn+FHI9saBt6c4kLDMaHhs2e4yarnuzUnTjjLjIEWi3U377p7V8wU0hl4jWB62oddEuY8SJ8ARPvSiII3Nbdc3VUNAuHdVSMWVKxzAwY2Xg1uQyiW+kcOI9jMOgYlK81y1Py0h0N3sCVrbt2fUI48+ssaQ6847V/6wd4kgbYSUVddkPh06OL/ux1poyQvoBEOpco4dQSYEq9wwy9u7zhoNOCKZ1H7cTmdLvvgbMrHLCRPSEkDvaBB8cpfr09lMSZcpSIC0GRG7dCtuQMnEJ3JtXGlN3K2WPmzUDpIHfO0Ly2wlXFpPl6VpVcNH8+JfGSJGe6wTb7e1h1QrN2z7U+lAxqqZqlNBSFmH1t4qOlFdgUm7ncZw02l5p2g1Qi8yeK5lt2bVsZGyakLkcqGOfeVHS9PRMNcuWKtqB/ISbUhKztCmO8FOkeEGlAb3fKmfSsg4dNR+GHCNQjpLK+UjeW4QUZ901j5pXsQ6YTsFoUVQirC+y7CxBE2ZB6YTTjqrOnUwmlORXXSAJpujW0Sdmq1yZUqr5fLC0bLNW0KyNDwOb2Fv2WEHM4V85mBdLzFbHsVddaJO14KpskoX9eV5263OxakP07uJEDdhd22QEq7SZm3Zd9JAzVN5MzLWyspNc0LABM+ctZWO5UdIHPDVYfLpNg8lBeM1QTLtuTmgMbLeBS3bR5fEUDDDg8EIusvI6XorKVIE2CbLlSKxReei42SuDsNFPhxbTUo4lLqKUpqF2FCixTaM7mjeefvy3FYmmD/TfIip01if82yJyc7Et6YnKucsqlE9Xo2UmKMEWVWQvAFBfwwH1xZHJb+Uw+DxnGubNFleEG9EYWK9vu5Fj6ScvVpeOBiMpwlpxK0CxjizJJoL0zeDW4JWP8fC7U4dQjR3wounoZ1PFuEqDFf59uxATSYuW2KCNg2WEPcVtYqu6zNkEOWZGA5MbhSplUoUaA9iDq63SHvaQGEQqSZkRAeN4vSSYrsrUzgXe/DNsA/RQe0CK0CXmF/gdjG11jUIgbe8QCXXqwExseOVOqz4kbwIREbW7r2y+ey+jg97V5Ct1cXNWMg5eSmxNgRUm5iGypA6DFFMuq5NSMDz3rGamt2c+4BHTj29hlWPXNHFGOgpu0vo632DYZwTc+TtasQn9BbJPo3vN8M92lN95wURT5+0XlU6nMXLNmIRNC1VdSRPxjLewTVo5s4s5mq4UmyoMx5CHSktSyiTVJsM2cmyGggZV7cVNVi4jqmRHFHGZbPs+tOtuC7v1maFOzs/UpJYyk/sakROJ+l83PHHPYnx5rkDdWoVQMFWq1cssatWNkjW3i0c+SJW/SSOwYgjHWULyHXVGJDSw93uuGwS9Qb6MBTOGCq0MlRLjZJHqxPUkjU2afihgKv1Hk2EI0cjErLu9j1nHThd21t8zoQVgulgONykU++urKIT0lCt98uTyXlGkPNtQ6pscogKmiuLHYEQ9wSSUu3UUVmQo6DHo0ZotQ87+XDAbtO0ykw5BDFkpjXG7RpHwE4h4TEnYzcJhxi7EPvNyTdggaTBEDoRUYFNvZatJpzXaEzYZaMMM2vzwN/gu5E4cmeaS25dJVq4FvUGZ9JTG/HrJtBxFaI9vKVgOj3ENP324W0+6nqdqv4LL3TNZzf/z46Jnqc9X1/UeJwmhm7w6cHr078i1C8f3jo/BSI9j8P6Yoxfx0p/cxj28Z8f6M3778/3pL6eFz+PoAc3nt8hfkurYOyH7v6lr4vHqxpghzf281uH/fxiqg++/3gk+k0R8NsNni9bhN2Xof7yPAmcz8PSan4PIwzS75fx65AQELgDP6V+/wUjiS9h18zqvs77gZbYO/yOvf3+fwDUfco8Ay4AAA== -->
