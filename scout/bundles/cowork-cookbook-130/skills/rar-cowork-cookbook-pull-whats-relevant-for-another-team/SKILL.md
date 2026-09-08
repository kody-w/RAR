---
name: "rar-cowork-cookbook-pull-whats-relevant-for-another-team"
description: "Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_another_team", "rar_sha256": "647e7c99d108f4b05cfbacd816e1bbb0a6dc7d8ff82f98bcdf9105b941504e21", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "beginner", "read_only", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pull_whats_relevant_for_another_team`. The original RAPP
agent is preserved byte-for-byte in `pull_whats_relevant_for_another_team_agent.py` and in the RCI capsule.

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

Pull what's relevant for another team from a campaign brief — Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team.

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
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team
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
    "campaign_brief": {
      "description": "The marketing campaign brief document in Box to extract sections from.",
      "type": "string"
    },
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
    "team": {
      "description": "The team the extracted sections should be relevant to, and who the new doc is shared with.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_another_team_agent.py` and embedded as the fenced Python below (sha256 647e7c99d108f4b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_another_team_agent.py` first:

```bash
python3 pull_whats_relevant_for_another_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pull_whats_relevant_for_another_team_agent.py   # or on stdin
python3 pull_whats_relevant_for_another_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pull what's relevant for another team from a campaign brief — Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team.

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
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pull_whats_relevant_for_another_team',
    "version": '3.0.3',
    "display_name": "Pull what's relevant for another team from a campaign brief",
    "description": 'Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'work_management', 'beginner', 'read_only', 'automation'],
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
        "upstream_slug": 'pull-whats-relevant-for-another-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/pull-whats-relevant-for-another-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5fa337bb6c4465d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/tailor-content-for-an-audience'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'work-management/pull-whats-relevant-for-another-team', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A focused doc containing just the sections relevant to the receiving team, saved in Box and shared with the right group.'], 'confidence': 1.0, 'deliverable': 'A focused doc containing just the sections relevant to the receiving team, saved in Box and shared with the right group.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_brief': 'The marketing campaign brief document in Box to extract sections from.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'team': 'The team the extracted sections should be relevant to, and who the new doc is shared with.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Get a partner team only the parts of a campaign brief that apply to them - without making them read the whole thing to find their section. A focused doc containing just the sections relevant to the receiving team, saved in Box and shared with the right group.', 'expected_output': 'A focused doc containing just the sections relevant to the receiving team, saved in Box and shared with the right group.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Extract the sections relevant to the [Team] from the [Marketing campaign brief] in Box and create a new doc with just those sections.\n\nKeep the original headings and wording intact so nothing loses context. Save the new doc in Box and share it with the [Team].', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A focused doc containing just the sections relevant to the receiving team, saved in Box and shared with the right group.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team.', 'example_request': 'Pull the sections of the Q3 launch brief in Box that apply to the events team and share a doc with them.', 'inputs': [{'description': 'The team the extracted sections should be relevant to, and who the new doc is shared with.', 'name': 'team'}, {'description': 'The marketing campaign brief document in Box to extract sections from.', 'name': 'campaign_brief'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a partner team needs only their relevant portion of a marketing campaign brief stored in Box, rather than the full document.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PullWhatsRelevantForAnotherTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PullWhatsRelevantForAnotherTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_brief': {'description': 'The marketing campaign brief document in Box to extract sections from.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'team': {'description': 'The team the extracted sections should be relevant to, and who the new doc is shared with.', 'type': 'string'}},
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
    print(PullWhatsRelevantForAnotherTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
