---
name: "rar-cowork-cookbook-weekly-marketing-standup-prep"
description: "Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_marketing_standup_prep", "rar_sha256": "6dcf33774c2eb321986fa54608b5ad371c62b69880e2467d4eb773847179021c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "beginner", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/weekly_marketing_standup_prep`. The original RAPP
agent is preserved byte-for-byte in `weekly_marketing_standup_prep_agent.py` and in the RCI capsule.

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

Weekly marketing standup prep — Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top.

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
  Upstream entry : https://coworkcookbook.com/recipes/weekly-marketing-standup-prep
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
    "team_channel": {
      "description": "The Teams channel whose past 7 days of chatter should be reviewed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_marketing_standup_prep_agent.py` and embedded as the fenced Python below (sha256 6dcf33774c2eb321…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_marketing_standup_prep_agent.py` first:

```bash
python3 weekly_marketing_standup_prep_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 weekly_marketing_standup_prep_agent.py   # or on stdin
python3 weekly_marketing_standup_prep_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Weekly marketing standup prep — Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top.

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
  Upstream entry : https://coworkcookbook.com/recipes/weekly-marketing-standup-prep
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/weekly_marketing_standup_prep',
    "version": '3.0.3',
    "display_name": 'Weekly marketing standup prep',
    "description": 'Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'beginner', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'weekly-marketing-standup-prep',
        "upstream_url": 'https://coworkcookbook.com/recipes/weekly-marketing-standup-prep',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b78913e0373e508',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/weekly-marketing-standup-prep', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A Word standup brief - campaign progress, blockers, decisions, owner updates, and a live campaign performance read from Fabric IQ - ready to share at the meeting.'], 'confidence': 1.0, 'deliverable': 'A Word standup brief - campaign progress, blockers, decisions, owner updates, and a live campaign performance read from Fabric IQ - ready to share at the meeting.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'team_channel': 'The Teams channel whose past 7 days of chatter should be reviewed.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Walk into Monday's standup with progress, blockers, owner updates, and live campaign performance already in front of you. A Word standup brief - campaign progress, blockers, decisions, owner updates, and a live campaign performance read from Fabric IQ - ready to share at the meeting.", 'expected_output': 'A Word standup brief - campaign progress, blockers, decisions, owner updates, and a live campaign performance read from Fabric IQ - ready to share at the meeting.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "Before this week's marketing standup, put together a quick read on where every active campaign actually is.\n\nWalk through the past 7 days of [Team channel] chatter and any marketing email threads that decided something, then check the standup invite for who's attending.\n\nPull live campaign performance from Fabric - what moved week-over-week, what's underperforming, and where the signal is strongest.\n\nGroup what you find by active campaign and pull cross-cutting blockers into their own section at the top. Deliver a Word standup brief I can drop into the meeting.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word standup brief - campaign progress, blockers, decisions, owner updates, and a live campaign performance read from Fabric IQ - ready to share at the meeting.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top.', 'example_request': 'Prep my marketing standup brief from the #growth channel and Fabric campaign numbers.', 'inputs': [{'description': 'The Teams channel whose past 7 days of chatter should be reviewed.', 'name': 'team_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call before a weekly marketing standup when you need campaign progress, blockers, decisions, owner updates, and week-over-week performance in one document.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class WeeklyMarketingStandupPrep(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WeeklyMarketingStandupPrep'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'team_channel': {'description': 'The Teams channel whose past 7 days of chatter should be reviewed.', 'type': 'string'}},
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
    print(WeeklyMarketingStandupPrep().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
