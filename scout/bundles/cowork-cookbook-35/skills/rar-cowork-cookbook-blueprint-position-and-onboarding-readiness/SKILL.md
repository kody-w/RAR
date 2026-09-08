---
name: "rar-cowork-cookbook-blueprint-position-and-onboarding-readiness"
description: "Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_position_and_onboarding_readiness", "rar_sha256": "1599ff453edc3d652655ce739cb28ecce70a466847ea3f7ab51011b1961c903f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "hire_to_retire", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_position_and_onboarding_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_position_and_onboarding_readiness_agent.py` and in the RCI capsule.

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

Open Position & Onboarding Readiness Blueprint — Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
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
    "asofdate": {
      "description": "Date the vacancy and onboarding snapshot is taken as of, e.g. 2017-12-31.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legalentity": {
      "description": "Dynamics 365 legal entity to analyze, e.g. USMF.",
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
    "vacancyagedays": {
      "description": "Days a position must be open before it counts as stale, e.g. 90.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_position_and_onboarding_readiness_agent.py` and embedded as the fenced Python below (sha256 1599ff453edc3d65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_position_and_onboarding_readiness_agent.py` first:

```bash
python3 blueprint_position_and_onboarding_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_position_and_onboarding_readiness_agent.py   # or on stdin
python3 blueprint_position_and_onboarding_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Open Position & Onboarding Readiness Blueprint — Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_position_and_onboarding_readiness',
    "version": '3.0.3',
    "display_name": 'Open Position & Onboarding Readiness Blueprint',
    "description": 'Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'hire_to_retire', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-position-and-onboarding-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-position-and-onboarding-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4605a20456933bb9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'hire-to-retire/blueprint-position-and-onboarding-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Human resources role', 'Prerequisite: Cowork D365 ERP plugin toggled on in the session', 'Output matches: One workbook plus an email draft listing vacancies ranked by days open. USMF has 97 active workers; if the position hierarchy is sparse, expect a partial report naming what was readable.'], 'confidence': 1.0, 'deliverable': 'One workbook plus an email draft listing vacancies ranked by days open. USMF has 97 active workers; if the position hierarchy is sparse, expect a partial report naming what was readable.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'asofdate': 'Date the vacancy and onboarding snapshot is taken as of, e.g. 2017-12-31.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legalentity': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'vacancyagedays': 'Days a position must be open before it counts as stale, e.g. 90.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives HR and the hiring managers one weekly view of where the pipeline is stalled, so long-vacant roles get escalated instead of quietly ageing.', 'expected_output': 'One workbook plus an email draft listing vacancies ranked by days open. USMF has 97 active workers; if the position hierarchy is sparse, expect a partial report naming what was readable.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Human resources role', 'Cowork D365 ERP plugin toggled on in the session'], 'prompt': 'The attached image is a workflow blueprint. Build and run it as an automated task using the Dynamics 365 ERP plugin. Follow the diagram exactly: execute each phase in the order shown, honour every decision diamond, and stop at a red halt node if its condition is met.\n\nDo not ask me clarifying questions — every input is bound below.\n\n## Input variables\n\n- legalEntity: USMF\n- asOfDate: 2017-12-31\n- vacancyAgeDays: 90\n\n## Trigger\n\nTrigger: weekly, Monday morning\n\n## Outputs\n\n- position-readiness.xlsx — Vacancies, Stale, Pipeline, and Onboarding sheets\n\n## Notification\n\nEmail the staffing summary to me\n\n## Guardrails\n\n- Read only. Do not create or modify positions, workers, or onboarding checklists.\n- Produce the workbook in this run — do not return a plan or a methodology document instead.\n- Do not include compensation figures or any other sensitive personal data in the output.\n\nIf position or onboarding entities are not exposed to the plugin, report exactly which check you could not run and why, list what you did complete, and stop. Do not infer vacancies from the worker roster alone.', 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ', 'example_request': 'Run the position and onboarding readiness report for USMF as of 2017-12-31, flagging vacancies open over 90 days.', 'inputs': [{'description': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'name': 'legalEntity'}, {'description': 'Date the vacancy and onboarding snapshot is taken as of, e.g. 2017-12-31.', 'name': 'asOfDate'}, {'description': 'Days a position must be open before it counts as stale, e.g. 90.', 'name': 'vacancyAgeDays'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to know which positions are vacant, how long they have been open, and which new hires lack onboarding records for a legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BlueprintPositionAndOnboardingReadiness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPositionAndOnboardingReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'asofdate': {'description': 'Date the vacancy and onboarding snapshot is taken as of, e.g. 2017-12-31.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legalentity': {'description': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'vacancyagedays': {'description': 'Days a position must be open before it counts as stale, e.g. 90.', 'type': 'string'}},
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
    print(BlueprintPositionAndOnboardingReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
