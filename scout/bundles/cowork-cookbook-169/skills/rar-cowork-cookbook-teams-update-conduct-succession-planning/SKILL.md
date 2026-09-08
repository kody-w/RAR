---
name: "rar-cowork-cookbook-teams-update-conduct-succession-planning"
description: "Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_succession_planning", "rar_sha256": "e6219b012ce43d296217cb467c2663a8bd51d5993f30efb7809465ae67a09de8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_succession_planning`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_succession_planning_agent.py` and in the RCI capsule.

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

Conduct succession planning Teams Channel Update — Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-conduct-succession-planning-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 e6219b012ce43d29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_succession_planning_agent.py` first:

```bash
python3 teams_update_conduct_succession_planning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_succession_planning_agent.py   # or on stdin
python3 teams_update_conduct_succession_planning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct succession planning Teams Channel Update — Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_succession_planning',
    "version": '3.0.3',
    "display_name": 'Conduct succession planning Teams Channel Update',
    "description": 'Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-succession-planning',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-succession-planning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '524afdf07b876a42',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-succession-planning'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-conduct-succession-planning', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-conduct-succession-planning-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of conduct succession planning. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-conduct-succession-planning-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct succession planning, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted', 'example_request': "Draft a Teams update on conduct succession planning from D365 USMF with an Adaptive Card — save it, don't post.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-conduct-succession-planning-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you want a reviewable Teams channel update on conduct succession planning status, with KPIs and quick-action buttons, sourced from D365 F&SCM.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateConductSuccessionPlanning(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductSuccessionPlanning'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-conduct-succession-planning-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateConductSuccessionPlanning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
