---
name: "rar-cowork-cookbook-ppt-exec-forecast-maintenance"
description: "Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_forecast_maintenance", "rar_sha256": "6ba31713935f59036786d583e2350463ec153ab9d03428c9bcf9e20ec8d559b6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_forecast_maintenance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_forecast_maintenance_agent.py` and in the RCI capsule.

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

Forecast maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-forecast-maintenance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 6ba31713935f5903…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_forecast_maintenance_agent.py` first:

```bash
python3 ppt_exec_forecast_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_forecast_maintenance_agent.py   # or on stdin
python3 ppt_exec_forecast_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_forecast_maintenance',
    "version": '3.0.3',
    "display_name": 'Forecast maintenance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-forecast-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '334b38916f46e0c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/forecast-maintenance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-forecast-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-forecast-maintenance-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for forecast maintenance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on forecast maintenance for a 15-minute monthly review. Produce 'ppt-exec-forecast-maintenance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads forecast maintenance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive forecast maintenance PowerPoint from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-forecast-maintenance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready forecast maintenance deck for a short monthly review, sourced from Dynamics 365 F&SCM without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecForecastMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecForecastMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-forecast-maintenance-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecForecastMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
