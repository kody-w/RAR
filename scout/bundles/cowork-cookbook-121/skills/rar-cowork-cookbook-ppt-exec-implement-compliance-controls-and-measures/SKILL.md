---
name: "rar-cowork-cookbook-ppt-exec-implement-compliance-controls-and-measures"
description: "Builds a read-only executive PowerPoint deck on compliance controls implementation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_compliance_controls_and_measures", "rar_sha256": "61a125cded6b2c2f299951b1291d5f20a8e8f80b5452decca2d5777a1d164404", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOjWJLnV9HGmG1VDRmBhAChHGuzBR2I+xRIdLZlcd/3IUFtf/d9SBGZVd3Zs9s989eqrFIC3vPbf+4ej99e7L6Lyubl84vm28WCtrMsjvxmYRfeYlfeyiYFX2XqgP8Xbll0Tez0Xdm0L59ePL91m7jq4rIA26k+zrx2YS8a3/ZeyyIbF/7dd/suHvyFXN78Ri7jolt4vpsuygIQy6sstgvXf9Its3YRg1t+7hedPRNdtOC7bxdBU+aL/VjYeey2izWOLY7/U9sJC8/u7EVQAlkXIWBSLDI/tLMF2B5346fFLe6iBScznxZd4xfeJyCY9xpkdvhpYbsz/U8PJe2qAk/j+6LNYqDRosoAy7by7RRYoSg7v30Duvp3e5atffn85798epnlfPn824ub2S249SJX3QHoynyIv/um2+5dNbLwBN9u+8afLZfZRQi2VSMwfQGuK78BeuTglucHi/ern1s/Cz4t/v3f05vdhO0vn78Ui/fPl5f5P7UvFl3kL7rSbjvfW7h2ZTtxBpR/W5DZzR5boHLXN8XslRZ4rgjfnju/UyqrxZ/mZz8/mbyFfvfzl5cSiPBwwZeXXxbAwF9emn7+/TZTqX7+5S2b/fnzL9/ptL2T+G43EwNSv319v34nCxZ+XxoHi6+afNi982p8N658QPx3+s2fp+jv5N5N8vW5+Oey+rT4MeVZnz8BeZ+x6QC6PyYLbAB2vrwlICZ/fufRlCCIZqf9/Ms/IutGIHqzuO3+n+j++Uk4AgkBrPVukl8+Pdz3lwX0rts3mv+YbQUC5p/RBCz/YPfNUP+I9sOzf0M6iwuQCR++/CG5H22A/rT48z/U7T/b8GkRfHnZ+xnI4sZ2Mv/z4rdHiPz5J+/7zZ/+8ldA+v9KRiv7xn1Q+JrbRRz4bff1659/ah+3f/rLn3/qKxDFvp1/7ZvsRzR/ZNcHnz9Y8H3Vz3/cC/ifi7Qob8XiWw4tfiur/9H89W1h2ABhvt9vPy9+n4nzB1rMSnwwfZrgd9nYAll/Z8dfXv4KoKgA2vQPPJuR6N/+bSHEblO2ZdAtNLfsuwVwcBfn/iy8HsUAZNsHajQ+sGsbA8O+rwPxP3t4lrgMFr/+L/eB/q/uO/rDVdV9nRH96zeU/vodw79+YPhXgKlf83eo+/VtoQNWZROHcQGgWSVl+Uthh2DvLEYFlvjNAKDLGTv/FWT46/xjEReLX/8Fbl8fhN+q8dcHsMdPdFR3zIyMbZ/5b7MNzAhUiqfGLih4zxrlL7LSBQIGMcD4uVK0ZQbKVjfbq03jLFt4McAeUPjGB21g088zsV9//dWx2+hL8YTy9eJZEVsYLPgmzuL1FWgaZHEYdV8K343KxU+//fWnxf9e/Ge7HsRnHjKoMe8eAxKymiQuQAb2s0mAM4H7Abw8PPbbX9/tDcgUoHgB/8ZB7D83gwhOfe/D+NqJfEUwfOH4wOj+XHfLpgP1YRF3bwsmWHyTFzCdH80VJCrbuXrP1dIv3BFQtYE63ywJSuWiBWHaBqD29q3/4Pqr09gPEXMABXb360LYyaBelRn4ZxbzsQhsLosYmP9baDzvAyLNT+2C+iDxthDnmF1UdmNXUWO/8wjsp1/mRuB9OyBuLwr/9qX4Y0fxNA9YBCzjvrv0dfb53I0AtPDaD96PNfZcVfVHdW2+FO17ctjN7AoXFAvANOxjb47I/3gPqTYq+8x72A9IOlN694L37pVHDH5rFH7YBc0B9hHTi8OPeqj93EN96ZHlCl38f9x3zaYiaVo90KR+2C8Ooq5eny6cJZ/N92xeAduHPI90/d4FfSDdB+B/KbIYxGMz/sdz5cPx72ueIAos7gGQUh/0QdQBSWa6j6SYg7xp5nSyvxQflQWosnjAKLAaQBCQYXNgfzCcn35IGgGYmK+/dxmPIGq82Rgg8BdV72QgKAPf9xwbuKqLZod+eBlkiD8n+S2K3egPWs12B4EI6M/ejUGqgurz9g3tn08/RP/DxmczNW95NJo9yOvmQQDI4c8Czm6avQnE656NP9Dz84MIUCOvull3B8QM0PR502/8uo/buJtR9GlXvwKg/jp/PzWd7/r3CiQTMBZImaoH1n0k2Yw/OWiVgAwgWkHO5XEBWgdglHcjPAja+YwYAJHfe9snxcftd4X8R2bONe9j46zIvGduI55hbRfj74FF/1GYAHr5vOLB928j7Ru3mfYMri0ASMDx4+mz33h7tgzPnmTxQffz301WP/9zw9ejCTj/MQA+L6Kuq9rPMPws3B91+w0kPPyUtZ1r+OuMDq/fMv71Ox68fuDBK+D/+oFAf2D1tMLnxT8n7h9IvKfL58Xqbfm2nB/x7+H2/gHW2b1S11d0fvqlUP3vWAzYlzmIt9mXI2gavhXOjyWgeoYNQCOw+FlI27n+3kDJf1QO4Jgvxe/jf84/UJiKcI7XtvwdLjw6CJALTz9+K3DgUdEB3t7clYb+PBo+sqX1Xz4XfZZ9egFw6f8LI+Fc1PI56Nt5sATpBZq+LvYfV7OL7CZuy2IehOLSm2/+cfqWwe1m8Xw6F07vWyA+QHhWsnlWmyehWfBurGZJn5Ph3Es+sOre/T116fHDzt5A5QG4mLW/T4D3kjeX/N/l6dO4wKgu0OTTXDMA/ACRgHFnJecct1uQNEDMH8ryqClfnzXl7wXaz9Xo92Vnht0K2P+R3Z8W/lv4tjhrwvGHtL811H9P2ARdykzLKz/PBfvTO9CBbzAEfVp8m2eARu8T5uOvA0UPhvc/z7PU7MrHlvkH2AO+vm369jcTx3/5y4/keqDh1zn+nlH0t9KJM8qBKjAb+A3k8v0Zq7PuTen1rv+u+b+Q5q/IEsFfl9grgj4o/9BwYGaI/dtXIF7YRX8vng76Ur9bOKDUBDOYP9c9pH10H3MzPYfDXCTfJV1hrwDl5wY8B1JF2Qy6M48fsH/wB9UF1OjZ1t+d+N2U5WNGnSUFpu+ef1L57QWklT33LO+J9T7kgOUAjF/buW2DARYBhuD6iRrg2X/H+PNOso1s0GsDmvjKXiGY6/ke7iAuEiDb7RZbOStku/KwAFnahE8ExNLBUAwBBnNtxMM2m4298lY4ii5RQO8JRzPnPJ7FnGUE1nkFWe5/fwxuee/6PfWZjfdt2prt8K7mby8OjoKVJ7RlyOdnB29X4ObGuUcXqMH9a5uSWaeymbSm7bE4q/7a9fhjudltu+pg3o5+qkksfa3SnlYuYc9TQakELgNpznayitDoHDcdNPXGMLkrXeT8wmNTbhQnV7ELZFI1834pbil8Ey3t3sDkamqEdJnydOiFdX3tBPtyGrUgO54K7IzGI2aImXXIebMNmOHOwxBxhu9tGCfkXjxUuXLTfbZkV3oQMWTOnk6Dm5/YRLjv9+IJ5Xn1armZeZK2ca+stry+2aB1hm6tbq3i2yNzEiojzWnR864sZatm2zHXU33djE4stLc12m6L6i6p1lhKbE62OYfGvYUyuCpvd+ZWrkDPGFXQIQHm7Je3hOcyndW2Z7ZnUmNbevsjRsDBxUnxbTDsCewYe8O6gbdTdBlE1BrS6tYSKaJdjVPOdtDBHMIxc9tbmQdoZoq31GxujOPvueM9F7p2K9zEy9XWOUaNFGifpadrvOa36OirBX1lZCZq0kavD1luniOE1fbNddpnHoN18QGq01G/c/xhIPatzOVmuXGz4t5XIqxsJpVj4qUZcDrMkhF/IAWIt1Qdv9bGuWV15dyg0cVhEXRUTSbL2XG5Lp1Vs2EuWSHhrGiGqyk4TvRBzDZItcIMmHfz0jZuK12lKLNja44hscvd43dhvDe0fZ/dGFkgdph7rM1JEoU9LLararlsr7vGKk91JcDG7iCVOsdmts9Vy95byTi2W2sKfK6MCyoxmnEsoquCD90BT0ZhhTANCTGnY1U3DjXQjLrZDKc2Z5tA6Zlb7JKod79UiuwYztmkSpbYKWhaHGQUuWhIfHWMhJbgwxguG2op2tez6NYK3fHkOmGbbGVw91PFMbehE8PU5FZEjQkxcTdSnlA2cFxxdSHes+MtR5QzlJZtBkd+4i0bGs2H2xFBQ5/jryeX7bUrKwvJkp5M2KEriNctvPAT3IH0Se1g0fVlRxC4qrCtSt4pdp6ZnQyQIshKFL4HvH4AcMPdU3YSLtucXmkti96PKOypEJoMcs6LGrw5jeokntbYOlCngRoJw2yPASampyzEEZcjNOa8ab0buzG9KO87S3I1HV+f6btwDAPhInXs0KM7Ck3OBstcpby1JAdSW6shUtzz+FvQlRLtYOoJueVUf2MSw7sn9Xl/PfZIlJXeTb6QxLIGgT7dL8ebaFOStE38G424fUHeUTE3EKuL78J0GkJryTmoF9CGIWorRA2SSUtWQXXHhxWKXXDC3cUGBOxBZ/ao8tY07p2JaArFTnRNAo9bJGBa9tyxFzXM1uvj/T6N0dLZ43tx3RKnccixCz0IcgTRrrEn6cL39Zinl/3xsGf9o1ruVSSUUmiIU+tmeZDVrvZD2ZMgxLhBHu+HTvPCI04G6Y43zopY4IOwyvvDMbT8ahdVG3bZ8zsBUmNYbxgwzS3vFcIT0ZLVIFkfz/IJKZ2uO/giK1336ilzkjoIk82FUhElZI8TLqUHWS5smGERi6/PciBxVRLBmF0cTXVJnQOHTZZhREJ5AZEuwVrtpOw9uL/voA2RsEuvyXvWOdM8sySShnZXZb474qoK4RlEduQtUdYiy6YjQpt6xBV+J02CFp6KZN1eFa7RKQL2rFJzVtIk+7ubkNSsze/h4JRZG6u1ID89n82lSzohj2K1pckVLsZ6IPihjG+3NFagy+CQb1GDhvZ0aAtYTAlnR1Ov9xL3t0sluTDGFko5WlEschfhZkmA4n/b37rROWRT6jhSUmr8ROg5qQoe4+RWTjKKxB6Z5F5VhyA5r81UUduA28rrTZunG4XNWZZZl2MZdXV+tsQeS3UrbU+ZXldn1rhvxm1NVhWFMpUfo4esZxt+xyaMYpv6JVBsPkFFJldNEgvrzXpUznDBYfVqErwr6VVmHML5cQ+bfXuJ79ZGra89byvSHjBzjZbWLjytGXq7gdxThRD+xdu5rFaJwgEK9VYul+XSBegeW3J3Ks9+i6s3QRtO/XbbXCV2dbtt7Pgg0Fv/MhTTBifSAcNJCDKY7aWAYR+pTA87KuGUCDBm3ilyPzFZRVJrftRSwz700LE+BtWR4kd3g4pLam8Y2z6n6k2Ghrdb4GyuRzKmyEyPhvQgHczSXTYkv+QUaquVVK+E1nE/bvlSCCPVavHLYZqsY03HSyPhSTO/LaWopyJaFM+bsTo7cjJuIkQYTOmYegZqOderaFCN2cCiVw+RcQzamj1E2VAfL7B5g3b0lryc5QMUcwJT8dTK252MSu5STrrSB47T7pZYuLxSsaI8lLWwP3RdcSRE3dhQeXniZFLrbntQXsXCmNx6U5ShozH6AVNg1dEVs9wzy1WvTgfZE46tmQibgtNwGUjjEiOJTcAyztrwTljEYXzGVoTWCCKjsNpkKMRZovCyqmslyzTWcdtw1zOXXtq54zKvhjBeQxcaSxOR6Hj4mJ+w/TWsdkcVDaiGFZvYOGhjLCNipXgsi8YnWwWZCfYcl/Q1PuaWRawP0n3L7GhlNJxdh8TEWnMVhYJgmqyuGjOSBnU6G8NKGStEXWlqIo2Nt6mKSaPgLUiOmh7l1MlvqzPRM8SmMBgFE40py6rR7qLU4hqcOIYkx05FPnB6JrkixYRaUes85Q64d+D9hFWEHYh60WPPB73WLQ7Wwr3OrnIaL9uKPl/OB+hqxKFRs/oN+IDmLFrj/HN5Y9OkcZcpLdqb07IglnfurHJHuLzC20xSD/uxhq/ZnvaFlj/vLZutmRbJ6Cy4aDrlFCV2vR03VhHlXY9wR4KnM3Kfjg2/XUXY8Rh4NAQfkORwYv21h7iF3ufSSUKj/HzZs32N8SYdAuERXF9ykXjowt0ptlmIResDp0o7WK/KgTImkTO3Gre7k16z4saQM89TlK79k05eDEqQrOuVaAllCZhFZXUn6I7c2oRO+AYUMevVzlblqld99dZKym4pC2S1p7didWhY1z2giN4hwY4hbURPUWcpR4NO1VQd1S5+yleSN8i1V17HfcloOWUdPBMST1B635K+zDmmaF+udI86LbyFpcOGCAfqAsr/VlgW/IaUtrBmmfd7VvbKGLhCZmjUeTcqQXW6Xni/TqPVqoF9F2WgfV67FIi2lIdWu4JRQGW3SJVBbzVvQ1yW2OiYrlrnPFG8FR+VUZEtgTu15K7kWzWYzJHkKO/i9/Qu26dGvivOU+bl46g4IoxajXPPMU4YprqM70HJEE0JeiDxvBKws0akQuBjnQIpE3s9mCCW8ar2lvn2es75Iqz42utgjl8hbG2LurMSOxBtsVXmtyRrsvV94wyXBp0Ikyf90YKUSIkJxt5R0v0w8TW/YleSfbDOgtyfGw0SqPAy4ZhI6zxuy0WKB4GAny+WqATkZFSKS69ia/AFgtK1KYIMVdkNEg35NEKx4yU6i55JDDyKezpGVUc9RwMM65m+ZA8r0IJegnKqvXBJoeO9E8u9Q3aGG2xVNTyDPRFJSqyR6jQY7S4so3BcODHhkZd6MVoX/eT1+xNx9tIcJcV4p1xLhFZBOTZbUAGxVIpwgVSujZsJOETqCivQIz7sBHGA+E0W0pecj+7Nnte7siyzMNrfdMNEqOUZZGfcGoOnFfkqr0X/wouwbyN77LTX6akhDWu6EjCoZlYI5cypsXyc99X7Hip5j11145Fz4+0pEfwbmuD3THf1cjSiNiNvMbLHV2i2V5MEdTpo3zFbEJ8KFt8k95py+k01VuFpEmvkltXI9pRWiEi3PmL2aU1tfFmNR5j2NHGwk3pf5SstLo3YvzMZji0bPRdgLmQNccjztaQkxIVlp/rutNhepfwUdDxngDKYxIlIBlFQ7xXjTiE7MEaPR6kabBHaxQkP5eSVJKNxGtlWCjd7w2pG+bjWPG2tbATmdtJXchRCE5SsuSLzGcU4ETfZu3eEIOfjkadxSpLxMPe3lrmegE9PjhJQ3g6H1I2RKCQcJkTKuYmpSraXXxis3mjiaF24zdUwLJf1PcfJCD3NiQi/TZqYJC1PCtvTus0Mg9aRW1lKOhFD+cWIluJlSx3BcJaceP5WtdIyVFNQjsGUyueKcJAjjlJ4+bLEmyOqW0tR7wy/20iHYbAMsdzhoOcjbucoNYgSP0oWqweFJFMb6zSA4EXUtar3oWr66ygWUs+2Yl/sjFGFmrU2wlzBcUZ1IoFtTptiieJaa+PQmQicaQuqKXvtsTW65dZEKY4Ty0PBZKA6MO3F8PTG6TSnwgWOF7Rqj61dt9n6y660bijWS4F0vtDwxV43ZmZEZBec1TyxiZ2UDVnhHSz5xvjJsQhG/bZrBUs8aaiaVB2xXksbyVoNOaFG9gnMHQnSZxGUrHQ5hnSN6w5nulonTtTus3K6c0xe3pCTfTC9Sk99eqUUydk2cQbvseP6dEOKRqppzEcY/IBOcWjBZZLi9XRl4Fq9rMNln6n95aYg2wG3eQXPc0QCiHw9KajknaXebBCNyLS1mRda0C2xmEb8EwutLyOOC6vh1LAIm1wCzzfu22W/ZNd6vak7TNdQRqpV2ewn2TotT1grVKO71i8XQoZEPtK81BMk1PBaDZu2mIP27uCfchTPgp28Py63u5UuRsmmDnCxP5IhPVojGKGc1VU91TXQmY721xxZwvl+J9s9FDXXFjoOQQ0FW7yW1iBRhxGGblFHDHvvSiSIJ9/DA0xyK2MtO9c7sanoQuHBYAIWmzf6KtaMSG2uAAVheEhl+CBbR9sAFc8pYMKEqXLj2LTqIJR/ObNVj+6zaCwvNuiLQ0yM77XAuFO8qeIpx1B6y9JDJVXQWtTVKJRAtRVa1dtTEIWxsXK7nGi+T6fTdeUsCc7I9SI4b2gsyh1/n5QyEIer80MJhgXe7bAwqYVBMB1fONywAL3prnmxkWp5G5wwJ9FTUkuUDEh4mSFKaLnb9sx1TfB6w6aCaZNAlpoYLbKR70Ee63CNICaKFy4WryPQElwG0FgpOFKB8FXg4pxAQ9DekMtRCBONtNIdixEy1Vjb0SjUIjhQImVlXSO7XCyGAR8nyLRsLgaRs0FNW2CgZ3lnu78mUWGty62FXbzrPT7s5YmbMALbwQfcbe63qGnIxKiY+KimWkzQFG56S4q6kdeUDq3bpO/wreeez1iDn528bFmdWlFRJIupfj7q5ZJyfPZ+JeTrzoASAWPQjl1tUWlitcyRaNN0sk6fhrsvn5IVhjZ1D525uxUVdKjnjOb2252LA32w2PCGMWUk7KSi5sUQIxgAkKE4hhOx9R0jNvz6hq8T8bi3iJ14Udd85MSglxy3Udtb6RWPlxed40CPsG5ZB3L2g9iwZbNmOjFcr5ZHh838znfF3EtrRoCbK23uBwzae/1OapuQH4pmLvG4W8KlJt5hYdJ6caV47VXYVDo1GNhyMCLBVs/YkJmJvmovQIDwvk/OYhjV8pSBeYBfD8JAKiFXmCU6RcOGCk1F3pRBBR0IO4yFCJWdgj4HBu3dQSpxK4EAc1l/JYnbJmhoWrchEV9tq0vk6yZIAL66X4qMMk96e5umoNiCjoM7NWftMDWw128GENFW2tsNnthYjU9TtLahftsnbe40MOjQYHYHVfmyMmA7jjeXS+Vinej2fdphFAupWLTLNbW0L9243CTrtdkZEBqpldmLBAQpSS5ukgYFQDYghTncKVgqiRb0VFeRyK/0WbEbYTzVO2MHtd4o9pIS0ZaDrkoI8wS0gQdnInddcjbKIM3vNNdxRLZhxJvXo1eu1O/UxB2TpIINAahxxZbnqyDDpnKu7ZFTPdEhynCPutCI8PGFsPdXj5UZPnHZdWeFuZqdu9C/sZozqevW8NfbjXODPZKO+8DdHPkrrdDhqKzVC1qqVrMnnD4ahWnMMKIM9gmSEHLuQVxXr5lmYrj9yrFXPa5tWRzJUOAjszuYFMSDltK/6F7HLVMs23gm0tj3tnMAkI/GMmGv+B03JYcZIgJpRTuqhF68g6RnbtYSWkJXYquugkwzpuFsdJo29u0g4wqVH89nIae2cqD2G0cvxolcZkOzClv86rLloez2y4Ly7YIscRYSCpM7iD1em6Z1K+Rxqva6tKsGptx6SFCZ2B0jO2zTK1aWQLGwwoeTTNidfSr44RLnZBJArhAPjhmCeleGq0Ofb0eSDoQ9WwIEdIcBMojJxdc4CcO11KRHP3Q7FKe6wvEKqZrCwpvcviuoAL/V19E/3VXec7fYprtrF+Hm3YJj0bHidozjIi4cWrV6mspjtQihjkMR7A6LVDfG2x2DyBNlNcWgEF15sSA0h6gVew0HXaEPo4XLzYWHsJJYrxBVdvGEpNfaMUyPQ8/cSXaVpGnYOxbULnfhQVpTMYyMutNh7ejy15Um5+v4gJ+lCyRhqD01XoOQQZxUNn+91tHmCJ/3qywyoMvB2AowbbirKbC5upn6a3Y3huVqUzGu1Q7w1vBbLh4DRCY3bnsdlNa/C8iG5GxPlhrTG45HXTDUlaOYxrLA69uIQ3gv3GoK2ifbBpsa0e6u3EBtWl6qjR5dNe6EXJrtyMBYT3fu+uTseATZwn1lnhB/Lw+DbogZpPTYGb8EBBhNth5RCLsiH88sWVP9nFG6ThoH4agbioYdvHViM9oSQWuc7fDVMmWlk+BvOQsSSwk5dCzN7XvUz0giTd11uT4M/fmIL1UcggWvo3u+gleb7VW/W3hMwz198fG7s1zub75Bj6HXyEd8O3EoZ+o+5R9MccWVcRUh1F7Plqfd/bINXD7YQA6010NxpMop2RZ6sFStVrgSEIBPAdbua29z4w/IbnkvVw3SByef8PcBzVIgYu8HkiT/9PLp5fup4Mt/5d24+ZDov+086nms9PFCy+ME1Le9zw9en/9LUv7l00vjxkDG58lcm/Xh+4HW35zLvf4LZ50zwfH5UtrHiffz7L6zw/kN75e48Pq2a8avbZk9XnoBO5y+nV8Cbef3hF3w/YeD3ndVwU8wYDzeWvGbr1359XlIOZ/MxcX8Qovvxd8vw/fzy08v3vtLVl/XOPbVb6pZ/ff3JIDW67fl2/rlr/8HSsfR8KsvAAA= -->
