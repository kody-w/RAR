---
name: "rar-cowork-cookbook-pull-whats-relevant-for-your-team"
description: "Extracts the sections of a source document in Box that are relevant to a named team, preserving original headings and wording, then saves the trimmed doc in Box and shares it with that team."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pull_whats_relevant_for_your_team", "rar_sha256": "5d287d435f426c545f8c78f8149018f01a8766dfa3729fdefa47132905845ed5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
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
