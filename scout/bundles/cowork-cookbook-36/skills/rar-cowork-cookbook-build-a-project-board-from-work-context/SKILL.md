---
name: "rar-cowork-cookbook-build-a-project-board-from-work-context"
description: "Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_project_board_from_work_context", "rar_sha256": "8cd82b69f908fda7e0daa99d82cbae515e735e140ecf7fb6b9bbeb1841dfaa81", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_project_board_from_work_context`. The original RAPP
agent is preserved byte-for-byte in `build_a_project_board_from_work_context_agent.py` and in the RCI capsule.

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

Build a project board from work context — Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
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
    "lookback_weeks": {
      "description": "How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.",
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
      "description": "Name of the project being kicked off.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_project_board_from_work_context_agent.py` and embedded as the fenced Python below (sha256 8cd82b69f908fda7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_project_board_from_work_context_agent.py` first:

```bash
python3 build_a_project_board_from_work_context_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_project_board_from_work_context_agent.py   # or on stdin
python3 build_a_project_board_from_work_context_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a project board from work context — Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_project_board_from_work_context',
    "version": '3.0.3',
    "display_name": 'Build a project board from work context',
    "description": 'Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'build-a-project-board-from-work-context',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-project-board-from-work-context',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27367604374329b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/set-up-project-boards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-a-project-board-from-work-context', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.'], 'confidence': 1.0, 'deliverable': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'lookback_weeks': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'project_name': 'Name of the project being kicked off.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads. A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'expected_output': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': 'I need to kick off [Project name]. Review my emails, Teams conversations, and any related files from the past [X weeks] to understand the scope, stakeholders, and outstanding tasks.\n\nThen build a Monday.com board with the following structure: project name, task owner, status, due date, and priority.\n\nGroup tasks by workstream.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A ready-to-run Monday.com board grounded in your actual work - with owners, statuses, and priorities already in place so the team can pick it up and move.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews your recent emails, Teams conversations, and related files for a named project, then builds a monday.com board with project name, task owner, status, due date, and priority, grouped by workstream.', 'example_request': 'Kick off Project Atlas — review my last 4 weeks of email and Teams and build a monday.com board grouped by workstream.', 'inputs': [{'description': 'Name of the project being kicked off.', 'name': 'project_name'}, {'description': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'name': 'lookback_weeks'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when kicking off a project and you want a monday.com board scoped from your recent work context instead of assembling tasks manually.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildAProjectBoardFromWorkContext(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAProjectBoardFromWorkContext'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'lookback_weeks': {'description': 'How many weeks of emails, Teams chats, and files to review for scope, stakeholders, and tasks.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_name': {'description': 'Name of the project being kicked off.', 'type': 'string'}},
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
    print(BuildAProjectBoardFromWorkContext().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
