---
name: "rar-cowork-cookbook-scheduled-brief-measure-adoption-and-success"
description: "Builds a morning brief on measure adoption and success from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_adoption_and_success", "rar_sha256": "a66d8368a9e3cddb94441f964a4ec532d2fe2fc51af137958e4fd199b25cbfd6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
