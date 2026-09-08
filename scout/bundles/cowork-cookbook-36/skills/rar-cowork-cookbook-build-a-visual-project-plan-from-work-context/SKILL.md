---
name: "rar-cowork-cookbook-build-a-visual-project-plan-from-work-context"
description: "Reviews your emails, meetings, and files from a recent time window to identify workstreams, milestones, and dependencies, then builds a Miro board timeline or swim lane plus a summary data table."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_visual_project_plan_from_work_context", "rar_sha256": "edcfe7bfc9eb651ca7eaa60b30a1e7fe350299b1d91ecc096f6a076ee063e0e8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "miro"]}
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
