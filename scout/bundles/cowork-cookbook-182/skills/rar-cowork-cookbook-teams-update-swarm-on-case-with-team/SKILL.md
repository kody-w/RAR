---
name: "rar-cowork-cookbook-teams-update-swarm-on-case-with-team"
description: "Summarizes swarm-on-case-with-team status from the Dynamics 365 ERP plugin for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_swarm_on_case_with_team", "rar_sha256": "d46ee9182427339479a21a918faa4da9c3a2a627826cc4a1cf3578adcd156566", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
