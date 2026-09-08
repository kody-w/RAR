---
name: "rar-cowork-cookbook-automate-recurring-project-reporting"
description: "Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/automate_recurring_project_reporting", "rar_sha256": "38f198377f37a2e2241dc9c968bc1ca49359484af240ac875643e3c7b262bd47", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "advanced", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/automate_recurring_project_reporting`. The original RAPP
agent is preserved byte-for-byte in `automate_recurring_project_reporting_agent.py` and in the RCI capsule.

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

Automate recurring project reporting — Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho

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
  Upstream entry : https://coworkcookbook.com/recipes/automate-recurring-project-reporting
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
    "cadence": {
      "description": "Delivery schedule, e.g. every other Monday (bi-weekly).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "monday_board": {
      "description": "The monday.com board to pull task and status data from.",
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
    "project_name": {
      "description": "Name of the project the status update covers.",
      "type": "string"
    },
    "recipients": {
      "description": "Stakeholder or distribution list the update is sent to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `automate_recurring_project_reporting_agent.py` and embedded as the fenced Python below (sha256 38f198377f37a2e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `automate_recurring_project_reporting_agent.py` first:

```bash
python3 automate_recurring_project_reporting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 automate_recurring_project_reporting_agent.py   # or on stdin
python3 automate_recurring_project_reporting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Automate recurring project reporting — Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho

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
  Upstream entry : https://coworkcookbook.com/recipes/automate-recurring-project-reporting
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/automate_recurring_project_reporting',
    "version": '3.0.3',
    "display_name": 'Automate recurring project reporting',
    "description": 'Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'work_management', 'advanced', 'integration', 'monday_com'],
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
        "upstream_slug": 'automate-recurring-project-reporting',
        "upstream_url": 'https://coworkcookbook.com/recipes/automate-recurring-project-reporting',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22ac98ad8c1e46d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/automate-recurring-reporting'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'work-management/automate-recurring-project-reporting', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A recurring stakeholder update - drafted from real board data and delivered on cadence - so progress, risks, and deadlines stay visible without anyone chasing them.'], 'confidence': 1.0, 'deliverable': 'A recurring stakeholder update - drafted from real board data and delivered on cadence - so progress, risks, and deadlines stay visible without anyone chasing them.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'cadence': 'Delivery schedule, e.g. every other Monday (bi-weekly).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'monday_board': 'The monday.com board to pull task and status data from.', 'project_name': 'Name of the project the status update covers.', 'recipients': 'Stakeholder or distribution list the update is sent to.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replace the manual "pull the board, write the update, send it out" Monday-morning cycle with a status update that writes and sends itself. A recurring stakeholder update - drafted from real board data and delivered on cadence - so progress, risks, and deadlines stay visible without anyone chasing them.', 'expected_output': 'A recurring stakeholder update - drafted from real board data and delivered on cadence - so progress, risks, and deadlines stay visible without anyone chasing them.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': 'Set up a recurring bi-weekly status update for [Project name] that pulls from my [Monday.com board].\n\nEach update should highlight: Overall project health, tasks completed since last update, upcoming deadlines in the next two weeks, and any blockers or risks.\n\nDraft the update and send it to [stakeholder/distribution list] every other Monday.\n\nCreate a skill so this runs automatically.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A recurring stakeholder update - drafted from real board data and delivered on cadence - so progress, risks, and deadlines stay visible without anyone chasing them.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho', 'example_request': 'Set up a bi-weekly status update for Project Atlas from my monday.com board and send it to the leadership list.', 'inputs': [{'description': 'Name of the project the status update covers.', 'name': 'project_name'}, {'description': 'The monday.com board to pull task and status data from.', 'name': 'monday_board'}, {'description': 'Stakeholder or distribution list the update is sent to.', 'name': 'recipients'}, {'description': 'Delivery schedule, e.g. every other Monday (bi-weekly).', 'name': 'cadence'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a repeating project status update drafted from their monday.com board and sent to stakeholders on a set cadence instead of written by hand.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AutomateRecurringProjectReporting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AutomateRecurringProjectReporting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'cadence': {'description': 'Delivery schedule, e.g. every other Monday (bi-weekly).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'monday_board': {'description': 'The monday.com board to pull task and status data from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_name': {'description': 'Name of the project the status update covers.', 'type': 'string'}, 'recipients': {'description': 'Stakeholder or distribution list the update is sent to.', 'type': 'string'}},
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
    print(AutomateRecurringProjectReporting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
