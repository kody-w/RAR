---
name: "rar-cowork-cookbook-blueprint-position-and-onboarding-readiness"
description: "Runs a read-only recruiting and onboarding readiness check against Dynamics 365 F&SCM via the ERP plugin and returns a position-readiness.xlsx workbook (Vacancies, Stale, Pipeline, Onboarding) plus an email staffing summ"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_position_and_onboarding_readiness", "rar_sha256": "1599ff453edc3d652655ce739cb28ecce70a466847ea3f7ab51011b1961c903f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "hire_to_retire", "advanced", "integration", "dynamics_365_erp"]}
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
