---
name: "rar-cowork-cookbook-rebalance-your-week-and-protect-focus-time"
description: "Take control of a fragmented calendar before it takes control of your week."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/rebalance_your_week_and_protect_focus_time", "rar_sha256": "a1570e97b55813c2048f18ff7bd91bc5a04cd39c25173b90bd208b0f5351ea15", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rebalance_your_week_and_protect_focus_time_agent.py` and embedded as the fenced Python below (sha256 a1570e97b55813c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rebalance_your_week_and_protect_focus_time_agent.py` first:

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
    "version": '2.0.1',
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
