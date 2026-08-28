---
name: "rar-cowork-cookbook-adaptive-card-decommission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_decommission_assets", "rar_sha256": "7a0e1037fd41d4334de645807c232616ab9caf7857df7e5ffaf835a39bd30d74", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_decommission_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_decommission_assets_agent.py` and in the RCI capsule.

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

Decommission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 7a0e1037fd41d433…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_decommission_assets_agent.py` first:

```bash
python3 adaptive_card_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_decommission_assets_agent.py   # or on stdin
python3 adaptive_card_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_decommission_assets',
    "version": '2.0.1',
    "display_name": 'Decommission assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '378227b6827035ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDecommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDecommissionAssets'
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
    print(AdaptiveCardDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
