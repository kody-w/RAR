---
name: "rar-cowork-cookbook-ppt-exec-forecast-maintenance"
description: "Builds a read-only executive PowerPoint deck on forecast maintenance from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_forecast_maintenance", "rar_sha256": "6ba31713935f59036786d583e2350463ec153ab9d03428c9bcf9e20ec8d559b6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
