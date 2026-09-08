---
name: "rar-cowork-cookbook-build-a-visual-project-plan-from-work-context"
description: "Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_visual_project_plan_from_work_context", "rar_sha256": "edcfe7bfc9eb651ca7eaa60b30a1e7fe350299b1d91ecc096f6a076ee063e0e8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_visual_project_plan_from_work_context`. The original RAPP
agent is preserved byte-for-byte in `build_a_visual_project_plan_from_work_context_agent.py` and in the RCI capsule.

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

Build a visual project plan from work context — Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context
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
      "description": "How many weeks of emails, meetings, and files to review.",
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
      "description": "Name of the project being started.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_visual_project_plan_from_work_context_agent.py` and embedded as the fenced Python below (sha256 edcfe7bfc9eb651c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_visual_project_plan_from_work_context_agent.py` first:

```bash
python3 build_a_visual_project_plan_from_work_context_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_visual_project_plan_from_work_context_agent.py   # or on stdin
python3 build_a_visual_project_plan_from_work_context_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a visual project plan from work context — Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table.

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_visual_project_plan_from_work_context',
    "version": '3.0.3',
    "display_name": 'Build a visual project plan from work context',
    "description": 'Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'integration', 'miro'],
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
        "upstream_slug": 'build-a-visual-project-plan-from-work-context',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5901ab2e79f619a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/build-project-plans'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-a-visual-project-plan-from-work-context', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A Miro board that maps the project end-to-end, with workstreams, milestones, and ownership visualized in one place - paired with a tracking table the team can update as work moves forward.'], 'confidence': 1.0, 'deliverable': 'A Miro board that maps the project end-to-end, with workstreams, milestones, and ownership visualized in one place - paired with a tracking table the team can update as work moves forward.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'lookback_weeks': 'How many weeks of emails, meetings, and files to review.', 'project_name': 'Name of the project being started.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch. A Miro board that maps the project end-to-end, with workstreams, milestones, and ownership visualized in one place - paired with a tracking table the team can update as work moves forward.', 'expected_output': 'A Miro board that maps the project end-to-end, with workstreams, milestones, and ownership visualized in one place - paired with a tracking table the team can update as work moves forward.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': "I'm starting [Project name]. Review my emails, meetings, and files from the past [X weeks] to identify the key workstreams, milestones, and dependencies.\n\nThen build a Miro board that visualizes the project plan as a timeline or swim lane diagram, including owners and due dates.\n\nOnce the board is built, add a Miro data table beneath the timeline summarizing each workstream with columns for owner, milestone, due date, and status.\n\nPre-fill what you can infer from the source materials.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Miro board that maps the project end-to-end, with workstreams, milestones, and ownership visualized in one place - paired with a tracking table the team can update as work moves forward.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table.', 'example_request': 'Build a Miro project plan for Project Atlas from my emails, meetings, and files from the last 6 weeks.', 'inputs': [{'description': 'Name of the project being started.', 'name': 'project_name'}, {'description': 'How many weeks of emails, meetings, and files to review.', 'name': 'lookback_weeks'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when kicking off a project and you want a visual Miro project plan and tracking table built from existing M365 work context instead of from scratch.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildAVisualProjectPlanFromWorkContext(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAVisualProjectPlanFromWorkContext'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'lookback_weeks': {'description': 'How many weeks of emails, meetings, and files to review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'project_name': {'description': 'Name of the project being started.', 'type': 'string'}},
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
    print(BuildAVisualProjectPlanFromWorkContext().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
