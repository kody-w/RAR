---
name: "rar-cowork-cookbook-teams-update-conduct-succession-planning"
description: "Summarizes conduct succession planning status from Dynamics 365 ERP for a given legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON for review; call when you need that update drafted, not posted"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_succession_planning", "rar_sha256": "e6219b012ce43d296217cb467c2663a8bd51d5993f30efb7809465ae67a09de8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
