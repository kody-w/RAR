---
name: "rar-cowork-cookbook-rebalance-your-week-and-protect-focus-time"
description: "Reviews your Outlook calendar for the week, summarizes meeting load and focus time, then proposes and \u2014 after your approval \u2014 applies accept/decline/reschedule and focus-block changes one at a time."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/rebalance_your_week_and_protect_focus_time", "rar_sha256": "19b3c5ab3a68b369f1643e86fc2fe953b565876781e125c5a2dad3e5451ca6cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
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
