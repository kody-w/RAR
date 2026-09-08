---
name: "rar-cowork-cookbook-teams-update-plan-workforce"
description: "Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_workforce", "rar_sha256": "606fe6d44e13f8484d8609a25dc8f15409e8fa2722f069cfc5fc0a9851bc8780", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_workforce`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_workforce_agent.py` and in the RCI capsule.

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

Plan workforce Teams Channel Update — Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-plan-workforce-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 606fe6d44e13f848…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_workforce_agent.py` first:

```bash
python3 teams_update_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_workforce_agent.py   # or on stdin
python3 teams_update_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Teams Channel Update — Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_workforce',
    "version": '3.0.3',
    "display_name": 'Plan workforce Teams Channel Update',
    "description": 'Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted.',
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
        "upstream_slug": 'teams-update-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b855493a6429192c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-plan-workforce-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of plan workforce. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-plan-workforce-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan workforce, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted.', 'example_request': "Draft a Teams post and Adaptive Card on plan workforce status in USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-plan-workforce-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reviewable Teams channel update on plan workforce status from D365 ERP data, with an Adaptive Card artifact they will post themselves.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePlanWorkforce(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanWorkforce'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-plan-workforce-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
