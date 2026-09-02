---
name: "rar-cowork-cookbook-adaptive-card-source-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_source_assets", "rar_sha256": "d69021989a09bdf77d51d4613d576a0db15d1e39862469aa49391feab20541e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_source_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-source-assets:6f5077ce403ab117fd773a2359ce1f36d42bf378719c2083452db741466bc9e3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_source_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_source_assets_agent.py` is
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

Source assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_source_assets_agent.py` and embedded as the fenced Python below (sha256 d69021989a09bdf7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_source_assets_agent.py` first:

```bash
python3 adaptive_card_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_source_assets_agent.py   # or on stdin
python3 adaptive_card_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_source_assets',
    "version": '2.0.0',
    "display_name": 'Source assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ff8e8a850edced1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardSourceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSourceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(AdaptiveCardSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
