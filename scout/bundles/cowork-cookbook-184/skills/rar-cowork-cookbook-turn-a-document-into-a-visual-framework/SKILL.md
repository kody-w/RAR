---
name: "rar-cowork-cookbook-turn-a-document-into-a-visual-framework"
description: "Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_a_document_into_a_visual_framework", "rar_sha256": "82fec6ddc21c7c54a3fbd8b9a1a3ee2d2a811ef41320b33abf1e56a8fd8b7575", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "turn_a_document_into_a_visual_framework_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/turn-a-document-into-a-visual-framework:5875ee06e73672b167b0a15e6fc68ff4cdfcc4d29d3daef4977827a9366c7497", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/turn_a_document_into_a_visual_framework`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `turn_a_document_into_a_visual_framework_agent.py` is
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

Turn a document or deck into a visual framework — Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_a_document_into_a_visual_framework_agent.py` and embedded as the fenced Python below (sha256 82fec6ddc21c7c54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_a_document_into_a_visual_framework_agent.py` first:

```bash
python3 turn_a_document_into_a_visual_framework_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_a_document_into_a_visual_framework_agent.py   # or on stdin
python3 turn_a_document_into_a_visual_framework_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn a document or deck into a visual framework — Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Turn a document or deck into a visual framework',
    "description": 'Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74a9754863ab3617',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.4, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class TurnADocumentIntoAVisualFramework(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnADocumentIntoAVisualFramework'
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
    print(TurnADocumentIntoAVisualFramework().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
