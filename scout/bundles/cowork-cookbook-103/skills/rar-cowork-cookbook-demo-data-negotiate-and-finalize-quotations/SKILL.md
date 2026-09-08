---
name: "rar-cowork-cookbook-demo-data-negotiate-and-finalize-quotations"
description: "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_negotiate_and_finalize_quotations", "rar_sha256": "56e43a27ced3ed2c9ee3beec87d33f8ca90ee2fc26dc42fd45c98fc83e4dd0ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_negotiate_and_finalize_quotations`. The original RAPP
agent is preserved byte-for-byte in `demo_data_negotiate_and_finalize_quotations_agent.py` and in the RCI capsule.

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

Negotiate and finalize quotations Demo Data Generator — Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
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
      "description": "Number of demo quotation records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 56e43a27ced3ed2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 demo_data_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 demo_data_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Demo Data Generator — Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_negotiate_and_finalize_quotations',
    "version": '3.0.3',
    "display_name": 'Negotiate and finalize quotations Demo Data Generator',
    "description": "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a81675e8de85f47b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo quotation records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic negotiate and finalize quotations data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for negotiate and finalize quotations. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic negotiate and finalize quotations records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo quotation records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo quotation records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for negotiate-and-finalize-quotations in a sandbox D365 tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataNegotiateAndFinalizeQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataNegotiateAndFinalizeQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo quotation records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6ebObWLLnV9HcFzFV9bAvYge/6IhBC0JsktgkVO5wsYPYd1BNffc5SPfarm73m6k388/IYUvAObnnLzN9+P3F7tqoqF8+vWi+nS92dprGkV8v7NxbrIuhqBPwVSQO+Ltwi7ytY6dri7p5+fDi+Y1bx2UbFznYvvNzv7Zbv1mgxKL27TRu2thdeH5WLBo7BferrmjteTV47Ba11yzifGGDh7nnFONig5HEgvvv2lpepH5opws/b+N2+rBoWjsE29vIzx478sV2dP10MQv3kCuI66b9sHAB1/Zt4YeHArXfdnXeLHzbjRa5P7wx/qlZlHWc2fW0SPzpFajij3ZWAhlfPv369w8vMfj98un3Fze1G3DrZQN02Nitrfhh0caAB5t7XJwDFe/+6V2p2SKpnYdgfTkBk+bguvTroKgzcMvzg8Xb1c+NnwYfFv/+78lg12Hzy6fP+eLt8/ll/qN2+azDoi3spvW9hWuXthOnwBavCzYd7Kn5qhiwHvBIHr4+d36jVJSLv83Pfn4yeQ399ufPL0U5uwgI+/nll0VRA351N/9+namUP//ymhaDX//8yzc6TefcfLediQGpX7+8Xb+RBQu/LY2DxRftuF2/8QKmjksfEP9Ov/nzFP2N3JtJvjwX/1yUHxY/pjzr8zcg7zPmHED3x2SBDcDOl9dbEec/v/Goi97P7dz1f/7lX5F1I99N5oj9P6L765Nw5NsesNabSX758HDf3xfQm25faf5rtiUImL+iCVj+zu6rof4V7Ydn/4F0GucgP959+UNyP9oA/W3x67/U7T/b8GERfAbZk8Y9iDsn9T8tfn+EyK8/ed9u/vT3PwDp/y0Zrehq90HhS2bnceA37Zcvv/7UPG7/9Pdff+pKEMW+nX3p6vRHNH9k1wefP1nwbdXPf94L+Bt5khdDvviaQ4vfi/K/1X+8LkwABN63+82nxfeZOH+gxazEO9OnCb7LxgbI+p0df3n5A2BQDrTp3CeyfHr5t39byLFbF00RtAvNLbp2ARzcxpk/C69HMQDTB/IBBYBdmxgY9m0diP/Zw7PERbD47X+4D1T/6L6hOjwj9BcPwNuX/B3fvgDw/BK8IdyXr7jd/Pa60AGLoo7D+eFCZY/HzzlA57yd2Ze13/h1DyDLmVr/I8jsj/OPGbR/+wtcvjwIvpbTbw8Qj59oqK73MxI2Xeq/zjqfIz9/09AFJcEffbcDvNLCBYIFMQDzD8AWTZH2AEln+zRJnKYLLwZYAwrY9CwQXf5pJvbbb785dhN9zp/QjS2ela2BwYKv4iw+fgQaBmkcRu3n3HejYvHT73/8tPifi/9s14P4zOMIismbh4CEgnZQFiDjugwsmyshgHrbe3jo9z/e7AzIgJq6AP6Mg/hZ2ObMSHzv3egaz35ECXLh+MDYwNBZWdQtqAeLuH1d7IPFV3kB0/nRXDGiomlBWS793PNzdwJUbaDOV0vmRQtKchs3ASi9XeM/uP7m1PZDxAykvt3+tpDXR1CfihT8M4v5WAQ2F3kMzP81JJ73AZEalNzVO4nXhTLH6KK0a7uMavuNR2A//QLq0vt2QNye6/bnfC7J/myqR4g8zRPOHcfcYjxc+nH2OWhRMoAOz9aifV9jz1VUf1TT+nPevCWDXfuPfgCIMi3CLvbmEvEfbyHVREWXeg/7AUlnSm9e8N688ojBrw3BI5jeQ/lbo9Ms5tZhMfcOi7f+aK66HbpE8MX/vw3TrDq726nbHatvN4utoqvW0yVzhzi77tlUAmEWIC6f6feti3lHqnfA/pynMYivevqP58qHI9/WPEGwq4HdVVZ90AdRBFwy030E+Ry0dT2nh/05f68MQJvFAwaB7QAigIyZA/Wd4fz0XdIIpP18/a1LeNN5tgcI5EXZOSlwS+D7nmO7CZCqnhP1zYkg4v05aYcoBhb7XqvZG8BegP4CCBGD1APV4/UrWj+fvov+p43PZmje8mgUO5Cn9YMAkMOfBZw9NcQtgCu7fTbkQM9PDyJAjaxsZ90dEDlA0+dNv/arLm7idkbFp139EoDzx/n7qel81x9LkBzAWCAFyg5Y95E0M55koNUBMoDoBDmUxfkzVt+M8CBoZzMCAIR9i6EnxcftN4X8R6bNNet946zIvGduAxYBEB3cmb4HCv1HYQLoZfOKB99/jLSv3GbaM1g2APAAx/enz37h9Vnynz3F4p3up3+aeH7+a0PRo4gbfw6AT4uobcvmEww/C+973X0FUAU/ZW0eNfjjXB0/fq2OHwGzj++Q8vEbpPyJxVP7T4u/JuafSLylyacF8rp8Xc6PpLcwe/sAq6w/rqyP+Pz0c6763zAVsC8yINbswwkU/a8F8H0JqIJhDbAJLH4WxGauowMo3Y8KABzyOf8+7ue8AwUmD+c4bYrv8ODRCYAcePrva6ECj/IW8PbmbjL051nukSWN//Ip79L0w0sOIvCvzHBzVcrmKG/mERDkE+jS2th/XD1AY2znn38efg+PH3b6CgAfAFTafB+Jb7VkrqXfJcxTW6ClCzh8WHgPJAZBCrSdmc/JZjcgekHgzlq1Uzmr8Rz35gbxAflfnpD/zwJp39eI76vDjINP3P++qPwM5lO7S9uFocncLz/k97Vb/WdmZ9ASzHS94tNcHT+8oRD4BhMGKDPvwwLQ8m18e8zceQcm41/nQWU2+2PL/APsAV9fN339jwbHf/n7D+R6avEFVO38B45RuswBgQYQ+lFX/7miArHfg/WbFVDixzZ4L6BfnkH1j8yeVXauvjNkPsJ2Xvhh4b+Gr4u/kOMf0SVKflwSH1H8dUyb8QfCPDQHmA4q42zEb975ZqPiMdnNcgObts//iPj9BcS2PUvxFt1vowFYDiDwYzM3PzBAAsAQXD9zFjz7vxka3kg1kQ06VUCLIH0cs1HK9T3M91CX8X3M8X2XpjwMC2jXZpa+jwYuSnoujgYeTrgMHbg05uOetwTqfnh5gsCXudmLZ/EIhgqWDIMGOIIuPeBFFCylSZp0CQpd2oxjEw7B2M63rUmce286P3WcDfp1fplt86b67y8OiYOVPN7s2ednDUOIA58pR60d+LKkx3RoXc3MBK09ZOcpxDjMbIQhHlxHQLsWW4tTaByugmVMurS5d2RUcEzMY+vgKlEH1MumNcedDZJEnYZzUp5VsiC7C/md1ptAxrZuibmZuUxUvzCMSzTtr2pEGUEIG/2oCYV5ibaZG48HQnM1wcRucWqNKRGZgtBTY0tBTo+euvw2mJmrkT0bMVtvs8T2/dBr4trSYSFMp20TsMOO9SVClHEoqJ0SktIAwd1+3KkXPlMTfqtybadObNtH/oU7ZwSuauPhCBfT9uYJXm3uk7gbMvBMO96s1mN1lR5hoWgmloY1mnHj9OaROIZ3y/ju+kp6vshZi0KN119KJOjrijxiZayHjI/BUDIBQCcvQ0KF7Ibe1zF21kL1PI5cJnnXUMKWHaOqN7UlWIzbnW2OieAl3q/VkyPeGX0LbCTIg6FrES1PxtrlieXd16DtUoias3SLvRO/PqtOvOGIHqcvkdGKxJHftg1xT7j4AnGmddEcw7upBYQgJFTWsC5J2blRA8oooctV4TcMtldPmiKJ1oEjEGglIOz+zKfjNulUSb4oh0JLqOPhxMVsvlxdw/36PuCTvZsUSic9zcKdbNxsOr6yT5ycVgd1lfByd0yt7VazSS3IqJXFUFM8yQKnWdZ4VeswIOSzdwi5O2vy5opJhZwuh/u0jRMwv9z2nkRdb1CT8uUenqypZthEEKd43+49HYtP3ubGeTE+XLabaZoSJclugsksu+yaSf5qrJeFnDh6RVFVsQyHdmWG2nEf4yWc+UNb+Gx2ps9GfcnUk6jebHGlVOfBLJxzuHaYDK3QIt9HKEebRoeEKSqTCmFkNhQdJq47rILI3pKc6wr+SYEEuUhXkasF/V6E92a9FvCirfwT6mzCZBqCsLOOuoUcRwA3y3wgsyCml0pQXzbwVV9pN8jSaH8c2I1sj6yFj0xUOPjqdhl2fF9scYi7wrtyi6x8WjWCgwF5EXMj9rBdH1U4kW8jJJtHHKUHdNNdxAE5sGfUc2RWrc54zaWdCiGZxfX5VhdSqkKMHSxzCcyWV2JHktFZCXdCp+3zCk2uCgWdGxDCnEkUecpcTq6cx6nSRiK/9rlpszU4JiTXW65bXQwyVDA/2FF0oOOXO222t4GKiA0Z3vlDNjQZrayW98N4cNFVVtLqLYs9HmKWJWeR8g1pOpfZiD2z2fNH7HBLsaxNKTIrNVMkJHKnSzSK4fKgT0p/uHtUYNrbah8JwplEkuDo3NR0x9KVpmlkcG3a3X7H3keoloIo5AV7rA40pMfSbjiOEqNek9vpoBO8sCnwyWMMKNr3iCkiJXM/1QSROKtJuCxlC9+Tu+uavCtQfd8ck3BCjV1fEzwnutN0b+939XLs7D7JRomgpLPJ3WEjLwwIunLiMW/Cvars/IOUuatT7qa01Cn1oSWbZU5X21Ma8/Bu3d/6IEG5I5fiPtTUDr/BEA8SPM69urTB8x2fnE4Vxq0okeL022FQkA7f78i85vmhp5fNCSlcLx6sXDgPg4Du9nDkHHFT49uo3IXddGNF8TBwZydsLgdUp2QivPRZ0RR7Ue43TGA6oqGjGdHAmxObVbgdMNgl393Nere87+73tWj7LCOieCcHhysBvFFgmsd6k+8NTAur5abA5HQtJFfKH4V8S2VaxvL0Ld/FW43aSP0y5LU1lyxB9uZXGQ4V+pAGI7pWrUbIbxbMxwLOKeN6FfhEsj5p8JCIzEmOD811ZxdGcUqsnULRcMVUzB7KteXYx6EqO/bJxGHbPpGpcst12zcQ82IvGxI9nCLhuo/2oF7fEjPe1553XclijwUnS7oNh/XZK1bTehyh3FzLdj+0pSmx/rgV1Kroz1AZWBdvGs71YXDZ+qZDOkAz4ra6qnIan8r8SOyh/raEj1KCC8FNvAq3MHcPzr1aicrQd9Yop1m0FPnDdc/pzUgzkOvu+ChHja1uuXHYHyAI6gEGQCYWBqBoBqJznKblxU85vbhY/VG4Daq1DfdKsz7l7N1o+im+RI4UuVGOX1kVyjuSdU8GagYutUJMzd2rGD+JViNuwvKm+Ls1qfEs7i4rWurlYEXpx7jFwxUYC7Lzac8wcTxkcjFJVxEUc3qy1WFX+EyxtZINu6QpMactN137PHa57cjYcDKitZa1O5YIdOSYzghkVLSJy61EyBFJ5Ba54YKRsGM06vcKBA0pTligQqJ2vzKbZIo3y6Q9s0DO+FbuVmmA9RaTQ3LaGLSQuoVFlGMx7GGKQfvEyW1+bVTU8SYvI5Q2ry55l1HmulsfaV51ZU0yQEHrnF5s9uJ9SG5yxI+gyF0aC5K2PkHFdKpFcqVu7YLY3vdnQmczaz3xhBjkYh1GMNMjKbnyxGTwJVacrHElSsyK6KRBlgSTNsvtJcope7k8emUT8pUZRRsdLeJ4I6+2egKp8rg3jldW0KqVoKXUgJGTGk/7HWadFCVWd0LTVeSKI9hqE0vn1TprKmeZ2TlOuxx8vNnx/iJB5yS4aSnpqtJSsM/VJLF6GlnXy6jtUwClzCVktiU1npHzUA2Uq21XHOgvTvXI9qS3VQM/ElDWWsHJoKaCDGl4ZqzRzV2Ry9Ogb5OySPGhNtk02TZjTh7PKlfAhmAMqyBW0fWmSjaJQlL5kl8io326VuyxGg9oeLYKieAsTxsz+dRDxOG2VT3I3pyhAK/WjnPLhkTyRTK7QrVV30Jt18mbZCMjFL1d93i5CRkM52g7VCQG97CSJu1bee+Ga7obLH5yx3XFZ3wYAwXwcSmOyLa7VdxkC77QilvxhK4CvSzyyrgr4o4BfdzIgg7skOvb9ihYArAMPXCceWWk5cG/Llf8iEC4uPbgdZgHZ53DxYRcanhHIscVHSa46TvZSYe4aNqeS1EuQ3qr9ZqhUuurW5dQ0EfbvcwLqKtUG8JBTGvFkOsEG23ewLETCVoDfn0qWO3MmduV5jc8pG7skA6MrrIMBQ+osbvD/BLXemY6FX6zP6ScMB5Om5szNwnJ7hzjNx4Zp50p7vReWHWNiai1aeZD5wV3JI8UsVQ4Yy+eckKXZJuNpG2qiWXCndJte3bWIzb18t0h2XV4ulkeMSGXAqGSIsPbqlWD892fCnWfsgeBR7RIY07nSVrR7s3QWUJTknB/XGUXqZL5nDANYrIckpDSSxRmxzAyURJNjLoNTMOVuBo7bcNxe6z2PIn7R2UiDzUbm7uEBx2tcA9rZWhZ8Tit11DgJVG2vZ2Eyk8gX8yqbN85YkjH5alMRPtopWJpGdckxQirPMbS/SaA7jvYtBDM6zSx6jGLUGHv2GKmF+WSfYvPfnY3dPLeVXXMMJUEOkxeJ5UhRJFlr1Gkq+2tdb6FjreEuHJ00227qqtKbuy2XKarp+NVSGyjWDZ7c725sml1C1dnpFIjdaWVSWrva+20OlTQil8phNJYPqOAmYzbrTcyz1tSuU3GO59hEyQlE3NkNtFdjBIkxhVsPWVICuCwr2WUH9nV5mCX/q7P4b0WENuq3jmtSziu05iyf4nJwz0ZvQ5WNmhF6iMiH8ZCGdNg7ycBIg510ISEiR8Eo+8ukqm1ponEWACFo75fn7lRx/DwMMT2ig2Xxdbly/UGzBPRnZxCkrAx87gka1ikpl5CSLfPRyqoimFVSOkmNwEg+julsDwjYhvnlO6XQ1c0rYYICE1IstIU2CSMYrwMcvioH0fc4ykU6ibznpyQUSgOYEzIdB6A75m2A+EUiUpWMFnXukIkGMdKZI0+p3aqCzqZa58go7pDllU05mNHI2JTegljVEl7p/a22SV3YQOVpr7DBYYYkVQP0bw861MI1xvsdApMyWkanRVHVvE9ML6d4MKZ0BpWdCk9NtJR3I7Gdbs9Def9ddqvL8e8Xp6KvU6Z+oVYeUvsstajs5b2qXA0W/nYdKilClnlQORNhUZnpV+MdasCKVnycCHhKgEjmoutFQ8qt0J4c4elxvQphAGjrmq22l3V7YU9h2iVHAryMCqpLSGWZSLkLmeUoxEPSVCwps+No5xcskuoDpv6eByXGI7o7MYyIRNHznAH0w51V0/kkS1jd9hfKk9fTqG4PLrbABPYYX3iFdmw2oLbNXZISkIcNeJNPW3OumVXVIVX1wYeUuJmpOwuSnRPIu+IzUi+PKA3XatsoukzNro6G/1e3/vJiE5LuSuWDlpWBu4Gay1TeEZhBN0nQ5OVOfp+jhTZt8py1ao80Jm3LN8VJaDI2ESSze+twEt5GmM56FYer4QWIHlGetl6V8AwT+pLPL/6Ug4mVwHen1EQCoMHSrznFLoHHHZLxH1X9tXO2mIur3LmiJwx11hNYLzsGUO8ICdmGpd7WhhzXjkrG1KpCnvdt/iZ0RG+ul9SOjazKx1syHxjYRYGDfdbw8BX5IjiTq9yd84sW/lcHFoUHym/P0+QE9YSOrnny/WcxUrreWNrpMdNIO0u5hbR4+W+CxXA7HiweXcHuulJZFQzM9E7FW/MlCQi3Wm3jBlYIwJGDdXdr0bUMW8oW0cIXK4tNbUkIZVXlalAZbGJ1sTGZNjrePEGE9/heUNcZGodLZu2qO8BJjVkGw8XB4ZjWrEy8kBtEhlF1E0AgQnH4Tu5DcSO6QttOXibdtiWU7MDQ/qmIX1nOsIUpMBDj9zATHvVzZyCBHhaskgQ92f6elEQEp3iZVhqMVsLrDcy3D3RtmQuUKoEVVnIMxvJp6lat+4I2bPGOmqLfUxlG5ydNH4VHmT54gn5IQrRtDCl9iKSBSqao1irl6697e8ge1WPLfzSzfKDdLAIbBRC2zLGCY7bwygi1Z5y1zg0HTZrTTGkO90yR9+DMktVh/iKBcPGJNDr/ZAYl3NQbnbG3t3DHOHfpS6vidqppE11t83WVQ4Y4SJ8aXPe1PK0lcKSRCauNyxNbd8pIStnLCdnm5KhiYFyGoQfJX2vcbqNIOt1FwcRJsQ39L6sL2c6Gy/VrvINa5ch1OFQoBZ6JxUU0lHUdW/sjblUlS7r/ehftKUPesFxz5yFvWrV21ryckjvyNWAifpeYMdxyjiGJPDyOpnGEoBCcNdXmBpSHFls0ZWBlGwG38TDbXUYMghO1zrKn93LYdNNYXW53/o9pfs1caF7/kbQtGsiF9iQVGvcxqpvHDS0Pgi3G+/p1d40sF1worI2j63WQDnIcb0p0SWvt3MCoUn1TnglzFMmf6mtLu+M5r6tbTiluKYrM4tsiLRNgReKKyLLsBJdGiTRddjNfNS2SbpMmH7X1aTHq1K8EQlnC+sUtx+UMy1UIryJ0LNS496eqFPapZcXq1UEK7C3HFHez03CMTkit41I4Fl8vxRV1hfXVruu4klKl9dbjDtRiiteGROstq5kP2Ro70TK2sTCAHkOp/x2MszkcBg8V1A9w0EPLJyq5oRUEdJb7HKigmzHhRDd2BQB56YjUSvvyJD4vUZKbrpTBsOgqePinh/hhtwfiftNuVMd5BzwyeUJu1ozQp4rW4wxSSZXRR4bsVpg0DUAFTkNNAIFGUfoWVueA2FIe5ZCtDguRir3dZJ1dESTcr3KLbUAQVQf+ywRcfhAkrbK2BJIX4eqESLlsw3dpSssO4VCEl9v4nDT+Mvav/VxliSD2J8d/mIEGYBOCDK4c7OubKXIMXw8lcdEtlb+tlm2vKHtZIyQy1bRiWoUd2J+SMg7PilYoUq1XHHF8kisOGoomWx5KXjazEZSJ1XMHvSbcg0zLTWQ2i9X5ZFQMfkCmxFBDHfQiMX+0aC40FjtsZO+pyKHNo7dkkUVbCB2dqlCtnGMRsZh0mxFbNGlk6Rjxq0mpHUAGEBFhqb4zuBTI6539DFdqT2F3h0tlQ6EczaVDJORTQnfHFPbhXaNGfJdhZ20ERJEaJNMHgFgWoOLHZLJcUHrCselKOQ16xhp49wUqevrC+gQ0uSOljVzptpWDiSZ0c5Qft7o5X1U2NSsuwQXbxkJGxvfl0ZR9M5lYeSlgkXRvbbadsfX6J2psHN9Qam8I9hMPZIccjGyEo5rtKQmCWNYlkXh2EyvfWn6Sy2LuUxgtlQSbuliZ0bYBg+OPaZC5a4RoNKrmKM+cOmp21Egf2kfbdHa8xQUxkBOTBWzFIvj0WRMlAq6yac8Q0Gao3EY667rDvusOjUlEll0v99uLuuJItBWy2HLCW7XxpbQ450tlRSrIQO50FtaP66cpDntyoJfX+Vyh2ClRC/XDknt804xoQ1fgqZgjWFbI9xW010fdPQY6AxbrDbK5By9Jre9HqDmKVGMGk/xsgu5FN5UvthQF9sLJbwnnZWz4c5HvFVYxmUPPUnGfQnjy1tWYiNsmnbAiMc1C0fVcRNSBF3CiIWfKghxdxg/4Uspjy7tSK93m2q0FNRRvWA0T64JIs+9dglMcCsPg9Hiti56+njM6uxwcZEq9Hw9NzPGpdqxvlKbMo0uscLIA1Ln1r1QfVgthAHTGbzkiKlN/VZAcRS7kzG6FRgVYVO63kX77emAiSNVKsbKOA2mYq6kVHWTA7Ya6I7MJtomNS7fhIcDIkO8sXPWdmbGveXzpY4JAod6BzxpJ7pHK/6CXaN2n969Hur9ei1LmOtiDD46mC8csr7bTDfUYNornoMyhanuxOPC0GBNaW5NWR7Eyq1CGCWRmo+uMHzHhsoIuoHbuXC+nZjtmd8cjsRl3SnwmGf4njtuCrtjrbbqoUB0wFQBD2dGS0UuTOZjlb/97eXDy3xg9nZa+195W2w+3Pl/dsb0PA56fyXkcUzp296nB69P/yXp/v7hpXZjINvzdK1Ju/DtAOofztY+/oWDwpnQ9Hwt6/1o+nnq3drh/DLzS5x7XdPW05emSB+viYAdTtfMrz0285uxLvj+/vT1q2rPm838PsiXtnho5L/MryXO73/43izU22X4dvAINk/AfbHbfMFI4otfl7POb68XAFWx1+Ur9vLH/wLEvL+2ci4AAA== -->
