---
name: "rar-cowork-cookbook-demo-data-track-additional-information-against-a-case"
description: "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_additional_information_against_a_case", "rar_sha256": "678d021f0cd1e666d0ab3f0b1e9903af7cdfc7773f675d00d6f8294ef2acab75", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_additional_information_against_a_case`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_additional_information_against_a_case_agent.py` and in the RCI capsule.

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

Track additional information against a case Demo Data Generator — Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_additional_information_against_a_case_agent.py` and embedded as the fenced Python below (sha256 678d021f0cd1e666…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_additional_information_against_a_case_agent.py` first:

```bash
python3 demo_data_track_additional_information_against_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_additional_information_against_a_case_agent.py   # or on stdin
python3 demo_data_track_additional_information_against_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track additional information against a case Demo Data Generator — Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_additional_information_against_a_case',
    "version": '3.0.3',
    "display_name": 'Track additional information against a case Demo Data Generator',
    "description": "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-track-additional-information-against-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-additional-information-against-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a1d6d67f357c4387',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/track-additional-information-against-a-case'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-track-additional-information-against-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track additional information against a case data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track additional information against a case. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-additional-information-against-a-case-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track additional information against a case records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo case-additional-information records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': "Generate 25 demo 'additional info against a case' records in USMF sandbox, stage to Excel first, then create them.", 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need sandbox demo/training data for tracking additional information against a case in Dynamics 365 F&SCM. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackAdditionalInformationAgainstACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackAdditionalInformationAgainstACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-additional-information-against-a-case-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackAdditionalInformationAgainstACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWJbnV9G8jpjMbOzHjiR3VMQgIZDYxCIEIl3hZAexbwKUk999LtJ7trPK1TNV3X+NHLYE3Hv28zvn+PL7i9N3cdm8fHrRA6dYcE6WJXHQLJzCX2zLoWxS8FWmLvi78MqiaxK378qmffnw4get1yRVl5QF2M4FRdA4XdAuMHLRBE6WtF3iLfwgLxee0wYfHd9P5rVO9jEpwrLJnfkKLPXKxm8XSbFwFi1g65bjgsEpcsH+T30rLbIgcrJFUHRJNy1+9oPQ6bNuYegS+8uHRds5EeDYxUH+IFAsdqMXZItZ7ofIYdK03YeFBwTq3hZ+eOjWBF3fFO0icLx4UQTDmxw/tYuqSXKnmRZpML0CLYPRyassaF8+/frXDy8J+P3y6fcXL3NacOuFAeoxTuecGsdL6a8aHr4pSEdOUrQdvQU2AOQyp4jAvmoCVi/AdRU081JwC6i2eLv6uQ2y8MPi3/89HZwman/59LlYvH0+v8x/tL6YdVl0pdN2gQ8MXDlukgETvS7obHCm9quCwKjAaUX0+tz5jVJZLf4yP/v5yeQ1CrqfP7+U1exFIPfnl18WZQP4Nf38+3WmUv38y2tWDkHz8y/f6LS9ew28biYGpH798nb9RhYs/LY0CRdfdGW3feMFTJ5UASD+nX7z5yn6G7k3k3x5Lv65rD4sfkx51ucvQN5nWLqA7o/JAhuAnS+v1zIpfn7j0ZS3oHAKL/j5l39E1osDL52D+v+J7q9PwnHg+MBabyYBATu74K8L6E23rzT/MdsKBMw/owlY/s7uq6H+Ee2HZ/+GdJYUIE/efflDcj/aAP1l8es/1O0/2/BhEX4GWZQlNxB3bhZ8Wvz+CJFff/K/3fzpr38A0v9XMnrZN96DwpfcKZIwaLsvX379qX3c/umvv/7UVyCKAyf/0jfZj2j+yK4PPn+y4Nuqn/+8F/A3irQoh2LxNYcWv5fV/2j+eF2cARz63+63nxbfZ+L8gRazEu9Mnyb4LhtbIOt3dvzl5Q+ARQBWmt57PAb48W//tpASrynbMuwWulf23QI4uEvyYBb+FCcAYx8ICBQAdm0TYNi3dSD+Zw/PEpfh4rf/5T2A/6P3BvzwDOJffABzX7oZ5758g/Iv30H5F+cJdV+cLzPg//a6OAFmZZNECVi50GhF+VwAvC66WZCqCdqguQHwcqcu+AiofJx/zDD+27/E78uD9Gs1/fYA+OSJkNr2MKNj22fB62wHMw6KN609UC6CMfB6wDUrPSBimACg/wDs05bZDaDrbLM2TbJs4ScAf0Ddm57Foy8+zcR+++0312njz8UTzvHFsyC2MFjwVZzFx49A1zBLorj7XAReXC5++v2Pnxb/e/Gf7XoQn3kooNC8eQ1IyOtHeQGysM/BsrloAvh3/IfXfv/jzeKADCjFC+DjJEyeRW/OljTw382v7+mPGEkt3AAYE5g8r8qmAzVikXSvi0O4+CovYDo/mqtIXLYdqOZVUPhB4U2AqgPU+WrJouxA9e6SNpw+LPo2eHD9zW0eHgpyAAdO99tC2iqgZpUZ+GcW87EIbC6LBJj/a3A87wMiDSjHm3cSrwt5jttF5TROFTfOG4/QefoF1Kr37YC4M9f0z8VcroPZVI+AeZonmhuVuTN5uPTj7HPQ2eQAMZ5dSPe+xpkr6+lRYZvPRfuWIE4TPHoFIMq0iPrEn8vGf7yFVBuXfeY/7AcknSm9ecF/88ojBh/NwuJbUC++74feghpoMAf1Ym4wFnOHsXhrsOaa3GMISiz+v+y4ZvvQHKftOPq0YxY7+aRdnn6bu8/Zv8+GdZYNqPTM0W/tzzvEvSP95yJLQBA20388Vz68/bbmiZ59A5yj0dqDPjA98NtM95EJc2Q3zZxDzufivaQAbRYP/ASmBLAB0mqO5neG89N3SWOADfP1t/biTefZHiDaF1XvZsBjYRD47hwSXdzM2fzmX5AWwZzZQ5wAi32v1ewcYC9AfwGESEB+grLz+hXmn0/fRf/TxmcXNW95dJg9SObmQQDIEcwCzp4akg5gmtM9m32g56cHEaBGXnWz7i4IJKDp82bQBHWftEk3Q+fTrkEFsPzj/P3UdL4bjBXIIGAskCdVD6z7yKwZdHLQIwEZQOCCRMuT4hnGb0Z4EHTyGSYADL/F0JPi4/abQsEjHedi975xVmTeM/cPixCIDu5M36PJ6UdhAujl84oH37+NtK/cZtozorYAFQHH96fPRuP12Ss8m5HFO91PfzdN/fzPDVyP6m/8OQA+LeKuq9pPMPys2O8F+xXgGfyUtX0U749zMf34KKb/ABU+vuHOR+fjjB1/Yva0w6fFPyfwn0i8JcynBfqKvCLzI/Et4N4+wD7bj5vLR2J++rnQgm8QDNiXs5CzNyfQLXytl+9LQNGMGgBaYPGzfrZz2R1ApX8UDOCaz8X3GTBnIKhHRTRHbFt+hwyPxgFkw9OTX+saeFR0gLc/N6RRMI+Fj3wBE92nos+yDy8FiMV/ZRyci1k+x307T5Ugw0DD1yXB4+oBI2M3//zzqH2snmRfQXUAkJW138fmWwmaS/B3KfTUGmjrAQ4fFv4Dm0HYAq1n5nP6OS2IZyDnrF03VbM6z8lx7jUfNeHLsyb8vUD690XkT+UDIOOzEnxfdf5cU37I72vj+/fMTNBJzHT98tNcVD+84RL4BsMKKDzvcwfQ8m0SfIzxRQ+G7F/nmWc2+2PL/APsAV9fN339bw03ePnrD+R6avEFFPviB47ZlwNAMwAzjxr8rjGQ9T1Sv6mOkT9W/L2OfnlG1N9yeBbbuQjPyPmI2Xnhh0XwGr0u/qVU/4ghGPURIT9ixOuYteMPxHooDkAelMrZht+c881E5WNGnDUAJu2e/6Xx+wsIbWeW5y2434YMsBxg4sd2bplgAAiAIbh+pi549t8zfrwRbWMHdLqAKrVc+QiGhojnowFFUT7iuHiIuGiwXiO4Ey49P/SWyyUeUkvSRxCfClfYmghCzPEcd0kCek9U+DI3i8ksKLlehsh6jYUEiiE+8CxG+P6KWlEeucQQZ+06pEuuHffb1jQp/Dftn9rOpv06Cc1WejPC7y8uRcwRRbQH+vnZwhDqUtjS1XkXaqigJNWNKOiKRjmn0+1MYwlut/woR17J+UVHcRpKl22ijyebba1+OMQlSyb7YhvY4vpep3Wbxtqt1pckcZHpNEpqhPKPVXizhKY9SsvoAhF7dnVQBiqRkBYwstUWwe9XZILjBh5KwWjiZEXfKiYxc1T1IMq4WW23IwvKJnv+FsJ5A+mGuAp0exKMUEMMe6MLKXHSRqTahthRu3OORprchm9YhtDd+KAQt2u1Xq12FAytoHvZXK7ZNrrz1eEuNFrCeX1meXoOKfht6VxVUwvyW8sJZBa3eXpITneCk8az6VjTXV/vDm25HMpxOtAqZQRHyRl2Um+ebcJQb83GTE6TflNiNhHFksBCd2Wy+L5mhmDfoJRXNMMKLuJJTHEvPOEwMkoByu5A/QPyQqxJngolYTbtdu1caesqwzvPQsTjgdVs48z7bsgc+TK9KJN3Pw+cZ+mMxNFCtGGkWC9iypf2qWAd7aOsp9BKMHbEfVLaQVu38FZz9K62xInMrIq+EHedGI7D1NjBtSNcpTtDLWUFZkV608qWaeqG6SJtE1aCJgLXVrYbRcZ0tcrNdrIqCUl13k/qDt3sChuauEzdUZHobejzUbwK5f6gdGKPMjfGw1rnXBKTrsnpbTOJQpRl907ZRMnJ1Jm1ZbhpAHGmrRG9sOROgiwxMJ90FTJ0F2bplPu28uBsZDVVPV+Xxso+2ba7DZHp3KcxzN/5UtLVtG6kuo3QA1QxYyefc/Ear1TlKpoGpNtCdiz0ZZVfbsSeg08Rpl2PZQHVnc5sEdbcHFbJKSlW7nKLxcTWdkd72wVkP+69WpZqrj2XohnT7pii1LLOLjGy3xpWfE4KU8JWon+omUlLxZVqh6PJUZnqVYEqQ7vkrA93hVfuqRwmIhrTKyMYjgdXjgfHJyVVlJdrMCgRFWqaLrs+0hFxyDdF77FUYNPSGUwBR1lRe2ZXbTUECxRoRyD9Dl9vDxx3q0x1YNX1FaWcKDSl+nY7BAEBj2QJO4OiwtPRLlc3cT/5PnE8JWeBQKODjvm7AkpHAb24O0MjWdZkIz+f5DFsrAO9G9yrQGl6IKemWIqWyWuG1DByoQ2dqdz4pAcJsMXhCsJUSm/ZIa91fouy0dnnE8ditkfNNISByTZLiVy5dxJXRjUbFGcjH3cqY4ScVxfyXWmj/O4RtH/EFFQpuZio8WVxFs2RS0T5pBaMh9oqLHMqLosqfuxKN4X5ASPzujZFjYW2fQrJHszUUpyE9xav4SVwpHDKjJJ10qLA7+KFOxjVMIWx4t2Rq3On7XJvkxhlxBtT8pj2hlTxBt0goo/uzsl2ZCU1MDe3JLWHyqTOXbeDdYZn0huCp72r8pqa0NUwJK4srq3eXAcx2pdKVAtHR6UyvMjvV82lPeeGFKPILZUc5e6wpaSGHPgZvy/uNC/LWbDlOY+OGHSZS02ewh5aY6sovaSRfgCqepC39Eqdic/rXRTyR22A10UYqxtko4SyqHkaySHcjdyGNRNDtroNR5LHtI21gu0B4m55F3Edc41MebdyMXonIEPuAcyl69NaYC8IixpGPKrDcB+drFpiF8uGJWG9Mqtsw5xYAr4C4mJMVitXKVGar3vLWvYE+Aw+BaW2GRgj4w4sDqG8dl3eDzVpykdIVEXIIjpMggWeRpZ9HpupJwXjpuBbQy9Bm63oK35sNKlvTpx9EKWI19u842hoyrb3YXn2937F9UNJSddVyO8jw9q17HXZX0oj7KMrRO0NnU0qxIiyPVccNrcrdjd8hbd31BoTVcPjk2HLWns8OPFpbWxr9zTZYm1xXWFqOM/v+WPF7gzZK84au6z2BzsyHXi5Z50wFtk5ZHnecmCAAn0WUph/laJSiFl6kAdRlS+X8FwPl/IWHcqGuZR7bcKZI3vdUYFAr+qEUZYEeSwy3E8FNZPadjxRG+W85jIzMeDeQ/STt2T3pZRi93E43PEwqenkHph7V9Pi4S7AU7Pib/ccg6yTvV5x1h1eNxiEWkHGnyL8qijyfdIuO+Qgt1sNp+96C4uJFrtLEBIRu0VBP7SMeJRhrPP6mu7PqDIybbrG86lOE8GkC7LrD5HgHeuD1pkXJeLy03A9nb0pWjF7xYCuWmUxTOT6Eo86RM6mjKDfO04NZN7dBltnvA5ZxIXUWRs9lrH2DVcn9jInuwuxri8k494mDOXC3GNvcbmTmrWHUG0gNivVMWjPJFOLRXdeOug9rjLUifH68c7EakmLbDQVO6TKtdupQCkibLdxxZN6Uwdjcr+mAi73a+u8w9uxlYxdqZwZYp9NfROlYQE3B6S7pcsmrdWeNJGUEm5I0q1JgT/4ntHohZrT6igE4UlhgzKsC5cTNr7ss6MR8ZAqJedDb29OrB6OMNZ02SpB9Eg61UTScoQuCJhKMs2aOwBnJXJyS/NtR3mcZxB6Lx5q7WBD57OWZERLpxoNQJ7eRLSxMQqnaShQG7mrpLO21vFVqdOjkS13mH+7bNRWC8aDEGenIF0bhHGOlHVySTWGPAgo003ojbnGQXzTkL1mb9OyYhxI0LyacSOHoS/xMXCImmGt8XI06kNXpc6ZEjL4VKY8IfHHYdsrKwwMjJdbehPPU6GutyfF0JCRd8yD3QrIJu5S0N8cXYbcjqeNQZ7cjM6Po3qiE28s0QuUhkzIlhupFKEuXju6nURKLpz04ipduMi5cJJ2lo3ycqeWyUHuyGNDj+5g0biCupe1p0fI+uBF9tA0x2V78K3IWZYuK9BcBvn5PqXkuzagoLOEYluSiAt9Qc9FK2s7yuLGFHEqjOtbndP1g2SPh12tedvQKsvT1gRBya0ThpaHTY3usERw7GCYrJYhS76Wu1BJtYMDy2ycW3w3xdJZKahBvcnGnustNsXOROTt6m0ZAaSNIsKL3Yt50VSK4fGqA7YUe/lAHkMkYjk+oiAdOVxQuKEO6wM9eawsU96yuRpXz0k3A8j17XSpK9kJqYHbscsVH3MoqcoszoDCA5o7fOecN+3kb9ALg2q9F255vCEVcr87mjFx3aPjxJ130wnmN2x7QXUXMybE0nBydVf7TMpLgc0OKlKhCEmruW5WrHGlqilpGzO+VHJuw0tuROjzVi+W7l0509fRUCjTt82oAWFnlOeaDrnrMnUqIzrx52F7HBMxNWJpGiQ3OtEm2ob3pEy2pCSDnK1BiQv2AJFIyoSNnmANll12khuHm6Kk4uDQtdWuIjb4+tBgND6dnTOOXfp6k1cyogcKK6UnqZAytdAM3kDO/rVVWU0SnK2Ot+XJGjWCR1aBAmf56na1Samw8D4goONEyrixHXaV6ru2blM33c7xsx8K2R4NvIqHdwjo405cesO3oA88nC5CAHmwvDtvoeWubskut2REtQjZOKwyzm5qdUUb+s3cMizHbu2rnkTTLmJ4sR1qLTZPms94tEOJFz5L3LAyFEcYhhylc0yAaaUPbb6FQoG4wRu8NhNnvxtqRMsUXBay7uKh0OGKexFR30fXvEIQcUBUR3NqtLhzJRfuXWIZ3gooxNY33jeD1u8h6UZdl0EAHW/ubj2YhXvfuM61v6N6WdfXvuunIOXHlFEmqloamnvpZVpQwyg5cvpme2kUIt3a9s1bi3VGQhYkNMsqqcA8sabCIonoqNmSGhi6FK4arneOz2i3MQfxtqb1WivM9VR6wbSKD4mhN+Jxj5HVjSBCBsHtDm9w06lve6tT+IsWH2vXzNbIPUnXO5bXXVDICJz2pUNt0OPFb0EMUQaWQ8slw96MuI6FgHNX5/R4HRnbb0yRV3RNX96dzuu1fOMaPcavIINtzl4O+nsGqvZrIocFTXdsiDV0/rISxlOgFZqLjE0oN4ds3yoKxdaGudvvVOdk6zFT3JoSMVr+1OhXyxZuBpMQU8+lamXcLkgC2jk4x4aclzJFue0CBZPXgtNO51pG+oOlbuml11vuVb63B/ROZUK+PXbMWeFo4P0t1zIma0jnrVDJ0a3cZJlLYJEyGOTVp4aoXkqNmMih49TdQZPzLGUgT1xG+aHd3dQm2wgb0HhQ5NrstxrqnVc4SAsYx5dgnLsru4ppCT6ZTk3bEY1rGzi1dw2k4/YOBOkm47l7rS+BVte8g6arfqwnDUDLsduivt8R4UqA7D3vnGubJcbEptKbzg/S8nw5omm4XJK8aqoTKgGAXeWhoZ0AhFnrulwrG/rGO0EKacn91kSMyGV+RSTeirnXfMkS961/HtNczK0tqhwwKdUVhTuqdk9Ph/F2YTvS07hOZcsC3gxaleLbBsW8MrjBkoUoVRyeiSRI81C5WFjsGvxZIdHRPdwxdPDH05l1DYFlfeZUnqqtvFFSb9UAwapuj5VnMSA01lDMyTmI9Z04XY+C2V6uKxuNkUM4lbf8KlgnChaJQTTx2BTQ03HEkrAdTh2+uTWu4Du36lKSNwqUjKUf+CvUXSZKsoIt0Sz8lDJ6VOpkEiXxna2PXpZ0NnkOsSCIO0Sr+oms8HEZXYUxPwd1L1H9eA1Udx/21wgLteu557hwuT6JN4RdUWyOuMkSacKI8W2onHZTEbPulYyG/ahdtm2eEhcRonCPEXVOhYD5a4rjRgO2YK7lWsC5v0B0yHYBdZNxBBN3VR1e1f5sxyjGtfkpkBHUuyjxSIqmpsEdwsUyS8sUDq+7ACbE9WW6R1cdvcDwZEHmPakHgu2189qDwrxula0RRfykhRdXI9Zs39tDn9ohSqe7EOnvwp6mlmbbBxEXG3Kl7kJvCOlEPyCHzThmZCWt2yNXyQlp12Sh7Ue9Rs/mal9cgo4WOROgEFsXaHVP8PyoDNoFKmWVFO84Agbv7LzsY6mw7356YHOp7324OFKUvvIloozInuCslai6+bST61ubXs8eSd8I0TuBtm1J9nndH6vT0fXbMzug1Gonmkc/Oe8pxAc9+dqFnbgLpFizN4fjQcvVQ1EMq01XoLzpczkE5s7t0LhGcPEsY7vV7NYMzb6znaJHhPMFuQsdg2w6G0OlKxZ2an1beRMTF0Rql2vfdJM1xK8oNR6vGlbFEVXpPHdhQluCkW3R5NxZH5mS8xSkjDvFYpW67jOOignaQMLhIquBkykRswlVvqEmuZz81d5A+Uu2xtYpe6+o9HLMVmBiUFK8GUmoGYnJVxRpfbKm5Chu+bSRJ2/y7sFGCFanCBr7PCDvK27FRNC9qdMBXtpMbjL2SRVRaK8UkrC5HhvSqxHyLsqYn5A5wTS6R69uoMWOC7k5ym1DpR0vD2S0l2oSayi3Y1oUvYN5I/M6zCHXDX/Q98eVeLirLLQf3E7T0Njf+AQcBKNkMdX+bp0rJd+6aFw1TNvQhXy05fx+TIKSRztWy6EzJ0v46Ge9wOwU86IvGcQqROTYW4oJQOQQC4xbSop7xhi6jUJYg/RaTs2NZF9VGz9KdV/LRFqGU5uMATpcrZZ2XN9SxO1YBHmnw7dT31XrzGxMKLCTZZJcRriGgqUh9t4RNxwhV7KEJIjVfgwuA8ltlyuhjtZhUchbfH0mQ1TjcYtszPVcyKyaFPpSbJBeqUG90/Ggjl2IxqncYNUCPyY4sjTxJi7M2zlAEq3CejMILzsNa9bxGF8pvFnyiEjtbyCfFJkM2A2eqxGfJvZVGApdsbbBNUzydDcIN0u+Ng1+10FvEB62ork5SxB2chGiRBoyaOnbFnLza71huOUqNY59swKQzxSnQj/qgs2haJLhqZ9MNk5u2OVQrQEAVeHKMEfq5GiWg55uHE5LWVA2h3XF6O5dw9tzaLKUPcA+LcS9aYCR88KpeZSr+MkiSo+smZXbx4mE6tk6KkPmSp3gXS5TfFfjBxGXBAZtHKxf6ssDh2XE0QjrbodtBlzYZgG+TrDMdLwJaxvX7y+1ZUEFl2QdPZo94eeglREvJ7lhXF62r6faHEHuy3KBVVNR3PbymRGt41o3+f5AKdj6mKK7i3kS7Rwmnd5cLVcejvMitr50oMlDBto3a/I01GB8OOsheVcOUtc7eaYHu2XAWULr4QcXzHUC1nhUNmyptaUqU3w/FYSstTglWLA1pfsbrkQsGJYDIzcza6lx9iG/ZMi11+g7Fdsc7WvdtIYp606PqIHwsI3YFuegNOmOaLHk7q5VV3e4sJZeeita8arW6hBYoC74Bqy5GaoX1slXl+yN4qPVtU7hqXC4WEeu6lo/3DO8A/gAXU5hbreOiCl3umIzvIFMtFmH3gneuGmrclW539pSxaHLPPUQyKWWUtHLZ4gRq/2w3eL4zoh29XQ/DSdsF7odXW6YbnAVvy0c/yZv9tpOlu4EiK5jzGTQtQ6ElsKddSQSN8rduMzeVIici4LWE27UlNwqnECuWd9cJfTs+GsspI+wa/XC+p5NOKyvx2u9ZFe2p9yOKgRtA3x/V8ptxQ/QsjujU3rejGcm6EbLdGAD5GKI81fqOAQqATuQR/lXswFYIvm5K08dznVulecYGwghmXHdhdqvjzwmyPsjll8UMD0H2ApGBowU8LWLMl4aCtxxB8cIYtMRfaxMpbOrqK7pLb+sD20iIlNLKW6MG2Z4tfS2IyVtRPnbRKlX55Qm3XmvDTC1XfFEjpS4dOstlERUag23dstBnANnOHy5ojbFUFBvhh6luTjSDeEZIHsnhhy1xkVCdNRAg3b5GhVKnUywmFUzQ+ldMej7M7yCg5CuBo6kEX+Eiq6mDi3G6da9P18cUKPL1WGH73ZOAEZbCtdCITQCBh4kdotsd+5Oomn6L395+fAyH7a9HfP+195Pm4+D/ttOpZ4HSO/vlzxOOAPH//Tg9em/KOdfP7w0XgKkfJ7RtVkfvR1e/c0J3cd/6eBxJjk9Xw57P+l+HqZ3TjS/bv2SFH7fds30pS2zx3soYIfbt/MLme38zq4Hvr8/zP2q7nyiO2vSlV8e7/K9b06K+Q2TwE+cLni7jN5OMsFugAd54rVfcIr8EjTVrP7bawtAa/wVecVf/vg/1lxSTjAvAAA= -->
