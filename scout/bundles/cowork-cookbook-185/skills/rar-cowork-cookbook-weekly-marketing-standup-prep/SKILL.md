---
name: "rar-cowork-cookbook-weekly-marketing-standup-prep"
description: "Compiles a Word standup brief for a weekly marketing standup: last 7 days of team channel and email decisions, standup invite attendees, and live Fabric IQ campaign performance, grouped by campaign with blockers on top."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_marketing_standup_prep", "rar_sha256": "6dcf33774c2eb321986fa54608b5ad371c62b69880e2467d4eb773847179021c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "beginner", "integration", "fabric_iq"]}
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
