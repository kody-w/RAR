---
name: "rar-cowork-cookbook-demo-data-manage-benefits-enrollment"
description: "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_benefits_enrollment", "rar_sha256": "bdd023f1f38de5e9c6edfe45189cae4060e6d173cb3c18196a52b7effe2684cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_benefits_enrollment`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_benefits_enrollment_agent.py` and in the RCI capsule.

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

Manage benefits enrollment Demo Data Generator — Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
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
      "description": "Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_benefits_enrollment_agent.py` and embedded as the fenced Python below (sha256 bdd023f1f38de5e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_benefits_enrollment_agent.py` first:

```bash
python3 demo_data_manage_benefits_enrollment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_benefits_enrollment_agent.py   # or on stdin
python3 demo_data_manage_benefits_enrollment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage benefits enrollment Demo Data Generator — Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_benefits_enrollment',
    "version": '3.0.3',
    "display_name": 'Manage benefits enrollment Demo Data Generator',
    "description": "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-benefits-enrollment',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-benefits-enrollment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a132d15468021f8c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-benefits-enrollment'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-manage-benefits-enrollment', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage benefits enrollment data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage benefits enrollment. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-benefits-enrollment-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage benefits enrollment records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo benefits-enrollment records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo benefits enrollment records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for benefits enrollment in a D365 sandbox tenant; never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageBenefitsEnrollment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBenefitsEnrollment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-benefits-enrollment-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageBenefitsEnrollment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPaWLblX6Hv+5CZT/bVPOCKF9EggSaEhNCASGc4NUtonkAiO/97H8G9trPK9bqqoz81DhuQztnzXmsfiz9e3KFPqvbl08sxdMsF7+Z5moTtwi2DBVvdqjYDb1Xmgb8Lvyr7NvWGvmq7lw8vQdj5bVr3aVWC7XxYhq3bh90CIxdt6OZp16f+IgiLauGBe1Hadx/Dsq3yvAjLHizxqzboFlEFlC06oM+rxgWHU+QiD2M3X4BFaT8tfg7CyB3yfmEele0vHxZd78ZASZ+ExSItgZ2LzeiH+WI2dbbyw8IH2vvvlswyPzwcasN+aMtuEbp+sijD25sRP3WLuk0Lt50WWTi9AtfC0S3qPOxePv3624eXFHx++fTHi5+7Hbj0wgGfOLd3FbcEtqzfnNt89Q0IyN0yBivrCQS3BN/rsAWOFuAScGfx9u3nLsyjD4v//M/s5rZx98unz+Xi7fX5Zf6jD+XsxaKv3K4Pg4Xv1q6X5iAsr4tVfnOn7qtLIIQgN2X8+tz5TVJVL/5rvvfzU8lrHPY/f36p6jlZIHOfX35ZgAx8fmmH+fPrLKX++ZfXvLqF7c+/fJPTDd4l9PtZGLD69cvb9zexYOG3pWm0+HLUNuybLhDktA6B8O/8m19P09/EvYXky3Pxz1X9YfFjybM//wXsfVafB+T+WCyIAdj58nqp0vLnNx1tdQ1Lt/TDn3/5Z2L9JPSzuXb/Jbm/PgUnoRuAaL2FBBTpnILfFtCbb19l/nO1NSiYf8cTsPxd3ddA/TPZj8z+neg8LUGHvOfyh+J+tAH6r8Wv/9S3/27Dh0X0GfRNnl5B3Xl5+Gnxx6NEfv0p+Hbxp9/+BKL/j2KO1dD6DwlfCrdMo7Drv3z59afucfmn3379aahBFYdu8WVo8x/J/FFcH3r+EsG3VT//dS/Qb5ZZWd3KxdceWvxR1f+j/fN1YQHUC75d7z4tvu/E+QUtZifelT5D8F03dsDW7+L4y8ufAH1K4M3gP24D/PiP/1goqd9WXRX1i6NfDQBKBwCVRTgbbyRpt0gf2AccAHHtUhDYt3Wg/ucMzxZX0eL3/+k/8P2j/4bv8IzVXwIAbHNcAbJ9ecftL99w+/fXhQFkV20apyVAaX2laZ/nxQDS0xlHwy5srwCrvKkPP4KW/jh/mGH4939F/JeHpNd6+v0B2OkT/3RWnLGvG/LwdfbSTsLyzScfEEA4hv4AlOSVDyyKUgDcH4D3XZVfAXbOEemyNM8XQQrQBZDX9CSDofw0C/v99989t0s+l0+wxhdPVutgsOCrOYuPH4FrUZ7GSf+5DP2kWvz0x58/Lf7X4r/b9RA+69AAcbzlBFgoHdX9AvTYMHsM0gUSDADkkZM//nwLMBAD+HQBMphG6ZPM5l7IwuA92kdh9REjKUCuIMogwkVdtT1ggEXavy7EaPHVXqB0vjVzRFJ1PaDkOiyDsPQnINUF7nyNZFn1gIn7tIumD4uhCx9af/da92FiAZrd7X9fKKwGGKnKwT+zmY9FYHNVpiD8X2vheR0IaQG9rt9FvC72c1Uuard166R133RE7jMv8yzwth0Id2eO/lzO9BvOoXq0yDM88TxtzOPFI6Uf55yD8aQAhRV077rjt4kkWBgP/mw/l91b+btt+OB+YMq0iIc0mEnhb28l1SXVkAeP+AFLZ0lvWQjesvKowSf5fx1tFt+NNvN8sJgHhMXbUDQT7IAhKLH4/2dKmmOw4nl9w6+MDbfY7A3deeZmHhNn25+T5WzdbP2jD78NMO8g9Y7Vn8s8BYXWTn97rnxk9G3NE/+GFiRAX+kP+aCcQG5muY9qn6u3bec+cT+X76QAvFk8EBAkHEADaJ25Yt8VznffLU1A/8/fvw0Ibz7P8QAVvagHLwdpisIw8Fw/A1a1c8e+JRWUfjh37y1JQcS+92pOD4gXkL8ARsxlAojj9StQP+++m/6Xjc85aN7ymBEH0LDtQwCwI5wNnDN1S3uAW27/nMqBn58eQoAbRd3PvnugZYCnz4thGzZD2qX9DI/PuIY1gOeP8/vT0/lqONagS0CwQC/UA4juo3tmYCnAlANsANUKmqlIy2ftvgXhIdAtZigAUPtWQ0+Jj8tvDoWPlpvp6n3j7Mi8Z54AFhEwHVyZvkcM40dlAuQV84qH3r+vtK/aZtkzanYA+YDG97vPUeH1yfbPcWLxLvfTPxx7fv73TkYP/jb/WgCfFknf190nGH5y7jvlvgLMgp+2dg/6/Tjz48cnP378ASD8RfbT7U+Lf8++v4h4649PC/QVeUXmW7u3+np7gXCwH9fOR2K++7nUw2+oCtRXBSiwOXkT4PuvFPi+BPBg3AKUAouflNjNTHoD5P3gAJCJz+X3BT83HKCYMp4LtKu+A4LHLACK/5m4r1QFbpU90B3ME2Qczie3R3t04cuncsjzDy8lKL1/7cQ2M1IxF3Y3H/VAC4GZrE/Dx7cHToz9/PGvh1718cHNXwHmA0zKu++L741HZh79rkeefgL/fKDhwyJ4gDCoS+DnrHzuL7fLHog/+9NP9ezA83A3j4MP2P/yhP1/NOj4TxkCQF8PZo6w/zuu+NuiGMBQMMfTe0BH8Jw1f6j866D6j5ptMBvMSoLq00yTH95QCLyDwwWgm/dzAnD57eT2OGiXAzgU/zqfUeYcPLbMH8Ae8PZ109f/bfDCl99+YNczqF8AfZc/yJJQ3QB2AVB50Ow7pQJb3wv1W0gw8pcfOv7Om1+eBfX3Gp7kOpPujJOPkp0XfliEr/Hr4l9p7I8YglEfEfIjRryOeTf+wIqHnwDBAQ/OIfuWi28RqR5HuNlgEMH++T8Of7yAsnZn9W+F/XYGAMsB4H3s5pkHBu0PFILvz0YF9/6vTgdvMrrEBZMpEOIFAYLhERrhTBCS4dKnwiAKCRJllr4bEgiFhFSA0rjv4T7KoEvKJTGPDqMoxCiG8CMg79nyX+bhLp3tIpd0hCyXWESgGBKAvGFEEDAUQ/kkjSHu0nNJj1y63retWVoGb84+nZsj+fWgMgflzec/XjyKmOuF6MTV88XCEOqFGOxNuxN8IpfpLh5MM63148m9y9LRSxG0k274QePX5YBiRJzJukjkbToYk2P6N07TueVawzJYx+/ddDgQzVR6Ru05nbtOJ13BIrVUoqvGe52q0PHlDBPuVNhKzbcNO20MTUQurT/Jvj3ispdi7HLJHOqrTy8VHxZOGgxvI0ndhtq4IfeyVlGyskqEo7/Zl04vSOczVzjHrV2o0O6Wwew5qiVBgO+4rugTbUYOg0xyGaS80lgnxs4hVeju/lW314dcZfvNcN56m+OJNRhDqhGOJ9J2vyPPdXjZ2CvLubbH7cYnprUYOF1zv6+D6xiLo0TW5/zGkkKOBJ4WQBJLt/c1oRWtRfllS5KwymW2hDFwqdFZemA82RER2cnv16nCXZNiNiGcS2m9IfgIUqq2tv3DLp2q9nhlR8E3dCWO8hprY7lqct4R19aB5c9sopYkM4UGxG6kvLOENg0OJRvqZLKDyZiaIv2YOHmQisPZIjfucZfud5cVzcl9Tql40kH7E3avQtIt8/tuzBCugc9ity6TcGfvK5e18kE7ciy82rDpplWQzJAD2Rr29SaTjksBFXfkynBX8XTwXP3EmgYWn9wST4rQXqo3v9alIuUuqJWYx2NyL2PClnZbHmoLeerw1Y7pQAacfH9JLvywhgvSRijXivQ+TcM0uUNmZ231rakF3pTv82w4Xw+nJZFq52OkJIW52UpubmXb6kSKkZ4UXXL2tEmHHJkH7gR6NUxW0MEbmEUQugtH5VyvYUu/6o6clIc1l6W+Dt+N8ITsOJlmFel+HcUqkG/B2i4s7iRn6/Z42xOTSwbosdMpI5F3cTMePd4NrSGzdFKctpSowETF7e2zumklAV6VZ9c/3O6KZODZFm7E/XrDmAOiid72cnMtSjloqtB359LJVds2eM+I1ZBXE/JUr4eaaHUna0MtztZcrfQik2YjvO+Rot0p8JbE95nZs1dlZLVrFfkHD6eutFnCh7UuZKMPGx69nRi+PvGDyRZlHax6WqzxfhTEMk1ZrWtlp0g3u4jG1dg8OBdxGV81dhKMG9vSm8q117F9j0jL48bsbp8dcuvSGe2JZn+CKlmXNrmbxvI1S6RdAoS27lZYMyvaZielmhibqAtC6FdFyYqr/FqqBpeSJWYa5yKUBaO/LA1qfQrlHqLx490/VMloT6JodvlGtPWU34G/g9RI2+PpCMUGC4Om5xolSSPav6X4GPpyWh9ZK+6d3b0cleGyoszdWV1pHeReHG7lisKZxCgzWZ86t/UrpE4SZI3sAjSz0hW67Q4rd31NdvfxcEOawL1Her6BrMl0nV0nLrUlq8usKmU8z1/Ia+cifYjcRtTkb6ft6tJHEzfeSbLJV6p2cj3qYlj53a3PcHOa5NDppqwdx4PCY8crt+F4Vryn1hmbTr1nEd5hcvTVWVz5jhyqS8g4mdApSjbbqc98LdJPRIkE18t9NP0Q0/Vk3UCWoK5jf1f5FCGR9OoQUmFXqSwcGePOjcdQYNPOIuNb7TiGvG5v5klUUaFzZbKVRaIWViey55vlTt91l5ALQzudYr0ZFe7O4Vk+Mgi9PxF6YtaHnRGgS8Y/n6HeMTpYlKtlTbB45W2Yickz0/fsIozCNb0l2ICCadXik+CW7TL9EtIm7+9HXdZjLwmXhHGxY2tpZ5v4vDQNtkbudhx3+GFtUH7D1LXJ5ucpYPUQZo+3FJQbf1+eOpUStItoHPNhk3uuYnHyISnG0ENJmNke2RpW0iRRcp5wjv4gjXuKTyT5HKs1otQdxS1rzwL8kwrIUT5M2+HuJ2cqmlhz616h8YCVznG02G5VsBZ2RbL6KJ2gtnRSRxoq/bBfDqQLoWi6tFs5ZCEusDstWMpJvl7u85KlylzdKxEMU5Rq9NghWxspdd9q3aYrb2fLlXSoho/SHh/MMB0Pd3nZ6OUVtm6rpU10KpZcWIBXMJR6I8RfpOUSWi4H4TJCfZT01bCUjXLdxCE412QpImYr75wNEFeQAXTaJCxapCjouU1FIjRGRAnPNw19UtZt4aU7Xbpe97kt+WYG5nzXFwXc3xei3tuidtimxi0dLeMY33acaEIXvTbXbGyvj3WiBKzq2eKqwjRbLbBsk+wPa+Rmx3DslKZwGZajo5XtNptawpQEmdgrPH2/9mNO8md7LfdL7artuHC434PLUlnpCFul/SBe0kI74/TBO1i7GlUjR9xS0plpHZK1VkfFFJdX3FvGGyVVTKTOmErZ1uP5JggBhlo3hYbXK/mkxqyNx5xqWT5/8fGlxTdXehv47CTn8pnTvKqBILnEskSJidHvqh1TS6vtXr9e613iNpxb3cb0cjDQs2MBWRm5MtldqCujETGnAmc211x3D+tYOAtBnK/HxL9viCASdcZqN1FvbYoboulJk9asoRubI+qpE9vsTWODHJXRKlfuChA42xxQfA/kHQtuw9OVud2zNi8qjVdANca623SHSRL47iJg8EdZYgUzp00qeuJa7wKf70n/vEOkRk4otzLzleieEnuX72CfWzncRsLH09ZWG/0eTpftplfw43V9uFL77T28yIdu1cVQ3SEtvyP3KRrVHSdl91HIfNnMWdllPcXV6zWediZ7Ph6OS2rT+GnBXxjTdhxwMzgqtc64RL8Rz1qJnGEoL5x4TaYKVjt34SAAclynu7o9r/eRttT1dpDywNhe1yznw1Z/AfbxyYFDBDXf7XF0IFECjIVr+lat3NMWiwajwvcCd4oKg9pmNzjODItr+n2wMoQjGZnsZV8UFYsOjrSSOoC6BzXhDjURUSYn7eylu2P3yqrdbnQD3SsZATos6W5b9EANJ0q1FHJ1OVCEvxVUejSoqxeydHbzAV0XGd6SFK1e9oyosSxpNarpao4qiAG2KVZWnEAFmtrxlfDbjNSOS1NM1+1ZM5KLAZVOe5E5en00+HZPRbQgWOSFXmvmardLm3xTayXnxEZ/sxX3ZCm2zayXG9iDL0wA2mtjby91ZuQnW9FQ0VsyOXOJhZ0D6dxEkWkaSxKcxVdIpKqclklzV5QMc65Oh8Jwt+tjJrIIRWLxSpdaM26ErSnp2ik3K5/U4BCQNlvxG9wL/ciqxyXdbLWd2l5PaIUjNSLbFzjRl8TaZB0ekeO14IzbqTjEZ4ff3+pKdnWcHG+GWTMMtm1W1UnQSpXL3TrehltGQqmlWzpiTuhdrBTHcEzGoyAh9MagWa5u1rvwPsBHeUz0Lt9vOyD5EDRVxQoQpBTi8Qyiw3S7quFl59gcsfNQiblcSR6GShBhBGyoCXca8q67Gxhax35JlYN2yQbAPSXvb5td7TSeZPGeWlBtiyEV0xotqhFF7Emuk20x6shm57Un3vBjS1dpesK13L72yo3sQPrWDSdkbZIy4+YWo/JSZPemeJDY03k/bjZJ4VpO0vScXYzORtwg5nDTW4SOesJ2BP928taebw2qlWFHo2Wxkw8TS/WsiHl3Wrcdb5y6otKs/nA6DJuA4IIrvk5luNnEN12t0aK1NQHe45a2yTyt9IglOORcL7SHhdhA4zZSYxCU3o6gZw4ML/HOdMTapMuw5ggKt4lit9b98yrJ+mbVb1RsfT5E8eboXOPTzTdcg5JWtk7g1YHGK5U8JYIf3HXzauQUpN5RnTtOYpZflTQkS/sA5leZsD2+2xJ70Wh4zpSOdsS7UxrJVz+Jj+VSGGkSuTKQdkfocMBb/Ag1jmAu93tHWiuNhuVLhOYv2mYl6Z6l86OJu/voqLSdZTH7rlCXh5yMnYaqu/N1tBUwBu8BtTpMvhf2u2LXoJO0zbeOx6FaaAk7I8xzjb9Ag9TfCKaR4POZZ61DiYXB1A3itdi7BL3l6/4WQlIZl6oiHGKzmFCW17TTOh79Y8nH+JDqmsim8DTw7KE3EwdJwYgHF8OtkJRc064rX8OkXqaqyWp2/iCe9CnwwuHgJf3dF9H7VAanaQVzlob5bVTf7Iqzt75ymOS6z67VeshPBOLiK3kzKktXwE1seRGmvNidWUNMnJV34sazdJH0XSvXB2MliGMITkstXXQmZKG4QWIwo7lgCkSjVe2zhHhqIgOdOnlCG5pai8s8taB7i28EX0pyLVXviCsUaK70jg6GAb+N++YOI3ahHA3UxXRRcQo42DHJlVNRu+l1AcKuGTgTUbRxb5PLzaqdQQknLFB7w2yRqDmGTL0WBINPuW0qC5gHiz5Rh0luTuR9AkOWZA8XKWszIW025+BA8rR51v2+upyO5zO2VehWK9LRhyYYQDs8QocVtF2epvN03KTLJHIHrPUBKY1yrxd4bdBpKQthHTZbhyvdix6fKyoQhmR5Qo8NfnWWrITEzHYst3tb0ak9hbhrrd7Yd327raFTxkTbizdFHJXfndPhiu96MOy7W2gs7RbDeHWHXVMC9tp7zGeRqVN4SZA0Q3aCUWNS3l6Hq0pEjU6vzBM4IAeQgSBbtQPA7F3VUGA2pO9Mu+WJzHNsS2eCjlKkbBz2m8C8O+192FJ9wMNrQqUSGaB4FjWHYENaBCXSB3eP+VkjKgffxM8XBm+r2WAz8a6tniDKPq2Xd0gnjmWZ29Q2ymAZlVDbK+vO3hp0tJI8Fxvbdu8oGOMmFHOLuMtkX9I02nX7daOu6cSAl8clPDawM3HxRUbPETyh0C4wTF+G6esYnHzpxB4yho1CndnKsnBJqB2swAkpdpC8h1NjuhxXVGQo0JnaaiupPiCWf4C5ZFqRYqzfSmkrQN3EV0sXcWWruF/PZruVzOXJO4RBLK/Ha52gbIXVUYHzsnobu7HuiZvAlXBBGal9tTcqvr1FmcJnnV2ZEa1RLkX73S27VJc7f4+Bs8PIB/IqzC7HUDIvFccYJKxAVNirvV0Z6nV/ttAbOHBkdzPsqxMuI1Gtm8xwbXQM5w43Is3wlTg5K3MCPI3f00s7gKVg6kmEsW8jU5QpcEMpZM3T7D4AFbOFKrce9dh18G4HCq/18Ar1SO58HieF1VB1OitjCG9Cv9WJBBxvL6idJdu00xmf56jw3oqc3PtxxmmAsU74CcyuuWQYRnAcoVoRPIAxp6YynM3d3rBeyOs9z12TBq3BMB5i3Q3ytUO5nspco863YhmOGuqrYK5f0mXjQ+Y+cfQuEYczfyw8RDKKIhAKCV3C7CHGM9Ai58DEBMhz/KnzeI8ZypFk6Hus0Dy0pmo1k8dA8AdyEClEENXdOjBEEidxzpMhQDKnsjmv7+w1qKlit2yVJYOiiORJgT2E7hTyCXfhJoZYRV63oREncE6mFWrwpjP2I6nf0D2hkRbf2y51I8uDdDeKyO24wm+OgUPerT5Prvqej2TvmE3cNiub1SiQE8q1KIwVu2wtslVH7enrfV+NO5FjkKgjL2cpMewDwvf3RNaGNKyxDVMrgxUcZJReCYVwvou3ysPJq31tfKqhovOWtIbS9ofKadTIvZQQqtIl1yPDMUhJcDqiIM4fuLDcxKdohdplaTJkYcPt1aNJSaUggZqup3hoCFy1vHUQ5iN5Iu5HAAbMLroVsDlmDTP0e3tId1N/zomcarEsVNQcu3MVc1G7a6cafmjfwXyFhz0HnXUyaSXyFpAZwTsib05dTcTo4driTtKuO75CWZ+mesDH8OU03QYk3tpSsEkh1d2KEDLCAmHcfSTQRecGZ2yOoFqOS4cRJbNYAHU0BOLWI0uzK/pJ18ebGJH1lkJ33JaxCwzRsd4sxx6MjSeZn7SEQQtlhLHmWhWMRYdQzB8Eq/aP3sCKhnkUua7tNlpvnmlFcGBBznVwjBfBJKjBDLymNxTimRZUWHsC2e/soA6KEstp1bzUPdJs7laxzoYderFRzwXT83XnHfsKO9tDoKXWWZ4wFg2xSzHtCH/fara47zO9UaHkzHMqjhV3UIi8BSOSAIYCDK3Fhr4z0NnfErYunVWOciELoh0Dh8cV0nfgSIlT000/1KQr1CpXndIevWoF06lTkafuloSOgej7VOe5uk5BXeT2d2EP9TXeH8j6AjFE6dL3PdOQoYDvuhKiubGdsjtCIpTISdv7psmWkyhEm5104+pwEK6wDAWCWjYxPKWXkDBOlbAL1YZzMNpdWipQBnu51dF3IpNLpUwY8wiftANGB2aOeqWpjR5VgMQSABcrbMzsvrop5lGhAtpu71G6w53Q46dlytxU49xjXN6HEIqL8C1cipt8cNZxYwD4CEjcUzQbG+4kHVuVP1JrYh0vx0kgtmKnEMkmuAh3z9+tVnTAX+6RhF29+6lH1xyA9y0rcjhBRSJapK06YLDJQg2f3TBiRDlMvt80S0U9ApraBiOKa6lqhZNvjSCocFilDyeoH24WBsGrYElSnAqD00oPMeWSJYkNF11XJGCodu1hk3lidUsIgr17kiNwLDQOuA4z6qrxSJi9Bw15sWgwrylofF5SHc6jfkMPPR+6FtFDhePid+WMidopveWEV9+Y47RkqhG3bJopg20UaGsA3UTsM0fukIEDDZ07JFI0q0Yk5GyI2xtxdXdGjHenwPDCPpBYIxmF67GILg3XJ3td1g8RzjGVkGUxrV7Do0oeTnQgtB4zYRuXrnHYvKK1uhUG2QsZN/DKzfXu79ekfpbX2ACYHFG8eDgvEZ6AXMSkUrkQDltLDQ11CQ0uxJyi6IYyfL2i/fWxhCebvxapYXqS48qn8YogKk2PiaKJirE/tJqlqOrYMty5v0zwqj/Eq9XLh5f50djbM9l/6+dg89Oc/2cPlZ7Pf95/6vF4/Bi6waeHrk//nlm/fXhp/RQY9XyA1uVD/Pao6e8en338Vx4CzhKm5y+t3p84Px9j9248/xb5JS2Doevb6UtX5Y8ffIAd3tDNv13s5p+3+uD9++eoX50Bn5O0Db/01Zc27MGnl/mHhfPPOMIgdfv3r/HbE0WwcwJpSv3uC06RX8K2nj19+7EAcBB/RV7xlz//N2QI8Jg+LgAA -->
