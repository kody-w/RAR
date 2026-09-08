---
name: "rar-cowork-cookbook-pull-whats-relevant-for-another-team"
description: "Extracts the sections of a campaign brief in Box that apply to a specified team, preserving original headings and wording, then saves the excerpt as a new Box doc and shares it with that team."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_another_team", "rar_sha256": "647e7c99d108f4b05cfbacd816e1bbb0a6dc7d8ff82f98bcdf9105b941504e21", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "work_management", "beginner", "read_only", "automation"]}
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
