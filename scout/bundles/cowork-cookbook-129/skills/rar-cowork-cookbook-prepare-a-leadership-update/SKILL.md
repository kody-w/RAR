---
name: "rar-cowork-cookbook-prepare-a-leadership-update"
description: "Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_leadership_update", "rar_sha256": "e4dc5044a513cfca26f14ab8fc6adde83a34de96e229bf05a1f8fbe6fb8ea2c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

Prepare a leadership update — Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_leadership_update_agent.py` and embedded as the fenced Python below (sha256 e4dc5044a513cfca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_leadership_update_agent.py` first:

```bash
python3 prepare_a_leadership_update_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_leadership_update_agent.py   # or on stdin
python3 prepare_a_leadership_update_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a leadership update — Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Prepare a leadership update',
    "description": "Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle.",
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a4564a552a21989',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PrepareALeadershipUpdate(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareALeadershipUpdate'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
