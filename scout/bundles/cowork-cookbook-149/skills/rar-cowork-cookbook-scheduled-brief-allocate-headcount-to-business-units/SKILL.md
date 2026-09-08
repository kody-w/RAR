---
name: "rar-cowork-cookbook-scheduled-brief-allocate-headcount-to-business-units"
description: "Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units", "rar_sha256": "1aa13af97eb5f6da3ea2c241d0a1f44f61e4f394a84568e2d2f315dcb912c584", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_allocate_headcount_to_business_units_agent.py` and in the RCI capsule.

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

Allocate headcount to business units Scheduled Email Brief — Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_allocate_headcount_to_business_units_agent.py` and embedded as the fenced Python below (sha256 1aa13af97eb5f6da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_allocate_headcount_to_business_units_agent.py` first:

```bash
python3 scheduled_brief_allocate_headcount_to_business_units_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_allocate_headcount_to_business_units_agent.py   # or on stdin
python3 scheduled_brief_allocate_headcount_to_business_units_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate headcount to business units Scheduled Email Brief — Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units',
    "version": '3.0.3',
    "display_name": 'Allocate headcount to business units Scheduled Email Brief',
    "description": 'Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-allocate-headcount-to-business-units',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-allocate-headcount-to-business-units',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63308f512c55037f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/allocate-headcount-to-business-units'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-allocate-headcount-to-business-units', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where allocate headcount to business units stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on allocate headcount to business units for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate headcount to business units, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft', 'example_request': 'Draft my weekday 7am headcount allocation brief for USMF and save it to drafts.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly headcount-allocation brief for the responsible owner, drafted as an email and a Teams channel post rather than sent.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAllocateHeadcountToBusinessUnits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAllocateHeadcountToBusinessUnits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefAllocateHeadcountToBusinessUnits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
