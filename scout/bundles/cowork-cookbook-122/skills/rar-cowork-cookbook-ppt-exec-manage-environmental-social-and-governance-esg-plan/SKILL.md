---
name: "rar-cowork-cookbook-ppt-exec-manage-environmental-social-and-governance-esg-plan"
description: "Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "cc7f009d1de7a9d4740d514c87e650d277265529c135ffb4f6f9612fdf899812", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and in the RCI capsule.

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

Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
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
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-manage-environmental-social-and-governance-esg-plan-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 cc7f009d1de7a9d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan',
    "version": '3.0.3',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '038309a0572a3808',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-manage-environmental-social-and-governance-esg-plan-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage environmental, social, and governance (ESG) plan reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage environmental, social, and governance (ESG) plan for a 15-minute monthly review. Produce 'ppt-exec-manage-environmental-social-and-governance-esg-plan-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage environmental, social, and governance (ESG) plan data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an ESG executive PowerPoint deck for USMF for our 15-minute monthly review, with speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-manage-environmental-social-and-governance-esg-plan-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready ESG status deck for a short monthly review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageEnvironmentalSocialAndGovernanceEsgPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-manage-environmental-social-and-governance-esg-plan-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
