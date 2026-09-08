---
name: "rar-cowork-cookbook-ppt-exec-configure-monitoring-and-alert-systems"
description: "Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems", "rar_sha256": "425560de7e6120ba19364f4b980c6958104388ac65f41cdf545eb3d564a1d8ef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_monitoring_and_alert_systems_agent.py` and in the RCI capsule.

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

Configure monitoring and alert systems Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems
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
    "comparison_period": {
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-configure-monitoring-and-alert-systems-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length and cadence of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 425560de7e6120ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_monitoring_and_alert_systems_agent.py` first:

```bash
python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py   # or on stdin
python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure monitoring and alert systems Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems',
    "version": '3.0.3',
    "display_name": 'Configure monitoring and alert systems Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-configure-monitoring-and-alert-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51b06d2d30874e92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/configure-monitoring-and-alert-systems'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-monitoring-and-alert-systems', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-monitoring-and-alert-systems-2026-05-24.pptx.', 'review_length': 'Length and cadence of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for configure monitoring and alert systems reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on configure monitoring and alert systems for a 15-minute monthly review. Produce 'ppt-exec-configure-monitoring-and-alert-systems-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure monitoring and alert systems data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': 'Make me a 15-minute exec deck on monitoring and alert setup from D365 USMF, with speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-monitoring-and-alert-systems-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length and cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx status deck on monitoring/alert configuration for a short monthly review, sourced from the D365 ERP plugin without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecConfigureMonitoringAndAlertSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureMonitoringAndAlertSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-configure-monitoring-and-alert-systems-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length and cadence of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecConfigureMonitoringAndAlertSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1WXRaz14kUMSIAEEiAWSeDqKLPvi1gEksfffQ6SqsrudveM38xfI4dLCM7JPX+ZeQ+/vrlDn9Tt26c3I3SrhegWRZqE7cKtgsWqHus2B1917oH/F35d9W3qDX3ddm8f3oKw89u06dO6Atu5IS2CbuEu2tANPtZVcVuEU+gPfXoNF1o9hq1Wp1W/CEI/X9TVoqyrFBBKq/jByy3Ctl90t64Py5lRlMZD6860F1Fbl4v1rXLL1O8WS5JYCP/dWO0Xgdu7i6gGsi5iwKRaFGHsFouw6tP+9mExpn2ykLXth0XfhlXwYZF23RB2HxauP5OdL2a+TQMeptOiK1Kg0KIphm7RNaGbAyNUdR9270DVcHLLpgi7t08//+3DWwqu3z79+uYXbgduvWlNzwNVVy+pw/031dgqYGfFjIdes9EKt4rBluYGrF6B303YAhVKcCsIo8Xr149dWEQfFv/+7/notnH306fP1eL1+fw2/6cP1aJPwkVfu4BwsPDdxvXSAuj9vmCL0b11wA390FazQ7p+FuX9ufM7pbpZ/Of87Mcnk/c47H/8/FYDER5m//z20wLY9vNbO8zX7zOV5sef3ovZlT/+9J1ON3hZ6PczMSD1+5fX7xdZsPD70jRafDE0fvXi1YZ+2oSA+O/0mz9P0V/kXib58lz8Y918WPw55Vmf/wTyPsPSA3T/nCywAdj59p6BcPzxxaOtQfy4lR/++NM/I+snIHCLtOv/j+j+/CScgFwA1nqZ5KcPD/f9bQG9dPtG85+zbUDA/BVNwPKv7L4Z6p/Rfnj270gXaQWy4Ksv/5Tcn22A/nPx8z/V7V9t+LCIPr+twwIkcOt6Rfhp8esjRH7+Ifh+84e//QZI/2/JGPXQ+g8KX0q3SqOw6798+fmH7nH7h7/9/MPQgCgO3fLL0BZ/RvPP7Prg8wcLvlb9+Me9gL9V5VU9VotvObT4tW7+W/vb++LoAnT5fr/7tPh9Js4faDEr8ZXp0wS/y8YOyPo7O/709huAoQpoMzzBDODHv/3bYp/6bd3VUb8w/HroF8DBfVqGs/BmknYAAR+o0YbArl0KDPtaB+J/9vAscR0tfvkf/gP4P/ov4Iebpv8yg/mXr8AcfvkO318AjH55wPeXJ3x3v7wvTMAGPI3TCiCyzmra58qNATLPIjRt2IXtFcCWd+vDjyC7P84Xi7Ra/PIXOX15EH1vbr88wDx9oqK+2s6I2A1F+D7rfkpAcXhq6oMa9yxL4aKofSBclBZzUQAy1QWoVP1spy5Pi2IRpABzAOfbgzaw5aeZ2C+//OK5XfK5ekL4cvEsgh0MFnwTZ/HxI9AyKtI46T9XoZ/Uix9+/e2Hxf9c/KtdD+IzDw3UlZengISSoSoLkHlDCZYBJwK3A1h5eOrX3162BmQqULCAX9MoDZ+bQeTmYfDV8MaG/YgR5MILgcGBscumbvu5+qb9+2IbLb7JC5jOj+bKkdTdXLDnChlW/g1QdYE63ywJyuOiA+HZRaDcDl344PqL17oPEUsAAW7/y2K/0kCdqgvwzyzmYxHYDLwKzP8tLJ73AZH2h27BfSXxvlDmWF00bus2Seu+eETu0y9z7X9tB8TdRRWOn6u5OoezqR6J8zQPWAQs479c+nH2OWgySoASQfeV92ONO1dT81FV289V90oKt51d4YMiAZjGQxrMpeI/XiHVJfVQBA/7AUlnSi8vBC+vPGLwW3PwrxqfbsH/Wcu0nlumzwOGoPji/982a7YSK4o6L7Imv17wiqnbT+/Nfefs5WerCrg+xHlk6vfG5yu4fcX4z1WRglBsb//xXPnw+WvNEzeBMwKATfqDPgg4IMlM95EPc3y37ZxJ7ufqazEBqiweyAmsBcADJNcc018Zzk+/SpoAhJh/f28sHvHTBrMxQMwvmsErQDxGYRh4LvBUn8z+/OpkkBzhnN9jkvrJH7SazQ5iENCfnZuCLAUF5/0bwD+ffhX9Dxuf/dO85dFbDiCl2wcBIEc4Czi7aXYmEK9/tvlAz08PIkCNsuln3T0QK0DT582wDS9D2qX97O6nXcMGYPnH+fup6Xw3nBqQR8BYIFuaAVj3kV9zRJagOwIygGAF6VamFegWgFFeRngQdMsZLAAYv9rZJ8XH7ZdC4SMp5zL3deOsyLxn7hyeUe1Wt99jivlnYQLolfOKB9+/j7Rv3GbaM652ABsBx69Pny3G+7NLeLYhi690P/3DHPXjXxu1HnXf+mMAfFokfd90n2D4Wau/lup3gGrwU9ZuLtsfZ3D4+K2YfvwOBx8B248POPj4Ap8/sHla4NPir4n6BxKvVPm0QN+Rd2R+tHuF2usDLLP6yNkf8fnp50oPv0MwYF+XINZmP95An/CtXn5dAopm3AIgAouf9bOby+4IKv2jYACnfK5+H/tz7oF6VMVzrHb17zDh0TiAPHj68FtdA4+qHvAO5iY0Ducp8JEpXfj2qRqK4sMbQMrwL05/cx0r52Dv5vkRpBXo7/o0fPwCngOP066u5pknrYP55h9nbA3cbhfPpzP0PLcAFeJHbH+tZA8gnrVt+1ns/tbMcj7HwLlxfKDU1P8jffVx4RbvoOQARCy634f+q87Ndf53Gfo0LTCpD3T5MBcLADxASGDaWc05u90OpAvIlD+V5VFMvjyLyT8K9Idy9Pu6M2vfDHOT9qhOIMk/LML3+H1hGXvhTxl9a6X/kcsJ9CkzwaD+NJfsDy+8A99g/Pmw+DbJAPVes+XjbwLVAMb2n+cpavbsY8t8AfaAr2+bvv2hxAvf/vZncj1A8cscis+A+nvplBnsQDGYrf0OUnp6hu1sgLYOBj98af4Xs/0jhmDkR4T4iOEPqn9qNDAppOH4BYgW98k/irZ73H8BbvBI7Zegz42Py0cnUg4gPKO0f8mKEh8B3M9NOBCxT4rba8OfCPGQApQZUKxna39343dj1o/5dJYXGL9//jnl1zeQZ+4cHa9Mew04YDlA5Y/d3LrBAJgAQ/D7CSHg2f/t6PMi1yUu6LUBPRwjCBIJQiokUQzxXJRZkniEewyN+CRD0CiCL2na9UkiwlE/iAicCL1lQJC4iwZ0GAF6T1z6Mrer6SziLN/sUZDl4ffH4Fbw0u2py2y4b5PWbIOXir++eSQOVm7wbss+PyuYQcFNytMbD2rJsCYObOtabhptS6aDJTI/O0v1zmJB0gzO6HAZwpkOX6RlunWOvdDXwYbV9gcaN+9SNAQWbVwuOxrP94TGHqw+R93CJGA5MAjLn6bcb+j8AoYyQlA6JD0brk4XLsTnNSxk5emSBkglt5NaVKJ+IKHUFE7nuqCpPWK0Bzz3xQLS+gi+OaFw5H15EHdnrU0UfplWDsfwiOzmK3e5M6zVjVhdt/jkE2FxqtTRiKZOMLKJgfMbDXfwHaf8lNlZ12NZqkoQ2BInTmdtmPJtqTIinrapzPARs2RKOw1WpOmvtmlzuDRSt9XS1cTUm9N9vYKyO7ITLCM93lRptXKOEozuym1eokeViH3NVBSI0a73ivQ3dWr2DBNq0Fq+E520EZvOycYVteT0q6GWgegZ24q9w1MhKPt7pOzts3iQPS3zDvrY+3c4uprs+ojy3e3G2xZ7cN04EyBSW5oKqfEtxzkrrU8z3020Pc02V8hWuwqx6kt2wrbAPWdJzvG1gU8nMjr6VwMjNlp2GVHmDm8t5CqbB146H5zLRtrGXJVEO5VteaNrRtJSpDBXL45qla4hCUMinctbZveas8Y7YqlLgyWWFT1YddzFEKLC6kDscnRt9JvSPUj7glB0SeT3Q9TYPG+45MG3hg2L3i9aEZ8bb48jo0ZjCGU20mHkT/eD5hggatLt0Q3kKXejfdNdg0KjbsJQJrB0lw68snVd8c7mOybXGjmfjgMMxIlt4VKeoEza77J4E2mTNvaKSm32ZrrJki16kSi3teKx55TY0LY53sAihICOg1/a5tJLjwfymNeIx0ONy52S3j2wV8w7gQ7SSjdWJDW67AnycPTQo0tsRZ7aWjiBQ2mzrs8TVBzLAk7N5YWYNAbEDcXom3ENX7YKx9PWgGhbT8hG16XEWiuYE6Tcu4AnLVhzdupKip1lxQ0F5iTJsbvdTQuROTesdL9oKVg3WrOvrs3kpOVlsJc+LIxT0lstF+71UFta0bCl7gTaXE7wgTFUh4SgckMKR1xddgOayDDhcI2t9stVzycMMIm/0s+55XrHlrunUNij63bN2Zsbr0mGR4WsH25RwdDLdXMRzXS0PA0tTce9IHhUIhtTIut7axvjbssfLle+xooDzbnX2pE37hr4U5Er2Kfpo+SvsdjM4hrruKLaNaN/WjtFUHp2Z+4nahQ9voQ256lDTatj8hNOIzV6JsEkE4Qqt8cZFEerYL1CGBm1UkjXb9GxhtY39ThFlCozEQWir6jTQWFUzL0yyGhhlC2uqZ45ieWZps5w0SRMZ41Gt13pbXY/cvU9YvHKbuNOEGXZSoiDsueisLTZwmScklxrUZmwluqGZosgNj1UwsReWUEWrVCjsDjVgZ6nhCN4cp/T4g3v7HEjtoxC62jf3uXchslqlE8SqTYyHR3WUl+vsWCwWO6a+HJOlxWWblK64Y1dMnrWwQkHgjZdfDzB9WVVT7BaeTVF644QTT4dCKKeQntcasntcjS0pqk6zmU2JBVPBmxPkDgVfXzq15mtrCTiHO+lY5OouENxkpVR1mmqd125upnmWhOaBl3WEzuubAUl+rXMr0TzDudccLNaGuAiUitb6RJGzhih975YLSlSLxxizStX9uyVhCJD5/iy622EwkV2iVxbL3Gh/e6OtL3H7nFQCSzRT29xNpiSxezGSuz5C9nvzTwuDG1VYKctXgYTvWoZyHMFsnSoVYBj2kTGIaf7+taL7v7E+jAjbfr9fkSsizgZ5trIt8uBcjqtzXPXc/EiCvVGz6e1Y6qlYQZS3enbvYOqx8IsjtV1h13jIj/tU8+VbCPEC7rblTuOazwlYFir18YidYXDOuXba9RwZt/voPa879GYKwtXXpO2paEuOYU7oSpWRYr3BYurGOlM4ug0dOcQFnYH5dyvKJzSbpZ9K08nOZOFpRPokt66MDGW5NnVDjUjWY1hF6EWbKbTSMtOwmFYvrUVkqkygtxUuLS5k+QWhhkHROwtOrXDmDejdK2uhdONFkeuOO8Q6yPNAMw0DDo7uq28SlJc1ekNMWUXubyZI+PffYuSNAXvbggypammitDhgOmufjc69rpt4s0kH0RixVmWskOg5LYShNJs9ubGIne+xteZeGL7XVIfOZ9NVXdMr6yNcav4KniKN1TnG2MvMR05J0WexMgo9iDlDNKE5VoOdRDIOypE5B7aJfRecVfdVkBR0bcmL2JIkV8l5Nnbxla33/psYZBH9VRmBhkG7JQ7dGNsh7b2ywJbFQehAx4z6/Jg8pSaYNcA3U8rJN8Ou1sDx4MY9wdRb9b7vL3he5e01iPJoCHZa1Hkn07rs8BmbnC5XMtGh+jkkpvGDkgyMGuDzfWLBckFu7asI4Ibxjbvh9MBxNfKrxJRke85Rk+gHcpcSM/C3Ah7Ww8P4xYAhaVqoyt7R3yLybCxlZXmEEjNmHIn/ZChd+qs62lhF255zJRpE7M8a11KtD2hUGCVmV4FuJLYoyCltKxZV5I6FszuXEj4sPIIBzp7WsHzIi4wisHwh+HEZTzOyefmRl5ttHZ3rVFtw9OVq0+yA5HiYRS367YaXBdXxON2C/k6Yjq7PLxBdR5sGPEQ28fbVjrBZrfNigE1YLPeHJplqap114jW2eIh+xhvjzfJHLWo3rg2pstBVzdSKe9Y3hcVl9ogFY1MsqXLglnfYWrnp1ux4KBJPu1p57xqsFtsWk5QyfsUuub39TLSL1O8w+7a2veU7qjTsgjSNL8NO/qeE7wQSSJE8piRryX1TlOaR4z3DVfRB0neJeUysJJ2bZnZ1gzWrnIo1yfMWTcK7+7pfCVsYS5qECuUZKesdmEiJGLNopciqQ0wtNuOsuToUTiembWGBJdTKDvr6DhaPr5cB2So+DvmKkMIfdivXE7Lh1A9jL56gPPdfltHHE8hGB92hYSYGaNhzn6bcq2jmUlmQiqhcPUGFyWsCT2fwDy3KTl9q8aJZB9BA7LrkOhiigiHQ01goU5v7yhpuMMbBDZqJTXqoI81UyNuw5hdI2TIDZ9wd/m+wu/mkTMOkbR2LNfoiqm5hdG59RGPvU+iANpNgy/kyowRsWys1EZYV0CPPmcwva0d7xHWZ6vSI8KDbtE5ixlpPsX7OqX2R7rB3Fg8mGjbVoTOTdMqj1A5s0q/w/aYdVvLm/uG8exouGVCcDwRJ57heDBux7mAX6gma7Jp5SdJHEz7S2nwHs2yyWjyxz440oFbbKd2tAqGxeJeIHdB36F9xEeFw9KyLScEWx7apj0uJxi+uihvRDvMUFBeYQ/9OeRVmB3wbhJwjejSbJ8WviawZdFo61VpEjQdXiUaGjKH2RdnU7HQ0D9VhkAQp83UI3VwhRylh6kNU7g3u45u+jApHsFqsSn0wyaDvC3oSpR1sGdWXogd8mEKYWO0qqrJhbiVo+O2XGcXtqXNJeF361RdIYf8nGwcG7PJghvvNR/VXLmdyFtt1hB17u8ibR3GEjlI/WoitiUyyJQjH73uvg+y0ebZaXQFZcVtzZO0V2/QdbXfXSHpWhSifdolaJLtNz1IriJ2zng6Btj6Uuf2Rtguowu627eB5YLm5+pRuT74V75PiHgPRL+rRMO6dhH03OUSKKvr1YurfH2+23Z39XJb06l1UB273alO9RwW7VRj9luXsUBgC+GyJr1YcqGtiXo4Koo79jilB6d1pAS7aWbRn/ZGbV03Heaka8+7lJ6g2MpV2dz9YMmWU13vB8TIqZPLSrBIntsqzQKJ58JkJ/UU6LWG/JgSkghqllnhtHGUlFRLtpMPGQawtXGIT8NynjhP+FW2V0sL60KY1fWSNw97dptbl9DpOYu9eG0fToSMm5cTsiEaUZBPoMoqWGQddkc/y1YJDpcp1Skacckx3ZdYPY0rMWRaUIWYbOkdzFWQTrSEg2aT1ejpZMmDlE2t20lNIQ5Rvl6Zw4i1dC17ZHlfE2dNJtZYXpUbuapdAT6uAxQhnHNk2nHGFAQNVRFlXFwlBbOI1Jvldds1vYrETlrwYL7zS2415fdii1y649p0aO2iuBsFEczuGAUkxF2v50RVIabrioTi6sx0Q7xL6C19spSVSjFpgvLHskd0bx9mwlUlr2J6GhXsfCG2JB4hjmuFttFaN2EFVSpoMMuu4G+ojxLQNSO5SD5wcdT3cnCFDWZ/6DqBSTRPxLdKLav7cMI09aog1lZECmkfqpe28FpUK0+tisuK62XgNjM5jVOUes0493qSgvambA4XyZdxympa+8axLo0dfWpgJ8zkEXeL87eIdYip8I87XURLZMfSFE5Ux8SWxA0e7ZciJ1hdNOquy54hZGjtQtXAmAN7zmT7ycRSltHzirpU9x1SGc6JwwEkT0gohbzuRhsfUtyaqtZ2X58zVeaKMk3NyxWNTQgVIn1tuieDiFaUh01Mw/Cqe3XWydXJ/XVMogZJeHfHvMW7wHUCCVqa5dnT8fRM6dGure+nW3it7BJ0gChxlihDOrRHtYMuy0LT4o5sLcZd7pk8Opj5TRJFlYYvu+WGtpbNQREUZQKNZEdCK0Y/U83QppsSIRt4C+19E2uPPiZdL2fIVJDWYpem6ixxU23ukqO7PMqjux2nYyQ+ugdeHlOmDyJjGoRohFEl82Nos3Qotp0MbyDuPrNJT5q11SAnpa3KOyd6d/ew2pYzjlY2jrcX/UMzojqOC30G2kZvCQsao9e+5YleS0EneGrjXa0YlNdE56ogsOuR3fiy2QQ3HWZv/jDZhTiCMfGMjM6E0rKPpKNcIbes2sUou7FqTwy3Q1IzrJ9PLA4qYAEbTua7vRts5Lt0v16CxDfvypUjsE17SoTG3FvAGYV6oscJE8EMplzF3cmHkcLwT4iLOygOoCth6SI9ijBMLs3z2awKaUv56XTFOR6iXFPK/Sg8NBp/0em5uIzAO/oVg9VSgeqOKNAJ8VbnHXIq6uVSQqJm3F2rHdkF3Xi3CvSQGqxRGtwIwb7vBJhTTWsTxNXORdF035F1ObZKfJdR1NsZMJacWrEwLiPDugrlpDoVYfYxIllHH2+0uL+HEKhQHMxPfq3jSU3Z6RH08nzS6bFfbgiRoK0EJCFoGezxGmaiEIQWLFzI3KuEUTnoTpZlG6EwcW50kJUdKnd3X0XsUb2p0oG5OhwNehLxXFTCxnWtkoH560QqIpiuqbaMactzbJ2XSM1rpZuHy6ZzCTcnBTSKqh57dbjRA9BYalB5II5J7ww6duXP90JgOVyihSD1xfsRCW78Cc8uox/j7q50RLXuBeSWti56pLATHY67u4u5KkN5pq0wAXe6eef2XK2dtpHTtUaiXBHvYC1eenHWyviKImA1SN2hUjXSz/yI8JE2C44bv1yrpDV6qBEYqG2K2+PJI441wlgCecLr/QFHMxt3s5Rwk+ONoe67kd/KDXVZI4QHjbaQryFSI229K+tttg3XEDEWG1S/WsWKEMIyz7ZgPtuHttKival3kci4ENlOV6k9XVcSRlL3G92ua2wbENcMQm9UAVq+PHUKql+GWWWPx0ugiQ7bw5GiL2OBuC376BiezYMZoPDUt1HFBVbLCHvW7VbE+dz4FKP4Q8wP8OpMZxkroPWqujgSuqQ3IQdB6KVa8hdFRqe6IHQ2xDU7KnLaKyCaQCFbIY6bHCYggbt2E3tLuaNTHpiDW5/RttP7aeTruxyVxWZ5TSrhihKhzR67y6Vf0x0i6UF9FiOHU3fMuObOK4hVnUMeBtqtTy5raTP0LSfhCpTtLm2an00VlrcstNG6PsVvkQAmqBzLj2hvtbd+NLdLMEZrLt/viQzuj+FYUBTCBKwaD8aeFJY+GDjq5WHjnfFtQHYmYg8TpN5XCXW0vVWG9bCSyTCPoV5+hEuBI7teXgZNkK89g97I0fWU7lhIvwvGdUc0WOG6vkFcW0/vbezU00TEy5dj0Sk2s9so+XkkvdOpPyCYKeIUKeT2nopcTwnDmliSXeFT6No75Wl7VXdQf3CSo7CW4shcIt6AIaA5HBXJIxl7p+ZXHlkdTwlpxFdFjvNAyk7ni2CIWHDUdvv6XBESkjRLMVzmh3CgdmjrE0V8wpmlvb9JsJkpZi2XquL15j1ftuiS5a6wdDqelNZW0/14cG+mERL8WiuFHFln7bC5wjIUaWBqXWnjJb8R2rne7HQ1XTrY0rlffNJZDstd64xZcCpM0bxBreS1VXwPh8uBQHbDxu7hQx/FeJPYF2zKT14SO3XuIHvPGBTQ/N1Nz6+vh1TJ6PHkEhSi7VwFuw4SHAfGabtDEC7Zl2FGMndtcCOQtrm5VOuR65HMljiPSveHVWAT0nZXHqJ7z9bcuh/tK9PlGBV6+81aVvYZgeEXtVgXcDaEYkcuXSbe4DV5SjFRrsPJV1jGxo9RQQiReZ2Ks2Kcl8PlQlNl79sgNUIyOIvnHQxLy86tu4rJRhXzRArZbTpTgcZVWZn3C1p5kmPtBCs4IUIfNExCE4HmVxpOraCsoltp2Spy78gwCKqdWh8hHGs7TDi3ZLSFiV4EEbShVAlTGfhKhCLmgebhfNXKkjLOUU4dI0ouLZKAzJTL7s2Oj3V26V8q32liOV2tGrLe+qVKLpXt1j37x8DCaJc8CRXo+UN0D4nIxlud8kzQl752iyNjJXuIV56Xski7WyaMMBXLzhwKkwTcOXjHcOtoudaGYNtTro6rchsc1CLLmJAofOG6vbLwanciC4uzJuqQ1LfLJrFbaBiOMA0HEduMIsEiwQTFCM7wJy/jdloHIHRJkipV0aY93E6hwPdQIOFUlY3wtNErlvZ0lmXfPrx9Py98+6++MzcfHv0/O6d6Hjd9fdvlcS4ausGnB69P/2UJ//bhrfVTIN/zpK4rhvh1yPV353Qf/+Lp50zs9nxJ7eth+PNQv3fj+S3vt7QKhq5vb1+6uni8CQN2eEM3vwzaze8L++D7D8e+LxXBpRs8X2UJ2y99/eV5YDmf1KXV/JZLCIrmt5/x6yzzw1vwOun+siSJL2HbzKq/XqAAGi/fkffl22//C0KqyXauLwAA -->
