---
name: "rar-cowork-cookbook-scheduled-brief-swarm-on-case-with-team"
description: "Builds a morning brief on swarm-on-case-with-team from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs 7-day average, next actions, a saved email draft, and a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_swarm_on_case_with_team", "rar_sha256": "c145dbffd83bd0d641158324e5d4afe31a3f1e5650795c42226a19fcee54e684", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
