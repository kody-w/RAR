---
name: "rar-cowork-cookbook-ppt-exec-perform-predictive-maintenance"
description: "Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_predictive_maintenance", "rar_sha256": "47b06e8a98e6ea1d148deaff4cd2406c5c76d66f48ebcf5dc410b8a6177e6317", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_predictive_maintenance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_predictive_maintenance_agent.py` and in the RCI capsule.

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

Perform predictive maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull ERP data from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 47b06e8a98e6ea1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_predictive_maintenance_agent.py` first:

```bash
python3 ppt_exec_perform_predictive_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_predictive_maintenance_agent.py   # or on stdin
python3 ppt_exec_perform_predictive_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform predictive maintenance Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_predictive_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform predictive maintenance Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-perform-predictive-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd681fa875f95cce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-predictive-maintenance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-perform-predictive-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for perform predictive maintenance reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on perform predictive maintenance for a 15-minute monthly review. Produce 'ppt-exec-perform-predictive-maintenance-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads perform predictive maintenance data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on predictive maintenance status from Dynamics 365 F&SCM ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on predictive maintenance for legal entity USMF from D365 ERP data.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready predictive maintenance deck for a monthly review, sourced from Dynamics 365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPerformPredictiveMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformPredictiveMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull ERP data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-perform-predictive-maintenance-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPerformPredictiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
