---
name: "rar-cowork-cookbook-dashboard-set-operational-targets"
description: "Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_operational_targets", "rar_sha256": "2625b99ca69dc262f7e494414e0df78c55c11990e031c7c86d089d2988109c37", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_set_operational_targets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_set_operational_targets_agent.py` and in the RCI capsule.

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

Set operational targets Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
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
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from; defaults to USMF.",
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
    "output_filename": {
      "description": "Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 2625b99ca69dc262…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_operational_targets_agent.py` first:

```bash
python3 dashboard_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_operational_targets_agent.py   # or on stdin
python3 dashboard_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_operational_targets',
    "version": '3.0.3',
    "display_name": 'Set operational targets Interactive HTML Dashboard',
    "description": 'Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c187ff48f63ffb49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of set operational targets with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull set operational targets data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-set-operational-targets-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing set operational targets.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a standalone interactive HTML dashboard for operational targets from Dynamics 365 ERP data (legal entity USMF, most recent fiscal period), with SVG charts, sortable table, and RAG indicator; read-only.', 'example_request': 'Build an operational targets dashboard from D365 USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to pull data from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants operational targets from D365 F&SCM turned into a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardSetOperationalTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetOperationalTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-set-operational-targets-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZF/sIJATCFRXRIAQSIEDMIl3hZB7EJEZBdv733kjn2M4q162qiH5q2ZkSsPea17fW8ub3F6dr47J++fSiBk6xYJ0sS+KgXjiFv9iVQ1lfwVd5dcF/C68s2jpxu7asm5cPL37QeHVStUlZgO1sUAS10wbNwlk0LdjuZGURLJKiBbe9NumDxUE7CQvfaWK3dGp/EZb1oqzmTYCCky1ap46CtlmEdZkv6LFw8sRrFmtss9grMtjXOoufsyACK4OiTdpxoasn5sMiL5t2UQceuLkIk8YDzwHRpPR/+bAYkjZeqAa78GKnbpsPi6asW8fNgsXj/x8eaiokC8T0E88Biv0FkHL8j2WRja9Ax+Du5FUWNC+ffv3bh5cE/H759PuLlzkNuPVCv+uiBq30TRPtqQjYnjlFBNZVI7BxAa7BGqB1Dm75Qbh4u/q5CbLww+K///s6gI3NL58+F4u3z+eX+Y/SFYs2BjKXTtMG/sJzKsdNMmCC1wWZDc7YAKHbri6etq+TInp97vxGqawWf52f/fxk8goE/Pnzy1fzf375ZQHc8fml7ubfrzOV6udfXrNyCOqff/lGp+ncNPDamRiQ+vXL2/UbWbDw29IkXHxR5f3ujRdwUVIFgPh3+s2fp+hv5N5M8uW5+Oey+rD4MeVZn78CeZ9B6AK6PyYLbAB2vrymZVL8/MajLvugcAov+PmXf0bWiwPvmiVN+2/R/fVJOAaRA6z1ZhIQfrML/raA3nT7SvOfs61AwPwnmoDl7+y+Guqf0X549u9IZ0kBEvbdlz8k96MN0F8Xv/5T3f6nDR8W4ecXOsgAGtRzAn5a/P4IkV9/8r/d/OlvfwDS/5KMWna196DwJXeKJAya9suXX39qHrd/+tuvP3UViOLAyb90dfYjmj+y64PPnyz4turnP+8F/PXiWpRD8Q3CFr+X1f+q/3hdGE6W+N/uN58W32fi/IEWsxLvTJ8m+C4bGyDrd3b85eUPgD0F0KbzHo8BfvzXfy1OiVeXTRm2C9UrO4CBHYDFPJiF1+KkWYC/M2rUAbBrk8yg91wH4n/28CxxGS5++9/eA+Y/em8wv/yK0F+aoP3yHUJ/eUPo314XGiBc1kmUzMCtkLL8uXCiGYEB06oOmqDuAVC5Yxt8BPn8cf4BMHbx27+k/eVB5rUaf3tgc/JEPmV3nFGv6bLgddbPjIPiTRsPVK3gHngd4JCVM/qHCQDsD0DvpsxA1WlnWzTXJMsWfgJwBYD8+KAN7PVpJvbbb7+5QKzPxROm14tnWWuWYMFXcRYfPwK9wiyJ4vZzEXhxufjp9z9+Wvyfxf+060F85iGDgvHmDSAhp0riAujb5WAZcBRwLYCOhzd+/+PNuoAMKKgL4LskTILnZhCd18B/N7V6ID+uNtjCDYCJgXnzChQ3gP2LpH1dHMPFV3kB0/nRXB3iuVj6QRUUflB4I6DqAHW+WrIo20UDPNKE44dF1wQPrr+5tfMQMQdp7rS/LU47GdSiElTschbzsQhsLgtQQrOvgfC8D4jUPzUL6p3E60Kc43FRObVTxbXzxiN0nn4BNeh9OyDuLIpg+FzMZTeYTfWIlad5orndSLw3l36cfQ76kxwggd+8847eWhJ/oT0qZ/25aN4C36lnV3igEACmUZf4czn4y1tINXHZZf7DfkDSmdKbF/w3rzxiENT8H7Yvx7/veL52CYvP3QpG0MX/h63SbBCSZZU9S2p7erEXNeXydNTcNM78nn3mLMuszCMpv/Ux71j1DtmfiywBUVePf3mufLj3bc0TBrs6mMVRHvRBbAFHzXQfoT+Hcl3PSeN8Lt5rA1Bg8QBC4H2AEyCP5vB9Zzg/fZc0Bmafr7/1CY9QAW4AJgDhvag6NwOhFwaB7zreFUg1G+Ldu8XsS5DKQ5x48Z+0mp0Bwg3QXwAhEuA/UD9ev+L18+m76H/a+GyH5i2PVrED2Vs/CAA5glnA2TmzB4F47bNHB3p+ehABauRVO+vugvABmj5vBnVw65ImaWesfNo1qABQf5y/n5rOd4N7BVIGGAskRtUB6z5SaUaZHDQ7QAaAJiBs86QAxR8Y5c0ID4JOPuMCwN237vRJ8XH7TaHgkX9z1XrfOCsy73lE3iO8nWL8Hj60H4UJoJfPKx58/z7SvnKbac8Q2gAYBBzfnz47htdn0X92FYt3up/+YQj6+T+bkx5lXP9zAHxaxG1bNZ+Wy2fpfa+8rwDAlk9Zm29V+COolB+/S/6Pb8n/J8JPnT8t/jPh/kTiLTk+LZBX+BWeHwlvwfX2AbbYfaQuH9H56edCCb7hK2Bf5kC+2XMjKPtfi+H7ElARoxoAElj8LI7NXFMHUMYf1QC44XPxfbTP2QaAqIiCBxJ9hwKPrgBE/tNrX4sWeFS0gLc/d5FRMM9uj9xogpdPRZdlH14ASAb/zsw2V6Z8julmHvVA9oBFbRI8rh4QcW/nn3+efqXqSeZ1QQcAjrLm+7h7qydzPf0uPZ5aAu08wOHDDNog60FIAi1n5nNqOQ2IVRCmszbtWM3iP8e7uSF8AviXJ4D/o0TM9/j+qNSPJgAgz19AyoZOlwEjtuVDlO/rgtMD8efs+yHTR1H58iwq/8iTnivQn+oOYFB1c+c1l6Q5nf/MfC5LP+TzNd7/kYkJepB5r19+msvxhzeAA99gfPmw+DqJAJO+zYaPQb7owNj96zwFzT5+bJl/gD3g6+umr/+s4QYvf/uRXA8U/DJH4jOe/l46cUY3gP6zWR9F/BG0QNwBIBJwc/AavS7+ZW5/XMEr7CO8+bhCX+M2z35sozdZygxUgx84I5hx+jmZPNd8RbxviTuLCOB/rN5Sly69Z1O6fOLG8slk+QMBgASPEgIK8WzYbx77ZrfyMUrOsgI7t89/+fj9BSSXM8fDW3q9zSJgOUDcj83cgS0BBAGG4PoJFuDZfz6lvBFoYgc0yYDCClttXILwHIzwPXAR4gFKoCiCBrAf4ltvs/EQhCDgAF4jHu5tMR/eEv6K2G4RmPDWOKD3xJwvc5+ZzEJtCDyECWIVosgK9kFgr1Df32JbzNvgK9ghXGfjbgjH/bb1CrqnN02fms1m/DowzRZ5U/j3FxdDwcoD2hzJ52e3JBB3aQnuvbaWBQzdmQ1cjfZlf9BazsRv0B7pxlCDtdW95lQ1SL2cPJscfzzvxh2lapOTaloMRRpxLTBp5VnFcM5Wl7Umxmh2LA9+swrlO0Rs8VN1L06sPR0N3g7c4qrXW1NSoLZyNswNAnMHRMvCTUf7ZdCHG/Mgt1iDKBBTVsultO7Rm3Fyjrg+xB5GbORziuiJ4qs+YziTkdS1ZSbGzYHRdWJBYnSDA1lDDEjYYOci37jo5W7x4lUTuHI9FH3a4kvzmLTXujhWJ+pQVkZFSluKYI5xIHHdsR5TLcWXN/0oFpiJocWZb3rCVgdmud4mA++hYViq7tFWUMm7BcNdDdPYUN37RKFSISBQIBfLDSGup8vysJ3cXjsg091NRKYUyKqWLhak29mdzFrOJ/ZmpEBYAqU5h8cmilOKU01XcZDQPLEhv+gaJUeTZrc/XI6UYpNWriqBVuXbA8w6Gu3yVri/UdC+SeAEjUAQKruu8iayF3IzP2qDcoPIXbMWDUH3e3VC13s6I7RJRHjltNypGqfCe2Ylo+SEttmBNBLONFHieBK2+/N44eG82kvIPgtcXkxg4iry48Hem+iO2h0qzRiyPVFuVjaBGbIQ5JdALzNNoe63juM57myngy/s4yQ1lF0Q92hgb5gR5ZvLFoUHebuazEJTiejU5lEwXifI2J+xqEPEmr5nUrbuql51WziSNxdfp9J8Xx3LraDSur+trcBWm7t/kRNlq6hVehOvZSKTG5SAp9MaFtIwHmkPikr4It9u/oqn9iecvFyu2ihAjja6rN+NBTTtm2G4UbroXmDOvw27VjivI85tV4aD7CvpVHY+lZQ45UCGUx+j5mrvlnvW2uqcb24khrP4uieFtXm/H4jE37mEIgz7kNizURLwa5W5iskdzYLr3TngFtLHnisft0go24K04yJ7XVB5iZ/Q6WYGVqaP68nxZKEiXCEHaRR2YYIica3XFHSi/LAjlx61Tqda03NoIEaJKyFodcA4A5W0znIumXFUsaY1dxKDe8rIrdWzYuadDennCYH6E0pKVHdKOZ72fdJfD2zTqN0xFPcrtyCryxUbsghe08jqituSzZru7swx7AY+JMaGiTBqT+1OEk6S57Ms80vYa7aattWQiHZjjCVpfn3Ih6bYihw8SpPcrLj8QsDUKXFD2kXvSXUzcidHUPjoWvDRLlqNhRl+8BIvSlWZUyBtPPlUjUsY4aGBmCp7g2OjwjUsjNEd2bu5zO2IrWQA0GPYYb1oOiGNMzx57t3AqJn06NKJEnU7FD6Xrn7QyWnIN6gd8op8UZHV6aLtbZAO27WQnS/Ntjib28zc71d2GCKwk8vikocvJ0+282xAjWxXd4azsVqH6URJsTT5rkOUtu3TUekPdjIIynHLn73ByEHzN/GbSoRbvm6PnM5R+4SK4INcsLhwX/mCpZukN+EMHY6idEvTPOm91XjIYopbCmtYsj0BbSaPBk5WqWDaALH12sw5F5Z4oE3Kmxf4bLJ7LPa3DDPSrYKzcaeOicSrKLNyFb4ALSbOFdG6SOvmcuR7jdyuffuohgjwRZDAx/TGuQLdh4fMxa3GXgVXXTfhLeVehHJzs1W5gsREC+XuLuHByvL6oFte4H23JHX4tG0QqqCr8riB1c26D/YoUjKhVZE1G2b7nmc3Thp5xLgTSEL02PXE29EB9g9oe5XJsjtez/aePdDr833J7UzxcFyf7Hx9J2PzfqkRiPDglWQjpxRTpfZUHm2n6iMNyEUH+j3vMvhaRTfGr1wkuoRHys4kRSvHo7E32kgnR17E3Zt88RCO3XcT2VL2pfdcxdnfiHVgQHgkefxep+0z4e5iPPVNgVNbm4R6k+mqXBnhNN8haWvflTyVcaK1lO3kF9OQ3U7V9YZT0mWbZ3qiu12I7LhVt1EwmtntomTy6gkvBzdYa1pTHuEc5+JwKe/lG2FaIXInlmaCmAW+4Vat5VecFmmyDCwwUefDaXc4xv6anoYSQrj9KBq3puRZLkKtIYzY0w4Tj5BskQiz2p53IZOb0Fk/0uuk3++72PVZkR922FiQATCOq4P6cNZ7HaGvV547suc58auRYSI4ztgGU2Bmb/L0WUOZmuSG4xRVso6STS3S67qNapurAoD97AnFT14OTWuv6owo9TILKvp6E2d461lnGSJJm74UVQJCzzGW1jBQvN42MXUf7jGzM3txpaF3n6Vv+jBh0CE7XMojEgN3y+x5C13p0vVXK2N5urPr6zE53jbLpFtFzZk1ynR3iCYrG+7udJbpejLWWdXgy/gSccmosnkdoDXM38+WvAfsaYY82rksrwoyN4XRDEifc70mIpujwYi7YwcXXIcmHFSnNiSY0iUL+SFtivIMZ+HRUe5Qat/NnuLv1qhR95anc7Xb31KVvwZjsNH1C6/ta3gD2RLZkDZJmjqCO14f38oVx/J0VDD1TmdPZElguIBiFuzBpZcNGlWzI25vS4Vc7voKM8qEGYfmwmJXMJ4a2DZlb5UpqYHIORCreBXuRg5NXlIpcLBqAw8+fIpFRVDEqyrx9lIreQ22RxKiFPqO1t4xyXJCX15BFthEwZ5Lv8rPuq5DF2Mk9bGyBllUY1XeHEDo5qsj5DE6EJetvBQzluJJzfZOpGNiCI3rY0JV57BRs1RmTfJGN9YeOVgKlhz7Ojuj5gYTzRMVrGzUrt02uYW7uDyfN6cKg0540g+VWy6RgVXNCAS4L9Ogyd3eB3u5v6gJam9GFW+GS4JVNE5Pyq2EOZf1Tte9vdF2F0EfShKyfPVyzQqnyTb7G8kPSgaTecatJD+9rs/MdA4sCz5BZ7KyI9s7IRanTWeQzhy6Osvm0jqqBBSsXdjsI+rowBzCTNdqSQ4Vfz032zja7tVe8xRstBh7vKf7QXQ5R8mY9aZsSFJvJPEwOYW00g0BoTYkvOc0ssmPt9OqgNQjFMtWfKrNng9TyxNXh2W4hpoo54Q4R2m8ma4HQV4Tst2C1mSCD0db7lj1hiaqvznKTSrxfm+o5xGjwqKQdlIqYOxOj2W1sNTA2ChkfYqcqxceaC6o1LxJI3uJm/eY1FDzirvISfOy+92lhINdeexoSBQWkfGNLZPcP9KqcSXTxNYz87i8kvsVlYcqcliPxEXPO40Oq0RAtL3B7/BNmd1SfYNJ8O6yS69NsGcmXN1dV3JqFlblIMtdsDnerqOJrUh3Oka3HHFqiXS49kg3rAofcbG+3qzLKspNLsDOlygeEqK8nHeHDSscaHFqdZ3LkOwkBdxVwh3G8lgcKmhqgJZFiqNOXw/qOtBcSDadpAQFzzmpq9rfGkpcZJfcMBrxdDns3Cp08AaNm/W+cjg/0C7lKnObe2647RTbiuFjVphNw1RDWcMn57IJVWpssT1m7ZDI3E2H0jkum2sq5KcNZXIqRZTFRKIjuR15Pp0uHg+PxnRUpag1KafsFLGzqBrhL7udnbIGcmEKsbd7QmjGIT4K7da2iMZmG+80LmEN7slTz+BWUWIprlWnfeIrwbRNpS0Reo2iE5Mqrq66yIv8JqWs1TD52qBJVXE8BSau2BdcF+h07TjlOYNYy9BPKZ8aV6nFb6YiSX6y4cUjo3QrS23jzJH5iyynNOXoRlXoLFam25Fdd82hEqvVEVa4SdXd4+6qQJVLnWmJKP3TdriftmSglpUu5uo86pycC9uyk2GmJ6OT8uHoisJVbNvTLvK2MMPWxwpAgAFXS5aNpE04xtUkkJqzbWOShAHzSyWcNMIBQOVreJ8klV07uIO1WHYa50OX4rIXTVC4iSso3Pdbf0EzERWPmNaAjlo+I3wbGVMSh3yRRRtl16d+uGbX6LrTjv01IWktT8jTFssug+Hqu6mbBDGOIWo3OsHxoERNqTQarUk3LTDLpYPF5MSRqG+IHiO6tFtv02uGx+g4Gbv7dliFuhkIHX4YUiSWVucjLhjJ6mrUSrOklFvQCypzoregCrcDjipovuKPNTnZQro/CPGxUgd8z8n9vTLrIavjmxPUVc0OCAFqQRqxI2qo6PKsU6XYaO4xXHZU1ZaBi8oXbkLr7THjlKJDh3V8Li9t3dXQwK/W/BrFGnlCGF6WdkYrUBuLKRJ7W7RjbjmYL4VBS9yvambzvHvozftWk4sTvarBHFDFKUnBO4BAWZC6aeLTO8qvQv/giwJ3sPjwlEV7il7GuOSct8T5nl83h84KSe904a7kYdIYWKn8KpC0UhkYBt6V9w0HJuRhVMSB9qPSOSFIrVcy71fb6ca0cLobZa+mDqIvHIi93oUUzMM7TbFUSbmt9nvCr4N9dYvvN7OKpPNa3/mjO7W4bq7v1yztSjaW4Jt0RGny5h5OTo6Ry4tnElrB2jB03fZFVq/bBHbwss1vrIhLK4sabkfjvjarIeODgAkyDlpbBSZwm6aog7AuyikffMO65GK7QTbrA6cePM6XmuZ2qOTwfMbujNmYZjDKKDeamyLbJEljWmkXeWkhXDWhAKXyWpNrP++1CdUKWW3XYxuEJ8NFBOYSWy3Bh+OeJFHmPAXZyTb4cM1Tl7xMbsWZ5FYrZ5eEFNeEa125nsNk3TLQbmtjq0184yctRNkLAllJ1QQ+zmXTKIU8EjpY2HaXwBBTDT3EJX5wyfRMn1aIx0ZEUyzLMFxu3TCjpLt63WRygVnLgxaxW9c3pzUUHHn7RrqnPYp1GxLn+/aQxivh0tSxzB0hVuhjDUvXJBZqTeBKO5v01Lix0QRjU5gaNZa+SqxkEVwu3W9IBXv1qZCgasVM4infHopL0M4lyxKaflzntHTBxjsXb4ZtWi7pTEHbCq7oPg4ODE1VAnvjewiB8q5bC7yqjBdmCgdqs1nBK+146ZsYtDVGXE5RosVgDC5CosnEK8HZk9AnZc7IRRnzyrJTy6WZVtwuNCYiZzEshBNT3qtnWk/O8qHA01ToxhN0ci8Jt3XZrlWQWL8KfLOiT7VlNK2wdBincQy+pmGqXLc5d2iXdmyEJZEdaAH0tyKOJ9Me31qbMT4kbNomnMFwzvXaUFGQFwTJuUx83UcKdk93BHa6GMhGc836pnSKQCIUo7C0fUDiM0qdHThRtw67tSVI4O0rsDAeDLQNE11TcBLPd3DF4dvWSgdUYmhkbYkUWjbqXUU30ZAJoZdLO38VlLGRejFNd2D4YmJYu1gbd6p0VmfxzvH8EEK3dBBf09uSykGPE3e4dNc5j0Jc6ezJzLSPi8aMHNvSZUddytOZvxhTm7ViQDN9n0t5KmyEEnGJ9KSfs7tSBT4Z2jktYqK0FYDraEgy7wXagHkv2a62m8LpRe4Sahd2U01SyzCEyCiiww1ma+SdYkihIwTZSNO6JBCZRFc9a9VI04QnddgluzLoBG/rSuiFudIQJmNlyRrG/t7J1AHEkYBVlqpGyxVXc/WBFAOUqpBlgDYySzgBUre9eDN7iUWc9TTmHVzmp3DTFxCywws6Q05JFW96K3ALbwt60zWTK2lo00ZRX7abYNXXvXtDQDMCrfN7n0btTW2PSEDfGg/v4Y6biixz9JKnwtu1Z8EcRBdJ1eLIdY1fhbXZgoY50yqzk0vpxmsIt9EwuEjRoihufUrJ/G1L9fL97OKn86mMDNO+yjp7Y0AZ3LueR/GnsdhUCoGj9t0iAisnGZe8VeelIO72liMO9eqsRbg/DMbQR3SucweQDeqQUVlaaIeoGcUkXtmGy5TB1Qs8ld6aysU1xhLiNdfnar5OPcFlk2GKtvUKEbS9LeOG1VhBAqbd8+SRedRZ3po5HHk1oHJlTVtY2ROgiw/7eDyOo49cyqWQrrTRzX2Ma/mlIKQnns5cB5E2BlRJSHZkrZCND+b9vmGT1ltrfqvyQTgi19oVM9eUCkKsQdpQee8PE3cgOnPIXZ0VdSSXpY3L0jkKr0KnAJi9VQ3j1Ho4cnTV5VTiNQoddSVC7MNxWJrra9+t9+LUnQnZ4e+2AIkko98CPea1VOYYxKoE9N5e9PMKv1W2Xey8pSBdxRO6ZNEkRdY2lLmFLRCutgyiiWb9hNmHIbrpkZA/B8tAJdlp621vDc7u/T13jZFrciXG4yE8CcfywJy9MISM7SbEyJFeJjvJTZkg2lYbDItTl+jFSisLz/X6ds0HWNS5Y0ffFdfwiGnqkcQS9/5AMHLH41V6OLlGtfKwwTvJxz1tJluMQVotWzquGzE33WrCnBotwY82rtV3yChvD71KcW5OXvjrdHWtIJQmGmnrBgpQxjmcgiggL7Lngb5HFWjpqOzhdBv3zEB6XWqgjQ6tHM0rNtG9ymS+2ldbABiRMw1IYblhTYUKrerBdDdohKdRyZCIC2pA9Y3dFn3BS9jU8r5v2T1DoPFy4xDjodt2Vo9rK47vmzXVjpBOsDi6P3g9SUSrJk/dfGVZO0U/MIborNkW7pdcKfT9Uot4DAqHZu10MHbPa4+uBw9LrLpwO/qydhD5NG6NpebJziY/rfZh7+NLVz0dulse+kHAg2kSCSGt8peo11tqF6HReYuo9+P+LK75as06l10ZRbfgtjtwqa+bBbX0OqyqUAQuBcnaewRmb8WSX+0JMIunNzRESOi6P6/K9anvdHEDKxixbOyGhQ63ZbZeXlLExnYs1JmhhynuGk4Hz2Cx2BdoFiPWAio450CB9iZx50u1Slbx4ZztZfpubXwPX6LQBqK0QRwpFE8IMTzDlN+ermDoG2/ikogn/+QzMc640VVFplhOa4CB8nCY6LvuEvB85PLXv77Mh6zvB30v//6ra/Nxz/+zU6fnAdH7myiPI8zA8T89eH36D2T624eX2kuARM+ztSbroreDqL87Wfv4L08n5+3j832w9/Pw5xF760Tzm9IvSeF3TVuPX5oye7yJAna4XTO/W9nMr9964Pv7U9ivHGeLl3XgOU37pS2/vJ3OPl6MygM/cdrg7TJ6O2sEe9/efvqyxjZfQOs/K/r2KgPQb/0Kv65f/vi/OQpFA+cuAAA= -->
