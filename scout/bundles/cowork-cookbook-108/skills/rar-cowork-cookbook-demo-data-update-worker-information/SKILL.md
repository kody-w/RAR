---
name: "rar-cowork-cookbook-demo-data-update-worker-information"
description: "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_update_worker_information", "rar_sha256": "1a50502eed61218738293dac7ac91e99147f82e72b0a941140e5c1fe3954a8ea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `demo_data_update_worker_information_agent.py` and in the RCI capsule.

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

Update worker information Demo Data Generator — Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; recipe default is 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 1a50502eed612187…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_update_worker_information_agent.py` first:

```bash
python3 demo_data_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_update_worker_information_agent.py   # or on stdin
python3 demo_data_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Demo Data Generator — Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_update_worker_information',
    "version": '3.0.3',
    "display_name": 'Update worker information Demo Data Generator',
    "description": "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aaa48a0f1a3f3bea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; recipe default is 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic update worker information data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for update worker information. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-update-worker-information-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic update worker information records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo worker-information-update records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo worker information update records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; recipe default is 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training worker update data in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataUpdateWorkerInformation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataUpdateWorkerInformation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; recipe default is 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-update-worker-information-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9GZ+WRfRjG4oiIaIUCAmIUG0hVOZiExD2LIl/+9D9K9trPK9bqqoz+1HLYkOGfPe619jH5/cbv2UtQvn16s0M0XgpumySWsF24eLNiiL+obeCtuHvi78Iu8rROva4u6efnwEoSNXydlmxQ52C6EeVi7bdgs0NWiDt00adrEXwRhVixmMWH9Mcmjos7cecPHrgzAYrDQL+qgWST5wl00QKlXDIsNRqwW/P+0WGWRhrGbLsK8Tdpx8XMQRm6XtgvbUvhfPiya1o2BvvYSZk8Bs8hgwQ1+mD50zlZ/WPjAmvZt3YeHY3XYdnXeLELXvyzysH8z46dmUdZJ5tbj4haOr8DFcHCzMg2bl0+//u3DSwI+v3z6/cVP3QZcetkA3zZu69oPX44PJ8VvPoL9qZvHYGE5ghjP38uwnm+DS8CVxdu3n5swjT4s/vM/b71bx80vnz7ni7fX55f5j9nls/GLtnCb2UHfLV0vSUFIXhdM2rtj89UjEESQojx+fe78JqkoF3+d7/38VPIah+3Pn1+Kcs4ZsPXzyy+Logb66m7+/DpLKX/+5TUt+rD++ZdvcprOu4Z+OwsDVr9+efv+JhYs/LY0iRZfLJ1j33SBGCdlCIR/59/8epr+Ju4tJF+ei38uyg+LH0ue/fkrsPdZhB6Q+2OxIAZg58vrtUjyn9901MU9zN3cD3/+5Z+J9S+hf5tL+F+S++tT8CV0AxCtt5CAAp1T8LfF8s23rzL/udoSFMy/4wlY/q7ua6D+mexHZv9OdJrkoDHec/lDcT/asPzr4td/6tt/t+HDIvoM2iZN7qDuvDT8tPj9USK//hR8u/jT3/4Aov+PYqyiq/2HhC+ZmydR2LRfvvz6U/O4/NPffv2pK0EVh272pavTH8n8UVwfev4UwbdVP/95L9Bv57e86PPF1x5a/F6U/6P+43VxAOAXfLvefFp834nza7mYnXhX+gzBd93YAFu/i+MvL38A8MmBN53/uA3w4z/+Y6Ekfl00RdQuLL/o2gVIcJtk4Wz8/pIATH1AHnAAxLVJQGDf1oH6nzM8W1xEi9/+l/+A+Y/+G8xDM2R/AYjmfnmC9JcnfH/5Dr5/e13sgeiiTuIkBwBtMrr+OQdonLez2rIOm7C+A6jyxjb8CLZ9nD/MIP3bvyD9y0PQazn+9kDr5Il+JivOyNd0afg6+3i8hPmbRz5grnAI/Q7oSAsfGBQlALU/AN+bIr0D5Jzj0dySNF0ECcAWwGDjkwm6/NMs7LfffvPc5vI5f0I1tnhSWwOBBV/NWXz8CDyL0iS+tJ/z0L8Ui59+/+OnxX8t/rtdD+GzDh2wxltGgIWSpakL0GFdBpbNBAig3Q0eGfn9j7f4AjGAVBcgf0mUPBls7oRbGLwH29oyH9EVsfBCED0Q4Kws6hbg/yJpXxditPhqL1A635oZ4lI0LeDlMsyDMPdHINUF7nyNZF60gInbpInGD4uuCR9af/Nq92FiBlrdbX9bKKwO+KhIwT+zmY9FYHORJyD8X0vheR0IqQG3rt9FvC7UuSYXpVu75aV233RE7jMvgIfetwPh7kzQn/OZe8M5VI8KeYYnnkeOecZ4pPTjnHMwo2QADZ4TRfu+5jEW7B/sWX/Om7fid+vn/AFMGRdxlwQzJfzlraSaS9GlwSN+wNJZ0lsWgresPGrwyfxv883iuxJezLPBYh4OFm+D0cyuHQoj+OL/v0lpDgUjCCYnMHtus+DUvXl+pmgeGedUPqfM2TTg2LMdv00x70j1Dtif8zQB9VaPf3mufCT2bc0TBLsaWG8y5kM+qCoQ/Fnuo+jnIq7ruV3cz/k7MwBvFg8YBKkBCAE6aC7cd4Xz3XdLLwAG5u/fpoQ3n+d4gMJelJ2XgnRFYRh4rn8DVtVz474lF3RAODdxf0lAxL73as4NiBeQvwBGJKAVAXu8fkXr59130/+08TkMzVseg2IH+rZ+CAB2hLOBc6b6pAXw5bbPCR34+ekhBLiRle3suwfKCXj6vBjWYdUlTdLOKPmMa1gCkP44vz89na+GQwmaBQQLtETZgeg+mmjGlwyMOsAGULWgp7Ikf9bwWxAeAt1sRgSAuG819JT4uPzmUPjovJmz3jfOjsx75jFgEQHTwZXxe+DY/6hMgLxsXvHQ+/eV9lXbLHsGzwYAIND4fvc5L7w+Kf85Uyze5X76hyPQz//eKelB4vafC+DT4tK2ZfMJgp7E+867rwC6oKetzYODP84s+db+H/8RGP4k+un1p8W/Z96fRLy1x6cF8gq/wvOt3Vt5vb1ANNiP6/NHfL77OTfDb9gK1BezVXPuRkD6X4nwfQlgw7gGCAUWP4mxmfm0BxT+YAKQiM/59/U+9xsgmjye67MpvsOBx0QAav+Zt6+EBW7lLdAdzFNkHM6Ht0d3NOHLp7xL0w8vOai8f+nQNtNSNpd1Mx/2QAOBsaxNwse3B0oM7fzxz8df7fHBTV8B8gNESpvvS++NTGYy/a5Dnm4C93yg4cMDkpuZ/ICbs/K5u9wGlCuwbXanHcvZ/uf5bp4IH4j/5Yn4/2iQ9T1F/IkcAPC1YPAI278s3miima/NVPG6UDowHMwR9R7YETwnzh/q/zqu/qPyI5gRZplB8Wmmyw9vMATewRED8Mz7aQF4/XZ+e5y28w4cjX+dTypzGh5b5g9gD3j7uunrfz144cvffmDXM65fAI3nP0iU2mUeqDgA0Q/CfadVYOx7rf7lPW3vJJrMTP3DELxT55dncf29rie/zuQ7Q+ajfOeFHxbha/y6+Bd6/CMKo8RHePURxV+HtBl+YMTDYYDlgBHn2H1LyrfQFI8T3WwvCGX7/A+I319Aibuz9rcifzsSgOUA+j428xAEASQACsH3Z8+Ce/83h4U3Ec3FBZMqkIG4K3gFo4A/CQRFKBKjUBoLXJ90fRoJaRrByYhCQxL1YJfGEQSHw5WPRCFGr3CXCl0g79n8X+ZhL5nNmpWCaHwE+BF+uw0uBW/+PO2fg/X1bDL7/ebW7y8egYOVW7wRmeeLhZaIF6KQN+5O0GlFJ2MsneysNtGjhXU8654vuscaIryhL1Lbtyeb826WJrtinVLomlMYCDag856W9ACbmtEw8GrMj+MUhYzAWJapoJGWK9FdF7wmDMjYGDzZLrJa3dFGd04sxynvzjpLk/3lmCGGPyKynI6l2VnT/qRPVw9bYnfEuGxzOPeT07Vik6shGvBJ0hxNMLL0gMcHWHAv/eHI8aKtxLcTYQUDpF8xDL+dIExFab7m3ORwLRxxlOsg4eUqrTXJijYXEjpKlCiWVl2vw+5w9vbntXjpdjebWCenXDPLi78VYwYrzRQTd4xwSNBaZzPu1vCupNVys+EaU3K2wiq9D+eTuyz0dbPy73uYDvW8hfxk0LC6h6CAO5F0IK+F1IoT5VJhcrBqjHMbnyrb4tjMT3le1aZk7duHg2sft9SUyCq/aUqdVtYpzzbkmtEqhhnXdKDmJTyE5oXJbjgin8i+MvZXXVwO6831PCaOW8k7bg9IY4xzwyopjnfKoLybI92exs7xhAxDsvBUlZxUcAeNAmcnLTqIhZult4pnh9SP2cBg+ay0HFD+Fskj+4ot1Ym+cXgs0czxzDIVdRIOhrC/u6eIyMPjSjXg2lxlCWuV4baIK9bPlsoabmRBVumtckjDbr1TGuqYmrfdQcuYCMeOduadGlZouBNta6dqNRaVWF3xXrnsHUfng5sc3bkDUW1WqZxsaktuxmrc2DSRcbF1rhuHu1CGutsdjsvElNqWNEkpOWPwLlHOaAPHUFWi54I1kGZ9uZi6eF+Vd35gerjrr2zgUftxazVbwyxbAxlLxoWVTahk3Smway684VaCy41NDFmOeCVvh7JyCZONvpST6VDtL/JoQP3NE6dEFZxbkeJsRCSqYer8rt2MwnCmhDS8ctvJQO5Xm+S6kRjP2wsu6Buup6A+xsyhMot2Q90L6c5zrr6CGrFY744hjctXQteckKXOVrlUHIjYQFw2UY4/7SBRzK5jpEQSDSWrcG3XxnC+eCZsxaM51k7SmAf+xgXO0Zxc8aStjt2BEY1JOFBJTO2UdsvI98aKy7PGuCqZHhrJk5JqHKw1ci+XqFEcW6S3XUtiET4+BFLinjasZh5tWdku15iyoj19henDge91d62GnLFhy41/OCXE5Cm7ZivstljBL3OKaaiTh98PnjpolUDvuTwCXa53jrvF1O0WVjc9nFgjiNZuDXkrlLed3dafOtjNB/viJpKcIP4d1zFsMMaaPWKmJEd6g95qebt2zrq3UriaZVsXyc2gPAk3OgmFRL4wcZKJmsVMveVTsNbK2LHN4fOApW5KZD7J6h5k3Kz4mh9AZcSQh8lleAzqhL9UWpxxWuyvDnm/Si+yv8EPAKfcg67lUp3mYyvFRzo0iwLbXKfzgclClBEUmLxVq6RalTtMdStd5BWJ4ZL1Gd7q95DcdT1uN8WNJXMhFKDUpSpUO+8mwmU2vi4SCQwxMRbT99RmQj9go8rgAx0VsMtF9M7r2sCda7zWjsuesVpFurM4zsg3xzTrrGiq5KbJ4ZELd/Y90liPVKUrAMtSLZSzqm+X0WFZxaEbbSdCNViiTmtFD/zAy7XS2yvkTj4PJc7CFnkjBmp1O/j18RrqJ5YMIDIYsZXgaJegP3PpJb9gnOxrF8c1zCgLadi4Hm8OvbxtGqk/7pkiQFV17WwM3iqnGkezXlZzCZYkEpJ3rCisD3V2bIuU4Dn/JjsJxowpudXWtGxcwztSQeFyuvOK25hxcTttDE7sInWjulaiy85Fk/CstAkhcGyssO1YuoUHI2MVjMvT1I4n9ljrHYdcYK5x5Lpf44f2SmvVgTn4ZUvaEqOmoMy6ItS6MjxHh6o/Fl28PdcM5m7NEZ40fuKIUDbgctroJExoeToFN6m/EU0z7Im1jNBCekxsKtXcUmoC9opkluRgrhKR+nDs28t9u2kr0YjPaRlNaLQ8bVb7aKSi3WDc0usBda0DpUwTNNhNbK9hdu1R+dBT8E64WJJ/dbydzDE3NCbybmR8A0aRyCfXyMGijJBQ1VUHUDu5MQF83rVMuLnczWpd3SVqU7OhgFxj2+Y7Z8VeYQ0k1RCkxCZ8i4ud25RwkjoNl0IutodmSyUU48vM7iThRdLTGAuR1OpcoubZHxpwrif6jXTHVvvzFbR7clhibWZNp1q5oRbks5sVU4oylIhFeUXbK6KIrAw3KOB//Gwk5x2WQNuIhWWZwiaC4JSMmYa9nln7eJ/lHMac8RAboVUWFMr6WFBratK2/Opw6F116qyx7SL0SPSM2Cb7Y0KSblXuxfWK75JLYJ5Ka89swFE42ufsxd4ipr+V1XWj8K1tSJbhX2qxQdb7beD1EFq01tLkyuhEHWxDYOEdz5uidUWoq2Ae7yY71hIfg1kZVKzEZQkq3apjkPK2W2o7azUSHM7i63XPmIHglDKdVcEQ9x3FNs2ZjQc63VgYb6E+u+9F6sjCkoI4kaOoNsxARSfxBmqy9DmbWm/E26kIbHMDo3Yp69l0F4qjfERXgtEL4qZOO6+w4T6jbkglguEiDa0shAk1pwUrPq9DhmqD8qicqv2hWlqMYEhYprGFXbq2DXPEGYmSzYnfKjfEFEa65DqfTeEtHqt43DkwGTsWRBcJR11v2m4/LFc7beA2JB801qXTh8jNiBMTZ40olP6E8WiG54c+aIpNHuZJ1y7RnUPJcWhcxra06AYl7iK1KlRa4lnrCiYDIthKCAlOpVjYi+mROufuWSRKEhbiTjCOvQ+7JSqUVcJbljw6ccFVUcNEUVFsLsepFQQ62TBqvy4O1GbPq8n1vNLhtQ/zCIxsslFjGri8iOwQpS1HbrBrk6M3km9OfAkHxl5JWB/ZCEcCUpRtcW5uaGMKm8l0B2U4NSIy+nmpEZzJIE1e9kgJ8U3Qi7yDy9YZKZtJPxNEy4WUNCZrxz/YW3pH2XtgVMcMVxcvQwuL73FOQlR0VeUYdQBFHC5kFWjbXiQROiOu1+3OpMwrga82coJJ91tMAUfxgKis7WlHUksH31uZt0PW1k3K7I4cGc6SdnZSHUk7NZaHtG/2GGp06nhmCG2toFi+G9xQiRyrdBzMFpatgKXKpbMjqtIbqMslRr8cmaLXOj4T7toRVqbUNHA4PvL9SbpEeYan2pbtV5SDrmi0KhXGpVzcoUSbUI60OFUHfkmZTZz4TGDduv0mqTTLI8Rc43asbR2pYooOTsyLF4fuseNYn1fs6OaXhEaDGj/Hspc4mYzgnXJO3F1hlcDBU1GVorG6jgeSwM2eDfVtjRN6uL/QtLrNsTrCq90eIvsyJlc1MwRC1iEtwBEkLQM0JeVO21HL0dLUlE8qjBv2/G6diLFK3M5raCsWfNtvkD22Vzq/iGnDwdd4rVyvQXZeS6le8IJraPxq0yXxyDMbddf0hXnJvTBgFcYjdmcpTbwoPZDoQCq80p8n3onTi5pl5EZvHQxiIUwyb6sED1wcOJEh62VTjjQwpO191cFVfU8VFrviiPzoNjjVhWIm33Yy6inYQEER1J3QQ7E8HG/0NO4LyTot72aODUXI2BvLkabDiFobZEtjg2rgGlxkUjywByQ+xhuPqYqeYTTFGcFpQ0lv49UIGr+t5PMmPVnuHgqrvm5D9bLX9whB6XvMvFqNeLvflSRMr5p9Fby9arHsULOGAcjsclM5O90OfSOi96O0cdtV0JCnpbx1iOB+qpGVa0p6PCXoFQya2YFZW93dKy9wuuaLrCtzV95d13fJ1VA3w7eZO0VSe0koTwwkTL2qdGVKVlVW7aHeJZJB1X6ZHjVPboqdIi8L2CpXrmVrGGnr0KAueS4fVjJvG7tlGLhlV0yFCrALysp0jFE276+25jCxk7Ejm55Ee6CoUCaZ5CQkFiRutKuFj53AGBf/tl6ti/0eUtpBsRzXjZYGFTbs8oCsb7V9CgKju94IRSMEbZupxv2kVyEV4StOtSdnwANwBD2fe7lMuLUkbQ+UK9GVHreefFwjGoccfDPd1aUL68JAHA1t6O8de04Mi2Rbmzvzg3K/3I91nxeXulrW9V0Epzxrd5X5zS1fuzAeF+TeBUMYs+rGToqgAHO2RhIixI1szqWehnaZl8Tq3F93nkGf1h7KU5ecFBxzbKc43TY7Hd1xF5S0kpYk0nsqjyYz3XdtpHXCfe0hV7EkJ4cgkMAizWklk+PN9Q3Fi5VT0Qe979fO5r4ua2XtxPAglIfj8YDB0p46O5eU2HAGMHur7xQxLQACO5LGtBgKDuJDBjuRjkdpFMZ+yrXRTbQ0EUr77uIcRi2AEXQDdLpCSSRotc0uIQ7D25u7daOSI/3oqHR3IW881YFFGCF7XVvah3O5XWNHr5cGPlk6ftGqPXXPb40XAk1Gi0kkTzHk8QIYZTpP9aG6b7bpdGwZyK2nNr8uyQuxzcmV25MNdopRKS/u2l3Dl7K5iw27trVgeUUQXos5BT0FYRyS4hh7hzwrJ3Lvc7mx9cHpwjpW5JYsgz4lg+ogQWtnfz+7YkdFDb4UecLg90l50NkS1zOf2fObUa53UTdEiA5TkyijfnVSY1AQ2mSjd8i/qfNQ5PvQCgyFq3CfDSuybWwtpzfHqmsAK+hTmW+XbKNuzyTFy0GtoxTTb8vkSO2hJXSNKB5tDg66N5ddAA1bamswWJ/BXj+YJ7/MWSbVmGg0SZ6Q+HxIdgM1XVdFArkTFHvWfc8Qk6V3Zs+nnFSKMOYPEGNaIi5t9sOdlJRlQwu4aiEuUeb7rXmqwbwCbU9G2Ca7zbG5GWx7IpWyJ6etEIuUBwv4OSN7WpKrFeKT8Z47+pjDrp3ruk6vyArD3EMuYXyTqxgjYVf36ncGEwT0rXHrrbylq30S0XYetfKA3GnW23v3pMh4PcdL1yQ7q4CO15KXogMYGoSJGDnnyIlwLJRcHOr6JAhYkJaUT54TUfSErjWReGgDWjx0o9O6hJpmIWm0p2vNFMr9LEzbPTrezSU9dsv+yvlCVJn5nkSdpQTjJ6xkT4K67doDK7fizSkUGqYh0z4655VRcGFz7u/hVeBp0I7rirjtV2dnWYhCPB1FVJFzpWHRxsCmwh04kuhL6zh4U0f2arbfsiMdgAFZOEg6hBR0pF+LWwiRy7jjr/CRwyTDk508yJabG9I1l8Pd1+gpO2NL/oJc7cOqpRF53dw6OouEE9Tpxr24if39tqwmnguwFSpmdaxcV9R6UPaYlVGIXxDDndaGW5bfGAqtc09zk+k4nU5M0GYHcFKLsUCSOMPB9o5w3HTpchN0rNbU8e6ewyYqJQRdLB1CWdP3/bFTVT+wzwpZ79cNUk57ZK1Fcdkgo7iqM393a83z+bIakwMeJpQTXpFxwKe2X3Oq4QRQCc5H+Jm/bSBCJw6mUlXSVQk32jCkB8S639I1raTH3anjXDre7L1sxZ1DhYTp6nRwI0TVwwyusInkDzbscTp0GjC3DKYrQWKmMlDNSclz9Y7StyTB1S5etteJtSLU87BTsII4zAm5KUJqA5yoanDu6zvIwsnKX7VicE64E7Xpgsramacq5DsXazD22rVAwSBf92ro25orbSYHB0cZPV/mXt7fT6GulKEE5ZQoUBO37m4e5x05wiTOHuz5IShS6bRc3bxgiZ5tCFutYlPo6/KEjns/54VbRHZL1t+SnWtVHHVqxssZJyJky9pCqAXbcgv2njr+EA7ETtqeci6/r/Pj1uxUbDC9Xak6fFTzAuU1So/I5X1jn+8SpPLhEPQN1qYbtd9ULt7ufduPS/nMOltfjarYQwtt6Ja8eJ12J3O8UkvtrG8IBysyuKaqzu8LzWxrgVT1VkGpdj3W00HMeo0lAXaitI/CxTR1RzX1nHZSz0QEo4qdFoJLTxuFi9CVJzit4a7mBNMjqmzVqQYDqmZTEF4loUMMSGUN6pA7FFaSRXFdjw7JIVAejFgeXbNwtQtPNXeGUyqLNxWCsT4/YWZQ+Xd1hR9SlTzC8r7Pyb5fTXmGJNOQOaHq5b6Oe1csiKfdltYCHdnKEZ6GtK7tQz0It9cTrWbBDUVMwnSPkibW8F4Lmf0x9rSbvwuWCE3o9HpgIMQRDnBxZ9wDRbuXQSFQzLWJNZJgOzKC84t9ksrTGsdbogvxAZWRHZFrdTheUd5EymHaIlaQa81ufXXE2IWjHAzqlR2Rl7aTckS8niFFyE/YsV2RdtPSg06liTXExyxWpGyET8duaKf96l437JFAtrjecfuNuDv5ZsLsa9LU1iE9UF2/iWEZA92IjnWLUjAerAt81C9QLFaKfgrlYkUA/toRm7s11T5/04MCiil7h1wvB/poB7QWabdApUM5q+r9PSyxC7RyAzC9UJ0NZVOzDSL3vvEutE7wWO+heGhCjCqpWywous5OCk2uPKQTielE7A0sgNKcs9UGujhLxB8IJLv6rNcHRHP0cq9T3dNpoysydYD2iu6uBCXjTvf+zPqqsgxlJ4SCM1mVQXLEzBPGG0ZJ58pmm5RnjjmwGJXzGocZvKmvbR7mlzlPmoQPzoJTcSKRshStUMNpwp7gvRHcdlUpy5tlH6W6nd2EFUKOIbZLMK+g90GG9qAaNIjgl3fJuEfDtMeu+zrE06W3LLbirvRg5NTR4boO+UlvYkwbjmxumzBOMN2ld6fcq7P7nccwSo/WlaFhjF2SFJjvVsUN4cZ86FLKodVrRxDutEF3YOpgJ+wAXYsQWgMaH26Yxs2PVv7615cPL/ODsLensf/Or8HmBzv/z54hPR8Fvf/E4/HUMXSDTw9dn/4tq/724aX2k9mmx9OyJu3it4dOf/es7OO/8MBvFjA+f2b1/qT5+fS6deP5V8gvSR50TVuPX5oi7d52eF0z/2yxmX/Z6oP37x+efnUFfL4kdfilLb7UYMCp5+dkST7/eCMMEmDM29e4frcjGEGOEr/5ghGrL2Fdzo6+/UYA+Ie9wq/Yyx//G+XNmeFALgAA -->
