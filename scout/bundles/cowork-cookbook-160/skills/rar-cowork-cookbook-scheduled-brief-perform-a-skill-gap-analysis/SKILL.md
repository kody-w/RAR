---
name: "rar-cowork-cookbook-scheduled-brief-perform-a-skill-gap-analysis"
description: "Builds a skill gap analysis morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis", "rar_sha256": "a2317082a396d0bee7cf029ee586bbac96debd42d95ee5f010b6e09ecd7c51b8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
