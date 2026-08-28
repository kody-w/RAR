---
name: "rar-cowork-cookbook-adaptive-card-revalue-and-adjust-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_and_adjust_assets", "rar_sha256": "71f8b65839f05b3399fec6e858bff260c17603ce89801b0078cc2bf258b0f12d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 71f8b65839f05b33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_and_adjust_assets_agent.py` first:

```bash
python3 adaptive_card_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_and_adjust_assets_agent.py   # or on stdin
python3 adaptive_card_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_and_adjust_assets',
    "version": '2.0.0',
    "display_name": 'Revalue and adjust assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of revalue and adjust assets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e509bc95d41b7804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardRevalueAndAdjustAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueAndAdjustAssets'
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
    print(AdaptiveCardRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
