---
name: "rar-cowork-cookbook-teams-update-define-queues-and-teams"
description: "Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_queues_and_teams", "rar_sha256": "d4c7d73d50d3c176afcbf116894222f870e75ebb8a6b31998a17eb3ddc09f9f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Teams Channel Update — Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 d4c7d73d50d3c176…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_queues_and_teams_agent.py` first:

```bash
python3 teams_update_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_queues_and_teams_agent.py   # or on stdin
python3 teams_update_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Teams Channel Update — Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_queues_and_teams',
    "version": '3.0.3',
    "display_name": 'Define queues and teams Teams Channel Update',
    "description": 'Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons',
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
        "upstream_slug": 'teams-update-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '662875b2de9feb84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define queues and teams. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-queues-and-teams-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define queues and teams, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define queues and teams from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons', 'example_request': "Draft a Teams update on define queues and teams for USMF with an Adaptive Card — don't post it, just save the files.", 'inputs': [{'description': 'D365 legal entity to report against (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on define queues and teams status from D365 ERP data, without auto-posting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineQueuesAndTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineQueuesAndTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-queues-and-teams-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
