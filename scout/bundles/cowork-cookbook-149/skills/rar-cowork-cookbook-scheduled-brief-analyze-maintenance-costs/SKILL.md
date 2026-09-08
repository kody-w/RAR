---
name: "rar-cowork-cookbook-scheduled-brief-analyze-maintenance-costs"
description: "Builds a maintenance-cost morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft and a Teams-ready su"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_maintenance_costs", "rar_sha256": "344981ca8c721bfc9c61fce177ce10d78e40130742b3032d94f4dc6097267428", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
