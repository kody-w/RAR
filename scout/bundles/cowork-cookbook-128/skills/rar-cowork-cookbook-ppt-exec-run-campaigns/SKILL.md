---
name: "rar-cowork-cookbook-ppt-exec-run-campaigns"
description: "Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_run_campaigns", "rar_sha256": "f166341952736a30f530b79f11f948583ecfd06be840a9b8560d937733f8e3b1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_run_campaigns`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_run_campaigns_agent.py` and in the RCI capsule.

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

Run campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
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
    },
    "output_filename": {
      "description": "Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for trend comparison, e.g. month of May 2026.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_run_campaigns_agent.py` and embedded as the fenced Python below (sha256 f166341952736a30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_run_campaigns_agent.py` first:

```bash
python3 ppt_exec_run_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_run_campaigns_agent.py   # or on stdin
python3 ppt_exec_run_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run campaigns Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-run-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_run_campaigns',
    "version": '3.0.3',
    "display_name": 'Run campaigns Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-run-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-run-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5419d0885b000c55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-campaigns'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-run-campaigns', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'review_length': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'review_period': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for run campaigns reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on run campaigns for a 15-minute monthly review. Produce 'ppt-exec-run-campaigns-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads run campaigns data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on run campaigns from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint deck on run campaigns for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.', 'name': 'review_period'}, {'description': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready run campaigns deck for a short monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRunCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRunCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-run-campaigns-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for trend comparison, e.g. month of May 2026.', 'type': 'string'}},
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
    print(PptExecRunCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1VXrELUi44YNiEWCQECJFyOMjuIfZMEfv7uc5DurbLb1d2vI+avkasswTkn9/xlZsFvL+7QJ1X78unFCN1yIbh5niZhu3DLYMFWt6rNwFeVeeDvwq/Kvk29oa/a7uXDSxB2fpvWfVqV4DgzpHnQLdxFG7rBx6rMx0V4D/2hT6/h4lDdwvZQpWW/CEI/W1Tloh3Khe8WtZvGZbeI2qpYcGPpFqnfLbAVsdj8b4PdLQK3dxdRBeRZxIBQucjD2M0XYdmn/fhhcUv7ZAF+5uGHhXwQPyz6NiyDD0CG4GOUu/GHhevP8nUPfdy6BqvpfdHlKRB+UedDt+jq0M2AwmXVh90rUCu8A6nysHv59PMvH15S8Pvl028vfu524NbLoe55oJY+lOy78OBM7pYxWKxHYMsSXNdhC4QuwK0gjBZvVz92YR59WPznf2Y3t427nz59Lhdvn88v83+A6KJPwkVfuV0fBsA8teulOdD0dUHnN3fsgGL90M7qLDrgijJ+fZ78RqmqF3+b1358MnmNw/7Hzy8VEMGdDfH55acFsObnF2B+8Pt1plL/+NNrPjvox5++0ekG7xL6/UwMSP365e36jSzY+G1rGi2+GAeefePVhn5ah4D4H/SbP0/R38i9meTLc/OPVf1h8X3Ksz5/A/I+g80DdL9PFtgAnHx5vYAg+/GNR1uBiHFLP/zxp39E1k9AOOZp1/+P6P78JJyACAfWejPJTx8e7vtlAb3p9pXmP2Zbg4D5dzQB29/ZfTXUP6L98Ozfkc7TEsT7uy+/S+57B6C/LX7+h7r9swMfFtHnFy7MQcq2rpeHnxa/PULk5x+Cbzd/+OV3QPpfkjGqofUfFL4UbplGYdd/+fLzD93j9g+//PzDUIMoDt3iy9Dm36P5Pbs++PzJgm+7fvzzWcDfLLOyupWLrzm0+K2q/1f7++vCcgGOfLvffVr8MRPnD7SYlXhn+jTBH7KxA7L+wY4/vfwOAKcE2gxP1AL48R//sdilflt1VdQvDL8a+hk5+7QIZ+GPSdotwJ8ZNdoQ2LVLgWHf9oH4nz08S1xFi1//j/+A84/+G5wv67r/MkP0F0Dwy1co/vV1cQTUqjaN0xJArU4fDp9LNwaQO3Oq27AL2ytAJ2/sw48giT/OPxZpufj1+wS/PM6+1uOvDxBOnxins+KMb92Qh6+zJnYCwP0ptw/q0LN0hIu88oEMUQrweEb1rspBNelnrbsszfNFkAIEAfVofNAGfD/NxH799VfP7ZLP5ROQscWzUHXLWbB3cRYfPwJlojyNk/5zGfpJtfjht99/WPz34p+dehCfeRxAPXizO5BQMtT9AuTRUIBtwCXAiQAkHnb/7fc3kwIyJSg0wEtplIbPwyAOszB4t6+xpT+ixGrhhcCuwKZFXbU9QPlF2r8uxGjxVV7AdF6a60BSdXNRnStbWPojoOoCdb5aEpS1RQeCrYtAuRy68MH1V691HyIWIKHd/tfFjj2AqlPl4H+PwjxvAoerMgXm/+r9531ApP2hWzDvJF4X+znyFrXbunXSum88Ivfpl7l2vx0HxN1FGd4+l3NVDWdTPdLgaR6wCVjGf3Ppx9nnoOMoQM4H3Tvvxx53ro3HR41sP5fdW4i77ewKH0A+YBoPaTAD/3+9hVSXVEMePOwHJJ0pvXkhePPKIwb1P7Uk/Pe6F27uXj4PKIzgi/8/Op5ZcVoQdF6gjzy34PdH/fx0yNzuzY57doiA+0OsR/J960ze0ecdhD+XeQqiqx3/67nz4ca3PU9gG4CoAFX0B30QQ0CSme4jxOeQbds5OdzP5TvaA5UWD2gDNgR4APJlDtN3hvPqu6QJSPr5+lvlf4REG8zGAGG8qAcvByEWhWHgucArfTL77t2hIN7DOWVvSeonf9JqNj8IK0B/dmQKEg9UhNevCPxcfRf9TwefDc585NH8DSBL2wcBIEc4Czi7aXYqEK9/dtdAz08PIkCNou5n3T2QJ0DT582wDZsh7dJ+xsSnXcMaoPDH+fup6Xw3vNcgNYCxQALUA7DuI2VmNClA+wJkAIEJMqhIS1DOgVHejPAg6BZz/gN8fes3nxQft98UCh95Nteh94OzIvOZubQ/o9stxz/CxPF7YQLoFfOOB9+/j7Sv3GbaM1R2AO4Ax/fVZw/w+izjzz5h8U7301/Glx//vQnnUZjNPwfAp0XS93X3abl8FtP3WvoKgGr5lLWb6+rHGQg+goT/+DXh/0Ttqeinxb8n0Z9IvGXEpwXyCr/C85LyFlFvH2AA9iNz/ojPqwDcwm/gCdhXBQip2V0jKORfK937FlDu4hbgDtj8rHzdXDBvoEY/oB7Y/nP5xxCfUwxUkjKeQ7Kr/pD6j5IPwv3pqq8VCSyVPeAdzM1gHM5z1yMhuvDlUznk+YcXAIzhP5y35lpTzNHbzbMZyBPQUfVp+Lh6gMG9n3/+eUJVHz/c/BWgOACevPtjhL1ViLlC/iERnqoBlXzA4cOMzSC/QfAB1WbmcxK5HYhKEJCzCv1YzzI/R7O5mXtg95cndv9VIG5G/T/C+6P8Pio7gJkPi/A1fl2Yxm7zXdpfu8i/ErZBUZ9pBdWnuep8eEMS8A06/w+Lr0080OhtrHoMvuUAJtaf5wFiNvHjyPwDnAFfXw99nfy98OWX78n1gJsvs/efPvx76Y6gTwr7xSvIk/vifdubtt/PnY8ojK4+wsRHFH+c+q49QP+bhrcvgFzcJ3/lugvDB/g91x/efRTmYgD9U5T2bwIgxEeAiHPrWYA4SvIZoGa6/4wlcERaBX9lqYfv/dtzxyMZavCrfb/xALK5gM+dDgjqtPvq9wf7uRrt3HEx6/8dCR4igFoAKursuG8R8c0v1WPKm4UFfuyf/yjx2wvIHXduNN6y521MANsBdH7s5pZpCWAFMATXTwAAa//DAeLtVJe4oJUFxyJktcJwhCJQElu5GBwRGOyRVIQgEYWviTUW+lEAr7xwjcMu5a2JFRxQGEliWLQOMQ8B9J7g8WXuBtNZklkMYICPwHTht2VwK3hT4SnybJ+v88qs6psmv714Kxzs3OKdSD8/7JJCvKVNenrrLU/w+p7fet/wOoNwdQS2rEGp2/Mx2fpH+3peGbjcrhiN4FPQvUkOl+TbHT11GnQ7kvXBx6ZsAoumcwS14r7ebzdx6qxXvqpDy/W0uUzL/WqDmumtYI+M3VjudotqZyevAkLxHTIcD7e1ZWbJsbBwJSLvPQkp+cqWxRFmM7+LhSaQrow9urDE85TEEzTmjtMUpPt9zxd3s9mZp9MdVawlRYWRBHo7Xk8F240hXE4YUR8RU2OJzGz6VL2LcIPEYnSeMmOJRVCYGvKJ9XSWu/M4avotf05ZerDOFR+npqE5p7Q9xHHQwEmT+Xa+uTTHm3fa6Y5om9eBwqr+eiVhHFp6G5TcH/3IC1C8i6JogyqmfZZi096YG6fd73x32h/vVl17rKhs0qZwlol93rKOG9G6t23u9qAz1xIpmJSwlD2sceyFq2Ijwgdlwzi7g0WLaCrfmuggrGiVX1soPa0ElNVZNFdaOlhbZCFcOsPX6/CMubrVXXV7HZVqz7RQTeayq9mSLPDHnQhf4Fg7HG/XDcnLd0uRXWZDi77tIjtXPu4lPi212uvPzYmLUA1VDj1seBs5lpdKLYmKjPXcdZquW78QXcsynDquxpOI8EXm3wk1T7U7U9UJcnRYvEotfDAszsmFgVlmdxtemZYmC5N+kAxiqeSmnW1ycewPxRk+odOWIlLM0JZZkqE8A8jnmWNqq76DYdGSrUI86jvtcFEEDTLPOVtRHHaBj+zkaSHDbXHmtjJK4xoWDSZ2W21TuVtpMiRIju43TXSdfKdmDYIXppqfheRylJN+47JIpQlrZz8MTW2LgTwa7ojZsuVMHma5RCPwpGjjhLhkTQeVs6VWTO7yLpNIiCvr82lXxXwAsQfSFnAxBxCZOpzWQVNkavstVbnlrUEyW1+FecZfFR7ekdMN06bdeWoM52ydlwq+O97J0zZHS+fiEBt9veUohO09vIZkKYK0CPfRqKVPTkRd1mN0yS/Q7rr2JEy0fENJbI2xuTqgd4qYIv3dFttAStt2Tx/3qBa2mzPR0Ta31rceUq7QRFvGe/2cF1HUUNkYbuQV5/Cm0OxVN6b26Ki4+6SgbdZhNq5yl9n0FtD+adwcjyVtUeSazCcyyv0DE2KHoOHr9Q457lSPTddbR0SdUstRUsR24YrN7vsrtIfP3hnAgdkJvsWxW3ZwLfZao0VihlN0Y/HrlT2cIXMapFjFgmyLlyvkpNeOkEvLyUvj/eDvrNJF1r7TOn3EsMMetQIqN7V8EnwSQcsdtD9HabRKEZqhAErSg84uV07OHA5E1ptFpB0HE9qssk66rO2rSKfMtpJAq9Fgp8iamMKY0PFc37nLVnWcJeo4RstDG9v10Nzrj5kFT9CJPttT6PKZd0dAIcyOhy3PCVtkakJ/DE2ILBC70ER5o40iD28PV2FS4tFQNPmih0RQJNf7obTs43g/dl4/uHqc7SwSYqS1fFuP620QpSNDTshlwo3ItkUPViXRpIcJ8kmq8yWck325hfmVqQjJYDCKpKs7vzW7SO1JUnFi7Jqmu7MoC1du7VmkDIerQDhSp0zfmLf7koQg1b+QVlej+6zwfXjNkHFrUuO6LtthM+lXAYfJehrXfItp2K2E9fa823gnBtueEfiscg1OYslu31t6YGaRL11so7jWw57Lhy2REGdNLkdcj1nDL/HBPtDVIMYWvh38bSXSjWZzzA1RZLU6l7nrawWleohNLTNncvtM2xhiqu6vrSeNbhpcEFo9V2yRnxnT9aewu7iCIevTuKGrUy1MPOc0xe3GdxaGCeENTW2ptmIONoY7VFoKL5+lnjBSiLnpt6oSBGgy9y3JrAab27sN546V4hKykUB+lh4T/2jkfBFhNeVfvYDQC8ZIV9Pm0PFheXMtV9IZZmlIe6wzw/R22ClUql+vy5XBeFsfUdFLyiSluXaCwzKJgyjCkHWoVCs2Xh9aB3WMgNho0zTR6419Z2KWFPPl7Yy1uHQ2YOnQW2PTiSMT9nuqEdGk7iqIgJhGbgkOq25YQSq0wMHlVFwzXtjbaeVYHXcTFHEt5TFW8UvysL4bMrlR16DCL5VevjPR3fH0cZOHRGJuYhYntxEt78gDAcPXkyegqXEs2oGG5TWjY0sMDGhFllNW5ebjerxVyBWtVyp34TdO3FUOTim2fKZazjtCvN5L+xJSxRW/Y1mKdBXQ0xu2H2lJ5gnHRDr1GHq09LIxFd/Hjb0rECPdHeDlWV4KeE4a7CVdDxEu6tVkqpln3GLisiOTBLbr8KSFCt2XnbK8yDHrWBW/dhqVlJsu1YRGnICOZpsN91ToJuVCTOMJeLMa9BrkzFZW+DrlHW6XiHsQRp0YRQVpa2eeB4Xs3FlStk7ZTLS2CQCBrA5lJBV3IxuE9jY1AjGVcjnz2DAvzMxsN3fBJHiMd+jOpuXmPPTbUzcdm73gkHFhXWizUODqeicsyh+cDaNZbRwvhVOOTsjRTEI2mhC0SjcjHrQgs+qw5G3KPGrwSXd94VKH3HkwsX5CwguslZHkm3jqnJSVHccpMgbymmeXNaz1K7jeReP2sikmrTkv88Bu7zLtbcrwTKSJkTl6eCuObMeng25Mql+J0pbm4DthjBtI4lzRFHTtRiFnKAu4iGkYT6Ig0qNgftrSkW8Ul4OArxSmVc8T33YOY0WHfaCDuWPyj5sr53O75b4vsbvWJzgvCr6MalG7b9qCO50vhNnQ7okgotIZHatMymFyEHY8U2OxxGGE50Fny6WxGXZwl5r9kZHvqrOLDQXervb7bWmkTq1hrW7qNbt3q0j26/aCMdKwxAq6a6qoZi7ZdNAcd484OmMu61I7qOtNA5WnwBJ4RpHRpmGb6263rZxuI4i2qo3hirMlm10Tkl6XGyhiRdpFjxnuwdHletQaWkwMfyUUiBpck4auSYe+8ZLHdgVfb4rLUtPQ+LBtD8e9YRPCsPK6A7RUYYzzM1XwmkN/ZzU/wyKYuvZ8Obgxcdyvb6l9SksJzmLK2N1qZFidVie1XK+n7ILvoKyB96KhxV57EsU922/uFQ23pYBDm7vI3wv2sL+cC0FhVRQrw5HYx1SyRazaHD0I8Qpdlc4VnchGA6G7hhP0TDzGrhna0tKkBZRJfcM6ePKeOxXDkY22u9xtdmrr+6jJUofGDLauvrslk0itXGq99g95gQQFMo6qahb7tUiLV9WsxO2dh+kle/W4aWgODaSWOrxaCvo6utTIclT2a55cBjLW3e6RbaUUc5XYM387Yun1JOpXfgvdj4VwCrfiGmvSTNldrlkhBuZKleW9LWm5CVqssY7WvCeSSiGcfYBCFe8k0G1p0cSliGnQsebyWN7o4Xj1CJaAE2KddqXqmsWhvuLopheq26ZMrAhbH6pEyXtESo0LN8CSnBOZuvV9ZsUUq3j0dlieUG2w4lB92BxXVUw7Wh7fMEk2MoylHOqcTwxFY+ccxw6b0aG4W14ZJj6AQc1bRriC+dXGVFwaWouligx9JghONIr4IWa3HYFcKpQjtWN33yNuO2m9jfF5HyY2Ae9ie31kdxc0G319WVcScnRHsdGwokoFgrQJKt/pNifBh2M8KehOl7kaVu+gQzRvcFor55PrH7gNzGWcnG/MRGkThbncJM3NBFt2lWZ7Yz37xij2zT0o92y/qbsVPxiQvrLLyx05cSeEaTynzmuRuMCweXT3PHGyEWh97GT8IuttKKIEblosPsi27UUyF0ptUNwMyVEMmDCMI94Kblvm3MXv76JZ5OS92+0hjr37+6NR7H1R9ckLiZjpymlz904I+M61fYWoedW1q6Rj7AgE79FnqHFVRkVKQhJWl91eZ6Urvb1AdV2ePIYNg1bN0FvvlRV9uG/RXSByCLdxtAYvjolnlmytCS2yJbJWBbE4RgKud7C9IgiAdwTP6WlJcvpZFXt0VHtX1kwfVdaNcL3XS8+wwh1SB00n+5LEBkiKebTHM8ZMXTgymuY7cqmtju3euOBLErEHNlXw2ne7wovWGCJreUVbXufcjl5WXDIpjFg64+XDyFzUZSjLoPRJNCrZidIl69PSwkQP0rST5KLjgXTPnosGFzULRgySRzPzug069ipCyJDekBrqMmqiYtJwltKdukQFqGtNxwyE8ZDxpSaN7VTEErcp0z29x+/NkUMxb8rInZAHdFpnJyUihE2NX1Zwp/K7fAP3UqLQRRznORrGWKrZt6OzWxl12/GoIYJxKbjyEoMMUSypgbnmEscORm/rEejZrpOQ2iGSVVMu3TjQYb2W1W5ib3e1rNfCULfhZhgCIjiQGylSK7m99IVLnkvNgO2LD22hAAlivdmemRUVLK9nOYpUSpMHAYbZ/iadeeuKbKdA7YW2nKRwby1B67TzEqzoU8/CyFPuh/0mGQrcL63jtdFXJb1GzSBM91QWaGAonW71zUe0AT/YE47RdrC6o2cnPpAn9ypAuF1h5Ia2ojtqRmslMMFExDclw6kXzOe5VSXoAOtTcofat/EMV0VLIGD4Sdc2ZVzBFHBu1HsARmLBlwQxOrVhG0SwAwB7f0cgvqdiDcXzgz2WF9fLCy/0Qi5PFI6B1SVtiYLuNLcdNDnBgC+XVxxbyqyZHg/jZnlADpBcMl2GRvu4ICNzf9ycTpVUwAGLYhaHHw5cZ+dnbNvoBLVTEGJZGSs10t2LhQ0azVaVZzBiSFwgms4SXEPKSwQbztI579NzXTsFUeqHe+g12an03Anp7kzT7MAo0o1LJTzDBFdHfLEtuZsaUUdClm1KxT3/ZKE67BiMexkPedSS2ACX6lHdKSo50KDMosNUsxsyU4170/lVhBKDVCNGAKEZaCMnot+jkJyefShK4XoLEfKFCreX9fXQ3NGJ26MnmZZERnbELUcup6TAnCLikZ3Oi3vyZIuA6hbUXJTbtSer66elu3G7M7GxktU1qNFpdymi7tZEa3rcJiXojjKKsr2Ug6RmpeX39I7es9SoR1CBKI3YHVYBNzaXnaQl8EXYrFYdfgJDQGa3rbyVuik4a/0U37ZIouH5zYZTI0Q4e1dG8lI2VEULri7TjQfE3gLQYwjX7JZLO8GDwwlrIJIkNHGDVWcujPaGNniwdCxWFFdIlgZBWrzM+m3h9Ca6hVY3Mr+VGlmSx0tL3kBZROL10Tr4a0KHKdQqxNKDdxXRKsVZCMu9U9qXViBzUrWHULtMbuHyVKvsvD3lhzDqYJxXUGFXy+xWxbdIGyswFZcRl7ecy5b3ddo37nDQ1SAJMChMarvIuwDXeKKd7H63HRjZdk2uN10P9JRrbMAVv9bPboJe+PJGbawbxbb5HSnImBWbxGvwDGlV/LzJuOXqsDIbwdL5pDuENL4alVV7Ms5Hfwp0xqksD6X3uxALW1a/RgXlrvVL09e9fd32MDlR8HljYORut8Rq8kxQ0GW8FEpBBUTvhavcXKqiAOVrN9jBRk3dof5ihpg9Gcf7Ogqi8MJ4pujqLdYfj+v+Cg/sqhxOBmndNAVikIQdTodKPvWdeerbAox9IXzRa3tATALf6DAeJNNwKapTg/SnSlsWZkjK487fhk7IDCyX71pZFfemtIJQcXXzmGY3lmGvUx7v3UnCP9m04LkDaHa3ezYLPQaacJFAwrAyxXM0MkdXLqfNaO6s0BGt+xZX2VE8E/mpsy9rjSHu4uHubIoO4ya83vdw2dU9krY+2e1ue7m/HnU8kpbyQKQtHF2VcBvENJzf5RKvNrTBwsqo4vZyw5x6en+h1qou2PY1yDl8HaIRw98ifd8LhOQTiea3nt1jbuTqPRgrchAjuhKTycQYVwVtUcR1fYMAo7Ven1ekDdl9mgfizVa7ML8Uo4Iv9y0nVN5F4c5BxI47gVL6Q3E42IaCycZwXMX9RdP7ZWmRTWwl1mYvxdERQ9oBhe/r9W0veavgrKj5gYdZy05WRnwNjDgLJM5mBt8d0tJqVhtpdQxw10fBTLQ9ld3Yu5idRhl5alY0aqkrDTo2jL+8e0ET+ikVBbEqLCF/V6r7Lt6lu7XepJEeEiJzEJjS5JIuxK5LA7oNgUbRUbTf5Fek1wa78i3o3g8kYa6IqVsOto3FPeVZO+egrIa8GKK+R8may/IQ19MTtaNILi2UdPIE3R0EvUiTtm1sJPTW9dw8ksVVvOw5eFwBRu7pCmqAuuOvoyV5Au3K/Fh4W6MfxvDQK9kQ4pK39d1Yv2k7v+sphlWYsAp4k4Ou13xN++pFwPcZhHptUEpXruK3wh3er5n9MXWnGCmVU9AmB40bzYDSHQ5xD7i6YaizaEVWvgWGn+oyJAdoGJvpCkZ1OoIRMvXXEn1dUnloN+kYoQd60jq11LrwvsO2tOwGB+FyCroc0TpLRzzN7tESPU05TEF+bPXbQY3GrgivZoNk7XqPxB7peEOA4vsk0EC3okAiVdv7fj2xTnpdLqlTUhfHsVGm8soEW6yT+qSh7mEX0OT+fsvXppqLPM0iMrF03bNcx3QaNqkiXqCs0A00O1hHE4mEIdOdEb9cuuMh7xgBLmrFMvtDhFfbW5y69y0BE2OylNPDqQ0uQVbcBmwVUKgS2EaSLC9FWQqtTd2lNcZowzkybnpz9UeIgmAAsHdmCFJo01RJrWfMkbtaJYSd9jikXK83H6L8OFDF9rhdEuyJ1KXcn0qrKNc1DnFt0ikatU7AxL4eoq1+DpdLOoDEzGlgTaPplw8v3576vfyLt8Hm5zb/zx4RPZ/0vL/08XiIGbrBpwevT/9KkF8+vLR+CsR4PvLq8iF+e4z0dw+8Pn7/6eR8Zny+TPX+6Pn5CLt34/kt4pe0DIaub8cvXZU/Xu8AJ7yhm19B7Oa3VH3w/acnrm8Cz09dK6APuOyrL4XbZuG8nJbzaxthkLp9+HYZvz33+/ASvL1R9AVbEV/Ctp61e3tVACiFvcKv2Mvv/xc5Pk5U9i0AAA== -->
