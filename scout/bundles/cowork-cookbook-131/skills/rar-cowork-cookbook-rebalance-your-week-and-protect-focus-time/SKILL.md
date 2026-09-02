---
name: "rar-cowork-cookbook-rebalance-your-week-and-protect-focus-time"
description: "Take control of a fragmented calendar before it takes control of your week."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/rebalance_your_week_and_protect_focus_time", "rar_sha256": "30277545414dd92cf18a6e6b5ec2677a579d4fa171adca8cfa9a277a47f5c4fe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rebalance_your_week_and_protect_focus_time_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/rebalance-your-week-and-protect-focus-time:422a3a7be27a0fa2a18cf427c5121ff790e67da3dfb31bec6da23a45434b1781", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/rebalance_your_week_and_protect_focus_time`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rebalance_your_week_and_protect_focus_time_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
