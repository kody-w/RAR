---
name: "rar-cowork-cookbook-prepare-a-leadership-update"
description: "Drafts a leadership update deck in Microsoft 365 Copilot Cowork, applying the Templafy corporate theme and sourcing content from your recent emails, meetings, and files; call it when preparing a recurring leadership or b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_leadership_update", "rar_sha256": "972860e659ba57808a4374d235bb1ac1df32c058faae3bdd3ca767d436503cb3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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
