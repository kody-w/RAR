---
name: "rar-cowork-cookbook-ppt-exec-produce-assets"
description: "Generates an executive-ready PowerPoint deck on produce assets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_produce_assets", "rar_sha256": "1273f6fb4dc3f5bbd73629a94a4553202088552a67d834ed39078149728b847a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_produce_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-produce-assets:5ea7f39705e09d812dcfa5ed5c82e46c07f069e14e8309cb27d6bd45ef7bb996", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_produce_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_produce_assets_agent.py` is
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
