---
name: "rar-cowork-cookbook-scheduled-brief-run-events"
description: "Builds a morning brief on run events in Dynamics 365 F&SCM (legal entity USMF) for the responsible owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves an email"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_run_events", "rar_sha256": "b6d5da367190223fd1465ebef265c725d79c6fa439680bafe2057222e49b753a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
