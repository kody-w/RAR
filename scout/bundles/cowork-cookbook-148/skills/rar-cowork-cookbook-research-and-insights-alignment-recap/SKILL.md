---
name: "rar-cowork-cookbook-research-and-insights-alignment-recap"
description: "Reads meeting transcripts, team channel discussions, and email threads from a research project's debrief sessions and returns a draft Teams recap of decisions made, open issues, and items needing a named owner."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/research_and_insights_alignment_recap", "rar_sha256": "4b8c0f371d4928a2871f5e23128a7a561e29fb6cd9df6c8bbcc977b9195dd25b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
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
