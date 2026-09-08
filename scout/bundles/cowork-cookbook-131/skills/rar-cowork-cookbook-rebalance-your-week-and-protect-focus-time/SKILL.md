---
name: "rar-cowork-cookbook-rebalance-your-week-and-protect-focus-time"
description: "Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and \u2014 after your approval \u2014 applies accept/decline/reschedule and focus-block changes one at a time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/rebalance_your_week_and_protect_focus_time", "rar_sha256": "19b3c5ab3a68b369f1643e86fc2fe953b565876781e125c5a2dad3e5451ca6cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/rebalance_your_week_and_protect_focus_time`. The original RAPP
agent is preserved byte-for-byte in `rebalance_your_week_and_protect_focus_time_agent.py` and in the RCI capsule.

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

Rebalance your week and protect focus time — Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and — after your approval — applies accept/decline/reschedule and focus-block changes one at a time.

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
  Upstream entry : https://coworkcookbook.com/recipes/rebalance-your-week-and-protect-focus-time
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
    "conflict_priorities": {
      "description": "How to prioritize when two meetings overlap.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "manager_and_management_chain": {
      "description": "Who your manager and management chain are, so meetings involving them can be flagged.",
      "type": "string"
    },
    "meetings_to_decline_or_shorten": {
      "description": "Specific meetings you already want declined or shortened.",
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
    "personal_commitments": {
      "description": "Personal time blocks that must stay protected.",
      "type": "string"
    },
    "weekly_goals": {
      "description": "What you are trying to accomplish this week, used to rank meeting importance.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rebalance_your_week_and_protect_focus_time_agent.py` and embedded as the fenced Python below (sha256 19b3c5ab3a68b369…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rebalance_your_week_and_protect_focus_time_agent.py` first:

```bash
python3 rebalance_your_week_and_protect_focus_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rebalance_your_week_and_protect_focus_time_agent.py   # or on stdin
python3 rebalance_your_week_and_protect_focus_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rebalance your week and protect focus time — Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and — after your approval — applies accept/decline/reschedule and focus-block changes one at a time.

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
  Upstream entry : https://coworkcookbook.com/recipes/rebalance-your-week-and-protect-focus-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/rebalance_your_week_and_protect_focus_time',
    "version": '3.0.3',
    "display_name": 'Rebalance your week and protect focus time',
    "description": 'Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and — after your approval — applies accept/decline/reschedule and focus-block changes one at a time.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'rebalance-your-week-and-protect-focus-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/rebalance-your-week-and-protect-focus-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eacf2b385b6d8d44',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/plan-and-prioritize-work/manage-time-and-focus'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/rebalance-your-week-and-protect-focus-time', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A rebalanced schedule that protects focus time, prioritizes high-impact meetings, and resolves conflicts - without manually negotiating your own availability.'], 'confidence': 1.0, 'deliverable': 'A rebalanced schedule that protects focus time, prioritizes high-impact meetings, and resolves conflicts - without manually negotiating your own availability.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'conflict_priorities': 'How to prioritize when two meetings overlap.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'manager_and_management_chain': 'Who your manager and management chain are, so meetings involving them can be flagged.', 'meetings_to_decline_or_shorten': 'Specific meetings you already want declined or shortened.', 'personal_commitments': 'Personal time blocks that must stay protected.', 'weekly_goals': 'What you are trying to accomplish this week, used to rank meeting importance.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Take control of a fragmented calendar before it takes control of your week. A rebalanced schedule that protects focus time, prioritizes high-impact meetings, and resolves conflicts - without manually negotiating your own availability.', 'expected_output': 'A rebalanced schedule that protects focus time, prioritizes high-impact meetings, and resolves conflicts - without manually negotiating your own availability.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "Help me organize my week. Review my Outlook calendar.\n\nFirst, show me a summary: Total meetings and hours spent, where I have focus time (2+ hours), and days with the most meetings.\n\nBefore taking changes, ask clarifying questions: my manager and management chain - note if they are on a meeting, how many attendees, what I'm trying to accomplish this week, how to prioritize conflicts, personal commitments, and which meetings to decline or shorten.\n\nThen show proposed changes with explanations: meetings to accept/decline/reschedule, conflicts to resolve (including emailing organizers), and focus blocks to add. Start with highest-impact changes first.\n\nOnce I approve each change, make edits directly in my calendar one at a time.\n\nFollow-up prompts: Accept and decline meetings. Create a customer meeting prep document.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A rebalanced schedule that protects focus time, prioritizes high-impact meetings, and resolves conflicts - without manually negotiating your own availability.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and — after your approval — applies accept/decline/reschedule and focus-block changes one at a time.', 'example_request': 'Help me organize my week — review my Outlook calendar and protect focus time.', 'inputs': [{'description': 'Who your manager and management chain are, so meetings involving them can be flagged.', 'name': 'manager_and_management_chain'}, {'description': 'What you are trying to accomplish this week, used to rank meeting importance.', 'name': 'weekly_goals'}, {'description': 'How to prioritize when two meetings overlap.', 'name': 'conflict_priorities'}, {'description': 'Personal time blocks that must stay protected.', 'name': 'personal_commitments'}, {'description': 'Specific meetings you already want declined or shortened.', 'name': 'meetings_to_decline_or_shorten'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when your week is fragmented with meetings and you want a calendar summary plus approved edits that protect focus time and resolve conflicts.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class RebalanceYourWeekAndProtectFocusTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RebalanceYourWeekAndProtectFocusTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'conflict_priorities': {'description': 'How to prioritize when two meetings overlap.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'manager_and_management_chain': {'description': 'Who your manager and management chain are, so meetings involving them can be flagged.', 'type': 'string'}, 'meetings_to_decline_or_shorten': {'description': 'Specific meetings you already want declined or shortened.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'personal_commitments': {'description': 'Personal time blocks that must stay protected.', 'type': 'string'}, 'weekly_goals': {'description': 'What you are trying to accomplish this week, used to rank meeting importance.', 'type': 'string'}},
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
    print(RebalanceYourWeekAndProtectFocusTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
