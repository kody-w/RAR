---
name: "rar-cowork-cookbook-scheduled-brief-swarm-on-case-with-team"
description: "Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_swarm_on_case_with_team", "rar_sha256": "c145dbffd83bd0d641158324e5d4afe31a3f1e5650795c42226a19fcee54e684", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_swarm_on_case_with_team`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_swarm_on_case_with_team_agent.py` and in the RCI capsule.

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

Swarm on case with team Scheduled Email Brief — Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team
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
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 c145dbffd83bd0d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_swarm_on_case_with_team_agent.py` first:

```bash
python3 scheduled_brief_swarm_on_case_with_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_swarm_on_case_with_team_agent.py   # or on stdin
python3 scheduled_brief_swarm_on_case_with_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Swarm on case with team Scheduled Email Brief — Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_swarm_on_case_with_team',
    "version": '3.0.3',
    "display_name": 'Swarm on case with team Scheduled Email Brief',
    "description": 'Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-swarm-on-case-with-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-swarm-on-case-with-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '527abf491f9b27b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/swarm-on-case-with-team'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-swarm-on-case-with-team', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where swarm on case with team stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on swarm on case with team for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads swarm on case with team, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary.', 'example_request': 'Give me the 7am weekday swarm-on-case brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a case-swarm owner wants a recurring daily or weekly morning brief with an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefSwarmOnCaseWithTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSwarmOnCaseWithTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefSwarmOnCaseWithTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
