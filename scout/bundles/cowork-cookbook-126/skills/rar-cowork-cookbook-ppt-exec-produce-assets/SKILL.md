---
name: "rar-cowork-cookbook-ppt-exec-produce-assets"
description: "Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_produce_assets", "rar_sha256": "e24b4b8f1a8c5f2f332fef0b3c5ced92834ba8b2bf115f4374006b42963d4fdb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_produce_assets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_produce_assets_agent.py` and in the RCI capsule.

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

Produce assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-produce-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_produce_assets_agent.py` and embedded as the fenced Python below (sha256 e24b4b8f1a8c5f2f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_produce_assets_agent.py` first:

```bash
python3 ppt_exec_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_produce_assets_agent.py   # or on stdin
python3 ppt_exec_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_produce_assets',
    "version": '2.0.1',
    "display_name": 'Produce assets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '720e9175233f441d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck', 'word:produce'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PptExecProduceAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProduceAssets'
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
    print(PptExecProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
