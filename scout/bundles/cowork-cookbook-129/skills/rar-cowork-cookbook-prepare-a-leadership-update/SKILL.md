---
name: "rar-cowork-cookbook-prepare-a-leadership-update"
description: "Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_leadership_update", "rar_sha256": "427cbf153ff2bd8457657b5db886e3457e79320a686d51be50c28360636ee005", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_leadership_update_agent.py` and embedded as the fenced Python below (sha256 427cbf153ff2bd84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_leadership_update_agent.py` first:

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
    "version": '2.0.0',
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
