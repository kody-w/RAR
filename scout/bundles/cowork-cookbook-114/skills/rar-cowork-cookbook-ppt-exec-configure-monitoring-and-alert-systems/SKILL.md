---
name: "rar-cowork-cookbook-ppt-exec-configure-monitoring-and-alert-systems"
description: "Builds a read-only executive PowerPoint deck on monitoring and alert system configuration from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems", "rar_sha256": "425560de7e6120ba19364f4b980c6958104388ac65f41cdf545eb3d564a1d8ef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
