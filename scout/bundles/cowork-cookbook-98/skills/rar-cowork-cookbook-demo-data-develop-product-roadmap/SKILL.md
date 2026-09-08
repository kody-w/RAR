---
name: "rar-cowork-cookbook-demo-data-develop-product-roadmap"
description: "Generates 25 realistic demo records for product roadmap development in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_product_roadmap", "rar_sha256": "c4c150d187ff413ceb23b91aa4d186326d23b3b8f45bf097fe22528671c541ff", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaSLbmX2He+6GqLvarDQnkGzdikBACBFoRWsoVLu0S2velpv77pADbVd3Vt7sj5tPgsEFS5smzPs9Jp357s9omzKu3T2+KZ2UL1kqSKPSqhZW5Czrv8yoGX3lsg78LJ8+aKrLbJq/qtw9vrlc7VVQ0UZ6B6ayXeZXVePUCxReVZyVR3UTOwvXSHFw6eeXWCz+vFkWVu63TLKrcclOrAAM6L8mL1MuaRZQtrMVuzKw0cuoFRuCLGuhh58Mi8QIrWYAxUTN+WNSNFYCFmtBLH3OyBTM4XrKY1Z01/bBwgAbNH4bsgLAPD6Mqr2mrrF54lhMuMq9/KfdDDTSLUqsaF7E3vgPzvMFKi8Sr3z79/MuHtwj8fvv025uTWDW49bYDdu2sxto91RefVslPo8DsxMoCMKwYgXczcF14FbA+Bbdcz1+8rn6svcT/sPjP/4x7qwrqnz59zhavz+e3+Y/cZrMJiya36sZzF45VWHaUACe8L7ZJb431N3ss4JUqyoL358zvkvJi8d/zsx+fi7wHXvPj57e8mKMFQvf57acFCMvnt6qdf7/PUooff3pP8t6rfvzpu5y6te8eCBwQBrR+//K6fokFA78PjfzFF0Vk6NdawMNR4QHhf7Bv/jxVf4l7ueTLc/CPefFh8deSZ3v+G+j7TD8byP1rscAHYObb+z2Psh9fa1R552VW5ng//vSPxDqh58Rz8v5Lcn9+Cg49ywXeernkpw+P8P2yWL5s+ybzHy9bgIT5dywBw78u981R/0j2I7J/IzqJMlAeX2P5l+L+asLyvxc//0Pb/qcJHxb+Z1A0SdSBvLMT79Pit0eK/PyD+/3mD7/8DkT/UzFK3lbOQ8KX1Moi36ubL19+/qF+3P7hl59/aAuQxZ6Vfmmr5K9k/pVfH+v8yYOvUT/+eS5YX83iLO+zxbcaWvyWF/+r+v19cQOw536/X39a/LES589yMRvxddGnC/5QjTXQ9Q9+/OntdwA9GbAGgMv8GODHf/zH4hI5VV7nfrNQnLwFWNoCYEy9WflrGNWL6AF8wADg1zoCjn2NA/k/R3jWOPcXv/5v5wHwH50XwEMzWH9xAap9eaHylxdaf3mh9a/viysQnFdREGUAkOWtKH7OABjP4D0jqFd7VQeAyh4b7yOo54/zjxmAf/2nsr88xLwX468PnI6eyCfTxxn16jbx3mf7tNDLXtY4APe9wXNasEKSO0AdPwJ4/QHYXedJB1Bz9kUdR0mycCOAK4C3xicHtNmnWdivv/5qW3X4OXvCNLZ4EloNgQHf1Fl8/Ajs8pMoCJvPmeeE+eKH337/YfF/Fv/TrIfweQ0R8MUrGkDDkyLwC1Bd7cx3IFAgtAA6HtH47feXd4EYQKULELvIj54cNldB7LlfXa0cth9RnFjYHnAxcG9a5FUDsH8RNe+Lo7/4pi9YdH40s0OY1w0g28LLXC9zRiDVAuZ882SWN4Bsm6j2Ab+2tfdY9Ve7sh4qpqDMrebXxYUWARflCfhnVvMxCEzOswi4/1siPO8DIRVgVeqriPcFP+fjorAqqwgr67WGbz3jAjjo63Qg3Jqp+XM2s643u+pRHE/3BHOjMXcWj5B+nGMOOpMUIIFbf107eDUj7uL6YM7qc1a/Et+qvAflA1XGRdBG7kwH//VKqTrM28R9+A9oOkt6RcF9ReWRgy/O/7tWZu4JFnNTsHg1QzOvtiiMrBb/f3VHsxO2LCsz7PbK7BYMf5WNZ3DmFnHW9dlVAnUeVj0K8Xvv8hWfvsL05yyJQKZV4389Rz5C+hrzhL62AhGQt/JDPsgnEJxZ7iPd5/StqrlQrM/ZVz4A1iwe4AciDrAB1M6csl8XnJ9+1TQEADBff+8NXjbP/gApvShaOwGh8j3PtS0nBlpVc8m+Agty35vLtw8j4LE/WjXHA/gLyF8AJSJQhIAz3r9h9PPpV9X/NPHZAs1THu1hCyq2eggAenizgnOk+qgBwGU1z44c2PnpIQSYkRbNbLsNagZY+rzpVV7ZRnXUzPj49KtXAHD+OH8/LZ3vekMBygQ4CxRD0QLvPspnRpYUNDhAB5CQoJrSKHvm78sJD4FWOmMBwNpXDj0lPm6/DPIeNTcz1deJsyHznJn8Fz5QHdwZ/wgZ179KEyAvnUc81v3bTPu22ix7hs0aQB9Y8evTZ5fw/iT6Zyex+Cr3099teX7893ZFD+pW/5wAnxZh0xT1Jwh60u1Xtn0HoAU9da0fzPtxZsePr4r/+EKCjy8k+JPgp82fFv+ecn8S8SqOTwvkHX6H50fnV3K9PsAX9EfK+Lian37OZO87poLl8xRk1xy5EVD9NwL8OgSwYFABTAKDn4RYzzzaA+p+MAAIw+fsj9k+VxsgmCyYs7PO/4ACj04AZP4zat+ICjzKGrC2O3eOgTdv1x61UXtvn7I2ST68AZT0/oVt2kxG6ZzS9by5Az4HjVgTeY+rB0IMzfzzz1td4fHDSt4B4gM0Suo/pt2LQmYK/UN1PI0ExjlghQ8L9wG/ICOBkfPic2VZdfzggNmYZixm7Z87urkHfCD8lyfC/71CyosHZhz/ExnMoNeD4ph3kIsfwc7TapNmoSqX/U9/ucy3PvTv19BAAzBLcfNPMxd+eCEN+AZ7B0ApX7cBwLjXxuyxic5asOf9ed6CzN5+TJl/gDng69ukb/+bYHtvv/yFXk/3fQEcnf1FPPg2tUFaART+E58CZb8m5HfbUfyvLf9Kjl+eifO3SzwZdGbWGQwfqTkP/LDw3oP3xT+t3o8ojBIfYfwjunofknr4CxUeVgKMBkw3O+x7JL77I3/sz2Ztgf+a538n/PYG0tea134l8KvBB8MBpH2s57YGAjUOFgTXz2oEz/791v8loA4t0HkCCc7KQXDYRTZr318hmOPZKGaTiGWtwD0CQwkXXGP2xl/htg+Ta99DURzdEGvEwVeI7wN5z6L+Mjdv0azUrBHwxUeAC973x+CW+7Lmqf3sqm87jdnql1G/vdnECow8rOrj9vmhoSViQ9raHs86pMObIelvHGdqOX9uzOZS8YNioUwv50wtCm7V9JShRvJw1veXLAkHjLrw9IGgRFTx87WJ2sejqpvXqrLRweC3cRCZG8IR5CW0mfb3AWPYATpxQxqn9b3nS2Krel550KbNdcA4O0oFiLzcqtS5O2eSdyAB7vxJg0ya9URKw0lByDmO34Y7aZPArBWuboahjbpe3jXUKeP9non8A7tRoKHZU9eoRJdeVJ/EPtUJxZHHtePQBnEa+cHcE9ZyUM+prOHENTrxYmBMe9cs/HMjwk7U086esqQVTtnHkTrqQVFOfRGKyu6u3uNGs4WzQ5mNqE+ZHakCuuk98UCQbnYiBse/5uv9aNeiOZGrVc2zUUTxSntWq03Bp/nFxBIBj6RcXp5S6M6eiH13oPO65JhsqCmMhSfmgKdyuYrSUxGm2224PySXUM7OG8LoKJKKmR7l7thQBNdQPC77PbbsSZPPT0atCMNev0TLiKf2A5sMkVtk2kju7X7ps+fJhlmEg+I89an9uUtQaehFvmRV/syN2a6QSSeIXInep6FiFsfYWjOkYtGFMJExtQpO5FYz6G250VlXYiXfOvhl5rE4L8GVjKcxfT15d1W7hbtzRmgUxaRtnC3bHNtOm7oe7+btFgWTkG59AtPU1Na7IglptAwnTheRm8yoh5sxImKqolrbJ+QmtIvcH9XRopmY58qJzo+kKpb9FF0b904cfWZ3HIeky2HFtAXYG+3UJvaDuCJ4WJrKAgOkvkfqfTCcsvi6gbEQoiW063ect75cz8DrewlpEilBqy0HNztvm7SYeatgJV6NEX6+SOmgValt7jVP2YbeeBCWVt3fWD/i6BvUMz53jVgWHzhvE1YbWa6PWRSiIb4za2F37aiIwjO3uTsQU0TjZNwtl7r3AywKmyOPCHtL3Ce7YckEx+DUlMiJrJL5r20XZTeJg2dN5v4s+dNF7jrH94z1hAeTkUISOQqncgOxh5G/rYSpla0ekY8K4dosdSls2tMEhGE8U7kNrnTR/HvlSmun16hNKEncmeyog7+1gIUram0WMXLZsxNpxiOslZ5eNRQ8OoRaa0ykFJyab+i8qHXJCNzeUjJp267EfZ/dcSNivQivKds5FtuANtebkYmhxuTTPQp4Ybggdrc1YwWgXpdox1S+C/VduhUGwSK1u7M0NmzaU0kn0UVeSqUCXfLNjrhEEYS5PSg4VmfDU8TeLOqG49OmUsOA55g6pXXUO8t1GLgMXY+Qw23jSuNvrWpJw5HYrvctMXLhVotyDt4v6WsWJZeCXSKgcMVjAvbi08k1trx8bhMzoejleN3RtxrreF0JSsO14m1X+8phmk5IVQTcRSd8/F6ZyWSlJlRmI+dtmzG+j0jO7NCxophJ2G6uqT6ox/S2VtaeBiupdN2cepamdgjWRdo6i9bkMSjVekoIgoMYS0bXoriXgf/3LMN2uOqsWKpvQ/gcZFknU01BDMHqTJIi05S7fe0cueGQ7ugkDC8521GmE6xVbwAcV+f3KNYoP4WtCm6YduRXPI5bZ45mK6YXL6Kn6IfpWiN+yO6VZNvwmI4NQwIRZChMm6C8o1lwcKn6Op1HTZaHxjJxcnlC1stpvceQXhSixN4w8nZdkxEv7KU4OxiHTvSIo1xZx6Wu7LwYO508a2Xu1FE7t7viur05MXygxJwQhkvtU5Qh9+j5jveVBLnUQYrPZlTRY2IeuK3LSaD/bNJ+6Y1tAwu1LOXBdXdhjoIorNOLqaz3zJjF67tKOJBX36tA4RRqZPu8PTHnyJ4US9LCar/GWKvHaU0obsG2V5bDMkZOK65D3PV1veVv7JmqC/SsaV2tl4hJq3p/LpGwqgrVqY9FXa90dVU0ZrZcOZg82t3ErDhLZ42CDJLL8sqVMifCInE7tQ16h1mBMQ/u9UKu1zWwALsVKMwY10sZZAqUravlVddHEiI3WAc5XlWQZUvSSkalnre0kpjuOUOy7Zj0dmkib/T4vkW0Eo3yY0mFNk9uj0RYNPlyv6TKU7MKsY1l27ebIu5PfRXAurYls7sWqndXvRqixtT7Yr8Nco4WMimHG0reapRiJoJL0Ya2ueSIqAhpZpD7fZvQZ9o+ZGdXsFp1zRahkd8qY1XZHU1irJ/qe9sszQ20cUohXfv76YxZ2+t2P+xNVz7wQms3/ZaNS+wcO/ZKPcYKuQLctUqoUbxEQ6fvpuAIt5x64pLauByK7TBp3a2DG4i3d3uq3O2C8dxSjHnTe4If/MSxLb/WCnHgCqbI+KYNqgLOfQWE+Soy5Zg3I1NTTHKEljfucMxPp+h+qi7DeZ9Q6vbEaSywN8fVgeEhYoP5eRyXO0XoVuujHrN5yxjoqqMqk9tFd+NOckGMpuHqwjOaNFpHo/QSXDNuMlcaqWOm3KbfShQTSoO1bfVyg1nOZGwrn94WuSL1ZDLG8NCuZKmWveEkUvHVi0kVz/VAJCMjlnf4keN3FYt0u2Dwwk6GD/LNqfDM26u1WpujMAQX6XBlHURHCvuEckQtwVfzvEG4TcE4HXFJtn1EbHGWDG/r/SbBrU5td3fFJO5nds8p4YEP9zF/IPZO5Kj0TeEV0mJLS0nK+0bVVoZ+sVzlUugbeOAu8ih0hQEtk9QIKDyq0cKYDtKhu5pDdC6KgoJA52PKVXtq3Ou+o+idA90a0GNIadDv4INw4yAsaQukp7KWWuf51tL3Sy87wYZ2D+/dZCL0aOijcorCFk3rYF9Vztmi5HS6qq4yXJicQWLQSu0kP4dhfs+d0uTsNfuQjbdIGabFmKanDZOue9Sgx1LTd+Rhk1qSHLhWS4eZu62ma4kEAtrqDEcufX0N37qACiyJq2+jYkLb/nQKpAtcyqmQIpEWdLlTUNlpdOlcNdBdjtvq/Y4R3equH68ZpUxeJhDVba9v+jtG0VpfnSJOKnLozNjS4T6m8FVPKkl3ePQAQVjkUKF6kw1VSG7C7az2ENx0WHSdBMlp7viRP1fRiWvheDly7UrnIt2pktXScyc5ilzlxlvxiZPas1QdaIpSo1ahY9MlLLrVhSrAW395C5zt3mwKYbnEiU6+76BboXn+hFalTCbXIzEwEFFYIheW0jXQA4se6HMAh1u0v0yJLFWboDtX8dK0CRxNrmEQiH5r4TQq27VaSJbLO/h01Ja7I+OIyXG3cTEcRZz7tXdP5+MI53FpbHT/5gZZHO5amEhPF745teVuwMs0MvLCrKiRi6wELQM3GUp+kLe0RjaK3+4s4npaLX1/x+PQ4TribNepyLDZNJMtFOOU73W+RK5amRXmEdN5r9UPe8vXTqDfvcunqx3UmCJp94Nu79tR8Z2Npmh4WVJgO3BgWGkvCSsDztiBNaJcwJVOoQAZMNs1B53obXCpJ6VidkiOweh5626TKEHp5qbvcnt57ZWJki57IMvAmckyl8zJ3IjLe4FHhkJPDisfTJ+Y6KDS4VAPsd3mzLPIcp9Um0oRCqasNIt3SN+BHbX3zpvB7u7JEoKQg3VrshpWPcLzG4by9SpqV6frGQ/upKabbKOCFmh9E6VKiYwpXCK+ikYHFJUpSQOYaKyD29Y5WFfitEXlEUsCHEtCXNIOPjkOandFCFKcGllU4mMsd2yk4bLmh2rKGLeKnT16vJbbtZoonL/lxsjn2k2oKil/GLAL3Gyg5bnGzAarMJUo9YPSXELjEAollyYkjNH3C7eJ866M7voZcYuYUtZQre6nuI5TwPzU3tbo0mNtdj1JgRLvruS11LCTGt68tcLFjnC77a6BiMUJz/lJzityF8qQT6Mr1bttury+U1wwVaKA729MN7HN5qaCmK0JH5aR3DnujgGTjgjNiqIu57ijZGxwaKOjnwsEtM2Qm5n3IWwWy1TYgEwsLqJ/8UTtCHFldrtZnNXmZ2l0MretgRp36YxMY2aD3Si54y+oDblFpZU7jXIvEn0qtqusCURkhS+Hy81iMRklo2xMEttAr/vQ2FrZbjDP9+PpnHIFKK/DdvC8Sqv6LNL36oiMSEhOy/6k9lRPgAZQofpYLcJqhI0V2OYz91E77ZjrsojJ+67pcyT0VEs/UsgGVXhp4wGkocm6uZ0PdtKV+mms0w4NE3Gi6U7WlqdjPQz72lRlaMgmdF3LZlcgHIafglxmr45FdqoBUlcYQJ8VQ2FYdEJPSywtmMlYxhfHyXs09fnd8cDdT11vHwdjJZ3LY9CgyDVu8nEVjj52HHGcE2UDQvIYPUJjrdgKwk4XFZK9+w6lYFVBIHkH9p4imvBBcnN0SbCvt1GFupOo8nuphzlERYN+OhIcKRwsy+V0zed2uclXMIMx1HQQNJFcNezKDq75FrXlw66AtTj3DuMddaOynvKrm+i7zrz07oEtNOwsW6xnwDWAH7uC2gOdWSd8pa9Nf1rXEwCCU5Z3Wiuslmdpqu5npMp4/7YmwrsEa1fOy3R2OV7yE27ipUFUa+o07XBzSZjnq7tzVWElkW0i7KFs2GJrXtOtDDv7EtnoXJ7GTRYy9zueB7tEWtElkXm1irgtdBmZNjslpE2KyoBabeqflAo585emgTbF1qrOA4qKlVnSYUBqFoYgmcNZnluv3FwPe/ygb4Mu6VE0O/QI3EJu50PwGcpb/r4TxlunT9iSgygDtuCDeiWhszWR3p4yGYaA7zW3M8TDFdYUc71r5Rup2sgayo1IPGyJ+23TChJ7VflCYnyn97eRcoROMOjp8eJC1gJb8BFilng6iIOSizdtc8gMp5l48iiuZBqxVzA+mNPhQh8vvsYajo9jo3TjiXJAVwm8Qeoxpgf25J+ga+a7iXZJHWe0sc3x7vFlM5lbdooFZSjBrsRv8fZ0x5TbEksRrZvwTGxbLjKcpR8hxWGJc3fSEuK4WtZ+I6EiK5mXID3E2+EYX4fVkoMnoi6Eu+0z8vmuI0kp1uyprHC2Rnd8pWt1M0HevqwNsAsPiS1ar61UXotoecPQrRn200a5oJ6giwOLsYOTK6vewEHMb2rB3C9U76UZeTTN/T1hApkY7jRJ8MaVx+WNBXhVCPmMyAP1zlM7WypBFZ2tgV02O+2S+ReeU7yz5HYWVY9+X+HDVWkCuPRcqApXkN+dmc00IaF2Zi/xWRg9VJmEgXf4c0lSdNWuhMPhMlWb3a5Lg2qyp1YFPOB2DCF2GOVRh+t20B0IuabHwq7PF9nBAtOcjHNqsG12wdemjITuQGbno3ik8Ma/DP6VTLt02QZr82In1aTvaup0kUw9U1mCq0Nv55c011b90cmiE3rill7eOqDCEGHSUpFnZMFwpuoa1vBJmTBKyOSiJsdjcY8NO25lwwkIKlVXbRqYXoeOw6bnt/sDIh1cxASBNKRDfCcJ0TKlizVyd9jbejIZ64hZx8mJhEXrpLVHhuzPih3Bk7HkCZhsMEW7YnyXnmB8GiYXkeE1cyExHLJwdwzTKZYvCFTr3iEdqh53ovtqCQq5ziZW0Rt7DWnIST9A2Q0n9VshFSZRsRXWt52ywkogQrjpS6ZbZWohxjekg+OTf66Mdiu6FnLFI0RILVc6OrCxj6floUPPRYPZse9fafGSuJR4h45pPzEUnV5jX2XKG26sYdO59CFb2GtT9b2QdTRIT4iAsnqwQRHHSUr2aOBPy5F29Cni6PSwCdQxzDc4xLFsfoEdIlP4Kcc6/VKSwE+KJwqn7ZK/1NrduXZRgAKvjASMck2PGHhQ3kiPzXrturS4ZVT1125tMfaW1/geT1engVL6nh7bnoGQ7brp3TvpcDJLWLW/P6w2kO7QNdbJTajjproOJbWxUQS1fMtucIVOsDGX+dyhlTzHmjVoMuUs2zQFh05mahUwdELy4myIt3XJmkeoGdHLYAXoeGUNjNjHhrDuFJNvvQLHhnO8mZBDpSWRfT+d8WLSBplN4l4oKlJbN43gi5edoi07bXctzgO/zW65F+fcvSUylRDMa29ztlbkalbwWBhOlcwX7KFCR7LEBEdvsazFqVQTCWvUy7aG+hJZeU679LCLyPpwaqbuWt2aTGEkRtTJDr6ieI5qrKLvsLU+ZT68ineQrBq6ZG22pjbTBYNVdlNcy8NNd7oGO3n7k0MkDujysRJfFwdQPi3IuPjAiQZ/uAFo9G9b1CH6mr3FEVXJodW4tmNAa9p2sEMgp8PS4IXaa84TWpjagdbxQ9zcaX5PGxN/z4XE9Q9pOPm+wTRTeZGkzZEVgFf6kAkyVYic7fJ2xu3tYZcj7Q4Xk8y24/Xt6Gz6FXrxxaYqNjvN4hyCsBvnTBw9ZVd1e1V0cjEg1TWShQeizdejtXRyAtQazyNa4sPr5uATsE2JPr4JIWQyjsQScVjsTOzhcxdI7rCh2V05Onxrm65zSiQHUZHKMfkUwvmdi0HwagzrrBZFtEoF3UHK4OrtMj2dnModKoXIzSLUo2xph5UuDJgUke1d1sMyvfbTGcu6nUv5DQq6PVJXWZ2436ndqudp6Ricy9sd06yczoOg9AhaPEfkqRDA9sJB+GSFwPlZ0BmHtMyNkHMogxyrvQxvRDrwFfrcEPxwXieU1zBe100HW66i1Cc9SGM2mpeH3TpMsLbWSH67OSTXOj9Y0+B1ztjSTSwG1xDPXKU8toYbyCpubtcYQVaH0ISgSe8tddf2e9aBAslYliderpMoN3XWX8KrTqyF3gkmds90G2TACfTeu7CysW5rX5K227cPb/OB1+tE9V9/j2s+wvl/dlr0PPT5+orG40jRs9xPj7U+/Rs6/fLhrXIioNHzTKxO2uB1uPQ3J2If/+mh3jx9fL4c9fWk+Hn23FjB/NbwWzT37k01fqnz5PGKBphht/X8omE9a+iA7z+ein4z43kcGgXZlyb/UnlNVM3nYVE2v3rhuZHVfL0MXmeEYPzrvaAvGIF/8apiNvR1xg/sw97hd+zt9/8LV3YpdO4tAAA= -->
