---
name: "rar-cowork-cookbook-teams-update-swarm-on-case-with-team"
description: "Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_swarm_on_case_with_team", "rar_sha256": "d46ee9182427339479a21a918faa4da9c3a2a627826cc4a1cf3578adcd156566", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_swarm_on_case_with_team`. The original RAPP
agent is preserved byte-for-byte in `teams_update_swarm_on_case_with_team_agent.py` and in the RCI capsule.

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

Swarm on case with team Teams Channel Update — Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
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
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON, e.g. teams-update-swarm-on-case-with-team-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_swarm_on_case_with_team_agent.py` and embedded as the fenced Python below (sha256 d46ee91824273394…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_swarm_on_case_with_team_agent.py` first:

```bash
python3 teams_update_swarm_on_case_with_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_swarm_on_case_with_team_agent.py   # or on stdin
python3 teams_update_swarm_on_case_with_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Swarm on case with team Teams Channel Update — Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_swarm_on_case_with_team',
    "version": '3.0.3',
    "display_name": 'Swarm on case with team Teams Channel Update',
    "description": 'Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-swarm-on-case-with-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-swarm-on-case-with-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '781bd1931bef517d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/swarm-on-case-with-team'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-swarm-on-case-with-team', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, e.g. teams-update-swarm-on-case-with-team-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of swarm on case with team. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-swarm-on-case-with-team-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads swarm on case with team, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not', 'example_request': "Draft a Teams post and Adaptive Card on swarm on case with team status from D365 USMF — don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-swarm-on-case-with-team-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update and Adaptive Card on swarm-on-case-with-team status from D365 F&SCM data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateSwarmOnCaseWithTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSwarmOnCaseWithTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, e.g. teams-update-swarm-on-case-with-team-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateSwarmOnCaseWithTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
