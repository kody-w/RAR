---
name: "rar-cowork-cookbook-pull-whats-relevant-for-your-team"
description: "Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_your_team", "rar_sha256": "5d287d435f426c545f8c78f8149018f01a8766dfa3729fdefa47132905845ed5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pull_whats_relevant_for_your_team`. The original RAPP
agent is preserved byte-for-byte in `pull_whats_relevant_for_your_team_agent.py` and in the RCI capsule.

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

Pull what's relevant for your team from a source doc — Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team.

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
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team
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
    "distribution": {
      "description": "The team or distribution group to share the new Box doc with.",
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
    "source_document": {
      "description": "The source document in Box to extract sections from.",
      "type": "string"
    },
    "team_name": {
      "description": "The team whose relevant sections should be extracted.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pull_whats_relevant_for_your_team_agent.py` and embedded as the fenced Python below (sha256 5d287d435f426c54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pull_whats_relevant_for_your_team_agent.py` first:

```bash
python3 pull_whats_relevant_for_your_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pull_whats_relevant_for_your_team_agent.py   # or on stdin
python3 pull_whats_relevant_for_your_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pull what's relevant for your team from a source doc — Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team.

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
  Upstream entry : https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pull_whats_relevant_for_your_team',
    "version": '3.0.3',
    "display_name": "Pull what's relevant for your team from a source doc",
    "description": 'Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'read_only'],
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
        "upstream_slug": 'pull-whats-relevant-for-your-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/pull-whats-relevant-for-your-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d19f985e6714bbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/tailor-content-for-an-audience'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/pull-whats-relevant-for-your-team', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A new, focused doc containing just the sections relevant to your team, saved in Box and shared with the right group.'], 'confidence': 1.0, 'deliverable': 'A new, focused doc containing just the sections relevant to your team, saved in Box and shared with the right group.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'distribution': 'The team or distribution group to share the new Box doc with.', 'source_document': 'The source document in Box to extract sections from.', 'team_name': 'The team whose relevant sections should be extracted.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Get your team only the parts of a long document that actually apply to them - without sending them the whole thing and asking them to find their section. A new, focused doc containing just the sections relevant to your team, saved in Box and shared with the right group.', 'expected_output': 'A new, focused doc containing just the sections relevant to your team, saved in Box and shared with the right group.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Extract the sections relevant to [Team name] from [Source Document] in Box and create a new doc with just those sections.\n\nKeep the original headings and wording intact so nothing loses context. Save the new doc in Box and share it with [Team name / Distribution].', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A new, focused doc containing just the sections relevant to your team, saved in Box and shared with the right group.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team.', 'example_request': 'Pull the sections for the Support team out of the Q3 Ops Handbook in Box and share the new doc with them.', 'inputs': [{'description': 'The team whose relevant sections should be extracted.', 'name': 'team_name'}, {'description': 'The source document in Box to extract sections from.', 'name': 'source_document'}, {'description': 'The team or distribution group to share the new Box doc with.', 'name': 'distribution'}], 'model': 'claude-opus-5', 'when_to_use': "Call when a long Box document needs to be cut down to just one team's relevant sections and shared with them, instead of sending the full document."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PullWhatsRelevantForYourTeam(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PullWhatsRelevantForYourTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'distribution': {'description': 'The team or distribution group to share the new Box doc with.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'source_document': {'description': 'The source document in Box to extract sections from.', 'type': 'string'}, 'team_name': {'description': 'The team whose relevant sections should be extracted.', 'type': 'string'}},
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
    print(PullWhatsRelevantForYourTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
