---
name: "rar-cowork-cookbook-research-and-insights-alignment-recap"
description: "Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/research_and_insights_alignment_recap", "rar_sha256": "4b8c0f371d4928a2871f5e23128a7a561e29fb6cd9df6c8bbcc977b9195dd25b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/research_and_insights_alignment_recap`. The original RAPP
agent is preserved byte-for-byte in `research_and_insights_alignment_recap_agent.py` and in the RCI capsule.

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

Research and insights alignment recap — Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner.

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
  Upstream entry : https://coworkcookbook.com/recipes/research-and-insights-alignment-recap
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
    "research_project": {
      "description": "Name of the research project whose debrief sessions should be reviewed.",
      "type": "string"
    },
    "team_channel": {
      "description": "Teams channel to read discussions from and to post the drafted recap to for review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `research_and_insights_alignment_recap_agent.py` and embedded as the fenced Python below (sha256 4b8c0f371d4928a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `research_and_insights_alignment_recap_agent.py` first:

```bash
python3 research_and_insights_alignment_recap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 research_and_insights_alignment_recap_agent.py   # or on stdin
python3 research_and_insights_alignment_recap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research and insights alignment recap — Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner.

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
  Upstream entry : https://coworkcookbook.com/recipes/research-and-insights-alignment-recap
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/research_and_insights_alignment_recap',
    "version": '3.0.3',
    "display_name": 'Research and insights alignment recap',
    "description": "Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'read_only'],
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
        "upstream_slug": 'research-and-insights-alignment-recap',
        "upstream_url": 'https://coworkcookbook.com/recipes/research-and-insights-alignment-recap',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '037ac8078e4159c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/research-and-insights-alignment-recap', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A Teams post recapping decisions made, open issues, and named next steps - posted to the team channel so everyone walks into next week aligned.'], 'confidence': 1.0, 'deliverable': 'A Teams post recapping decisions made, open issues, and named next steps - posted to the team channel so everyone walks into next week aligned.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'research_project': 'Name of the research project whose debrief sessions should be reviewed.', 'team_channel': 'Teams channel to read discussions from and to post the drafted recap to for review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Surface everything that came out of this week's research sessions - what landed, what didn't, and what still needs an owner. A Teams post recapping decisions made, open issues, and named next steps - posted to the team channel so everyone walks into next week aligned.", 'expected_output': 'A Teams post recapping decisions made, open issues, and named next steps - posted to the team channel so everyone walks into next week aligned.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "After this week's [Research project] debrief - the findings readout, the messaging review, and the implications discussion - pull everything together into one clear picture of where things stand.\n\nRead across the meeting transcripts from those sessions, the [Team channel] discussions tied to the research, and the email threads that followed. Tell me what was decided, what's still open, and what needs a named owner before next week.\n\nDraft a recap to [Team channel] for the group for my review.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Teams post recapping decisions made, open issues, and named next steps - posted to the team channel so everyone walks into next week aligned.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner.", 'example_request': "Recap this week's Onboarding Research debrief and draft a post for the UX Research channel.", 'inputs': [{'description': 'Name of the research project whose debrief sessions should be reviewed.', 'name': 'research_project'}, {'description': 'Teams channel to read discussions from and to post the drafted recap to for review.', 'name': 'team_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call after a week of research sessions (findings readout, messaging review, implications discussion) when you need one aligned recap drafted for a team channel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ResearchAndInsightsAlignmentRecap(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ResearchAndInsightsAlignmentRecap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'research_project': {'description': 'Name of the research project whose debrief sessions should be reviewed.', 'type': 'string'}, 'team_channel': {'description': 'Teams channel to read discussions from and to post the drafted recap to for review.', 'type': 'string'}},
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
    print(ResearchAndInsightsAlignmentRecap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
