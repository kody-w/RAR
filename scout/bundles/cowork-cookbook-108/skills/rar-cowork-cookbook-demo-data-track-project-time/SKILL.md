---
name: "rar-cowork-cookbook-demo-data-track-project-time"
description: "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_project_time", "rar_sha256": "ad0fc61f9cd8a15e226835a47e1d3b65b7609d9669e18466217134bf9eef4578", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_project_time_agent.py` and in the RCI capsule.

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

Track project time Demo Data Generator — Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_project_time_agent.py` and embedded as the fenced Python below (sha256 ad0fc61f9cd8a15e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_project_time_agent.py` first:

```bash
python3 demo_data_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_project_time_agent.py   # or on stdin
python3 demo_data_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Demo Data Generator — Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_project_time',
    "version": '3.0.3',
    "display_name": 'Track project time Demo Data Generator',
    "description": "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c165db4fa89128ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track project time data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track project time. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-project-time-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track project time records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo project time records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training project time entries created in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackProjectTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackProjectTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916edObVtbnV9E8b9UkebEfJMQmd3XVIASSAAnELsVdDjuIfV8y+e5zkWTH6U73dFfNXyOXLQH3nv38zjm+/PpmtU2YV2+f3hTPyhZ7K0mi0KsWVuYu6LzPqxh85bEN/i6cPGuqyG6bvKrfPry5Xu1UUdFEeQa2773Mq6zGqxcItqg8K4nqJnIWrpfmi6LK757TLJoo9T42leXEURaARU5eufXCzwG7xW7MrDRy6sUaxxbs/1To06IGQtj5sEi8wEoWXtZEzfhhUTdWALg0oZcuogwIumAGx0sWs6yzmB8WDmDffLdkB0h+eGhUeU1bZfXCs5xwkXn9S4YfaiBilFrVuIi98R3o5g1WWiRe/fbp5799eIvA77dPv745iVWDW287oNTOaix1VkV6KqcC3cDGxMoCsKIYgVUzcF14FdAvBbdcz1+8rn6svcT/sPjv/457qwrqnz59zhavz+e3+Y/cZrP0iya36sZzF45VWHaUAP3fF1TSW2P9TRULGKQC5nx/7vydUl4s/jo/+/HJ5D3wmh8/v+XF7CXgss9vPy2A4T+/Ve38+32mUvz403uS917140+/06lb++E8QAxI/f7ldf0iCxb+vjTyF18UiaFfvIBxo8IDxL/Tb/48RX+Re5nky3Pxj3nxYfHnlGd9/grkfYadDej+OVlgA7Dz7f2eR9mPLx5V3nmZlTnejz/9M7JO6DnxHLT/Ft2fn4RDz3KBtV4m+enDw31/W0Av3b7R/OdsCxAw/4kmYPlXdt8M9c9oPzz7d6STKAOZ8dWXf0ruzzZAf138/E91+1cbPiz8zyBfkqgDcWcn3qfFr48Q+fkH9/ebP/ztN0D6/0pGydvKeVD4klpZ5Ht18+XLzz/Uj9s//O3nH9oCRLFnpV/aKvkzmn9m1wefP1jwterHP+4F/LUszvI+W3zLocWvefE/qt/eFzqAO/f3+/WnxfeZOH+gxazEV6ZPE3yXjTWQ9Ts7/vT2G0CdDGjTOo/HAD/+678Wp8ip8jr3m4Xi5G2zAA6eIXUWXg2jehE9MA8oAOxaR8Cwr3Uv/J0lzv3FL//LeQD7R+cF7PAM0l9cAGhfHuD85bX+y0z8l/eFCmjmVRREGYBhmZKkzxmA4KyZ+RWVV3tVBzDKHhvvI0jlj/OPGXZ/+VdkvzwovBfjLw9gjp54J9PHGevqNvHeZ62M0MteOjgA6L3Bc1pAPMkdIIkfAYD+ALSt86QDWDlboI6jJFm4EUATUKXGJ+i32aeZ2C+//GJbdfg5e4LzevEsXzUMFnwTZ/HxI1DJT6IgbD5nnhPmix9+/e2Hxf9e/KtdD+IzDwkUiJcPgIScIp4XIKfaFCwD7gEOBYDx8MGvv70MC8iAwrkAHov86Fm05tiPPferlZUD9RHB8IXtAesCy6ZFXjVzAY2a98XRX3yTFzCdH801IczrBtTewstcL3NGQNUC6nyzZJY3oLo2Ue2DgtrW3oPrL3ZlPURMQXJbzS+LEy2BCpQn4J9ZzMcisDnPImD+bzHwvA+IVKCMbr+SeF+c5yhcFFZlFWFlvXj41tMvc8l/bQfErbkWf87mMuvNpnqkxNM8wdxWzH3Ew6UfZ5+DPiQF+e/WX3kHr9bDXaiPell9zupXuFuV96jxQJRxEbSROxeBv7xCqg7zNnEf9gOSzpReXnBfXnnE4KPI/6GFWcz1fzE3AItX1zMX0hZZrtDF/0dt0Kw8td/LzJ5Smd2COavy9emUuRGcnffsHYE4D+EfCfh7p/IVjb6C8ucsiUCEVeNfnisfrnyteQJdWwHLy5T8oA/iCDhlpvsI8zlsq2pOEOtz9hX9gTaLB9QBTwNMADkzh+pXhvPTr5KGIPHn6987gZfOsz1AKC+K1k6An3zPc+3Z301Yzan68iqIeW9O2z6MgMW+12r2B7AXoL8AQkQg+UCFeP+GyM+nX0X/w8ZnwzNveTSDLcjU6kEAyOHNAs6e6qMGAJbVPPtuoOenBxGgRlo0s+42yBWg6fOmV3llG9VRM+Pi065eAfD44/z91HS+6w0FCENgLJAERQus+0ibORZT0M4AGUC4gixKo+wZvC8jPAha6YwBAGNfMfSk+Lj9Ush75NojT14bZ0XmPXOpX/hAdHBn/B4q1D8LE0AvnVc8+P59pH3jNtOe4bIGkAc4fn367Anen2X92TcsvtL99A+DzY//2ezzKNTaHwPg0yJsmqL+BMPP4vq1tr4DsIKfstaPOvtxLojP7P/4AoSPzyL+Hc2nup8W/5lcfyDxyotPi9X78n05PxJecfX6ADPQH7fXj+j89HMme7/DKGCfpyCwZqeNoLB/q3lfl4DCF1QAjsDiZw2s59LZg2r9AH3ggc/Z94E+JxqoKVkwB2adfwcAj+IPgv7psG+1CTzKGsDbnVvEwJtHskda1N7bp6xNkg9vACa9fz2KzaUnnQO5nmc3YGvQbDWR97h64MLQzD//OMaKjx9W8g5AHmBQUn8fbK+CMRfM73LiqR/QywEcPizcB+iCOAT6zcznfLLq+AHwsx7NWMyCP6e2uc974PqXJ67/o0DKC/1n9P5DCZihrgHNhdcsfgSzpdUmzUJTTuxPf1mkLaj+sx3tB1S4zybyT5l/60D/kbMBmoCZiZt/muvhhxfqgG8wNYDy8nUAACq/RrLH5Jy1YNr9eR4+Zh88tsw/wB7w9W3Tt/8/sL23v/2JXE+jfgF1OvsTL53b1AZxBhD5UVi/llAg7NcI/d0mCPbTn2r+tVB+eUbS37N4VtO5ys7A+IjVeeGHhfcevC/+VSZ/RJYI/nGJfUTQ9yGphz/h/lAQQDUoeLOtfnfC76bIH0PZLCgwXfP8P4Rf30A8WzPbV0S/unqwHCDbx3ruamCQ74AhuH5mJnj2H/X7r711aIGeE2y23KXv4Ct/47iktcI8BMHJNWahhLdy1zaO2QS+3LgbHN94KxLFcWRFrNao7W88z0cxggT0nrn9ZW7bolmeWRhgBmA6z/v9MbjlvhR5Cj5b6dt4MSv80ufXNxtHwcoDWh+p54eGoZWNI4StcDZU4V6OXbYCr0gybirZyWpqtlhf1XAboGGEeOvcPsT7cOQE5hwbo2cz9z1lp0fvymHLDBFxrxxpjkU0PK2nekJomuIEoVzxyQQ5eDLmxH1HY6NEBIpxI6BjflaSM7uPIhFTHEM24SqqtCEmCrcQOgJJCMgyieNlwnDBlIpB52T5yBwtOxSvCXOZlOR6ZXkZM45Bwkv3yOI6NB2DfBB8XxrcDu7WJCksc5iWnYLbMALrQsJeVuRWR4RjpZjIXnei5foYl0yG3u8quj8NGmKZ41rZ7POaigbfiEXxcuBPgbI3BL4m+au6DAj9iB3Xaa+sqWulDiSOoHHSdKfDfbVp1zfSbUyWdA9od4/RdsjU1VgXl7tSUBezL2HevZW7vWFtTMZjaWk6mcvLIF0b9KqziXyJoXN+Qo1WCWDmeDYZazgzpz6nKiqmJhax6olrN4eY5tW7Vkgd3WzFE3knTppvS31s1GU0MATTOKPAMysmo25myiLpxhSWq47GNnm9gq82WiFmxKEHDRr1206iSaOWL0td4B2GxYXGCxjhiMSTIh8ThE/XGqO4GXFUV5RaUk3PbDW0PaWBE7TWwS8zb4+dL8tKxtKYVjnvHht6uBMy3NhumbSNM6zNTQom63q8y7oeBSsxpXx0bWipbXZBn9ssxB8kzBo0ndEvm1XHa4ihDJlLZTbGeGNM3lRqQytlPZbjTos2yuHmCNA5w47wacsoWNLl8eUmiIgX+XG/qWnpipyWAVwW6zxnLqsuYXcKB/H+AAdHy8y5RDqn/GpKNDq/ImOu4HrAWvuhopS13ZQJziknV3YS4+heK30611Hlc9Slu9GZdDavVigOBsvDOS0l3IrenchEErUGOnYGsxtkgkLDGjlsi3U8UPXSR4bSjzL9dqvNJUrvgui697DeLLCYGoxwvLTLDZ0fzyOJZghMJdyoWEVzz/WM9HRV2xM9K5PotF5lrXA+EJqLm+Sl9w7xxoFUAt6ODn0z9wVGG/fK7UFk6qt2QI55NPJiLVDEKRZS2GgN6kBNex0ZIVI4NhK172ol5Px0a5/9RK0lS2VvSRjrRas2dUivXDzImFjRS54qIYWJ2wPjRE2+Iw/Krr1OKLKbID8q7MBd0pZzDOg95GCaKKT+TT6nWE8Rbm2XkrpV0XJNBBuBG+iIZVUmk53hxphiE+3iom8MtbmEBVw5F7TyU08OdMMbOgy1URTnKEmvy0Cp+KnaXMzdltbJmxB3MUlOmkKVJyAyhGsyZ5x4temY8D7cm7VwHlhdoY4sZRTCicok/XRUzpsSdEQHpYyLnY7tJZrj6RMW7/f7Duscft/s4su4lkT1CifrLJ3uskk5VrfMBgEihHTFTrDRxdoa2W7jzhGbzUajb/iVukyHVpnSU5WmhLMqAzKIlzuUY7ZS3vqnHeIL2z6CossuveaoD6nFZOROrh7WmpOijsyyDRSy0nY0uXxL4xizGoMq9OviQGGq0e+MsLcqIbLPy4hilasKsW6/dTmIpVsrGkv+0hfNVUYbZQkRR7PuU9ZtS2sM5CAmOzKoRIPwSv8w8axCW0DGdupEka0O3qHY61lyoqDN9pq1SuxAZMTX+mTXUpbVmVRN3hWj4YRQWCmYwk20E+lLnjCoFEkexMmVcoLuCpUzaMndDOx2Vy86UVLF7qTrAEO3fI1KW6Xzh9tVpkahuZEVLt12h1V8KBSVVuJkzzd0drx1KrR2zCwGJf1E7Giei/s23Pr3ruWiVsu38qnARHe1y8SpOuINc4+9OPT54yijaEQuq3h3BG3LptdrkUrupX6l9kxX+8VKOdLVxvaWy2B3lqP+hrvRclMRW7wxdhs2p9FEs9CAFA04IA3HztFcmhL0CHe7fCNNOcldD/ytcIMsFlWh3PLnZQdpXJuk4ZKX4NuBO9zuwzoiWU0kxDo/IWFFEX4nbcj1bli7AtyvNyQJ9VKgsqLkpMXplmR+VN2CYBvG9BoTqxBDSY/laOWc1HVe7o8BeriYbirmpW1Loh1ZUXiKV2Y0lVoOfF2xjcfQI7SPmCtSMmZOhxx6uURtXKyCflpJ+dIyr5rfgOw6XCVC2mvXe3HobxvOpl3kvtnt9ZNX39e549a3EjuD+ROPAqS9R+eWFAjnBt2uemkUhwkexkrfrAwh9k9LOgq4iC/HSLRUcW0Dgxbb1ryiTX+85iyBHe7duYQYT0hA23E4SPzRXJY7XaJ9h7hS8trsWDhzAS7uEimn7/l5EpnNjVV7fIN5SW0LvqPjks8nTFcdCygtk2XsWeE4KN0xG/OiZ07UOkmJDcDXSaeRk2bSt1JQckrR7hjtyPLIp7wJh3AN3wRsNyaOH+ry4cpfau0cB9DBHKUDK24YgnW5+mwvr1xQXOLcGLQAmsi6vLPccJV4jVozHnXIqa1VKUvMLCa1PO914MIkpDTQNeT6iJb6xWToCjmGVyYt+6IzXH4dCL25HE/WMXTq83Xb3K4mtjx0x6G0hLgRyWDsotjkVQjdB/3+qGZpy5crzUyJhKEF67ZPvKjxl/hW2+y1+3Ur70hfLoxaHbhxcgpHYtBpxaIn2kiivU03R+us0QTrH3GFOWWotjVqlpcO11zsL+11adW2Ig1VtLyEMdEpA7ThTgO1m9hbowzpKeiMOLozulrhWxrymHJne2ranwyS7c/TxkAkn+WtLSVdHFwrAthATSPYe+i+pYNt4WcY7h/CwhL3InEyNYELfe6Y8ixsWSO1b5uez9lDdT7LLB/3CqUa6pG5u1sRgAS5zFJLO+NLg7EuO4OX9hkPOrqetrvdLRD43HWkpVfeku1+u4pQXnQ7ui3ESqEIAigFH+leu+pGVTmTt70ryjW8YbstmjdOmlcIQwf64B+uJbvnAhxSlsfrGs7FI0KDUqPFE0A1UGJ0pDySvZpQwbmZZNg4joFkhqccAY1H0KI2KUAwzIDxOD/v7VyML06pTHdU2ZMwJx3z7YhI8YVs22ufj4qNHTk40krWG1vdwkwI5ItQqFxBB4XChLzuLimKi5NS1rcAsHO3HI8Gf+FSHxpql2IBvrVgAKAq9T6ttTw13M7oKrkq1OO1OcD8nRCtgrlscz3gxYEWYiWkxv6khurlugw64h6VhYRhLaeEl1r0Wg/H97Jd042EV2gRbt0derSkkNmRnkRAkxexCL31GPu44+KsvjpaOLrnkIH6YLQCZV1jXKPHlAoxsblN7X0YLe8X1MJryLtj0b40RsyPqKhs6eRS3N1Iy72t3inGOou6NCA8314ivqcWJJlNBDFJtclyJLQpkROhrAi9Y8pDZZWmrqtmdXYh87AXfXk4gL59wOxbH68uPbxndx3DjpfEqdvjvgC9TTJFoDFV9xeJu8Wm0a+pLu9Wl3aUQs3upZavjsLlpLUT3bJMc8FOfs9eubxogsosdCKze2PbXvkpqAPezCjEtg9jW0kZvNw3J5++GESOiKBrNhyH4aFYqL1+19zytX+pGZiN5P7Y6NZ0q7KKuK8iZzvAbRXjknGAEZxQ3eaW5neQ/t4oLnmi7FTm3uvZFfQreIWMO6valrFR7Qcx3oXxjirxItdEp+6RoMqFboCpe5+LerZUtvVdbnlx3XGbla+ajjuGRnffbEhxBxolJTreu24beRhnXEI9PaGavY+52/kI2nJBOyvHNcS5cpcc2suVU7wKgb1Rh7xMR8iWiCsNzc86b2VhJFxjYcXxq05Mew3ntF4XoUkz4t1tRED318znRXuIPuzYSr+VNn/b27Bp0wGr6l5lHI5mWCmoatWOocvyXqLI4qLk2M3SmDWmScRwhlgm6VRUyHulJvF+8uS1bC+HSjqrx0TsNmYfdaJGBWxKj7u9edQwkvSU9TYyLdsiONJqCR8DPVB+Kc8nRbaWPTwRV5lJrSRbF6eM2C2Txr7xK1YwmV2JNUlt7t2hurV7C8NUacL2VBglROPWS63SthVd7g+3g5Zb5yEdCOoE2awH6nXuenI1qIqeXzhKawPnHvoOGFuGZGSdQKAExZbWfr663soKbxV8A3VQCesQr04oy2VpSLsK75XNVs8JhDhu0kA+XfYOchIJKoK4tXLRogNi30aWmgg+gYRgRLSd3hobHHavWLTMC4MPlDvCZmsFO5oXYtRpSZPhEVH3aee6HbeUIZwLYnXfGTfRN8yyjsSwkLyDS09g4rhRDCQySHXnrvldTiL2UmmyHjfHgutFaJnwvmR2UXjeG8zpElTl0gKDWGREB2ylgmyD0+VopavlBIaEHXkl+sM9T6oe1bJaIFRDNw+yaE46wyAu1zmn4dKtjol6D04EhVPR6U66YmLnXS6uwuXqcLEvwsFxsGuyDpZV3Wx87VqnuciorXREQUe4znBmZUK918OtVBBOb2PtsEcqHWFEdt9GKGxXU7MPfCPEEBPFcBKrD5cG4ZKqazsRhcqTCpXcCgbjV4FdqUwV04pZZd2upZkEAeNABfRBQxffpdbG04oMCaFwXQ/YciSRZucF5MG9HrwGHqTVaR+mEeIy4XhOh9OZ3RnHsrzlA3RbjQ4hKOIlNldVuyF2V/52g2P4rtbLcZ11hJVbd6FPEIm8VVZ42YjWSl91jmJ5rot6uRn22MGkAiJZ7ZfanlqBWdTtfHgpwHm7uu9OowmbUwbx8PZ2slZr0960+R4Mk1eHyfJ7Djh3u8vSEOX1LnX0hjExXSV3lo6gB9nq9MGl7l7Y8ExEpAeUoeUDJpXiCeaO2SbpV1xuCK55wq84r/t4sQ5QfLfq0A67QfTRKH0jEwXvit5D9o4H63ssib6iFK2utGsG3qYucgmM68SjBOQQVSEMyyla7jwimKS+2bX28YrE0Kic9SmONstmAEVH7VK0LyHcO2ENMmjmzqxQrbliCKf5lbyMkw7HoNXuSnLbeqSv3mXHRLJ0uKOZKpVjjJ8bUmbis28YOdRf29KPrel6QhrXAjOZmxvlACZT6wBK8tSUt0MNW4XpX4f0sJOGy3RD8RPMEo6dLEPhzt4TNQtZJVZO/d7DLX+ZsndD1JTtodqfhHU+heI6OZ7LtmBw2LBLens8TfG5oYuxpJqKOW+sfS2L0NnS4togiZbc3eI+rjNd4pFJKZI11GZ3bLOpp0mSDLavtejSVhxxO5wIZtUTbbVk+IYIpNqZxK4/ia1Fd+dOxC5c1CwdFYVgl0VZl1dZfcr08eol7bIeGMLbJtk5aG+BhTtD2iQHg0VWCFnHZHBIV8wkb2DEQCwc3zXx0Brw2RHHUzxsE8/t7VwZt+gZyo8l3lED4p2yayJgBI1lp/aguWfrSiIhU4ST2Ij76ZbwksPgtzSd1scoFS9Fq2BsOO4q9LaLcHub4LAtHCZqSWmKvtURKFvlWEh5irSONkVCDdWxlGSUYg+IbOrtqGjZWm7yBCSfuqYarhWU5o5OlYroLltIDgLJa7WTDidfP6j1ZVr7mVsla54hxC0zmdDkjKKNtFOi8lLIF/cSDB7szWe7bnPREtKndNNcE4ZOs1lZ1y1M4xvhXhdVsgxWPkrDkTvGo2zwsHppSL1piWmTVLqQChp+K1ZY2MmMoUqOB1/b++SCNok8o+TITiQkkZG9O10Y/ibKm4tSmMm9k5N+ohkr6ZpE3hDMbVA3nllSbLUv774vnGnNtGR4Txy5wRfznL/6o6fy+/tUkdXVCiZ5KqDjWry3m8tYIZKMHRnyGsPochwsd9hD/M52OYK33Wu53un3lC7MFW7Z25uE5RUudLBI1LlcUyt3TZdmEDDs8UDZPLFVYY2Epi1yXvUFYxfjgGr+fdgQJoyDkEaOFXzi1SG3jJZQCElqhKVTSLLNOULKMVuO9G2xKZdLdDV4BpLZQzw2JOQyPK4n9TnfnA/n2Oxx2zDai63yd82F6fG0d6VGSkGsOwQiKq2KB839IjdwkjhTKfR1pIwusVyRxQZBk66L/IKQDYHrVglVhuq4XinOQVYTtbJ8qri6yVmISQ6MXfjlii0JhIzu+saCVmqiERtblZRwkg8bUhbXK94k9HEptWv/jCHS3Uy4pFCgpZwqXMq5RyK+nKDckINMJslOghJyOLmCS/mue1h1q+bSGqN7EYcaWeGlswxX8JoTsJU+FPrpJgl4mUA1gGyEKHal7OVytN6wW1ceVA1Tmx3V2HJu5YyO4EhjpPBJajsSObHEAQu0dCISQrA2G967TUEzKtxO63ehk2p3C5sayJDPjZupa7qC5fsyOm63dpUKF1q+3jDySDBSDPUaFSLoOWsRpfHWqc6tV7vdCYI9Rs0CzM/xLKrEBumuNCRAaW/0w+oOCdNFMrasj0NRV0Bo3GWlEHsrVnE3AKy2sGq290Mf0zCsuGRcCmf45oDmsfc2NESwk+NQRYGSxPmGjLpOD/rBbbbW2vJvnWiqa26CxL69YjA/uvjmrlfbG3raRLez0qz3G79U0nLvWSZaIMkVXw8nDuGkrB3jq18ta3Hc8Fq/nlKCtHXWv8I0K8ZE0C/PuyCgcwNOrkWfllTEoWVeB8IS63BJDZaa4d5Nr2k4Sh1WbDeWzt3agS5UF+TeE3dkgcbLnBA7T0UwDYSIlNs1gjAWXKzha7e68QcCEi3PsVx7zTSTv6KxcCN4+3KzFlCJuLS3O7PHEAE18GifHC6sJra25LbtbSB9x6cwco9RqDN4meSVTIekijaJrmX5k3k/iRu9T/ZZvj94uWGOCXsIYHJb9DbuW+yWoqi/vn14m4+5Xger/9bLW/Ppzf+zg6Lnec/X9zMeZ4ie5X568Pr074nztw9vlRMBYZ6HYHXSBq8jpb87Avv4rw7w5p3j8z2or8fEzzPnxgrmN4Lfosxt66Yav9R58ngrA+yw23p+k7CeJXPA9/eHn9+Ef958Cp7PK/1ofh5l8+sWnhtZjfe6DF4HgmDz642gL2sc++JVxazk63Af6LZ+X76v3377PxIIUmbILQAA -->
