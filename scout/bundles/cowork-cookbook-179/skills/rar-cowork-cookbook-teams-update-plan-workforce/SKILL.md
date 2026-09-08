---
name: "rar-cowork-cookbook-teams-update-plan-workforce"
description: "Summarizes plan workforce status from Dynamics 365 F&SCM for a given legal entity and returns a markdown Teams channel post plus an Adaptive Card JSON file of KPIs and quick-action buttons, saved not posted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_workforce", "rar_sha256": "606fe6d44e13f8484d8609a25dc8f15409e8fa2722f069cfc5fc0a9851bc8780", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
