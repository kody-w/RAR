---
name: "rar-cowork-cookbook-adaptive-card-decommission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of decommission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_decommission_assets", "rar_sha256": "b57f65510120117f5a861b2dbeac139cb4fab0cc02f5bba0ec36e61f5dca302a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 b57f65510120117f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_decommission_assets_agent.py` first:

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
    "version": '2.0.0',
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
