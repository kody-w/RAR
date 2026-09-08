---
name: "rar-cowork-cookbook-scheduled-brief-analyze-maintenance-costs"
description: "Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_maintenance_costs", "rar_sha256": "344981ca8c721bfc9c61fce177ce10d78e40130742b3032d94f4dc6097267428", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_maintenance_costs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_maintenance_costs_agent.py` and in the RCI capsule.

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

Analyze maintenance costs Scheduled Email Brief — Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
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
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 344981ca8c721bfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_maintenance_costs_agent.py` first:

```bash
python3 scheduled_brief_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_maintenance_costs_agent.py   # or on stdin
python3 scheduled_brief_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Scheduled Email Brief — Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_maintenance_costs',
    "version": '3.0.3',
    "display_name": 'Analyze maintenance costs Scheduled Email Brief',
    "description": 'Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cac41b37bef9a51d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze maintenance costs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze maintenance costs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze maintenance costs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su', 'example_request': 'Draft my weekday 7am maintenance cost brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly maintenance-cost brief for the responsible owner, saved as an email draft and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeMaintenanceCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeMaintenanceCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
