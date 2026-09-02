---
name: "rar-cowork-cookbook-prepare-a-leadership-update"
description: "Walk into a leadership update with a deck that's on-brand, on-message, and grounded in your team's real work - without rebuilding it from scratch every cycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_leadership_update", "rar_sha256": "427cbf153ff2bd8457657b5db886e3457e79320a686d51be50c28360636ee005", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prepare_a_leadership_update_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/prepare-a-leadership-update:cb799c0d089b7cd82179a5ffee49596e41e2bee46c16294f07a4d69c077d7dc0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/prepare_a_leadership_update`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prepare_a_leadership_update_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
