---
name: "rar-cowork-cookbook-ppt-exec-produce-assets"
description: "Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_produce_assets", "rar_sha256": "1273f6fb4dc3f5bbd73629a94a4553202088552a67d834ed39078149728b847a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_produce_assets_agent.py` and embedded as the fenced Python below (sha256 1273f6fb4dc3f5bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_produce_assets_agent.py` first:

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
    "version": '2.0.0',
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
