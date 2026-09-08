---
name: "rar-cowork-cookbook-demo-data-develop-product-roadmap"
description: "Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_product_roadmap", "rar_sha256": "c4c150d187ff413ceb23b91aa4d186326d23b3b8f45bf097fe22528671c541ff", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_product_roadmap`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_product_roadmap_agent.py` and in the RCI capsule.

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

Develop product roadmap Demo Data Generator — Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
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
      "description": "Sandbox D365 legal entity to write to (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-develop-product-roadmap-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_product_roadmap_agent.py` and embedded as the fenced Python below (sha256 c4c150d187ff413c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_product_roadmap_agent.py` first:

```bash
python3 demo_data_develop_product_roadmap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_product_roadmap_agent.py   # or on stdin
python3 demo_data_develop_product_roadmap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product roadmap Demo Data Generator — Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_product_roadmap',
    "version": '3.0.3',
    "display_name": 'Develop product roadmap Demo Data Generator',
    "description": "Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-product-roadmap',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-product-roadmap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2be93e44b869a0f5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-roadmap'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-develop-product-roadmap', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-product-roadmap-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop product roadmap data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop product roadmap. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-product-roadmap-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop product roadmap records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo product roadmap records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-product-roadmap-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for product roadmap work in a D365 F&SCM sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopProductRoadmap(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProductRoadmap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-product-roadmap-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopProductRoadmap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaSLbmX2He+6GqLvarDQnkGzdikBACBFoRWsoVLu0S2velpv77pADbVd3Vt7sj5tPgsEFS5smzPs9Jp357s9omzKu3T2+KZ2UL1kqSKPSqhZW5Czrv8yoGX3lsg78LJ8+aKrLbJq/qtw9vrlc7VVQ0UZ6B6ayXeZXVePUCxReVZyVR3UTOwvXSHFw6eeXWCz+vFkWVu63TLKrcclOrAAM6L8mL1MuaRZQtrMVuzKw0cuoFRuCLGuhh58Mi8QIrWYAxUTN+WNSNFYCFmtBLH3OyBTM4XrKY1Z01/bBwgAbNH4bsgLAPD6Mqr2mrrF54lhMuMq9/KfdDDTSLUqsaF7E3vgPzvMFKi8Sr3z79/MuHtwj8fvv025uTWDW49bYDdu2sxto91RefVslPo8DsxMoCMKwYgXczcF14FbA+Bbdcz1+8rn6svcT/sPjP/4x7qwrqnz59zhavz+e3+Y/cZrMJiya36sZzF45VWHaUACe8L7ZJb431N3ss4JUqyoL358zvkvJi8d/zsx+fi7wHXvPj57e8mKMFQvf57acFCMvnt6qdf7/PUooff3pP8t6rfvzpu5y6te8eCBwQBrR+//K6fokFA78PjfzFF0Vk6NdawMNR4QHhf7Bv/jxVf4l7ueTLc/CPefFh8deSZ3v+G+j7TD8byP1rscAHYObb+z2Psh9fa1R552VW5ng//vSPxDqh58Rz8v5Lcn9+Cg49ywXeernkpw+P8P2yWL5s+ybzHy9bgIT5dywBw78u981R/0j2I7J/IzqJMlAeX2P5l+L+asLyvxc//0Pb/qcJHxb+Z1A0SdSBvLMT79Pit0eK/PyD+/3mD7/8DkT/UzFK3lbOQ8KX1Moi36ubL19+/qF+3P7hl59/aAuQxZ6Vfmmr5K9k/pVfH+v8yYOvUT/+eS5YX83iLO+zxbcaWvyWF/+r+v19cQOw536/X39a/LES589yMRvxddGnC/5QjTXQ9Q9+/OntdwA9GbAGgMv8GODHf/zH4hI5VV7nfrNQnLwFWNoCYEy9WflrGNWL6AF8wADg1zoCjn2NA/k/R3jWOPcXv/5v5wHwH50XwEMzWH9xAap9eaHylxdaf3mh9a/viysQnFdREGUAkOWtKH7OABjP4D0jqFd7VQeAyh4b7yOo54/zjxmAf/2nsr88xLwX468PnI6eyCfTxxn16jbx3mf7tNDLXtY4APe9wXNasEKSO0AdPwJ4/QHYXedJB1Bz9kUdR0mycCOAK4C3xicHtNmnWdivv/5qW3X4OXvCNLZ4EloNgQHf1Fl8/Ajs8pMoCJvPmeeE+eKH337/YfF/Fv/TrIfweQ0R8MUrGkDDkyLwC1Bd7cx3IFAgtAA6HtH47feXd4EYQKULELvIj54cNldB7LlfXa0cth9RnFjYHnAxcG9a5FUDsH8RNe+Lo7/4pi9YdH40s0OY1w0g28LLXC9zRiDVAuZ882SWN4Bsm6j2Ab+2tfdY9Ve7sh4qpqDMrebXxYUWARflCfhnVvMxCEzOswi4/1siPO8DIRVgVeqriPcFP+fjorAqqwgr67WGbz3jAjjo63Qg3Jqp+XM2s643u+pRHE/3BHOjMXcWj5B+nGMOOpMUIIFbf107eDUj7uL6YM7qc1a/Et+qvAflA1XGRdBG7kwH//VKqTrM28R9+A9oOkt6RcF9ReWRgy/O/7tWZu4JFnNTsHg1QzOvtiiMrBb/f3VHsxO2LCsz7PbK7BYMf5WNZ3DmFnHW9dlVAnUeVj0K8Xvv8hWfvsL05yyJQKZV4389Rz5C+hrzhL62AhGQt/JDPsgnEJxZ7iPd5/StqrlQrM/ZVz4A1iwe4AciDrAB1M6csl8XnJ9+1TQEADBff+8NXjbP/gApvShaOwGh8j3PtS0nBlpVc8m+Agty35vLtw8j4LE/WjXHA/gLyF8AJSJQhIAz3r9h9PPpV9X/NPHZAs1THu1hCyq2eggAenizgnOk+qgBwGU1z44c2PnpIQSYkRbNbLsNagZY+rzpVV7ZRnXUzPj49KtXAHD+OH8/LZ3vekMBygQ4CxRD0QLvPspnRpYUNDhAB5CQoJrSKHvm78sJD4FWOmMBwNpXDj0lPm6/DPIeNTcz1deJsyHznJn8Fz5QHdwZ/wgZ179KEyAvnUc81v3bTPu22ix7hs0aQB9Y8evTZ5fw/iT6Zyex+Cr3099teX7893ZFD+pW/5wAnxZh0xT1Jwh60u1Xtn0HoAU9da0fzPtxZsePr4r/+EKCjy8k+JPgp82fFv+ecn8S8SqOTwvkHX6H50fnV3K9PsAX9EfK+Lian37OZO87poLl8xRk1xy5EVD9NwL8OgSwYFABTAKDn4RYzzzaA+p+MAAIw+fsj9k+VxsgmCyYs7PO/4ACj04AZP4zat+ICjzKGrC2O3eOgTdv1x61UXtvn7I2ST68AZT0/oVt2kxG6ZzS9by5Az4HjVgTeY+rB0IMzfzzz1td4fHDSt4B4gM0Suo/pt2LQmYK/UN1PI0ExjlghQ8L9wG/ICOBkfPic2VZdfzggNmYZixm7Z87urkHfCD8lyfC/71CyosHZhz/ExnMoNeD4ph3kIsfwc7TapNmoSqX/U9/ucy3PvTv19BAAzBLcfNPMxd+eCEN+AZ7B0ApX7cBwLjXxuyxic5asOf9ed6CzN5+TJl/gDng69ukb/+bYHtvv/yFXk/3fQEcnf1FPPg2tUFaART+E58CZb8m5HfbUfyvLf9Kjl+eifO3SzwZdGbWGQwfqTkP/LDw3oP3xT+t3o8ojBIfYfwjunofknr4CxUeVgKMBkw3O+x7JL77I3/sz2Ztgf+a538n/PYG0tea134l8KvBB8MBpH2s57YGAjUOFgTXz2oEz/791v8loA4t0HkCCc7KQXDYRTZr318hmOPZKGaTiGWtwD0CQwkXXGP2xl/htg+Ta99DURzdEGvEwVeI7wN5z6L+Mjdv0awUDkbBJIkCeSjsgoihK9fdEBvCwdcobJG2hds4adnfp8ZR5r4sfVo2u/HbLmT2yMvg395sYgVGHlb1cfv80NASsSFtbY9nHdLhzZD0N44ztZw/N2ZzqfhBsVCml3OmFgW3anrKUCN5OOv7S5aEA0ZdePpAUCKq+PnaRO3jUdXNa1XZ6GDw2ziITKC4IC+hzbS/DxjDDtCJG9I4re89XxJb1fPKgzZtrgPG2VEqQOTlVqXO3TmTvAMJcOdPGmTSrCdSGk4KQs5x/DbcSZsEZq1wdTMMbdT18q6hThnv90zkH9iNAg3NnrpGJbr0ovok9qlOKI48rh2HNojTyA/mnrCWg3pOZQ0nrtGJFwNj2rtm4Z8bEXainnb2lCWtcMo+jtRRD4py6otQVHZ39R43mi2cHcpsRH3K7EgV0E3viQeCdLMTMTj+NV/vR7sWzYlcrWqejSKKV9qzWm0KPs0vJpYIeCTl8vKUQnf2ROy7A53XJcdkQ01hLDwxBzyVy1WUnoow3W7D/SG5hHJ23hBGR5FUzPQod8eGIriG4nHZ77FlT5p8fjJqRRj2+iVaRjy1H9hkiNwi00Zyb/dLnz1PNswiHBTnqU/tz12CSkMv8iWr8mduzHaFTDpB5Er0Pg0VszjG1pohFYsuhImMqVVwIreaQW/Ljc66Eiv51sEvM4/FeQmuZDyN6evJu6vaLdydM0KjKCZt42zZ5th22tT1eDdvtyiYhHTrE5imprbeFUlIo2U4cbqI3GRGPdyMERFTFdXaPiE3oV3k/qiOFs3EPFdOdH4kVbHsp+jauHfi6DO74zgkXQ4rpi3A3minNrEfxBXBw9JUFhgg/D1S74PhlMXXDYyFEC2hXb/jvPXlegZe30tIk0gJWm05uNl526TFzFsFK/FqjPDzRUoHrUptc695yjb0xoOwtOr+xvoRR9+gnvG5a8Sy+MB5m7DayHJ9zKIQDfGdWQu7a0dFFJ65zd2BmCIaJ+NuudS9H2BR2Bx5RNhb4j7ZDUsmOAanpkROZJXMf227KLtJHDxrMvdnyZ8uctc5vmesJzyYjBSSyFE4lRuIPYz8bSVMrWz1iHxUCNdmqUth054mIAzjmcptcKWL5t8rV1o7vUZtQknizmRHHfytBSxcUWuziJHLnp1IMx5hrfT0qqHg0SHUWmMipeDUfEPnRa1LRuD2lpJJ23Yl7vvsjhsR60V4TdnOsdgGtLnejEwMNSaf7lHAGcMFsbutGSsAEbtEO6byXajv0q0wCBap3Z2lsWHTnko6iS7yUioV6JJvdsQliiDM7UHBsTobniL2ZlE3HJ82lRoGPMfUKa2j3lmuw8Bl6HqEHG4bVxp/a1VLGo7Edr1viZELt1qUc/B+SV+zKLkU7BIBhSseE7BPn06useXlc5uYCUUvx+uOvtVYx+tKUBquFW+72lcO03RCqiLgLjrh4/fKTCYrNaEyGzlv24zxfURyZoeOFcVMwnZzTfVBPaa3tbL2NFhJpevm1LM0tUOwLtLWWbQmj0Gp1lNCEBzEWDK6FsW9DPy/Zxm2w1VnxVJ9G8LnIMs6mWoKYghWZ5IUmabc7WvnyA2HdEcnYXjJ2Y4ynWCtegPgvzq/R7FG+SlsVXDDtCO/4nHcOnM0WzG9eBE9RT9M1xrxQ3avJNuGx3RsGBKIIENh2gTlHc2Cg0vV1+k8arI8NJaJk8sTsl5O6z2G9KIQJfaGkbfrmox4YS/F2cE4dKJHHOXKOi51ZefF2OnkWStzp47aud0V1+3NieEDJeaEMFxqn6IMuUfPd7yvJMilDlJ8NqOKHhPzwG1dTgK9aZP2S29sG1ioZSkPrrsLcxREYZ1eTGW9Z8YsXt9VwoG8+l4FCqdQI9vn7Yk5R/akWJIWVvs1xlo9TmtCcQu2vbIcljFyWnEd4q6v6y1/Y89UXaBnTetqvURMWtX7c4mEVVWoTn0s6nqlq6uiMbPlysHk0e4mZsVZOmsUZJBclleulDkRFonbqW3QO8wKjHlwrxdyva6BBditQGHGuF7KIFOgbF0tr7o+khC5wTrI8aqCLFuSVjIq9byllcR0zxmSbcekt0sTeaPH9y2ilWiUH0sqtHlyeyTCosmX+yVVnppViG0s277dFHF/6qsA1rUtmd21UL276tUQNabeF/ttkHO0kEk53FDyVqMUMxFcija0zSVHREVIM4Pc79uEPtP2ITu7gtWqa7YIjfxWGavK7mgSY/1U39tmaW6gjVMK6drfT2fM2l63+2FvuvKBF1q76bdsXGLn2LFX6jFWyBXgrlVCjeIlGjp9NwVHuOXUE5fUxuVQbIdJ624d3EC8vdtT5W4XjOeWYsyb3hP84CeObfm1VogDVzBFxjdtUBVw7isgzFeRKce8GZmaYpIjtLxxh2N+OkX3U3UZzvuEUrcnTmOBvTmuDgwPERvMz+O43ClCt1of9ZjNW8ZAVx1Vmdwuuht3kgtiNA1XF57RpNE6GqWX4Jpxk7nSSB0z5Tb9VqKYUBqsbauXG8xyJmNb+fS2yBWpJ5Mxhod2JUu17A0nkYqvXkyqeK4HIhkZsbzDjxy/q1ik2wWDF3YyfJBvToVn3l6t1dochSG4SIcr6yA6UtgnlCNqCb6a5w3CbQrG6YhLsu0jYouzZHhb7zcJbnVqu7srJnE/s3tOCQ98uI/5A7F3IkelbwqvkBZbWkpS3jeqtjL0i+Uql0LfwAN3kUehKwxomaRGQOFRjRbGdJAO3dUconNRFBQEOh9TrtpT4173HUXvHOjWgB5DSoN+Bx+EGwdhSVsgPZW11DrPt5a+X3rZCTa0e3jvJhOhR0MflVMUtmhaB/uqcs4WJafTVXWV4cLkDBKDVmon+TkM83vulCZnr9mHbLxFyjAtxjQ9bZh03aMGPZaaviMPm9SS5MC1WjrM3G01XUskENBWZzhy6etr+NYFVGBJXH0bFRPa9qdTIF3gUk6FFIm0oMudgspOo0vnqoHuctxW73eM6FZ3/XjNKGXyMoGobnt9098xitb66hRxUpFDZ8aWDvcxha96Ukm6w6MHCMIihwrVm2yoQnITbme1h+Cmw6LrJEhOc8eP/LmKTlwLx8uRa1c6F+lOlayWnjvJUeQqN96KT5zUnqXqQFOUGrUKHZsuYdGtLlQB3vrLW+Bs92ZTCMslTnTyfQfdCs3zJ7QqZTK5HomBgYjCErmwlK6BHlj0QJ8DONyi/WVKZKnaBN25ipemTeBocg2DQPRbC6dR2a7VQrJc3sGno7bcHRlHTI67jYvhKOLcr717Oh9HOI9LY6P7NzfI4nDXwkR6uvDNqS13A16mkZEXZkWNXGQlaBm4yVDyg7ylNbJR/HZnEdfTaun7Ox6HDtcRZ7tORYbNpplsoRinfK/zJXLVyqwwj5jOe61+2Fu+dgL97l0+Xe2gxhRJux90e9+Oiu9sNEXDy5IC24EDw0p7SVgZcMYOrBHlAq50CgXIgNmuOehEb4NLPSkVs0NyDEbPW3ebRAlKNzd9l9vLa69MlHTZA1kGzkyWuWRO5kZc3gs8MhR6clj5YPrERAeVDod6iO02Z55Flvuk2lSKUDBlpVm8Q/oO7Ki9d94MdndPlhCEHKxbk9Ww6hGe3zCUr1dRuzpdz3hwJzXdZBsVtEDrmyhVSmRM4RLxVTQ6oKhMSRrARGMd3LbOwboSpy0qj1gS4FgS4pJ28MlxULsrQpDi1MiiEh9juWMjDZc1P1RTxrhV7OzR47XcrtVE4fwtN0Y+125CVUn5w4Bd4GYDLc81ZjZYhalEqR+U5hIah1AouTQhYYy+X7hNnHdldNfPiFvElLKGanU/xXWcAuan9rZGlx5rs+tJCpR4dyWvpYad1PDmrRUudoTbbXcNRCxOeM5Pcl6Ru1CGfBpdqd5t0+X1neKCqRIFfH9juoltNjcVxGxN+LCM5M5xdwyYdERoVhR1OccdJWODQxsd/VwgoG2G3My8D2GzWKbCBmRicRH9iydqR4grs9vN4qw2P0ujk7ltDdS4S2dkGjMb7EbJHX9BbcgtKq3caZR7kehTsV1lTSAiK3w5XG4Wi8koGWVjktgGet2HxtbKdoN5vh9P55QrQHkdtoPnVVrVZ5G+V0dkREJyWvYntad6AjSACtXHahFWI2yscNhl7qN22jHXZRGT913T50joqZZ+pJANqvDSxgNIQ5N1czsf7KQr9dNYpx0aJuJE052sLU/Hehj2tanK0JBN6LqWza5AOAw/BbnMXh2L7FQDpK4wgD4rhsKw6ISellhaMJOxjC+Ok/do6vO744G7n7rePg7GSjqXx6BBkWvc5OMqHH3sOOI4J8oGhOQxeoTGWrEVhJ0uKiR79x1KwaqCQPIO7D1FNOGD5ObokmBfb6MKdSdR5fdSD3OIigb9dCQ4UjhYlsvpms/tcpOvYAZjqOkgaCK5atiVHVzzLWrLh10Ba3HuHcY76kZlPeVXN9F3nXnp3QNbaNhZtljPgGsAP3YFtQc6s074Sl+b/rSuJwAEpyzvtFZYLc/SVN3PSJXx/m1NhHcJ1q6cl+nscrzkJ9zES4Oo1tRp2uHmkjDPV3fnqsJKIttE2EPZsMXWvKZbGXb2JbLRuTyNmyxk7nc8D3aJtKJLIvNqFXFb6DIybXZKSJsUlQG12tQ/KRVy5i9NA22KrVWdBxQVK7Okw4DULAxBMoezPLdeubke9vhB3wZd0qNodugRuIXczofgM5S3/H0njLdOn7AlB1EGbMEH9UpCZ2sivT1lMgwB32tuZ4iHK6wp5nrXyjdStZE1lBuReNgS99umFST2qvKFxPhO728j5QidYNDT48WFrAW24CPELPF0EAclF2/a5pAZTjPx5FFcyTRir2B8MKfDhT5efI01HB/HRunGE+WArhJ4g9RjTA/syT9B18x3E+2SOs5oY5vj3ePLZjK37BQLylCCXYnf4u3pjim3JZYiWjfhmdi2XGQ4Sz9CisMS5+6kJcRxtaz9RkJFVjIvQXqIt8Mxvg6rJQdPRF0Id9tn5PNdR5JSrNlTWeFsje74StfqZoK8fVkbYBceElu0XlupvBbR8oahWzPsp41yQT1BFwcWYwcnV1a9gYOY39SCuV+o3ksz8mia+3vCBDIx3GmS4I0rj8sbC/CqEPIZkQfqnad2tlSCKjpbA7tsdtol8y88p3hnye0sqh79vsKHq9IEcOm5UBWuIL87M5tpQkLtzF7iszB6qDIJA+/w55Kk6KpdCYfDZao2u12XBtVkT60KeMDtGELsMMqjDtftoDsQck2PhV2fL7KDBaY5GefUYNvsgq9NGQndgczOR/FI4Y1/GfwrmXbpsg3W5sVOqknf1dTpIpl6prIEV4fezi9prq36o5NFJ/TELb28dUCFIcKkpSLPyILhTNU1rOGTMmGUkMlFTY7H4h4bdtzKhhMQVKqu2jQwvQ4dh03Pb/cHRDq4iAkCaUiH+E4SomVKF2vk7rC39WQy1hGzjpMTCYvWSWuPDNmfFTuCJ2PJEzDZYIp2xfguPcH4NEwuIsNr5kJiOGTh7himUyxfEKjWvUM6VD3uRPfVEhRynU2sojf2GtKQk36AshtO6rdCKkyiYiusbztlhZVAhHDTl0y3ytRCjG9IB8cn/1wZ7VZ0LeSKR4iQWq50dGBjH0/LQ4eeiwazY9+/0uIlcSnxDh3TfmIoOr3GvsqUN9xYw6Zz6UO2sNem6nsh62iQnhABZfVggyKOk5Ts0cCfliPt6FPE0elhE6hjmG9wiGPZ/AI7RKbwU451+qUkgZ8UTxRO2yV/qbW7c+2iAAVeGQkY5ZoeMfCgvJEem/XadWlxy6jqr93aYuwtr/E9nq5OA6X0PT22PQMh23XTu3fS4WSWsGp/f1htIN2ha6yTm1DHTXUdSmpjowhq+Zbd4AqdYGMu87lDK3mONWvQZMpZtmkKDp3M1Cpg6ITkxdkQb+uSNY9QM6KXwQrQ8coaGLGPDWHdKSbfegWODed4MyGHSksi+34648WkDTKbxL1QVKS2bhrBFy87RVt22u5anAd+m91yL865e0tkKiGY197mbK3I1azgsTCcKpkv2EOFjmSJCY7eYlmLU6kmEtaol20N9SWy8px26WEXkfXh1Ezdtbo1mcJIjKiTHXxF8RzVWEXfYWt9ynx4Fe8gWTV0ydpsTW2mCwar7Ka4loeb7nQNdvL2J4dIHNDlYyW+Lg6gfFqQcfGBEw3+cAPQ6N+2qEP0NXuLI6qSQ6txbceA1rTtYIdAToelwQu115wntDC1A63jh7i50/yeNib+nguJ6x/ScPJ9g2mm8iJJmyMrAK/0IRNkqhA52+XtjNvbwy5H2h0uJpltx+vb0dn0K/Tii01VbHaaxTkEYTfOmTh6yq7q9qro5GJAqmskCw9Em69Ha+nkBKg1nke0xIfXzcEnYJsSfXwTQshkHIkl4rDYmdjD5y6Q3GFDs7tydPjWNl3nlEgOoiKVY/IphPM7F4Pg1RjWWS2KaJUKuoOUwdXbZXo6OZU7VAqRm0WoR9nSDitdGDApItu7rIdleu2nM5Z1O5fyGxR0e6Susjpxv1O7Vc/T0jE4l7c7plk5nQdB6RG0eI7IUyGA7YWD8MkKgfOzoDMOaZkbIedQBjlWexneiHTgK/S5IfjhvE4or2G8rpsOtlxFqU96kMZsNC8Pu3WYYG2tkfx2c0iudX6wpsHrnLGlm1gMriGeuUp5bA03kFXc3K4xgqwOoQlBk95b6q7t96wDBZKxLE+8XCdRbuqsv4RXnVgLvRNM7J7pNsiAE+i9d2FlY93WviRtt28f3ubDsNdp67/+jtd8hPP/7CTpeejz9fWNx3GjZ7mfHmt9+jd0+uXDW+VEQKPneVmdtMHrcOlvTss+/tMDv3n6+Hxx6usp8vNcurGC+Y3it2ju3Ztq/FLnyeP1DTDDbuv5JcR61tAB3388Mf1mxvOoNAqyL03+pfKaqPLe5ncE59cyPDeymq+Xwev8EIx/vTP0BSPwL15VzIa+zv+Bfdg7/I69/f5/Ad+wSHcKLgAA -->
