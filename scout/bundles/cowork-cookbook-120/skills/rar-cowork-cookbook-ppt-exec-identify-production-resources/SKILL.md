---
name: "rar-cowork-cookbook-ppt-exec-identify-production-resources"
description: "Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_production_resources", "rar_sha256": "d4a3468f6c45b0743c54c6612d247ac62fa9c25f14a62b76415b21737a640b00", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_production_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_production_resources_agent.py` and in the RCI capsule.

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

Identify production resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
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
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 d4a3468f6c45b074…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_production_resources_agent.py` first:

```bash
python3 ppt_exec_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_production_resources_agent.py   # or on stdin
python3 ppt_exec_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_production_resources',
    "version": '3.0.3',
    "display_name": 'Identify production resources Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6722916bfda5eab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'review_length': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for identify production resources reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on identify production resources for a 15-minute monthly review. Produce 'ppt-exec-identify-production-resources-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify production resources data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on production resource identification from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on identify production resources for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready deck on identify-production-resources status for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIdentifyProductionResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyProductionResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-identify-production-resources-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the meeting the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
