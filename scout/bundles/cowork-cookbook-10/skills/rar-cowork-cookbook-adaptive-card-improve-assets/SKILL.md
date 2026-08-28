---
name: "rar-cowork-cookbook-adaptive-card-improve-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of improve assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_improve_assets", "rar_sha256": "55051c82010aa11493901bd2c97f28837501a72c61a445febbed46d8c9978274", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_improve_assets_agent.py` and embedded as the fenced Python below (sha256 55051c82010aa114…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_improve_assets_agent.py` first:

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
    "version": '2.0.0',
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
