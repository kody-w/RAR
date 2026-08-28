---
name: "rar-cowork-cookbook-adaptive-card-source-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of source assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_source_assets", "rar_sha256": "320a3ad4dbcd9558daee3e98624462402873fdb6b79a8327ab695611a4abef65", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_source_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_source_assets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_source_assets_agent.py` and embedded as the fenced Python below (sha256 320a3ad4dbcd9558…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_source_assets_agent.py` first:

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
    "version": '2.0.1',
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
