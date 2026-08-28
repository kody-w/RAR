---
name: "rar-cowork-cookbook-adaptive-card-improve-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_improve_assets", "rar_sha256": "d532153957dcb266cc03b0b08ea50e854d9c2c25dc4cb876136205e09c41d910", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_improve_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_improve_assets_agent.py` and in the RCI capsule.

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

Improve assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_improve_assets_agent.py` and embedded as the fenced Python below (sha256 d532153957dcb266…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_improve_assets_agent.py` first:

```bash
python3 adaptive_card_improve_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_improve_assets_agent.py   # or on stdin
python3 adaptive_card_improve_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Improve assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-improve-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_improve_assets',
    "version": '2.0.1',
    "display_name": 'Improve assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-improve-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-improve-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fe7b5cf53c063e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/improve-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-improve-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardImproveAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardImproveAssets'
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
    print(AdaptiveCardImproveAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
