---
name: "rar-cowork-cookbook-teams-update-forecast-revenue"
description: "Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_revenue", "rar_sha256": "36bd5d9e5585b4b41398acb3affd47075b849b968ed739df16e9b86dd13070a0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_revenue`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_revenue_agent.py` and in the RCI capsule.

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

Forecast revenue Teams Channel Update — Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
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
    "card_filename": {
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 36bd5d9e5585b4b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_revenue_agent.py` first:

```bash
python3 teams_update_forecast_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_revenue_agent.py   # or on stdin
python3 teams_update_forecast_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast revenue Teams Channel Update — Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_revenue',
    "version": '3.0.3',
    "display_name": 'Forecast revenue Teams Channel Update',
    "description": 'Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21a515d6c0b032cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/forecast-revenue'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-forecast-revenue', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of forecast revenue. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-forecast-revenue-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast revenue, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes forecast revenue from the Dynamics 365 ERP plugin for a given legal entity and returns a draft Teams channel post (markdown) plus an Adaptive Card JSON file saved for review, never posted.', 'example_request': "Draft a Teams update on forecast revenue for USMF with an Adaptive Card — save it, don't post it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams channel update on forecast revenue status, with KPI Adaptive Card artifacts saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateForecastRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-forecast-revenue-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateForecastRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVpbmX9G8/cF2K/MViwCRHRUxCAQChCRAgMBZkWbfF7EJ8Pi/z0VSZtplV3VXxHwaOZ0ScO/Zz3POycuvb3bXRmX99ulN9e1iwdlZFkd+vbALb0GX97JOwVeZOuD/hVsWbR07XVvWzduHN89v3Dqu2rgs5u1dntt1PPnNIihr37WbdlH7vV90/iKoy3zRRv6CGQs7j91mgeLYYqecF1XWhXEx71jYizAGyxeZH9rZwi/auB0fYtR+29VFAxZ4tR20i4tv583Cjeyi8LNFVQJGPwLWqVfei59mimBpsaA8G4jW+wvarr2FoJ6OiyDO/EVj9773YAiki/37h0UBpKwfdHzvHejlD3ZeZX7z9unnv394i8Hvt0+/vrmZ3YBbbw/uWuXZrc++9FSeaoKtmV2EYE01ApsW4Lrya8ApB7c8P1i8rn5s/Cz4sPjP/0zvdh02P336XCxen89v839KVzys1Zb2LNPCtSvbiTNgj/cFld3tsfmdTRrgkiJ8f+78TqmsFn+bn/34ZPIe+u2Pn99KIII9O+zz208LYILPb3U3/36fqVQ//vSelXe//vGn73Sazkl8t52JAanfv7yuX2TBwu9L42DxRT3v6BcvYJu48gHx3+k3f56iv8i9TPLlufjHsvqw+GvKsz5/A/I+g84BdP+aLLAB2Pn2npRx8eOLR10C/9iF6//40z8j60a+m2Zx0/6P6P78JBz5tges9TLJTx8e7vv7YvnS7RvNf862AgHz72gCln9l981Q/4z2w7P/QDqLC5CfX335l+T+asPyb4uf/6lu/2rDh0Xw+Y3xM5CHte1k/qfFr48Q+fkH7/vNH/7+GyD935JRy652HxS+5HYRB37Tfvny8w/N4/YPf//5h64CUQyy80tXZ39F86/s+uDzBwu+Vv34x72Av1akBUCYxbccWvxaVv+r/u19odtZ7H2/33xa/D4T589yMSvxlenTBL/LxgbI+js7/vT2G8CdAmjTuY/HAD/+4z8WUuzWZVMCBFTdsgPo2gGMzP1Z+EsUNwvwZ0aNGXTrJgaGfa0D8T97eJa4DBa//G/3Aesf3Resr9oZ0b50D0j78hW7v7yw+5f3xQUQLesY4DTAZYU6nz8XdgjweWZY1X7j1zOiOmPrfwS7P84/FgDTf/mXdL88SLxX4y8PjI+fiKfQ/Ix2TZf577NeRgQKwlMLF2C6P/huB6hnpQtEmeG8+QD0bcoM4Hw726BJ4yxbeDFgBqrUq350xaeZ2C+//OLYTfS5eMIzuniWr2YFFnwTZ/HxI9ApyOIwaj8XvhuVix9+/e2Hxf9Z/KtdD+IzjzMoEi8vAAkfVQdkVZeDZcBBwKUAMh5e+PW3l2UBmQKUH+CzOIj952YQlanvfTWzuqc+Ihi+cPzZiAtQkMq6BZi/iNv3BR8svskLmM6P5qoQzVXR8yu/8PzCHQFVG6jzzZJF2YJC2MZNMH5YdI3/4PqLU9sPEXOQ3nb7y0Kiz6AGlRn4axbzsQhsLosYmP9bEDzvAyL1D81i+5XE++L4LKt2bVdRbb94BPbTL3O9f20HxG1Qg++fi7nU+rOpHknxNA9YBCzjvlz68VHC3RK0GoXXfOX9WGPPlfLyqJj156J5Bbxdz65wQQEATMMu9uYy8F+vkGqissu8h/2ApDOllxe8l1ceMcj+Yzfz7D/oV//xbAUWnzsEgteL/0+6oFlviuOUHUdddsxid7wo5tMfcw84++3ZNs7CzUQeufe9TfkKRV8R+XORxSC46vG/nisfIrzWPFGuq4E4CqU86IMQAqLMdB8RPkdsXc+5YX8uvkL/B2CIB84BJwM4AOkyR+lXhvPTr5JGIOfn6+9twCMigDmAWUEUL6rOyUCEBb7vObabAqnqOUtfHgXh7s8Ze49iN/qDVrN3QFQB+gsgRAzyDpj+/RscP59+Ff0PG5/dzrzl0Ql2IEnrBwEghz8LODv8HrcAq+z22XIDPT89iAA18qqddXdAmgBNnzf92r91cRO3MyQ+7epXAIs/zt9PTee7/lCBzADGAvFfdcC6j4yZwSQHvQyQAYAGSKA8LkBtB0Z5GeFB0M7n9Afw+grFJ8XH7ZdC/iPN5qL0deOsyLxnrvPPBLCL8fcocfmrMAH08nnFg+8/Rto3bjPtGSkbgHaA49enz4bg/VnTn03D4ivdT3+aaX7898aeR5XW/hgAnxZR21bNp9XqWVm/FtZ3gFOrp6zNs8h+fBbDj1+h4eMLGv5A9Knvp8W/J9gfSLwS49MCfofeofnR4RVYrw+wA/1xa35cz08/F4r/HUIB+zIHkTV7bQRV/Vu9+7oEFL2wBugEFj/rXzOXzTuo1A8EAS74XPw+0udMm2EqnCOzKX+HAI/CD6L+6bFvdQk8KlrA25sbxNCfR7JHXjT+26eiy7IPbwA+/f9uFJsLTz7HcjNPbyBrQLPVxv7jCiSl92UW4Uno138YZdnXk28h9WcU/bDw38P3xb/06kcEQvCPEPYRWX+cOb4nDahqQLR2rGbxn5Pb3Os9oGpo/yzJ6fHDzt4XjA9gMWt+H/+v8jWX79+l6dPiwNIu0PjDYpasmcstUHc2xpzidpM+ytNfyvIoPF+ehefPAjFzyfpDbZp7g0fbAUDwZRVNldi/pP2t4f0zYQN0HDMtr/w0F98PL5wD32BI+bD4Nm8AjV4T4GNULzowXP88zzqzyx9b5h9gD/j6tunbP1Y4/tvf/yQXEOwBnqAEzbS+C/l9afmYkWYVAOn2OdL/+gbCywb2tV8B9mqywXKANR+bucVYgQQEzMH1M1XAs3+v/X5tbiIbdIBgN4o7HuaRPoZtMGftrGGU3Niug9pB4K0JiMCczZp0SHzjewRKegGM+6SzwT0PRiECsmdhntn2ZW6i4lkgjCQCiCSRYA0jkOf5AbL2vA2+wV2MQCCbdGzMwUjb+b41jQvvpeVTq9mE3yaB2RovZX99c/A1WLlfNzz1/NArEnac69kZhf1yyjZDBMveaKq7fm9v9stkgr2b2vu6S7C6gKZwK6rDmqYmwTB3FBsvDV+tdEwLUnZpX9GjREojRYXVpaldKMMx4SAwzAUiT/1l5UtnaeP0O2xi3VvMHgr8JghiHHiiE1ZDV1lCmR+GQHEErcxWqxPar+uD7XBqt4Jd3Wxzr5WmS6ImV7Ua2h1RKKbK+cEZ1vpDuWbhzK2vCi2tZU1coxGfmTUnd3p2qF26ynYlKxi+LoSycDlYRmbRNHQwzBurZAl+Sqs+TVhlOG53PR+leimGJ0HHhDMGLT2IaDx12JXXzY0W/N1xqLyLpNBOIuUmLq6kfTg4QXCtJ5xsroSOBDHs9Cg7rfB1Aq0Z8pRudyStdxo+mSnMZ1x3vMRKrk9lLhARhyDTWJbjFvMZgybH3FgGuclt+gihKd3gA5O7xoN7vbDEbbu/y4aO4usUEu5F3vHaBkOkaHeAdeUSUzuJ7Ut2L4h3pJcO7RE/Xet6yU4HM0WDZhpZjdNUsbujF3onxnuVwkgthm+sKUZaa+3DY5FSkZlCuW0Luy6SUXtAOmPVgP5LccoYpUKaGPDR3o5H4kI0d2JAjzWXOUZu84KYYSdF0HdiF1TmbqfY+CXnYKTbEnzjEkip5sN9SC7UajRr25MOhlE10GXQuuCGQaXW6Rdu2GQXyztwHpSvfD6BtWLidfnWxLV7a8KMCappeyjsaaekzi5ZR9otEI+XRPYjYiCE2EShQyyZiEeEq1uFyjdrYm2KN86bgVkes3VvGnUrtZ2QMZVBlyY0lDamh0eb2/a0enW6mz4e1EbDO5pgT41VEQau6Pu45q9ldFjFoQtb6fpirNTV9raCuoZdlb1SmQITUP2S3ILoWNceb8jI4RxCh40dLq+ws55Ow6HpmlxA3Ii5D+35vJGOiMvt7EOKHTZuVg2qEOMcQ8OSvRWg5QALCX6uVZPF79K0sa6rcb/cHdElEuWXlSzbBYS5q0u/5LM1cLN+uB92OReK1wsjj0J20PQYh8p7NhTWdR9HoTK2bqmEF8rcE3vi3iwRl9KzMlR2ZyS2j5dUU2xeRwxOOfaj26ZS7kQyi0Ox2m5l9hprWVau5bzndfYURmOI0/d9tt7xSbEuLCpf0aJLAXUNhx4Rw7hYubdbTmaOJWgsaqKzDgJO1KVCtyUhFJPY3VZ8Tdvcsbb00tqtqTxdSjKZoKoyXHnndCrPariHLU7b2WGxUiqRRjBouB4J08LyLodXom7uLR06ecrWACZrNNudtk4SKndI13lK0hSTNtklj54v5yiZ1rCn1YFNGIYtb0lJNjyNUS6pYwErN6KeQ9dYHEPqHuLaPkUKtlvK5RBUQW54rW1qqzPpjlrVy0am1wPhn5Fc7Zkd42/LQmxiTcr2SEdvjqUn8V5Y8DpPnwN/yWvN0nAjOtrY5JnpIW8pbqZMXS455mJst5XPOhil3+h4qVtMRyDuvXM325wQt9Np13YUm/uc0tZHD91RIjQWG5G4czc1S0L0qNjXJGYEJzu1Ga43hXXesJuNWSUKqkny4YwufT3vJj8PuG1SjqFRrjF0uyp6cUjOCZTcpjEPNZd2ryc1hUj5LmQl2u5LlOmnVagF7Dkj7ItPM+vgjsUUtzUNJS77+OwvhSgjbucICm/YUVWNjDkOtaLfIUWNSckotDV9tQYftEOrOL7H21C3sdyBaKjSEirfybAkJbZ1LlGzPOJL3984JGdtE4wHc61Z3jcCnUHptVa2tGhFpy1GaDzn9YbV2qxE+wcmPqZ+x/eHQ0ip4pFw6rMp6QJLdxNVisO9I66iasRajtXtakcOlFRwcYQjLAPRt/ZKw9Y9vNBok+077KBkFCB5YhF3x1PYMjg5EBz0h4xUYikFuGNx07Fdcrpx8s7CJb+pzlkuyW0YM+nodf2ZvISXCIUJmvEiOQrRepNdJxz2ziW+YpR1y10GhC0Jtzptutt6YqRVZgxbmhNSyKKIbp+2a0hQDsfroZLxmmPYexuRa/NeS1OyZlxGuxBr+rYxrEumRJetpGAhNgi+dhG3flqFvaqF9UWgKlkOk5HlS1+TORCSpFQpKxIzhzjLPUzZ0TuEE6xLxEo7I4aToLqHnUA0nY+4sJYirJNspNO0S322Uw/FcTxANm33CKmNho3e4GEDkaYspXQa37qjNVzOHbY3LflSl5Zb8op8j5K712yOflp6u+zAsC3WJwztKuKyi1AxZaVYVdobTdNHkWHMezcl3e7QCR3P0xrUrIYpUBDpJKbHhDednjpjlh4aZyG9JMw5Q69MSwEMSlu6wPGaVak0pW98fT2VLiXDceAGy0CE5UoXJGrC5e6orm8DXYXQWqZ1kc2FtIgxxGzVO91CjaFlqnWlxH28jZL9mvSpxhePMWfoEdceGMIO+JzMTqG97NWxVsUgHiQu2qE7i6/LCKmiG5TZq+OygbCaYpONRmeRsD+aB6dDqnVpKALPkVvXStu7j1sNW/Krsqt2d0ShSRexyQBUvwTW27PMMrTCi04CO1ueP0WdtI0pnJ+KvD8c5fOG07YsnuI6JuqECuAIskRqGcmVsM4hW3dYPMPsXltffB3NT0hpVpx2bYRmuo1btarkkM4ElFqOxwu7leScD49S5FrwPkSznlB2AsmVTBxeV02ParLkbpeDaEibQ943XKRdGrUTNEohXQzmkGVxpOVmLUnHqUFAgmwp5ALJIbapAx/pyVPlH8niVF5SquqYYeVd6yz39/5qm2vENg6qML1VZ9NWD0fGSQL5ttdsRONN0Oy5hZrKFb9myVOe1OxFgkoH5m88tOVajTxKGkwqYbpy9xOl69fdyaLuS1zkrOnEjppsi0LV+cczg9X6iPSr1XkkRUTmTT1ICQSrwIRsunQD04eDGWx3NYTu/CazqhW/ZXjnoiSX5ekuHbXDiU4RwXA2BKL4FUIJ1C5SBFNPR11woYA1jiUz4BM06du1fOhyglkFU3S4IxUT5fi04dMtH7sBfoLR+FIfZLcvNlR+vXIVvYnlQGYsMXS6LMru6iqQsHIcZVH321QQqdir4BTvjoawG+SousrZmB/SUR0R9XTmZJU5CqwsjnJKcvm1BYhzdRBxEwvamRBZyL8gwWUoNx74e0MWF2K5xi6GKSagfelC2WjJATGmZA8PVr+tmzu0Y1g/Ou1Yrj60oKDx22N4j8J1Hkb+LjqZqUpkreyDJIHhAdvAgiuTzUZZdgPsaKJ9V0aqoHm3lDFf74MrAQYV/Sy6E7Y1EwFutixIPCH3PQsmdq6lD9Yk3/s7YzesPQSg2kwGGBUYg4ALlz3U51tCmGPJdjbL7ZLzPbvzUqVu0ytOXLT9iYN3iBXmG4pDhRHPrZOp2Sk18rtwXVOdkVtyqggdd73jmy1q0lO9Ijn6aq9jtsRysXZqJUa3m35Fn/bKGROKPqASfEmsw1EhatgN9XaqHSxVEWp1hM4qqE2shV3aXIMoDM2dluStjU15VFZ2R75s16pzlVHB7i20PXeN6kA+W4IpYUtbVnqvbakId9Tg8piJkxo+9MvRpy0uXnHbbbu/byaYUE8YLk8HolhJ6PXMKy1/jnmy5M6cF6+tNDcQLaUtQtz1zYVHeUI9b/a1ge9EQ8YY5KKhaWSa2tlEs0xMJaIpTrq44g+SFfZSKzjDLsG2VxVOqH1eZXC8N+879bZnIbtQBxHdsmPj7G5wcpEErSsLbNnv4H1KY15tHFiclGiEuIihVoqbJEc2e4lmafTKlxN8v07DkdztqVHM1ANT7FLuYMHQPZqGFkMMRGfMbJkuyy00rWX8wlhbXWkQ4oReeO1Ea2K23lDpSTHvQ9W5CJhIPI0UENmh+IoVg0ZjUytEkqMkdhdL4vtEadLb0j0tJYdVyFvhRnqg7U7b9u7sLOjAiTBzOd7yA+6x8aoqqfHI6BVquN6qcvB6q14x1T7o2ja61NypZ46+4QGt1aNtLNuGNeUKP4YUdDKYXRwQEY0rh3iH4dMSt5hApgHmS1s9Vgg8SNVqO/LcXm8O2a1mGTLz9uwaB8xxjL9vtqfMGmo8UwTMwMeGAk0erk0Nt+7GUghAXIxrpZYSCxc7+3hIutzVlKMQDadEMGX+0jtoqtXmiN1XjBb0Gh1NGcOb9xtJZbex4Vfb0bjvl/idcC8MaAZstMzqzfYcqsNeiFojulunAIJ2NrnVXJjnpJu3g/WxKUdrCrrwFNA3zodEOGpZv8L2se3kRaTqGGhe2XOTd6CpKi9nBe5IIH7Sc4jRNmfmSkH7aFN7CGwOBEWwdi1eyK4/4bozrU/IbXU9+IWX4khXSc5hqqfuPIYlbsWkGck94tvpGl9DrVWSWBrc1eiIGVcsHLIeSjBs7er6aDtddfNcPdgTh/1kky589gZIreCAk0iCvcX1lBC3AOeQLRVxuDngpHD2VJm+AZwqRXjfTJ4dCb2Uwb51sMmwi1GXtHL5jKv8MhYbMANer0MzEoVL6hyztpcjVBw7QiebYLifnXHV79F+ye5r1nBTl5BgdHkoIIcHPaHhdXHnIOpSjG5RTE61kUOgM95sTgMoPbkUygopmZi5Ki3+0GvYNVm2icJQpWMA5kO4pJp0QJy+SK6oak2m3eJOVVkphsCngTL6nLCZqdkaBxhKPE1MrGxpbO7KULDGQeq5fbFZrWvVNVoc1AXQGW2S8J7Gd65dkX1d1z2E0spJOUvEiRrOHdKMlnTe81qR6OZaWrKDC1yfOmgnVNU+mQzPcz3ujm1ItraP5Ojt8dOt0Gq8CUAtCEgnEstol1IwnzIDtsTWCNGA6YBDxFg+MoZRLu9md1um4mRKSOsZI3om1/ptSFLd2N+YoXCk8WwtJ7pa3Rne54K4yi/ohN0isq5sf3cIzJ3aCqlZSnFQhPezMp3qm3jLxq0sgWHlFvTBnj0YEqHCvtlkdpp4jEhxWXYxpXgP0fbSzu/mabkjTjtTjQh72k8R4fYH9TS6mqWl5ArpYfy4TwaC6PP7Rltt/ZJMkeAEhsXd+r7tFSz2zL5K+TO2V4j8qh+jVdWcMDAysMjK2uiBH2Pb02EV5SWXjUdUQQXfiY+1MjJR01mphW/Q4iKeugOH9uYhJKNrjpTWibxM5+DoebQxGnCN1rQwqUmcMBiybcN6ew1RIozr24bem0RwGkQd7eq+Hn331MBV0q0kRjp5cFXCCBEccfl2StDcwgSs9m466cTRyHG55+55vDNKy++X98EdfIo+Xi8XF7PMjX+nzsJ+hXuagJ/scR9uOslTyPQKC2WhgWpc5Fu9M+XNnfBQoOuwceCawDquKVp7kxUCVNStJzI1YlpEf1nCI9FyR6ZBJRZtrsEhJ9QVJDgdOm4v5LTvDak0WodY6TCL7leJRhK5bsnXddVts6Mz+it1DcZyrBVZjd5dcc0/iQ7FnXfIQbmt9tdw1bZ2TcbsnmldZyhuzqWq8EsPYhewKshu2O5PRre7Dsu0cPmB1qpoE+FppvTGicyvjMsrubY8OudOHvZsP6y7huIR1pWipW9qincr6r6dHTkyW0PcyL4sp77X38M7LMXKdGOP/NSddJ0oyi4lTyeBWtZScyxxrx9DFLQI1nSpWQRG7tMO1trcSw6xA5oK80ZGToVGOE57jKsLneAPfJS5iIyq6LpUsOSynrwL5OUZg16r1SVB4D5t0C5x1H66YZMaYgbSOg20hCZnhPZin2gxegagqyg9gd2QzLAlzEb0Nkcl+AIo2INqhFaNutKorJyssXJ4m+hHK5k6YwhN9NRMjmtXGToSCWgsQJOQxU5yrFF7H4yxxCU8Ru83DnJwj8FZYsqDdz0IDpTdQZ9X2fvqRJP6UTmUyboiL0sZIWoZStn1ttu4blTv8wblTRh09q2GNUvUgCZYwcppmZWGDU/HzQ3z9+ih3/cEM1zhY15n2SRzKmdQR55AtNOSVxXZlohgtVpmJBaAHuQcjMfdkYA72TdusLcKENSabi6mTOd9lrX4Yd1WNHcZl3UV1PsudK+e6N4vA9UYq9LN1642+jIh3w/H9V0ytGPA2Eg9BdGhgVzUA90mFro56pR7UBDIaslGYbtUBTBqMoqcS5ONg8GF35KVW0zotpaJfUm5KbM/HFZytAt77RTbW0wtKpfaMyXcMdi5zXPUGh0JOyrDzS0D9qCujWYjYQOM2mu03ILEdiFDJpFkeRhDv9mIPT7G5xTb4KBDdKpVc2uIfG8PBHl08V29ApPs8q4sNXiZuBzKYKANRu/mcdioEg2lUOAhMY5dQJW7Vb2xTpzjKj7tiQKXGxNDpiVbODaIUM5u73uf6YOsAxQSpL0vJ4bu2fMGYYzuMIx3eblCexKhzbOb1v64ZKHSyDkibbk8WGJJvGVWvEvLFYW6oLmyqlCMKfGCagomBRVjQf75EJf2xibYeEjXTNJF1zsSEubWlk8iE+F+Ri2pkbMQItZRehu0kN/208FMUBFbwQRpMveSHJgATZjeW2e4HWFncaeVe5uY/F4eT5U77pVDgmlyBe+88ykUTZdrCBTHbnvMI1dJEEL8PggPO2wlUBUJqRa8CxXDDqara0vJdtUm6N3g/RIthuy6D1cbphX6yjxBK4qi/vb24e37SeLb/+ydp/ko5f/Zic7z8OXruw2P0zDf9j49eH36H8rz9w9vtRsDaZ7nVU3Wha8Dnn84rfr4L088563j8wWiryeazwPb1g7n12nf4sLrmrYevzRl9ninAexwumZ+Ca+Z39N0wffvD/J+L/5s6K8KtOWX1xlfXMyvK/he/FwxX4av47sPb97rRZsvwNtf/Lqa9Xydjc+Wf4fe0bff/i9I87IFAy0AAA== -->
