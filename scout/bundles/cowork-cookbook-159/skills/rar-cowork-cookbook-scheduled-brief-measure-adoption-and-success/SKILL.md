---
name: "rar-cowork-cookbook-scheduled-brief-measure-adoption-and-success"
description: "Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_adoption_and_success", "rar_sha256": "a66d8368a9e3cddb94441f964a4ec532d2fe2fc51af137958e4fd199b25cbfd6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Scheduled Email Brief — Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
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
      "description": "When to run it, e.g. weekday mornings at 7am, or daily/weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 a66d8368a9e3cddb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_adoption_and_success_agent.py` first:

```bash
python3 scheduled_brief_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_adoption_and_success_agent.py   # or on stdin
python3 scheduled_brief_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Scheduled Email Brief — Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_adoption_and_success',
    "version": '3.0.3',
    "display_name": 'Measure adoption and success Scheduled Email Brief',
    "description": 'Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the',
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
        "upstream_slug": 'scheduled-brief-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '695c3b5c7045bd1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where measure adoption and success stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on measure adoption and success for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure adoption and success, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the', 'example_request': 'Draft my 7am adoption and success brief for USMF and email it to the owner as a draft, plus a Teams summary.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly adoption-and-success brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMeasureAdoptionAndSuccess(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureAdoptionAndSuccess'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am, or daily/weekly.', 'type': 'string'}},
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
    print(ScheduledBriefMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
