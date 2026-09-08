---
name: "rar-cowork-cookbook-ppt-exec-implement-the-disaster-recovery-plan"
description: "Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan", "rar_sha256": "4a9c13b36953b349da23d54a70b3bc9ebe39426f844404a6bda0f0967c9fe6dd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Implement the disaster recovery plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.",
      "type": "string"
    },
    "review_date": {
      "description": "Date/period of the monthly review used for the report and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 4a9c13b36953b349…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_the_disaster_recovery_plan_agent.py` first:

```bash
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py   # or on stdin
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement the disaster recovery plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Implement the disaster recovery plan Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a49392ebb920ed9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-the-disaster-recovery-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'review_date': 'Date/period of the monthly review used for the report and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for implement the disaster recovery plan reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on implement the disaster recovery plan for a 15-minute monthly review. Produce 'ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement the disaster recovery plan data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on our disaster recovery plan rollout from D365 USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Date/period of the monthly review used for the report and filename.', 'name': 'review_date'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX status deck on disaster recovery implementation for a 15-minute monthly review, sourced from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecImplementTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'type': 'string'}, 'review_date': {'description': 'Date/period of the monthly review used for the report and filename.', 'type': 'string'}},
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
    print(PptExecImplementTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
