---
name: "rar-cowork-cookbook-ppt-exec-manage-environmental-social-and-governance-esg-plan"
description: "Builds a read-only executive PowerPoint deck on ESG plan status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "cc7f009d1de7a9d4740d514c87e650d277265529c135ffb4f6f9612fdf899812", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6V5ejWLbmX9HEfaiqS0bghFHe1WuNDEIIgXACicpeWXjvjYCa+u9zkCJNdWffmZ7ul1GaQHDO9vvbe8fh9xera8Oifvn4onpWvmCtNI1Cr15YubvYFveiTsCPIrHBv4VT5G0d2V1b1M3LhxfXa5w6KtuoyMH2TRelbrOwFrVnua9Fno4Lb/Ccro16byEVd6+WiihvF67nJIsiXzAquyhTwLJprbZrFn5dZIvdmFtZ5DQLnCQWjCItXKu1Fn4B5FmkXmClCy9vo3b8sLhHbbgAl6n3YcFL3IdFW3u5+wFwd1/91Ao+LCxnlqz58FDFKkvwOBoWTRoBuQFnwLIpPSsBuuZF6zVvQCNvsLIy9ZqXj7/+9cNLBK5fPv7+4qRWA269SGXLAI0EK7cCj8n7qC7yDMhjpWrhRFa6zl226L06t3LHY5pAAtoBouD/AOwuR2Dn+Xvp1UChDNxyPX/x/u3nxkv9D4v//M/kbtVB88vHT/ni/fPpZf6jdPmiDb1FW1hN67kLxyotO0qBLd4W6/RujQ1Qve3qfHZBA9yUB2/Pnd8oFeXiL/Ozn59M3gKv/fnTSwFEsGZTfXr5ZQEs/eml7ubrt5lK+fMvb+nsvJ9/+Uan6ezYc9qZGJD67fP793eyYOG3pZG/+KxKzPadV+05UekB4t/pN3+eor+TezfJ5+fin4vyw+LHlGd9/gLkfQaiDej+mCywAdj58haDAPz5nUcNPPVw1M+//COyTghCNY2a9v+K7q9PwiGIfmCtd5P88uHhvr8uoHfdvtL8x2znpPhnNAHLv7D7aqh/RPvh2b8hnUY5SIgvvvwhuR9tgP6y+PUf6vbfbfiw8D+97LwU4EJt2an3cfH7I0R+/cn9dvOnv/4BSP8fyahFVzsPCp8zK498r2k/f/71p+Zx+6e//vpTV4Io9qzsc1enP6L5I7s++PzJgu+rfv7zXsD/kid5cc8XX3No8XtR/o/6j7eFbgGg+Xa/+bj4PhPnD7SYlfjC9GmC77KxAbJ+Z8dfXv4AiJQDbbonrgH8+I//WAiRUxdN4bcL1Sm6dgEc3EaZNwuvhVGzAH9n1Kg9YNcmAoZ9Xwfif/bwLHHhL377n84D6l+dd6iHy7L9PMP3bFaAdp+97+Huc/PAu88AWD8HXxHvs9cEj/D57W2hAZ5FHQVRDiBbWUvSp5kKQH8gT1l7jVf3AMPssfVeQaq/zheLKF/89q+w/fzg8FaOvz0QP3ripbLlZqxsutR7m61ihF7+bgMHFJ9nifIWaeEASf0IgP9cQ5oiBVWrnS3YJFGaLtwIoBGoe+ODNrDyx5nYb7/9ZltN+Cl/gju+eBbEBgYLvoqzeH0FKvtpFITtp9xzwmLx0+9//LT4X4v/bteD+MxDAsXn3YdAwqN6FhcgJ7vZJMC9ICAA4Dx8+Psf74YHZHJQ1YCBIj/ynptBTCee+8UL6mH9ihHkwvaA9YHls7KoW1AxFlH7tuD8xVd5AdP50VxTwqKZi/dcRr3cGQFVC6jz1ZKghi4aELiND4pz13gPrr/ZtfUQMQPgYLW/LYStBCpYkYL/ZjEfi8DmIo+A+b/GyPM+IFL/1Cw2X0i8LcQ5ihelVVtlWFvvPHzr6Ze5R3jfDohbi9y7f8rnEu49omcO9ad5wCJgGefdpa+zz0Fnk4GIc5svvB9rrLnOao96W3/Km/d0serZFc4cf+Mi6CJ3DsL/eg+pJiy61H3YD0g6U3r3gvvulUcMPjuIxZ+C+8PiGd3PduVbeC9+Bo3SL89OiflRP7Wb+6lPHYagy8X/9z3YbJ01yyoMu9aY3YIRNeX29Nrce87efbargP1DokeGfmuFvsDdF9T/lKcRCMF6/K/nyoev39c8kbQDsgKAUh70QaABSWa6jzyY47qu5wyyPuVfygtQZfHAUmA+ABogqeZY/sJwfvpF0hAgw/z9W6vxiJvanY0BYn1RdnYK4tD3PNe2gEPacHbbF1+CpPDmvL6HkRP+SavZ/iD2AP3ZhxHITlCC3r5C/vPpF9H/tPHZUc1bHt1mB1K5fhAAcnizgLObZq8C8dpnqw/0/PggAtTIynbW3QbJBDR93vRqr+qiJmpn4Hza1SsBoL/OP5+azne9oQT5A4wFsqTsgHUfeTVDTgb6JSADiEmQZlmUg/4BGOXdCA+CVjaDBADh9wb3SfFx+10h75GMc+H7snFWZN4z9xLPsLby8Xss0X4UJoBeNq948P3bSPvKbaY942kDMBFw/PL02XS8PfuGZ2Oy+EL349/NUj//c+PWoxO4/DkAPi7Cti2bjzD8rN5fivcbQDP4KWszF/LXGQNenxX19U+g8/rEnFfA/fUb5LyCivr66EK/5/k0x8fFPyf3n0i8583HBfqGvCHzo9N73L1/gJm2r5vb63J++ilXvG84DNgXGQi82akj6By+Fs0vS0DlDGoAT2Dxs4g2c+29g3L/qBrAQ5/y7xNhTkRQlPJgDtym+A4gHt0DSIqnQ78WN/AobwFvd+5RA2+eFx9p03gvH/MuTT+8ANz0/t/nxLmuZXMSNPPQCdINdIJt5D2+AY+Cx1FT5PN0FBXufPPP87cEbteL59MZkh5Y/AhMAM0AwoJH6M9St2M5i/kcEue28oFYQ/v3NM+PCyt9A1UGoGPafJ8G77VurvXfZevTssCiDpD/w1w7AAgBwYBlZ9XmTLcakDoga34oy6PCfH5WmL8X6E+16fti9GgoHr3KjIk/e2/B2+KiCvtffsjka5P99xwM0KfMxNzi41yyP7zj3odHnfyw+DrjANXep87HLw7yDgz0v87z1ezJx5b54unZr5u+/tLE9l7++iO5HuD4eY7CZyz9rXQaaP28dvEGsnpYfFn2YfFQ91/J9FcMwchXhHjFlg/aP7QaGCIi7/4ZMA3a8O9lOz3uw/PoDkwIKtf74AH2PC4fTUfWgS7Sj9p3mVHiFUD+3IBnIAbDdHzf8AP+DwFAqQEFe7b0Nxd+M2TxmFpnUYFO7fOXLL+/gJyy5hbmPavexx6wHCDzazO3bTDAI8AQfH8iB3j2bx2I3mk3oQWabkDccSgfQVYu6nqUtXKX1BJxCXTp0JRHEoiLURRGEgS2clCc8H176ZP+ikQx3/Xp1YpGMUDviU2f5741muWdhQVmegVZ7317DG6574o+FZut+HX+mg3yru/vLza5BCsPy4ZbPz9beIXa1PVkD+0Vmsj+VsRCipl8cGvcUgUoi51ODW0PQ1Gzjhtz1eZubY52omy3m9t9dzwUROopPHTXYQ4ioClKyHUyIpQtngVBNXY4JeYTbY7SVcvOAh63A0xY2zCDdTRRbcxwoNWeIbeKvDrnh0IPcgq7GBDOBIMXJ9RZv5VHxo8IQRKicFzpJI9AimpW3jHKpeG6vl2XKQxDvLvUq6BABe6a+drOUo6H83igjoWMcDKLNoTH1gK16sVNlKq6TV/vVwhtdEs63CtkJo+VWwl39mSTrFcoV/cIdz07FY7gTOkU+Dql47NygF24rLj+KAwdw1RLX9M9tW9MJtCRrJluFC0Ker26HAqV09UbdmkqXSqvdCgMTNK1WnOTDjhBN/hxJN1eI8hTAsFe3+fK3qDxS6Acc1bUl4pPHJvsfpbOmk3IRmDCpDpcFQGeeMEOOVGJh3YpcidNgLEJwdaoUyXdRd5to22/3sbLBtdEZPL06XDjTlzl0kZ94NRJ4/aiT+3QG2Wo58bBNkc1atSLcnSYvdm5x1YZVyc/d6BDuetXgmDECj+xqmxumeOt2OWDdlQDPTyyKrEityc/EcxbiDOqSrDNcNbZjdkbfhJ32I0oEoi4xAV8YrdHSqWaiUIqz1id701SpJq5U6yI589H2dTuzilJg5gw190GJz0TK81EoDJtLdH26uyINY44y0ubFc6YTPRVjbrCZk8p70qlE3uptlpGkin7lzBPmP0RiJJsCpsQ/SNWe1sMA/LQ9zUxZQaq19J6uQSGEa70KfZbZSOQYYEGUlW5GD9wAmVsCI/htehAW9QIhTfbDKUVeTSH9LItLGwoVFIP9pYx1GsVt9sqrY4q41R9u4kSbIvSFXqOolFOTohswoOe7rV8GUeEduJO/la+qvC9VzJHPfQ3FeYTccPQlw6ROHsf31XLPhRSujMgcWqcfNKFVd4s1/kmtzx21OzM2F+mFYfkBD9plCOcXMFombvYJOMAnWQ2rfILOeaEj4tHblkR0C7qskFtInra7yFS8ZYyjqMF1cCrjSL4mjmtzj2tne5KR6T5ms6hO6OOro1t8tKJPONMsjuNN4i81HfSAVpNwWbDcmOPHVMMGRB6Y0EDz6YZclJIunaDJe3WQnp2RXa7bhPBu0kyt1xmGwk5xbo5xKSyWWYWFl7vriz5W5oJ1rQ23RX9Llkhf97t5InL5CZfUxsxMxHT7QZhOnTrStDspeay5kpULUsu4kFL2YtOnMA/JWU8VlIq5ZrK4BKIU0d6ozDwyDLwaUMfokq8aV1/lcYpJNKKM1LkRuRLVPY8J4VZKEtPB8yHCX9yrlgvSCFUnbdDEGlNIbLH9eFCMc4+LZRN1krepgqYFWlGW6NH811xhm+tPK7TlPQM4XJKtiqS8uwWNj0YxdcndRqRZS8EUrLKyOsm9OTi7pdocl6V+g2h9jQN7TXooI3ENcllUW8TQzhCl7XSt4IVH3WsHSMh4FUevdvczfPOK0jm6dHoU2tDX+DDrsfaM49Ehdp7mLYrQ7nqMhvaafTx0EzyzoW7YYtSdHZAnEPWHe0Le+IQOgYQjibsdk8qWsfq47rl6UgGMSMmNbvHzCq1eyMakvX9NA1WJuz2ThxAbtckR4nMlbyv3DVXdVfzDqNDqawwjXdz87jfi9KaLdjVme+uMWmFQMVBkv2Vd6/9iZ6SrQbB6u66i7ci5wzb7CTGXBsgseSRfKhXpRTQATFuFY5wxFFkD2uGiaEh0FZC0e10BQA05sDb6B4peR2bozlCPCuVXLipjswQXxAvKZQmrlZ+f9VFO0s1oUviXBNGFqtsg8HITtFSjahL98jnfHC1jZXJikV62R/CzcWUHQ1T95qBBEgTdYAxxHCeIm6b9X2rYz2SFLvOhuqcI9E7mIh4fnOQ77Zb71iyMdSVRW8StjvFlBSnOS6kKTvm+z0p+j2G+oejizn5Zr81tY3UMEiISGTJcLADHw/siFuSfCPoi2SA+VVy8p2p0nYbbtilxBXc0vN7/E4yMIRYAiz1a9/PcaS1L/WZzkrmiOZ+E5tBsN1sRFU+UyGxvLgWE/I1ein2iiwzuQfv3ES9X9sq35BUtoz7BD5E00lZi2tbYryb4Nxb3ULsNb+svDW0TTc9l/h7pqJPHBOFg0KObTBMihSbXM8K61LuLTHjrnzBM4xlL4VLkqdbBNY7N4QP13q3Hb2KFvqlwE4BWu/hvEO1sRoLWU8iGeoz9trhA5Rlt2C4IAN/7/WNqgg8ya411bY5x8FoWU7ScYzPtRCqluuvw8TkFNPqNNrKgnHn3s7o+RamnOGNuiRMGWEsJZ3Bmc2WMR1YoXzF4HY8sg8vd/7gCliixzRF6/rSgjOIYApOdpIQqeCuGlfDYVl0oEIOMivL3n1fiFdpcIqzFW2zdsubQtqO49q+ROntziEnz8mOZ8knHFtKbC09yla7t5Pzlk05fRfTABJxb3uJ+mW0i63LQVU9LqkyPuFIn7gYBRMzNUNC5nndAa3W+WXobaMnxgSRBQfe3O/2RbgY3KU8V0HdYVekoUsFRdS4lkbKXJaDPK17gjSKaD/eHTvbHg36fNpTtREWTVMQmooSojqoY35Zseth7QrEpGn7ii911oi0i5hg43U3xgoCl+Nlt+02m8s1ckPGyfukH/brKoBGjb/ckunI87wn8JB8Osr18poURcp6MTMeNSw/KOxdIZ0oGHr9BhUQ2+3kbSsPK+pEN0fsuIYUwxYaU1PKjKQ0TnFlA8AQZkej5mjqKj+xO2knwEKb4oMuRkumODqGM/lYnRW3dlVIkFWxR5VuVmdtiUuH3cExYvKQJPnejk+aIe8Dz+nPjJJhKnK0UYHJGWivbjlJ9wuGvur2Jklrq9kPTLbWo3gfmCKvN4gtnbrglAVr0GqadACp6DgJCt2NUVbKLqwp7ei3Y+fvKZo646S4LuwAS28kyu+5pXHgku0+S5xDEOmkHUmGSmBX1Nysd8bo5Tsjp1ejpctcImq9SmPl1NKpJu4M2dtsjXvNBfzNLGAkE4vdQGgkUaj2HcdjN4fxCZWC4nTXV10haefjCN3d3kegtKEn5MCZUseqPKKjazo58Aq5nw5VCazqwzh13kqhZrgmW2615HJE+Ol2k/RMZtTzmYyQPiw1Vbk7MF3fkDI76/m2ipPAGnieOa/HUMNuOaHRxPqkr5Y2mUZrhCgpvRkFTRMLtHcdS+qUaCjo+l5Y5IBzy3VxEYOw1GVfBFnH7dZSYwEwEs/qxlWZ25k/Z2jZ9adJO6amH5FtyZ70qjdvsIiU7a2M5TO2Nu6HS4pTt8KfUhJmN/3Q6PcVE9ObLbonR2jPdOv4dkA04hYdl8vKYWgv2xV319dutKcpK3q0FTdBt7QOn9T7eKyTyaXH1SrbiMTdjiOUkUlxWcFO3AbRqjij+OGEDpZU6o2+1+KlTxBtYY7ecs+3J3O0VxmorY2pGKDvEgu1RnG4Ve4WtzyFm5XHGEnM5+U1P9KBRAYMEhu10FaM21JuthSaQV1X6pJFNzdBpzS7E4PO8LvBUW1txzKIwEdKhnARxweZZ97QiHUu0LBCph3HMPcG32QbDEXM4+BWxJGavHUVndiwlM89GajToW/tQyOde9u+0hFB5Dc0UMH8KGnUaZndtLLYQJhlxGIYqPlugjJZJuz2yo0Qe2zPuc3ikRKsWK4TQVvPUQ0bhIgjDcONW6+0W3UwSqkiBiY4QwO3ThRT0zfyUCgFAsk3BMr6oZgOEY7rXM9Xd8onz/2QX3Mbq6zIssEQcLQYuNP4fQ56LabaVVyUsvrVEUpXVjgyhXChiy+GRBWBZnkJW2nHaRD5cEzgC9+4+dTLcjpsnekgbfpg1W3juMESFQyo0UhNx+s2ojTXrtXDSYpydbmGRQ7ZyaiyCmotynCrTuK7k1A0LblhtxKkDjtl0vocCdCEt9pSx7uM0vgb1ZhSyAXOeVhnwj7d1pE5EittO6IHpb84neYsl/W2kOwmm0LTl3gnx5OjwW79Jtz35s436NrscYVcqTceu45XBIPbuiw7rul0ljgHTdxlE6Vvcv5ieBtilBkJA02FhOCqnND+zuqvg4jLqZTqHd4v+9WhO+Ya3mJJIsnHk2VrWC3I4a2P73ERHtYRBcmJSWz3TUMCTtUQG2WCbHDz0ErXsyR0+6LUjs716hcw2kxJydd2Zl+GFWh99JsVUb5W1GQqjVx9uuWdSfnXzWa3lpUc9UIFpc8JssaTykREpG9a1zdXKrocQqX2afdSe60h2u2B0AxzJRkGZFBEZt997z7QewHbumCeBFkS5AfWQkzGViyONrBMg3LPF0iacu93dbeUlnHdpTEU7jUpgsdUN+lSiuvDUrHbdDllPEcWKMZYDOmWWuaxRD0N5TnBTOiOapB0N73LdMTL1bagTdRFBIw83g9rN9EcMbnUF4viMqgSVilQpU6Xq9LDmzB2iUMD0UO/huA7zYanJtWrpQvmLtTYIpRVT92hFfCY8CVsRHTc7PpLq50H2lpSMdmqXdaFxui6KGiadHdzdJujsWQmTEE32OkkOQdJQ1HK8oOoTGtaRvRV4JLwEY/hdX+VKdwRz2WyW13Rc2lWXrlZbfFJxEo1MPjbdM4YE+V9jmagI3mqVGyrtVEbyjHK93CLiVJ5w/l+gilRaQt/b0d9kC4h7KpanUdN3KFSD/4+9Hi7rusCM9Hpmuw3AcTWwIE7qUAKK6adDXaXYHTC4eCAVS2/vcTitIL3Pm0Z7HKXQGh9RadtfZB3yJjQVydwV3LLxiF2Qpo+hI88lJ0FAS6thM/XZH/ddFOwA6VQVTiPiKB1kAx3WY5jEVNNsEocrTI1MyIfpMGz2SxPKHI3NBs1qQJrLzcjfAJ9JrFrNCY75DvrfKXPYLZKvRR1xxO2LAvhyKFy6ON70iIppymPh1NzBXPUIc9t1xTiiFL3xyVqsOWZPZ73MKK6K2zJ4BSC5kIH8dHtAnkRUx4ggo9X3t6hS1+PVxkIzSphVHl3iWTpkFNtfOpGARLsW8TJVta1ChpfMGxjNoZrdLVpXbv7Cb3da93YlTultgVVsqGJreH14XRmtWDAbAzfZxyI6ylVJWZ/tRm1BO1dIkaCFtxhUwa4I0TJuJOFpV1WRnu97g+kBSWVg503FdjjCEuiqey1ofGBdp0UbAf8FfptvJXPtuH450OrJqU+qUWWH/0rALargtyEQ9111mkArfGy1naOgZ+cydvwvqgF0FAVIjEKB2cXQKe6Su4wgh34RKzEgUWXNOSWd9aFrmx8H+6ieFXwU2hHfL0Zd2HRmckN9AlXjef7k35tj/Zgr3uxMosan1oxwFFkbx9Tr/UcMbOSihPw2meNdU91O7fbnps6OPV5XWLHinSWcAWJBGxMaieiltvdBKrUNr0eIpQeCjdCP/apEWuocU1t0D3uYlMMw0qa0mp/PeG90K/lgM+9YtLCntoEhgyKBlyqhbeXFfZGH9op5vsq9Ab1MJ724jpTjO62pkFRKkc2tiCRRFcQHnqa0Xs7ux2uebY3DlpznyY/X9Upzu+py7IyUby7wlJ+Dzbl1T+c1i0eikfYGQgMbXvdu46N1rYU1YbXcqPI+cqV1ygq3jvJopaWSrjb0IeYnDhkDE+csrD0yJPWbU+ehV6paM+m1hLdORc9b3d4vjQl1ven886vdp6uEHvPjwN8NANT2VTNxHnF8XKaGytsSYABJu1jI6ZSZIp6COqFNY/tFSOEVJu5VQg11k2AbzAqDKpQYg5CYZzPMV3erGBUqGp191zYD7VjzZV7BO3HaC2FE3W6dfww1KsQSeigE++5h2Zbk9VVbEMJ6bEXD96gUyPe9rsVsrbO5G5qLm1g7sjdcefu/SikskIaOvLATRKPF1ZInyWrH1UTX1ZY7QS9cC8kva0NqjwhHIb06zGn0CK6S/3yfqlH0m5LI8m5ziYxxDbEtPYlHNtWqWnvDEkdJnNPg6YxrS+imAzdGQpNdnfGsWy65hWI3PB4Pa8UAz2eeHKk4bJhb7oij6A9XK1Yqm3P/knYqQbUG9uphO5ZoEaIpDp74tjl5+PJMKoLxGCiKZ6c5pKXIh6WE1tdE83zJh6tHVK/8+TqKktjPOY95sVKTzs9Waec73eUfLpBW7psKL50L5skTIM4ccnTQVofuaXEqo7dQihN+KS42/UFJduF78mXiiCxKTmhrUj4VS4e3F6ceM8qentb7YbB150W0/qwu4qMO7noruGpYntArpdzdqHuNAeaHOlyObs7EgwScHto7luUP2GnaU1IaRc4bY1jIZGRW5xgkjZei/utOYl1fW7NO4Wloy85bLvLJPkgc2znXaB1uQ/yixBZG7LAx/v6fFBqmuV9WxQ7rUEGZIzTYHSg67m+i+bSnuqyQ+99ERL82Sy6kEz39IGPvabhc92VcQboPEH9SbtedcweCY/rIaN2cruX0n5V2nv9itn3cenL59il2V13SK73kwpad9w61SRXaVGVtQCHkhROkD3uw5d479rS0vDbK++ak15t0OXZVWx0bPF9S3XTKCn9UIGBDMMn4ZjxMAyjHptZ0lmSvGqlIFeIUnEoH3cEXObHTmLgiGlGZbMW1dbfVPnWum25PKqiaI0XYePE5gYz0MN1OLWG0YBBgwpwwhaU9ojJYnpS7i62owsmacLM9ejEHYseI6ULbrYNp8N+D4V+PV44iXaQ1RIh8e7oZ0trM65JYyfqVH8NbnjojBQnTqAFL3XGPZ/BFOiw0Xz0U1GDC8O7/G4lu/a+5z14w3mQdRSqVTzWorQE0cOuqIQXcNBHV63hs1vH28FL34lt86ztmfV6/ZeXDy/fDhJf/i1v1s0nS/+2Q6znWdSXd2Mep6ee5X588Pr47xH3rx9eaicCwj4P+BqQH+/HYX9zvPf6rxyezpTH50tuXw7Sn+8DtFYwv0r+EuVu17T1COROH2/UgB1218yvmTbzm8gO+PmnY+N35WcPFrXnWE37uS2+HCVG+fyijOdGVuu9fw3ej0I/vLjvB+SfcZL47NXlbIL31y6A5vgb8oa//PG/Acm/D371LwAA -->
