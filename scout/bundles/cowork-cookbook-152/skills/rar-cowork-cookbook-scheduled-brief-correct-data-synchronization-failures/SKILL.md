---
name: "rar-cowork-cookbook-scheduled-brief-correct-data-synchronization-failures"
description: "Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures", "rar_sha256": "91385dedf5f5bee3333ba7794649f71b722e73132524fbf150f21456d9b24a79", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_correct_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Correct data synchronization failures Scheduled Email Brief — Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 91385dedf5f5bee3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_data_synchronization_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_data_synchronization_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Scheduled Email Brief — Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures',
    "version": '3.0.3',
    "display_name": 'Correct data synchronization failures Scheduled Email Brief',
    "description": 'Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7f5b8851fe7e62dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where correct data synchronization failures stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on correct data synchronization failures for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct data synchronization failures, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th', 'example_request': 'Give me the USMF data sync failure morning brief for the owner and draft the email.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly sync-failure brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCorrectDataSynchronizationFailures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectDataSynchronizationFailures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
