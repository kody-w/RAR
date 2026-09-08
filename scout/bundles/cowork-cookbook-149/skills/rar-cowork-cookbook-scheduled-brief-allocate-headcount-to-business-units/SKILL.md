---
name: "rar-cowork-cookbook-scheduled-brief-allocate-headcount-to-business-units"
description: "Builds a morning brief on headcount allocation to business units from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_allocate_headcount_to_business_units", "rar_sha256": "1aa13af97eb5f6da3ea2c241d0a1f44f61e4f394a84568e2d2f315dcb912c584", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
