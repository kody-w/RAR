---
name: "rar-cowork-cookbook-prepare-a-leadership-update"
description: "Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_leadership_update", "rar_sha256": "972860e659ba57808a4374d235bb1ac1df32c058faae3bdd3ca767d436503cb3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_a_leadership_update`. The original RAPP
agent is preserved byte-for-byte in `prepare_a_leadership_update_agent.py` and in the RCI capsule.

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

Prepare a leadership update — Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-leadership-update
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
    "audience": {
      "description": "Who the update is for.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "extra_sources": {
      "description": "Any specific sources to pull from (e.g. quarterly review folder, OKR tracker) and the number of core priorities (2-4).",
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
    "slide_count": {
      "description": "How many slides the deck should have.",
      "type": "string"
    },
    "topic_or_period": {
      "description": "Topic or time period the update covers.",
      "type": "string"
    },
    "update_type": {
      "description": "Type of update, e.g. leadership review, board update, business review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_leadership_update_agent.py` and embedded as the fenced Python below (sha256 972860e659ba5780…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_leadership_update_agent.py` first:

```bash
python3 prepare_a_leadership_update_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_leadership_update_agent.py   # or on stdin
python3 prepare_a_leadership_update_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a leadership update — Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-leadership-update
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_a_leadership_update',
    "version": '3.0.3',
    "display_name": 'Prepare a leadership update',
    "description": 'Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b',
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
        "upstream_slug": 'prepare-a-leadership-update',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-a-leadership-update',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '888108071779f645',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/manage-communications/prepare-leadership-updates'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/prepare-a-leadership-update', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: A leadership-ready deck in Templafy using your organization's approved templates and brand standards - covering progress, priorities, and the outlook ahead - sourced from your real work context."], 'confidence': 1.0, 'deliverable': "A leadership-ready deck in Templafy using your organization's approved templates and brand standards - covering progress, priorities, and the outlook ahead - sourced from your real work context.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Who the update is for.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'extra_sources': 'Any specific sources to pull from (e.g. quarterly review folder, OKR tracker) and the number of core priorities (2-4).', 'slide_count': 'How many slides the deck should have.', 'topic_or_period': 'Topic or time period the update covers.', 'update_type': 'Type of update, e.g. leadership review, board update, business review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle. A leadership-ready deck in Templafy using your organization's approved templates and brand standards - covering progress, priorities, and the outlook ahead - sourced from your real work context.", 'expected_output': "A leadership-ready deck in Templafy using your organization's approved templates and brand standards - covering progress, priorities, and the outlook ahead - sourced from your real work context.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "Prepare a [X]-slide [update type - e.g., leadership review, board update, business review] for [Audience] on [Topic / Time period].\n\nUse Templafy to apply our standard corporate theme.\n\nPull the content from my recent emails, meetings, files, and [any specific source - e.g., quarterly review folder, OKR tracker] to ground the update in real work.\n\nStructure the deck with an opening summary, [2-4] core priorities with a slide each, a status read on what's tracking and what's at risk, and a closing ask or set of decisions needed from leadership.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A leadership-ready deck in Templafy using your organization's approved templates and brand standards - covering progress, priorities, and the outlook ahead - sourced from your real work context."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b', 'example_request': 'Prepare a 10-slide leadership review for the exec team on Q3, using Templafy and my OKR tracker.', 'inputs': [{'description': 'How many slides the deck should have.', 'name': 'slide_count'}, {'description': 'Type of update, e.g. leadership review, board update, business review.', 'name': 'update_type'}, {'description': 'Who the update is for.', 'name': 'audience'}, {'description': 'Topic or time period the update covers.', 'name': 'topic_or_period'}, {'description': 'Any specific sources to pull from (e.g. quarterly review folder, OKR tracker) and the number of core priorities (2-4).', 'name': 'extra_sources'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a leadership review, board update, or business review deck built from your real work context on an approved corporate template.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PrepareALeadershipUpdate(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareALeadershipUpdate'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Who the update is for.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'extra_sources': {'description': 'Any specific sources to pull from (e.g. quarterly review folder, OKR tracker) and the number of core priorities (2-4).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'slide_count': {'description': 'How many slides the deck should have.', 'type': 'string'}, 'topic_or_period': {'description': 'Topic or time period the update covers.', 'type': 'string'}, 'update_type': {'description': 'Type of update, e.g. leadership review, board update, business review.', 'type': 'string'}},
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
    print(PrepareALeadershipUpdate().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
