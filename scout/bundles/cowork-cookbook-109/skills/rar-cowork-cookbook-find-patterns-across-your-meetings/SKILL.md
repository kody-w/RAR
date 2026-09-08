---
name: "rar-cowork-cookbook-find-patterns-across-your-meetings"
description: "Returns a ranked pattern report across a set of your meetings: top recurring themes, a 1-2 sentence summary each, representative quotes, the meetings where each surfaced, and a recommended action."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_patterns_across_your_meetings", "rar_sha256": "4b1112720678d85a0b97fb5b33fd7f0df76b4daf9a974494a73c64c3ee6541e7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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
