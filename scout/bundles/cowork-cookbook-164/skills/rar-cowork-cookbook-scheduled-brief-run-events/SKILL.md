---
name: "rar-cowork-cookbook-scheduled-brief-run-events"
description: "Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves an email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_run_events", "rar_sha256": "b6d5da367190223fd1465ebef265c725d79c6fa439680bafe2057222e49b753a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_run_events`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_run_events_agent.py` and in the RCI capsule.

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

Run events Scheduled Email Brief — Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-run-events
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "The responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run it, e.g. weekday mornings at 7am, as a Cowork scheduled task.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_run_events_agent.py` and embedded as the fenced Python below (sha256 b6d5da367190223f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_run_events_agent.py` first:

```bash
python3 scheduled_brief_run_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_run_events_agent.py   # or on stdin
python3 scheduled_brief_run_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run events Scheduled Email Brief — Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-run-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_run_events',
    "version": '3.0.3',
    "display_name": 'Run events Scheduled Email Brief',
    "description": 'Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-run-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-run-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b172cb66c8760950',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-events'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-run-events', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'The responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, as a Cowork scheduled task.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where run events stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on run events for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads run events, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email', 'example_request': 'Send me the USMF run events morning brief for the owner — draft the email and a Teams summary, weekdays at 7am.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, as a Cowork scheduled task.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly run-events brief for the responsible owner, drafted as an email and a Teams channel post, via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRunEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRunEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, as a Cowork scheduled task.', 'type': 'string'}},
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
    print(ScheduledBriefRunEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
