---
name: "rar-cowork-cookbook-find-patterns-across-your-meetings"
description: "Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_patterns_across_your_meetings", "rar_sha256": "4b1112720678d85a0b97fb5b33fd7f0df76b4daf9a974494a73c64c3ee6541e7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_patterns_across_your_meetings`. The original RAPP
agent is preserved byte-for-byte in `find_patterns_across_your_meetings_agent.py` and in the RCI capsule.

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

Find patterns across your meetings — Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action.

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
  Upstream entry : https://coworkcookbook.com/recipes/find-patterns-across-your-meetings
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
    "meeting_type": {
      "description": "Which meetings to look across, e.g. customer calls, team standups, partner reviews.",
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
    "theme_types": {
      "description": "Optional kinds of themes to rank, e.g. objections, feature requests, blockers, decisions, concerns.",
      "type": "string"
    },
    "time_window": {
      "description": "The period to cover, e.g. the last 30 days.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_patterns_across_your_meetings_agent.py` and embedded as the fenced Python below (sha256 4b1112720678d85a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_patterns_across_your_meetings_agent.py` first:

```bash
python3 find_patterns_across_your_meetings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_patterns_across_your_meetings_agent.py   # or on stdin
python3 find_patterns_across_your_meetings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find patterns across your meetings — Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action.

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
  Upstream entry : https://coworkcookbook.com/recipes/find-patterns-across-your-meetings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_patterns_across_your_meetings',
    "version": '3.0.3',
    "display_name": 'Find patterns across your meetings',
    "description": 'Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
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
        "upstream_slug": 'find-patterns-across-your-meetings',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-patterns-across-your-meetings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51191ed0dabd2cd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/analyze-collaboration-patterns'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/find-patterns-across-your-meetings', 'uses_skills': {'custom': [], 'ootb': ['Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A pattern report identifying the most common themes across your recent meetings, with representative quotes, the meetings where each came up, and a recommended action for each.'], 'confidence': 1.0, 'deliverable': 'A pattern report identifying the most common themes across your recent meetings, with representative quotes, the meetings where each came up, and a recommended action for each.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'meeting_type': 'Which meetings to look across, e.g. customer calls, team standups, partner reviews.', 'theme_types': 'Optional kinds of themes to rank, e.g. objections, feature requests, blockers, decisions, concerns.', 'time_window': 'The period to cover, e.g. the last 30 days.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory. A pattern report identifying the most common themes across your recent meetings, with representative quotes, the meetings where each came up, and a recommended action for each.', 'expected_output': 'A pattern report identifying the most common themes across your recent meetings, with representative quotes, the meetings where each came up, and a recommended action for each.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "Use TeamsMaestro to look across all my [meeting type - e.g., customer calls, team standups, partner reviews] from [time window - e.g., the last 30 days] and tell me what's coming up most.\n\nIdentify the top recurring themes - [examples: objections, feature requests, blockers, decisions, concerns] - and rank them by how often they appear.\n\nFor each theme, give me a 1-2 sentence summary, two or three representative quotes from the meetings, the meetings where the theme surfaced, and a recommended action I should take.\n\nDeliver it as a structured pattern report I can act on.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A pattern report identifying the most common themes across your recent meetings, with representative quotes, the meetings where each came up, and a recommended action for each.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action.', 'example_request': 'Look across my customer calls from the last 30 days and tell me the top recurring themes with quotes and actions.', 'inputs': [{'description': 'Which meetings to look across, e.g. customer calls, team standups, partner reviews.', 'name': 'meeting_type'}, {'description': 'The period to cover, e.g. the last 30 days.', 'name': 'time_window'}, {'description': 'Optional kinds of themes to rank, e.g. objections, feature requests, blockers, decisions, concerns.', 'name': 'theme_types'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants to know what themes, objections, requests, blockers or decisions keep repeating across their recent meetings without re-reading transcripts.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FindPatternsAcrossYourMeetings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindPatternsAcrossYourMeetings'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'meeting_type': {'description': 'Which meetings to look across, e.g. customer calls, team standups, partner reviews.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'theme_types': {'description': 'Optional kinds of themes to rank, e.g. objections, feature requests, blockers, decisions, concerns.', 'type': 'string'}, 'time_window': {'description': 'The period to cover, e.g. the last 30 days.', 'type': 'string'}},
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
    print(FindPatternsAcrossYourMeetings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
