---
name: "rar-cowork-cookbook-scheduled-brief-record-production-costs"
description: "Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_production_costs", "rar_sha256": "9e809e6ff40f3a5f7cdaa5eceae1181ed4a050dfcd6ac6517ca383cdf2afa782", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_production_costs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_production_costs_agent.py` and in the RCI capsule.

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

Record production costs Scheduled Email Brief — Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_production_costs_agent.py` and embedded as the fenced Python below (sha256 9e809e6ff40f3a5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_production_costs_agent.py` first:

```bash
python3 scheduled_brief_record_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_production_costs_agent.py   # or on stdin
python3 scheduled_brief_record_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record production costs Scheduled Email Brief — Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_production_costs',
    "version": '3.0.3',
    "display_name": 'Record production costs Scheduled Email Brief',
    "description": 'Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own',
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
        "upstream_slug": 'scheduled-brief-record-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4381d33f8fd82d56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/record-production-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-record-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where record production costs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on record production costs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record production costs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own', 'example_request': 'Send me the record production costs morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly production-cost brief for the responsible owner, as an email draft and Teams-channel summary, on a weekday 7am schedule.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRecordProductionCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordProductionCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRecordProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
