---
name: "rar-cowork-cookbook-turn-a-document-into-a-visual-framework"
description: "Converts a named document or deck into a Miro visual \u2014 flowchart, mindmap, or framework diagram \u2014 using frames, shapes, and text; call when written content needs a presentation-ready diagram."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_a_document_into_a_visual_framework", "rar_sha256": "c8f840f91737c361ba735c44560f064ae87fb50eb970b732742bd5bc3d07eb7d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_a_document_into_a_visual_framework`. The original RAPP
agent is preserved byte-for-byte in `turn_a_document_into_a_visual_framework_agent.py` and in the RCI capsule.

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

Turn a document or deck into a visual framework — Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
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
    "document_or_deck_name": {
      "description": "The name of the source document or deck whose key content should be converted.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_a_document_into_a_visual_framework_agent.py` and embedded as the fenced Python below (sha256 c8f840f91737c361…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_a_document_into_a_visual_framework_agent.py` first:

```bash
python3 turn_a_document_into_a_visual_framework_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_a_document_into_a_visual_framework_agent.py   # or on stdin
python3 turn_a_document_into_a_visual_framework_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn a document or deck into a visual framework — Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_a_document_into_a_visual_framework',
    "version": '3.0.3',
    "display_name": 'Turn a document or deck into a visual framework',
    "description": 'Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'miro'],
    "category": 'integrations',
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
        "upstream_slug": 'turn-a-document-into-a-visual-framework',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '102af16c21aad53c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/visualize-concepts-and-frameworks'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-a-document-into-a-visual-framework', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.'], 'confidence': 1.0, 'deliverable': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'document_or_deck_name': 'The name of the source document or deck whose key content should be converted.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand. A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'expected_output': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': 'Take [document or deck name] and convert the key content into a Miro visual - either a process flowchart, mindmap, or structured framework diagram depending on what fits the content best.\n\nUse frames, shapes, and text to keep it clean and presentation-ready.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.', 'example_request': 'Turn the Q3 Strategy Review deck into a Miro framework diagram.', 'inputs': [{'description': 'The name of the source document or deck whose key content should be converted.', 'name': 'document_or_deck_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a dense document or deck and want its key content turned into a clean Miro flowchart, mindmap, or framework diagram.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TurnADocumentIntoAVisualFramework(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnADocumentIntoAVisualFramework'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'document_or_deck_name': {'description': 'The name of the source document or deck whose key content should be converted.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TurnADocumentIntoAVisualFramework().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbejRrbmX1Gf+2D7KjOFGKW8q9ZqBEgIBEiMEk6vNPM8iBnc/u8dSDqZdpXrdlWvfmqdk4kgIva8v73jBL+9WW0TFtXb5zfFs/LFwUrTKPSqhZW7C6roiyoBlyKxwb+FU+RNFdltU1T124c316udKiqbqMjBcqrIO69q6oW1yK3Mcxdu4bSZlzeLolq4npMsorwpwKgQVcWii+rWShdfWhhaows/LXontKrmwyKLcjezyg/zKr8ChB4iuJEVgJv3+W0d5cFzuP6wqEOrnK+zyI03NP+1cIAWiz708kVfRU0DrrPosyy557mziGXl1eDemoX/WHmWO77z+AQ08wYrK1Ovfvv88y8f3iLw/e3zb29OatXg0ZvaVjlJv7Q7AqVI/aHN/l1cQCG18gBMLUdg3Bzcl17lF1UGHrmev3jd/Vh7qf9h8Z//mfRWFdQ/ff6SL16fL2/zj9zmiyb0Fk1h1Q0wqWOVlh2lUTN+WpBpb431ovIaIM6sUg18kwefniu/UyrKxd/msR+fTD4FXvPjl7cCiPBQ/svbT7Opv7xV7fz900yl/PGnT8AjXvXjT9/p1K0de04zEwNSf/r6un+RBRO/T438xVflzFAvXpXnRKUHiP9Bv/nzFP1F7mWSr8/JPxYgAv6a8qzP34C8z+izAd2/JgtsAFa+fYqLKP/xxaMqOi+3csf78ad/RtYJQaimUd38S3R/fhIOQQABa71M8tOHh/t+WSxfun2j+c/ZliBg/h1NwPR3dt8M9c9oPzz7d6TTKPfqb778S3J/tWD5t8XP/1S3/27Bh4X/5Y320ghghGWn3ufFb48Q+fkH9/vDH375HZD+P5JRirZyHhS+ZlYe+V7dfP368w/14/EPv/z8Q1uCKPas7GtbpX9F86/s+uDzJwu+Zv3457WAv5YnedHni285tPitKP9H9funhW6lkfv9ef158cdMnD/LxazEO9OnCf6QjTWQ9Q92/OntdwA/OdCmdR7DAD/+4z8AgjpVURd+s1Ccom0WwMFNlHmz8GoY1QvwO6NG5QG71hEw7GseiP/Zw7PEhb/49X86D3z/6LzwfTXr+9X6+g7cX2fABvdPrP76DY1//bRQAfmiioIoByAuk+fzl9wKZnwFrB/QWnUAruyx8T6CrP44fwHwv/j1X+Tw9UHsUzn++gD16ImCMnWcEbBuU+/TrKsxA/xTMweULm/wnBbwSQsA/ws/SueaAGQp0g4g6GyXOolAXXAjgDGghI0P2sB2n2div/76q23V4Zf8CdnI4lnb6hWY8E2cxcePQDs/jYKw+ZJ7Tlgsfvjt9x8W/2vx3616EJ95nEH9eHkGSMgpkrgAmfawBHAacDOAkYdnfvv9ZWNAJgfFGPgx8iPvuRhEauK57wZXWPIjjOEL2wOGBkbOyqJq5uoYNZ8WR3/xTV7AdB6aK0VY1A0oyaWXu17ujICqBdT5Zsm8aBY1CMfaHz+AUus9uP5qV9ZDxAykvNX8uhCoM6hLRQr+m8V8TAKLizwC5v8WDs/ngEj1Q73YvZP4tBDn2FyUVmWVYWW9ePjW0y+gHr0vf3QMudd/yecq7GXvNftpHjAJWMZ5ufTj7HNQ6TOACm79zvsxx5qrp/qootWXvH4lgVXNrnBAUQBMgzZy59LwX6+QqsOiTd2H/YCkM6WXF9yXVx4xOPcCQMJ/1uu82pzvjcyrgfn/plmabUAeDjJzIFWGXjCiKt+evnkn8uwvQcuyAAH6zMPvbcw7VL0j9pc8jUCgVeN/PWc+PPqa80TBtgLWkkn5QR+EE/DNTPcR7XP0VtWcJ9aX/L00fJjdMOMgcDiABpA6c8S+M5xH3yUNQf5/eKj73iY8oqNyZ2OBiF6UrZ2CaPOBWWwL+KgJZ2O82xmEvjdnbx9GTvgnrRaAOogwQH8BhIiA20H5+PQNrp+j76L/aeGzG5qXPDrFFiRs9SAA5PBmAWc39lEDcMtqnr050PPzgwhQIyubWXcbeA5o+nzoVd69jeqomaPgaVevBAj9cb4+NZ2fekMJsgQYC+RC2QLrPrJnjqQM9DpABhCmIJlABILaD4zyMsKDIIi0Z1S9mtMnxcfjl0LeI+XmovW+cFZkXjP3ASBYiww8Gf+IGOpfhQmgl80zHnz/PtK+cZtpz6hZA+QDHN9Hnw3Dp2fNfzYVi3e6n/9h8/Pjv7c/elRx7c8B8HkRNk1Zf16tnpX3vfB+Api1espaP4rwR+vjOyB8nIEA3D8x4OO3LP8T+afmnxf/noh/IvFKkc+L9SfoEzQPnV4h9voAi1Afd7eP6Dz6JZe978AK2BcZiLHZfyOo+t+q4PsUUAqDygvmyc+qWM/FdMacRxkAzviS/zHm55wDEJcHD8Qq/oAFj3YAxP/Td9+qFRjKm3SGJUAv8OY93CNDau/tc96m6Ye3GWb/xb3bXJWyObjredcH0gh0Z03kPe4eWDE089c/b3+lxxcr/bSgPYBLaf3HAHzVkrmW/iFPnooCBR3A4cPCBeapH0gepTPzOcesGgQtiNdZoWYsZw2e27y5MfzWRRXV17lmfH3q+PeSzYkzj8zY9D3s/7Hi9KAt8BaJN34DxJfY9gPM53rluX8pyLf29R+ZG6BXmPHWLT7PZfPDC5XAFWw5Piy+7R6A+q/93GP/nbdgq/zzvHOZ/fFYMn8Ba8Dl26Jvf4Owvbdf/kEuINgD6kDBmGl9F/L71OKx45lVAKSb5wb9tzfgews4w3p5/9Uyg+kAGT7Wc3OwAkkCmIP7ZziDsf/bZvpFBpRl0MUBOs7G36CQv10TCOEg+Nq2CARzUBTDIR/CUcvbEL6NQZ69JSCbQGAChW0Xsx3EhQjPJlxA7+ngr3MjFM2iYVvCh7Zb2EfXMOS6ng+jrrvBN7iDETBkbW0Ls7GtZX9fmoC+4qXvU7/ZmN/6+tkuL7V/e7NxFMxk0fpIPj/UarkGD1FbxOxlhfvBuhsuzSjq0mqf+XVcXdyy4SayV+wR5lApOI6htle0gU91HW+4RrWknXcLsT7PlJWDhobBuWsRge2dLd1IgU3u1bHfiNM8JvURBdktrhw1zZFtXcJ04xg1TMXzDXTIdNTP9FPWmtFeC91lgfOEHeXIahUS8RGKGl2nrl6JBB6LIdtKQUcZPWZVeaqlpjoW5f2Ya0ScO30uSjp5ds0xljeblsLWbWx3Y5EU4sTnKpYfivTU3XEnSpIkqmLnvne9PUiCjQwKGiN7pRYzQzp49+GwNXFldPdJdfAIl5R2d9dfncUM8/38tCWWGr9ZSYSbDVt6Y+DxIeTHKr6Zo0TsqWAwDut11Ol962qn84bvKJQuOh6j3Vjmt6eDMvhwcahyJUJ2pHDnpfspohJx6XbZadLuyv1W8Ri1sQoKtU4XKhjPbnzS+bVOnTlqwydVfzKPNZwdYUzKjILwpAmFanE4g7JipVqZHpTwch+L+21HX6kNcjdxJqqP3CEND/yddrIdZjbZXT6ZVHTSIMtasz3LDyZWUBMVFF5cS8X1iDRsO9Ed68C1pTcWVgTJ3dDWTO5Yd1RKg4u8By4YqquxPtT3gu+sgRNUKSN9DPE0w74mnAvzHHYnq7WFr09Xk73H6qCfU6QtVypn4AqL53BbBCU1tsW9GlnNxZKaJ3gvv40cO4RpebnfcsGOI9Y/D4edNRQ9v5PhFLNCDOwKol7ceQHF7hM0XB2i5RU6k/xJOnPXuO+K/bFvaCFbnzQeEiuZ3OOjtfZFJbngkJfBe64W7kSGmPrtmtxOdXiNT1fUiKVCsOt665hiCkf+aj/qdaqtGHEpCjbFoYVbeBfYpoMaP252DrxqaG3JYO19rDsT1nOGGQXihI4jYqZhQ/exoiHp+pxvUrZ3O4AC6tD423tmX50VE05soRG0J+wkP0RX9IDEkwk3yjbeHlH4hK8Ev/SXpxQ/ri1+Fd047kxCTSJxiX6H0S69lrJc+NL9zIr0Pgex1SjWrhUqMVUOS5OIqSjzU5oeaXNwqJGpr1fxMsbjuVzCl1pu9V4jFJFvmEh3y1SnE9JO1vouCfACNailX0WojnIZdmiOWRDTVp8aZBYkp2xpqqbkSFKAppi6ZQx74/oHXxfyK3bj+hZz6NJMGKKHl2ECeWFiS+nNkvmSw+icWTmbdWZ44xmhKl/ajRYTFuh4IeTTatfmFOH0NyFD7j00mZO1StparcfpAGsbqdgW9ahMgRBHoIPgL9v7iXOOu/Kw5OWci2ml6cfMEMmrUdjCbmnutFYxrTuirk/jQdgZNzeREUYqUbvxzjfJrioxVulqGOjrcnXpLke1aHh+i6YrFruWSBztcnITlr3BV3AUOz3oeR0eVXEx2amF55O64dOmVt5wIUN1mN+vGH5pX3cGn+OQsq/AfmutrXrsGhiJ7gWnZukW7HRWNXzNaWkTCM0UrD00gqRVsdHLVER1+7K3rES9IKKJj0qG7G5XLzX26y6/2ZvDxtGsmBhvMHrOiCK11H6qJ/++j494ZFxQgkCx4ew6Q3I7yC5Hq32c0rWKnEbDlLnOMjEanc7BpLbXVUHXGzrgUwJFr3RLw3yh7UquvQXLDYcVOKd5UNCMZyWz9nQKF8OBW8thuL2tuaYmpptSX/fLExb3/CnanZlY4BlHTk/Bbk/xNUfzdydbwQ6A0Qyptvh+14gmz1+SG3eRJyKCgoOtDCrFGNA9g3qmoX21PBmdGpNHZsffw5SxW+5YWZfgfhRPbHUu9LREDtFEFsc+uIN6qmgpdcfsdV/SO/KaH6JgUx3yTawbFebVeHgM7QyKETHdj4MqpUkGnynx5qzsXB+crkM6Ikk4sfCPwhKSN0s1usu8pBCEAMErraC5MDpRDYbVFtthytElPI+1LzE1dDY6rhK8E1Zyut2csusGM89HuDTcPX0ZQFgvq21EMWIQGGhBopJZZeaFVwUTb1xOzhWynZpqJ6IH/tA0TsBL5pJE0WzJ9bEzUj2TOh4ujx4PZzfFvGRoeO6vW9ncA9TmjvtwuHWosNxqpiyHgeVe/PRmAxNcKOKE9/xd04Uqmc5x2ZXdipKVnhE2NcvaSeP0cqX3yk262Rx/8XW/cZBjfYKg9bUkTlYidW3RbyWWJ/Ug26V663Inlc0QhlkZCiF4jrvhOF3ZEji+HKy9tZkITY1ltsC6jX4uUPjIbCEKgI0uH3pnj3C6dDtj5CgiN27D92xzpQHApBcZJ6dAuy5Bv8ffZPGAOIToWOKF03c7SdMptAFxwOwkepeS3O5u3LKLx/pAYeOYHvTNFl5zpUAXMkcw5GG1yy9aBV0ifFItg70LCYWPV8on08OykhrLlFjpgkLjJpZ3e1Q0srSS1thKywCGbHpa6gP+ykA3ISDujHF1OIUiyYb38aGVYO9+uXM9u8Fc6xg6DXsw6+FwDYayazRI3Dc6Wid+Bw+oqPQKeUrcWLsFUithZR6MjljTlHbqNqAKD6yIuwx2lttiC1s+KhZdJbPwVde3OcUyXdSf1ru9MEZxKGS0Jh/3t6q+kNq6pm8cfktK5SIIx0S4GBjqheFptT1cEuZGJqLIrnDDjki25SczjQV3j0GSfaOOknkJ+BhfwoY9+tdyOQQ7N/MOB5i9ldPNEwea5dvlaUSgDBuHJFnpy0RLd2Z3JZablpyEzYFe7pkSjpnltN/rnNfDST0x1+Uk35ONAdNHnRNK9HDxiuuF24RKnO9P0vp26tWyl4vYYYbhdNHg5ZVmrntKF7Dbvuai00E1r32imQWX9NumOqWTMNh7qc0NEmZ1xtlLvXfKMCiyqFpgmN1y1M+xAWXyVs32x4nzYLJD0rs5opG5bIjElJXzjV86F01f+iq39VhtFBW+puIQu8Q5eV/2Z01QtMv+QG3pwOST6xEyLrpTqHTJaVnDrMfdUYlS/qLw8a50R9VWUdmMGh5zEu2Ay15f6ohxPEZJfIGS6GjGSLDWE6ZJ0Qp4YbrtMmEQpNXo4VBrhhK/J6/DUuyNoOxtSl5hRRbDmU9St6imZVlQNuLA79SWYrmrwZmnpImu16zFs7SGuZ2sFLS3Bz0PB8c7dtolENzdmSs6+JzdGCvGrFKrjqiSY8ytUGEN2AB00F65yWBbdCjFPaQrR33iS1p1x4jQSicZ8FCBrt1apXDM5qnMMWiqKPM9TSX6XnfQLUMCaKquori8SJhsyhqC7VfO4FY785AeXI4vzB1bLRNsnYbKNFHiZcWWBrel4UtL1/GmWSM0lhARLiDt2CPhejiHaFdBiJhjgsj1/lm0TORwPSN1kmMFqhmqdxoIfxWo9lmnQte5uHuDkQl1t/U4Au4Ojbg80hKjqvzByJJT7U6RMlx2qLYq1WXqK7kBqZpMIONdTyZjorpUvKJtfb4TqbG7+jdEY4cqHkmw9byLcFoVjD2O0LnDqYC+yGkQHhANlGiK4Wpnr+7VS66KyArC6fPAIewu2rnkyj3EMVQm3ZmrgrBcZhgirzerTCaik4/h5FEOY5nkNVzGuWzo8b1ndKLGUqZyiE/a3hCj0gtokhpwStGRKK5itVnfAGyF5i1w7hJT82yudFRnGuLeCWg5KrRtlYlTQQL837WedrRi+EKVCudkV7w6jtwkAfOa+wFqhppGi7VJqN3heNNDapXmPb52nP3NkqY91vBHWD9qFNYXx4wZCES8nBASyboKI9TMWpOcJQiITaqjIWXncbik9+MealsIAAe+DsWa6NtyvZSyretI5V1psvwcd1sXrgQN97RW3SrUlanN6soSWaYSCLS9CANzuS6Xe9G9ekNe1iFumdF92qkNrsKrzUjXu4jOGOGCbu06jUnb1AS+TJMQLyPSGWhizPlajcOqjnkdrfAleVGXwTTezT7JUEFeshMoUYpdlFednPSuOp01a0lC1Gpzw51e2ghL61R18ar3NQRpyJPXpaeBdo7l/mTht0PNupIEw7fSI0SwjCezQszou3c925vQvl70idpshg2KslOjSl2iSbm9iaEj2ZD9dJM5DbVtaJ0OuLRDDnER5htB3AbZpitonxlif9wOqMsPriOKd66K6O5o4+UZBqIROTuYXpOupHYSbRleupGLE0Q8trUXXbpD7wa02t0NK3c2mbCVG2EZnY/ijuWnc3a+4vmabN3uamfYquBKhSWPUmqD5mPDbC/7Nis5NDpKKyG2j7WkCD5bjhKTHikygUz1yNxuDUB3QvE6b9hdrevg1rutXZAj6hLTxcLdVhU7GkEvBRJyuBuOG0+AbX+LsXLiYeoK7D/8jbatdY5Xgxo5IxttdcJPN+MQEDEAcMMaTicCNHWUSlz0G0p50+3G8DlDZ4gTnFVHMru7BEeFKDXYQdmNJJ/mchwdb5YfSJfSMJJLfrSSaTUlDa2L1WYSDG21xwJc8IBZzodxPwZwvx/k+zbTsC0WxzCzFDLVr+/OflWaIDpc5KiW/A3B+B1GJpcttqSI6l71DBK59GEVOue+2bf+UW6qOEmsqi/N4H4+LU0asm8rzeUyamn11SmsYIJLC1dUriwPd9C62jZdMcB9JFcg8dSRNBOKwzZn2kZPl0qazh4zCPugso1doegau+RMwfBgL7asPPf2eGFiaznAb/CGMCOZ8OGbrhK0EDDm8miY50uXobE4tJc70woHyWAyXj/Ix4lx2bJaZlOyd/Z9wezqW3++QnYU1lTGWa2YeYO6g8Nk20Hc9qYdjk7UHPNzd1nHHDL6AxRHMGvjwVUIdByn1qi8PgGzn7fGmUVWgyxHByyo96B3yPoixjEitzOYvLBBf+ERKZlKQ4rj8gZL+xCJNR1rtgjPOfc2p49xtRGmSMBTjyXCu4kRy7zV6mmvGmrKsklrgp3Hhki7VFinyY6A+Ii/6UNHwXRtbQgci5tibI1cPKzaW6ScpFHX8+AEKwHr5SzY5uz9sFdFw2zJoqVj99heKE+UCyI/tmRrkRPhqRci22Qe5QAMuZ2LOHPMykrHA3uUiC52WNUUOjXDbpTZ9jum4Lo23OAb1hGocbeirxPv5rHMqMmW3U4hf10rnXbit81EexVL0h66K9mRUG+StLU8hIhPYpblqx3mYBhxtyJcjFjPxX241TbFrg4zUCK8rXdY3m6BqCRHpTQdu2ym5u4JotvgNk6conPXJW5RtcXJ0t1LWrqSUTPt2YLvlrJ1hRCADzFGWb+repHqmlC3O6jNAt3XYjk4X7uDeFIvbkaOnsEslwd76UpEyjiYgYY+GyluHzOckrEjaSnrw+5GwKYj9uHBtAnM8L0wkk5q3+tGz5uRRNl+cOeOy0nBWFQ5jZvdBRSl1Y5KofU56cjb7SC5J5mZfMI0+aKo0z2ENP3AsZC5zqG4EVZ87LucetJiJCQoztpHTgVvhdXePGNFBXNdcbZhiIFJ7G7bqjiqFJ8fwnZoe3Jzh3DmBkNb1iyVbQWBFoyQEQj2EblpDCx19uXFAdnUIIaP75rUI1N2DXrlsHDDukSaCW/KaxpLRpPaZjOJGn7GdYNXYLrxsDBTzgTVxIJRiJtkAg7Wi9uBfvwt4XA3VpgbUSY+re/jmhu0de/R4U4+sMkIYGh19iZ7VxF7xiUJfmeelq3AQAx9uq2Px7xsW+5sNBFWSVXVgS5wj+7ajeNUY6ypqxHmjMZGDCmouvWWoTRP26+Omihud+lSdBqaaNaq6caoPSbTGu+xY8zRE3lWOqff5RM5bkiUI5rViu+CilXoy3UgZNq+2doprVn1DDUtBNq37NxeW0y/7jw7grXeE5t6PSG65Eucsw6ni6At0aLdjjeuuSDmVFG9CavHQ1eO9n7dDPFqwzaI48kHm8VCCB/wdXe2mvjmcH6yVGCgrsbFAiwFuDttPIsV6W2gIFKI02xJ9iOFEMwtYA5DrwbXLepVDomKVNP7wtJwt+0VxHxUSk4Mq+idr+j1Mhcc0Vy3mwPpBwO0pOBDmfjDTWPXeXhdNrcKt1u+QoVr6DVRiHdqF4swaDNMbnmFl6ujsL0Yq0s3scE2ywn0yLEoAGzybrm+yDeEyzVKrcsQcTHEdb5kex3aoqLgsgNKx9vqNsCrrNKoc99LWOHpLbquHLwey6Hj0NxX65OJTiQ/yOgWF4Tea/YGna7XtGNizogg5aqUFeVwkJhV5EzmISBFpfFPkwr2aTvtGt6jO9kXTudekztR4fGErqHTPub68w5mfNqim+BQ7iCdpaEVL0MUaHwhdpQRWlZBBKCI6RYXYistD/uhIQvHR7ESG8p1vVHOIqpVGQ01jGUjZFcQjYIlQoScB4lKIBna4GQZ9ta0ataTcx4J3JFzyE7octrjl61UKCurZNArhdfQqmiJZNWeQX9G70fPKk3UjCfIXV1WwoE/2hozHwP87W9vH97mI7vXwdu/++bPfBjx/+xM5Hl88X6q/zhZ8iz384PX539bsl8+vFVOBOR6ngLVaRu8Dkv+7gzo4794ljsTGZ+v1rwfLz4PLRsrmN9BfYtyt62bavxaF+njhB+ssOf3Ory6nt9qdMD1jwdlRRN6Fbg+5M6s+WWcmf+8ygui+eWVt/m9ssYLXkdiH96yqCpmzV7nwEAh5BP0CXn7/X8DxWrNxCIsAAA= -->
