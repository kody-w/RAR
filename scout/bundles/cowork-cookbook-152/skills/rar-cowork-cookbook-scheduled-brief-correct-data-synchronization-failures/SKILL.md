---
name: "rar-cowork-cookbook-scheduled-brief-correct-data-synchronization-failures"
description: "Builds a morning brief on data synchronization failures from Dynamics 365 ERP for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to th"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures", "rar_sha256": "91385dedf5f5bee3333ba7794649f71b722e73132524fbf150f21456d9b24a79", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
