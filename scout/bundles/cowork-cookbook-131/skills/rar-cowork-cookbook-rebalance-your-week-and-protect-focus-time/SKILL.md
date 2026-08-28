---
name: "rar-cowork-cookbook-rebalance-your-week-and-protect-focus-time"
description: "Take control of a fragmented calendar before it takes control of your week."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/rebalance_your_week_and_protect_focus_time", "rar_sha256": "30277545414dd92cf18a6e6b5ec2677a579d4fa171adca8cfa9a277a47f5c4fe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
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

Rebalance your week and protect focus time — Take control of a fragmented calendar before it takes control of your week.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rebalance_your_week_and_protect_focus_time_agent.py` and embedded as the fenced Python below (sha256 30277545414dd92c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rebalance_your_week_and_protect_focus_time_agent.py` first:

```bash
python3 rebalance_your_week_and_protect_focus_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rebalance_your_week_and_protect_focus_time_agent.py   # or on stdin
python3 rebalance_your_week_and_protect_focus_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rebalance your week and protect focus time — Take control of a fragmented calendar before it takes control of your week.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Rebalance your week and protect focus time',
    "description": 'Take control of a fragmented calendar before it takes control of your week.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72697aaa2d36b418',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


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
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
