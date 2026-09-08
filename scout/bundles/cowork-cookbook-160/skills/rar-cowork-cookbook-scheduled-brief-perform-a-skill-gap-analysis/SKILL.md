---
name: "rar-cowork-cookbook-scheduled-brief-perform-a-skill-gap-analysis"
description: "Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis", "rar_sha256": "a2317082a396d0bee7cf029ee586bbac96debd42d95ee5f010b6e09ecd7c51b8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_a_skill_gap_analysis_agent.py` and in the RCI capsule.

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

Perform a skill gap analysis Scheduled Email Brief — Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 a2317082a396d0be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_a_skill_gap_analysis_agent.py` first:

```bash
python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py   # or on stdin
python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform a skill gap analysis Scheduled Email Brief — Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis',
    "version": '3.0.3',
    "display_name": 'Perform a skill gap analysis Scheduled Email Brief',
    "description": 'Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-a-skill-gap-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '574645d8f6ed647d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/perform-a-skill-gap-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-perform-a-skill-gap-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where perform a skill gap analysis stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on perform a skill gap analysis for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform a skill gap analysis, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner', 'example_request': 'Run the skill gap analysis morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly skill gap analysis brief from D365 F&SCM, drafted as an email to the responsible owner plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPerformASkillGapAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformASkillGapAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPerformASkillGapAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
