---
name: "rar-cowork-cookbook-scheduled-brief-record-production-costs"
description: "Builds a morning brief on record production costs from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_production_costs", "rar_sha256": "9e809e6ff40f3a5f7cdaa5eceae1181ed4a050dfcd6ac6517ca383cdf2afa782", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
