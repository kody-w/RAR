---
name: "rar-cowork-cookbook-scheduled-brief-close-periods"
description: "Builds a close-periods morning brief for a Dynamics 365 legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft plus a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_close_periods", "rar_sha256": "8cb1b46184571cbb13a5468b09992e980faee84b9b9bb27b357389a28a547dcc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
