---
name: "rar-cowork-cookbook-scheduled-brief-estimate-the-cost-of-production"
description: "Builds a morning brief on production cost estimates from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production", "rar_sha256": "91e092ed9695394cf8edd21264cebb7b8701f5183cceb032b0c37f1df58f542f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
