---
name: "rar-cowork-cookbook-automate-recurring-project-reporting"
description: "Sets up a recurring bi-weekly project status update in Microsoft 365 Copilot Cowork that pulls from a monday.com board and drafts an update covering health, completed tasks, upcoming deadlines, and blockers for a stakeho"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/automate_recurring_project_reporting", "rar_sha256": "38f198377f37a2e2241dc9c968bc1ca49359484af240ac875643e3c7b262bd47", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "advanced", "integration", "monday_com"]}
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
