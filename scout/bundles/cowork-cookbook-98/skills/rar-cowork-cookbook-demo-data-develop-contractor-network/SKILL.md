---
name: "rar-cowork-cookbook-demo-data-develop-contractor-network"
description: "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_contractor_network", "rar_sha256": "dcee5ec87e5f64845b846eb68710127c2c0e76c2f7800fae47d34f199c4accd2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Demo Data Generator — Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 dcee5ec87e5f6484…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_contractor_network_agent.py` first:

```bash
python3 demo_data_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_contractor_network_agent.py   # or on stdin
python3 demo_data_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Demo Data Generator — Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_contractor_network',
    "version": '3.0.3',
    "display_name": 'Develop contractor network Demo Data Generator',
    "description": "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e2ade0550ab4b436',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop contractor network data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop contractor network. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-contractor-network-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop contractor network records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for develop contractor network in a Dynamics 365 sandbox legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each new record's primary key.", 'example_request': 'Generate 25 demo contractor network records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training/pilot data for develop contractor network in a D365 F&SCM sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopContractorNetwork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContractorNetwork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-develop-contractor-network-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbOjVrbmX1Gf+2D7KvMwSIDIGxXRgBAIECAGDTgdaWYQ8wxy+7/3RlJm2lWu21Ud/dTKyCOGvde8vrWW4Lc3u2ujon779Kb7dr7g7DSNI79e2Lm3YIqhqBPwVSQO+L9wi7ytY6dri7p5+/Dm+Y1bx2UbFznYzvm5X9ut3yxQbFH7dho3bewuPD8rwKlb1F6zCIoaXOj9tCifxGwX0FrkfvtgFOcLe7GdcjuL3WaxwrFFA8RwinGR+qGdLvy8jdtp8aPnB3aXtgtTP+x++rBoWjsEbNvIzx4k8gU7un66mGnOcn+Yb+ULFwjVfl03q1f7bVfnzcK33QjIMLzE/KFZlHWc2fW0SPzpHSjqj3ZWpn7z9unnXz68xeD47dNvb25qN+DS2xZouLVbe/tUjPmml/xUCxBI7TwEK8sJmDoH56VfA1Nk4BJQZfE6+7Hx0+DD4j//MxnsOmx++vQ5X7w+n9/mf1qXz8Iv2sJuWt9buHZpO3EKTPK+oNLBnppvKtnAKHWch+/Pnd8pAcP/bb7345PJe+i3P35+K8rZdcCPn99+WgCHfH6ru/n4faZS/vjTe1oMfv3jT9/pNJ1z8912Jgakfv/yOn+RBQu/L42DxRddZZkXL2DkuPQB8T/oN3+eor/IvUzy5bn4x6L8sPhryrM+fwPyPmPRAXT/miywAdj59n4r4vzHF4+66P3czl3/x5/+GVk38t1kjuR/ie7PT8KRb3vAWi+TgACdXfDLYvnS7RvNf862BAHz72gCln9l981Q/4z2w7N/RzqNc5AYX335l+T+asPyb4uf/6lu/92GD4vgM8ibNO5B3Dmp/2nx2yNEfv7B+37xh19+B6T/j2T0oqvdB4UvmZ3Hgd+0X778/EPzuPzDLz//0JUgin07+9LV6V/R/Cu7Pvj8yYKvVT/+eS/gb+ZJXgz54lsOLX4ryv9R//6+OAEM9L5fbz4t/piJ82e5mJX4yvRpgj9kYwNk/YMdf3r7HaBPDrTp3MdtgB//8R+LQ+zWRVME7UJ3i65dAAe3cebPwhtR3CziB+QBBYBdmxgY9rUOxP/s4VniIlj8+j/dB9p/dF9oD83I/cUDwPblBdlfvkP2lxdk//q+MADtoo7DOAcIrVGq+jkHcJy3M9+y9hu/7gFWOVPrfwQp/XE+mFH613+F/JcHpfdy+vUB2PET/zRmP2Nf06X++6zleUb3p04uAH9/9N0OMEkLF0gUxAC4PwDtmyLtAXbOFmmSOE0XXgzQBTCbnsWgyz/NxH799VfHbqLP+ROsV4tnjWsgsOCbOIuPH4FqQRqHUfs5992oWPzw2+8/LP7X4r/b9SA+81BB4Xj5BEgo6Iq8ADnWZWAZcBdwMACQh09++/1lYEAGVNcF8GAcxM8aNudC4ntfra3z1EcUwxeOD6wMLJyVRd2CCrCI2/fFPlh8kxcwnW/NNSIqmhbU49LPPT93J0DVBup8s2RetKAAt3ETTB8WXeM/uP7q1PZDxAwku93+ujgwKqhIRQr+zGI+FoHNRR4D83+Lhed1QKQG5ZX+SuJ9Ic9RuSjt2i6j2n7xCOynX0Al+rodELfnGv05n8uvP5vqkSJP84Rz7zE3Gw+Xfpx9DvqLDOCB13zlHb76E29hPOpn/TlvXuFv1/6j9gNRpkXYxd5cFP7rFVJNVHSp97AfkHSm9PKC9/LKIwa3/7yrmfuDxdwgLF4t0lxgOxRG1ov/X3um2SIUx2ksRxnsdsHKhnZ9emrWYPbos+ucJZv1e2Tl93bmK2R9Re7PeRqDsKun/3qufPj3teaJhl0N3KFR2oM+CC7gqZnuI/bnWK7rOWvsz/nXEvEBWO2Bh8D9AChAIs3x+5XhfPerpBFAg/n8e7vw0nm2B4jvRdk5KXBa4PueY7sJkKqe8/flYpAI/pzLQxQDi/1Rq9k1wF6A/gIIEYOMBGXk/RtsP+9+Ff1PG59d0bzl0TF2IH3rBwEghz8LOHtqiFuAYnb77NiBnp8eRIAaWdnOujsggbIPr4t+7Vdd3MTtDJZPu/olAOuP8/dT0/mqP5YgZ4CxQGaUHbDuI5dmmMlAzwNkAKEKUiuL82ckv4zwIGhnMzAA4H3F0JPi4/JLIf+RgHPx+rpxVmTeM/cDiwCIDq5Mf8QP46/CBNDL5hUPvn8fad+4zbRnDG0ADgKOX+8+G4f3Z+1/NheLr3Q//cNI9OO/NzU9qrn55wD4tIjatmw+QdCzAn8twO8AwaCnrM2jGH+cq+XHFxZ8/I4FH19Y8CfaT7U/Lf49+f5E4pUfnxbIO/wOz7ekV3y9PsAczEf6+nE93/2ca/53jAXsiwwE2Oy8CVT/bwXx6xJQFcMaIBRY/CyQzVxXBwA6j4oAPPE5/2PAzwkHCk4ezgHaFH8AgkdnAIL/6bhvhQvcylvA25v7ydCf57hHejT+26e8S9MPbwAz/X9tfpvrUzYHdjMPfiCFQIfWxv7j7IETYzsf/nkgVh4HdvoOKgDApLT5Y/C9qspcVf+QI089gX4u4PBh4T2wF8Ql0HNmPueX3SSPmjDr007lrMBz1Jubwwfkf3lC/j8KpL8Kw3auEn+qDgD6BpAi/qPQ/tfiVSua+fpcL94Xhw50CrNZnQeCeM8G9C9l+Na9/qMAZ9AwzDS94tNcOz+8wAh8g4njw+Lb8AA0f41zj+k778Ck/PM8uMyueGyZD8Ae8PVt07cfJBz/7Ze/kOtpW9Bkgvb4H0WTu8wBYQeA+k/FFwj7NWD/bBYU+0vlv5bPL8/Y+nsuzxo7194ZMh/ROy/8sPDfw/fFD/9Kkn9EYRT/CGMf0fX7mDbjD38hx0NbAOegKM6G++6R73YpHtPdLDKwY/v8MeK3NxDj9sz/FeWv8QAsB+j3sZnbIQhgAWAIzp9ZC+79Xw0OLxpNZIOmdf4dxPV9zHc3hI8F+HqzxpzNGvcdfEMgMIISLurCPoG7aEBsYDiw/TXhrdYBQpLu2nZdDwX0nvn/Ze774lmumQ0wx0cAIf732+CS91LoqcBsrW9zyqz4S6/f3hx8DVby62ZPPT8MtEQc5ww5k3RZ1ulmTIeTKFrnQpZ6awuXhsPtieN1yzH+2LRDezGZaBL4nZycBsU23WGrajxJB2gKHTELddZCU6Jw2ZHOhdtSEosd0EDJhSDvD3fWte5040y6a1XCnkXFFbUUZdoXJJEwoN3enVC4uvUrZoeT6T5XgrEnxpaAnBV+1A0MFy9qOZb7omCZnXxHz0esYnVxM8hbTFHYjpPWyCp2cJmKz8ulP1VmvjYkUlD2mFepkTmJlRwLVz26BFFyWRfBvcVJ7oqzYrBG2ni9cg9Fyub8IFrMtMdugixtXDjdh5RBn1C+i5kKlw7sdE549E4NxCmCETOecKXNlxBbeiMWbjgJwSHVSHFoydMTUF9RsTuJ7ROV2+SbcOKjdGNm92vSKyk6xtZxDx3GQLvtyHgVQubZrgbVcY7a0LoIvSxjvyvSmy1a0ZHO6H3USc2oZQY5Kfv0kHKRHvg7hnGxkVPW1BINIrEtmZpL5Ph0351NIRaUEO4aqRUqZayQgMM2rc0HzX0ikyILaFl0U/Q4Dqo3caYciFO+LTXSDWPvyOwyRLfKfWITLKnbTCnU+d46UUZFtQNLm2sBqmlGIo5iYFwxJ0duUsNzZ33XRGtZs1K2qdx0fdjp9qQFFX673tQhnkQ1zc40tcGvdH8LrND0/C65wBerUZvShVKBEwuRG2HbP5RN440qnq7JPb885wZ13UWCftZOFlPRpM6jtl0fLuftOgkyzo02KGraSpfCd2DQoZOXq11zO1vHwDjx4elyazh6v4mlOF86hI5Ga9pyRkv3fCylSk4uK3ZZ2vQ5au2j0KPOGbRjbsybgVBqorMDuWBa57OvU5E/8crS9KLKJVjTrZfeUcv3e/c4rA6CtEpkqNrLNLsxO0S9qmY+2DbGFWq6PS8P90bPROOAZvCautCgu9zhhlOdLdNw85UwceE1E90g3ROQe1wHlgKrvXAIaGxlHGtud3ZiksRuxH3HQZnRTMFEi/t1Jq2WdrDv6cFKXW4ziLbfwsyqAfPCinVjz0xYzypsC50aIahXSsgyzk0bItr3EoUvdpHDFja31dsMGipUvQkZiLDyiKzKpXIszy05mLEuMCg7pLR+VZqBqhOEVEIqCn0pulzg0dxvdnd3qxT6jUqYK7GZ2ARqLTnboeUtHg+kc6N2jGAGHlFbnXA6rmuLZcWzFu8krtpJ+5G5sCobC1IRUHIUZAoUYbx4zZerRmg3lyouKjZsrxK63ZAbWxVHruXORrcl1LZC14NoMHjYrPRmr59qy6m2WmbyBj+k6Jkpd0x1PA8Hl4FIdrUVVMQULWRpGiIUJk3D5JN+8BI7uMI6dYMt7RbfoAssg4TEC4uvqFTwpu14x9Z2S6nqxXbwW3i/nE/cHTL7wqQ1byeo+UDtvTbzGSl3mTAHnk8OySk/k35muhmrKTolcNv+1gcJflJTAhepDlneyhznIG7JZLG/5OJ4pYuHQr7Ee2RQpDLaCpfttdcoNjCQ225tbblMcGBlT8HFTfGvsIFy7BQG7i6dtq1GcFmnTzdFPFKc4mhVzxwSQoDCVd62cnEQwztNDiQGogvJBByK2X1bCc6t6/t7rbZILXq5Vea8rLJKz627phesSopcmKj4kA/7MOhXkDWsYafdUfjhuhE6QxHk4zm5njernotNG477Ag5TnTqxQ+UpSHOVTjB1inIlchyMKs9ufkwu/Tpp9sm1KtDAxrer47jEmNicipLf33gNT/ZWc8mgIFBpeMrcSbheTUnrOHYlJa4R7ApH4w4WohipnGp572QJlSQ6G+M2F2rrdbJphYTf64TVknmjJMlNvPjUiWrdoJT1jKs3vA/E4wONMW1cbluc7+SV26Q4ktAb8sptKouXjO4qdTKs2OfGgqpcht28XLo5vY2x+0502c1tsk66oHU7SC9luIP9aBwIgRQttO/9O9XVntxN4U1PE1PdC01z4Q1ssyTLIJBqCGRwezuhtmauWbiGRrOhTBqOaWeTI8NmU6mpriW3k12LLLVG6+weaLFS2I6oRkFox5aSXMubtWvOu/0arul+S/vO1tIV+wQQkd6H5N41zuyVY4ZJUAvTv4RFItDlgVmBAB2cYUyukhJeUgPHI5Q5+OlZYpxVx9MueW0yL2DoEF8xBt2pJ6I55OJdi/Q62BL3eIBl0pAQlh5o6XjRKrcpbl26kdE15dgnJ10qqstwvqAtHXZgW1bvr/HYXBBRMBks0UULvkrbmAhVBffwPvJyXGJOVUq5gUhrUyXSF/XeI6ervuplZIj28qFKVK85naDTKYj2O4Hj49TTwKAiULyqQX0pxaeKFYvNqN9cB7Wu6cCA2kx5zOkiZtfxvgSxtKFuqX41dyFv8W1YMrhWOPFmy0wndceNPG7RdLvdbmx7342Jeb3DpDMUwxSeTKw/GIcTRm1DRlViG/b0NYI1sFVOdIyy2+M6jWJJKrvO8o5VuI6RUE8kMbsLSckc71SPlVdYY7ArpzBObPZG6fja7YhctLO7TUtfvnbmQA4KHR6OebCzL7ZR3iVcs9ZgdMdP2P5E6OUYwJZORzt4i7Roeh37PSyd8HQ4VIbKBuVQ6vC+K3bNUIoJ34njUdoJnoQVOkaKV1wdNTuKmrE8HZapejd2xZjvIT8LIJMjWFptbvfYlKO1tFmZxDW+V3HoIvfeBzgXOxeWtAaqIVUv4MnmKF2vFElvUweTMQc+BbRFhAEp7tmUdnICXipSNJArK4FCbN+usQN8PPLmKpRH2D9nVLOySxG0SCinM5Jo0Sxf6TAT8FXJTfrYnvVNbFDKoFUmKTlcy9wt0CzTrsny6fKW68qxWQndjdGMnIeXt1UfAURcwuKaPPX3NeQzt03YyUaUxv1qS+NcSsvx7pYc8i5GYi3sFf1qC2jQR+b1wAuoK1cGRqyOjQYnotHqjVLeyyDVdiq8h47XZGDZWx2hBUu4u5udIoZQ9QAEcwLaBDeZiVeWEmYOiyHYbUvqotqzeeaGmMNPlH+5sGczFuRNwsmjetq12EWgN8v2rsWxp5/aJhHE4yjpNR/TtBln+pSkHpPyp8462oi6cldYQRXKAeZ910NwbUmIO1yyi8MKCVdmRemZQcQaaVpwZrJm1VD8HtlNOzO29sx2sBKztbSN5+YnEVLl0Q6V3Xgn7wmqTbVzrNIjXZMudt+fNbJMBs/uYgLRCb/bt0N0pVWZ0Ut6eeaFZMPCDr0LRPXQ7YzcchzhTJ36dl9VJi9WlUgOlpIbh+t5OI2tKVe1jSpV5mVjxW51irHJNvCHc8ZPmMoZxGSrOYz7gdKScWvmyEruqs1WRdvtrmmtukLGrD1ddkRpBilWlYpccrG+UiOrS8KY1bDl1kgyBb82eWt6iCJd9sBC8S308VHYt7fzKA6xuVcT9lL5FK/VTaozW+4uM4127W6DZ7nMknFM0KH6XeaNDXuhLwfuOJxhUAVTom1z4pj2OITveNSLBEkG2nm5yjXmXlwWkhuwviDcL2qI7CAc9JGsXrWn9pY7UEbHHTP1mQRS4EJA2ORBKq93qNQBfZfsbkxD+1ay6x7FNb+ke6ZsdrRdsuNVEUUlkWGqvu4QTqWiMfS1Mh7J8lAAqfiLnW8NO+nJrTFuOuPUEQdj5U6MKCWSc2mdraEZLZOVtGQjVFFZ9Emjs6gy6vF0Nh3i5CQKA6+qZTfCWZCPo9fXGSmdBDVEK7Rd2zGqMaR+ax2iXaW0VhR+pNj4KuZ62T5n9mrdi9dtIHtRfLAPpJzKd3lZjqnWlVWHEHxSh1jpYv5ZMfZdqd+ZvvKSCuR6uiWXiESuUYi5GSVN7hKbZg9Mfe+0kyaRt7OPjqfKcSUITD8CumX8PQeC4BjVdxi2lQtbDleZKGIDp2pag2Nvx05RcqyXGbfMMKo4QCvZh/R9b2fhKc1oqhvEY+xdPLxjom3vSLs7kV8kiLak04Eze2/ZoLXBUZ6bDIKwr/qb4eEMdTzf5FtgHIkK8bV6vBin4pbjETNSWcXHE+ggM8Oy9DCnuCPi++V5WGtIXeGrasDvSwTyrvb1uk5BAozbqy6iJDIgyfqu+sXRHDRjn3sdKowRzMLR1FcHrGlOrXyVQCd/Vq9NK6Zu2uwuU3462KmgEBzT+WMLrU0sES+BXqU4zi/TlXijj0bjdNOp1yr4BgpQX0hX1AsyrSKlNeshnls1jn6whyEVr258ZYPKxYfbgVU3oYzf6B7kqFECwaJtvrrej0S7r8+TpMlUsxyvu2u+OTgO5xhLfgOrhZRU6X1zC053Fmqla2hjiZIHHN0pZe2f/eIkxmMRdGZLnXhvdcxO3aaAa69EamcgKvl6KYxbp7jNtR7t0x3hDsOpxaNe2daeWED9YdU5+z2aaYQarT2Cz+7NGqEqzDZOIsEjhXa5u3xHuPbW6S8MZIeQ2k3ttbUyL7riE3FLWtXP4vDce1vEuCH7ZWTL3KVVOpXkLE2YiPsRQVWZyq8qWWPo8dwSApg6hpzwqssOKs3tcYBvJ0G53cDYWO1TTs4O6317cBDj2IklwRVc6B/Dc+JsgFs7F7+00YifldHEe9Ix7TYv0fUILZtdw6zv7R3mnGOT9h3akrKD5AcHREJN6PAQ3OrhXHER70zq1uYo/N5D6yUJDSd0THJhJ+AIBO2hNbqXQYFaJrcLQhDLU4EUwjGmaIFlWm87bqbdIRoVWAn54LKiVJxbbrFRIbBUOp+pMt065rhFDvxaSmJlS7nm1ceNA4C0WirKk694rdG4WE76cbghWDC2OPoW3x0Dndj61wN2yy9sRmORw0tLUAljrQf5DO/GIGm4pDELByIKT/U85XLVok2ASd7EpCSMcoZU+MlN5w6FtrKWUrzKAjBf8WfCdfIga8QJt8l+wipeh6V7bqtwKS4vF6RYQ9Fe5zTdiFmLZUTswBsOhminlYUHiXyIeLKtA4C5uJPxbiaqjqq3Hj8Fu2Xhl9gptNmVTY/8HZ0CbQlNCnq/JXs2wD3zbk3YUpiw8y2iVoqw62CMEeV9jq0P24lcHSOutDF6z/mKOfRdf2G3/rmMMjypl6CpjvfcHrocM0rMmzWFboKeCy+sHoRxJlz4QlF7CrUOXi3cV6ncWGYDQecbtoQUXcBWOU6vC30abqUYeOEhb9AhyFoYVhr7NvjujemHjbKxp/oQkGAa2hsN8EgGFZf7vqIIOcfTqiJjrq4IlpdHdgwxeoAv8F3xls5YpvKlLiTEPQxkeOnQ5G7c7cxfOjhOtQnWn5XatwRNirfiBmc3o7S7TrLSSJXYb6PzWcvXboFV7cbbLFfXWhaugdvssPKuNNmOnE6H1pbvRLvLADqrgeH4YJzcmt0+TcEQWnCXAkE5NdsVTDFV9GV0VC4+szQGusg7mplbpokLEoyISWDtyLMjCHpgyGjsETENhgEYJ72Tot78pr/W6C5DajUvcBdDyCKrcTnmoRqH2kOHHYflbp9ZPmHAKIbhUO/RR+hQmqAXWq4307IOgmpnndfA6qPvhW0l3lQAfG3PrEmpQUrJQJRdv9aDKjBOnGHNv1xZJCOXm4o8AcDldmccqWP21kVKqwRL3xvXOxLDpgs83AhBNW9raJKbw0hdywzjEVpMQSKQ3GXbCFp1guzE8SL0akIrDAs1bpDKozIZbr7jMmjrhfw6uDPw6bhfD2TCRAgCJY1wxEwMbmGA1A25xTxsB8YrcnnU6I0YXB1+VBRRurayt6970BfE7WBIl4qbulMMZ5s71F7cUQKd9t2jlDAIKYyFXPbYFdWRv67Wew8vb/C1G5cKydzvy8Jgbmiw1DZqc6m1VrvgFmi+AdRZaIragX1pMF1INcmV8CzZSRvfRu1TW451tmk8Eb15qY3hS8E0a+m6RwhOcfZ9NKANaSdlkx20HHb2g7daJpOzIbV7cNNELK9A/yawK+V4IS1zYCqFMyg869crt8VWayz09VWKj5wsBEJBVa0xJLTrwhcw1d1TX9YMH2mZZCMsNwflupKI2JkyAZWdFSgqdY94FCTysgpVuJhB1ASdvHZLtAhPOduxnpI7ih/w/VaQa2G3J2BTWe7189FXz+uAuNfYEOCmyED1xu5Nf0NZZwmpV7tVzTnnldn1PuE73XljCm6Wunw+oRVBtBcrP/VVh8O8qF7lFXDSAdQlFJRT11X37PYcM6S/RosRsi9OjLW2hKp3qpRXq0I5I/nmuDFUikia47kseMY6WByySq8bmHFwAowi8ina8iU1MMxqxbohW413nTLkbFkR9JHhnQT1CUxu0QYhAm0D39WYi7klreSTbJXVvW57hOqrqBRV61pF+E7Y8FUfNBuRPCG8a1zuOU+CfrnryqaP9I22Wrag8K2WgRjcL8pO7PsL3Y5LtGWItcm7ARWFWXPZOhl6uTCWye9Osr0CydMvjePKg8juUNQStL2TFWbUii0fxV6493e/87o1UkGJiw51tIUOR6RO1ktLU+5aQcDwXR6aXY2o6TKzUOIMmeT5zuygAh/05Vk6JsyewVMTusnJ7nKkNPWk8cnoJ8hKW286MarXKVxLvsG6nu5symSPJtiew/NirezopUnp6PWu9P5RwcwTQaqF06AoW0HtCrJ6xBI5fqnYvmt7zort7+6OwUJSorkKWkl7hTh21pblQJ1Yn6uYS/njDla6QCXBDA/KWxBQ2IbDqLU7+ikkJnLgHcLirE8HuI+hK0X0wXk9bOLxcNo2oN9bE1w/GJVH152VMhRF/e3tw9v8AOz1EPbfehtsfprz/+zB0fP5z9d3Ox4PGn3b+/Tg9enfE+uXD2+1GwOhng/JmrQLX4+a/u4R2cd/5UnfTGF6vmj19RHz87l1a4fzq8hvMeibm7aevjRF+njDA+xwuvnX7KaZ3251wfcfn5h+U2am7Nd97PpfWnDl+crl2/xu4fzuhu/Fduu/TsPXk0Ow+/WO0ZcVjn3x63LW9vWGAFBy9Q6/r95+/98cbGo0Ty4AAA== -->
