---
name: "rar-cowork-cookbook-scheduled-brief-estimate-the-cost-of-production"
description: "Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production", "rar_sha256": "91e092ed9695394cf8edd21264cebb7b8701f5183cceb032b0c37f1df58f542f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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

Estimate the cost of production Scheduled Email Brief — Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 91e092ed9695394c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_estimate_the_cost_of_production_agent.py` first:

```bash
python3 scheduled_brief_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_estimate_the_cost_of_production_agent.py   # or on stdin
python3 scheduled_brief_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Scheduled Email Brief — Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production',
    "version": '3.0.3',
    "display_name": 'Estimate the cost of production Scheduled Email Brief',
    "description": 'Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b0ceb338f298aae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where estimate the cost of production stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on estimate the cost of production for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads estimate the cost of production, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner', 'example_request': 'Give me the 7am production cost brief for USMF and draft it to the owner plus a Teams summary.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly production-cost brief for the responsible owner, drafted as an email and a Teams channel post from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefEstimateTheCostOfProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEstimateTheCostOfProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
