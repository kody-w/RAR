---
name: "rar-cowork-cookbook-scheduled-brief-close-periods"
description: "Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_close_periods", "rar_sha256": "8cb1b46184571cbb13a5468b09992e980faee84b9b9bb27b357389a28a547dcc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_close_periods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_close_periods_agent.py` and in the RCI capsule.

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

Close periods Scheduled Email Brief — Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_close_periods_agent.py` and embedded as the fenced Python below (sha256 8cb1b46184571cbb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_close_periods_agent.py` first:

```bash
python3 scheduled_brief_close_periods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_close_periods_agent.py   # or on stdin
python3 scheduled_brief_close_periods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close periods Scheduled Email Brief — Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_close_periods',
    "version": '3.0.3',
    "display_name": 'Close periods Scheduled Email Brief',
    "description": 'Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-close-periods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-close-periods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bec66c862b17f837',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/close-periods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-close-periods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where close periods stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on close periods for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads close periods, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary.', 'example_request': 'Draft my close periods morning brief for USMF and send it to the owner as a draft, plus a Teams summary.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly close-periods brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefClosePeriods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefClosePeriods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefClosePeriods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
