---
name: "rar-cowork-cookbook-ppt-exec-implement-compliance-controls-and-measures"
description: "Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures", "rar_sha256": "61a125cded6b2c2f299951b1291d5f20a8e8f80b5452decca2d5777a1d164404", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_compliance_controls_and_measures_agent.py` and in the RCI capsule.

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

Implement compliance controls and measures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures
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
      "description": "Prior period used for the trend chart comparison.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-implement-compliance-controls-and-measures-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Target briefing length the deck is scoped to, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 61a125cded6b2c2f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_compliance_controls_and_measures_agent.py` first:

```bash
python3 ppt_exec_implement_compliance_controls_and_measures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_compliance_controls_and_measures_agent.py   # or on stdin
python3 ppt_exec_implement_compliance_controls_and_measures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement compliance controls and measures Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures',
    "version": '3.0.3',
    "display_name": 'Implement compliance controls and measures Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-implement-compliance-controls-and-measures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-compliance-controls-and-measures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '875088a09cae1f47',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/implement-compliance-controls-and-measures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-compliance-controls-and-measures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period used for the trend chart comparison.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-compliance-controls-and-measures-2026-05-24.pptx.', 'review_length': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for implement compliance controls and measures reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on implement compliance controls and measures for a 15-minute monthly review. Produce 'ppt-exec-implement-compliance-controls-and-measures-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement compliance controls and measures data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build the exec PowerPoint on compliance controls for USMF from D365 for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-compliance-controls-and-measures-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period used for the trend chart comparison.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready compliance controls status deck from D365 ERP data for a short monthly review, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecImplementComplianceControlsAndMeasures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementComplianceControlsAndMeasures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period used for the trend chart comparison.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-compliance-controls-and-measures-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Target briefing length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecImplementComplianceControlsAndMeasures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
