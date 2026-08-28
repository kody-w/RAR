---
name: "rar-cowork-cookbook-turn-a-document-into-a-visual-framework"
description: "Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_a_document_into_a_visual_framework", "rar_sha256": "82fec6ddc21c7c54a3fbd8b9a1a3ee2d2a811ef41320b33abf1e56a8fd8b7575", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
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
