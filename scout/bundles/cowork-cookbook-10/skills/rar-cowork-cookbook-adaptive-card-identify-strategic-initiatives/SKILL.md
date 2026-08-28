---
name: "rar-cowork-cookbook-adaptive-card-identify-strategic-initiatives"
description: "Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_strategic_initiatives", "rar_sha256": "fbdbe2a4468121db4448421bfbd92c63700797c2473d2802dde484b0b1cf7bb4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 fbdbe2a4468121db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_strategic_initiatives_agent.py` first:

```bash
python3 adaptive_card_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_strategic_initiatives_agent.py   # or on stdin
python3 adaptive_card_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_strategic_initiatives',
    "version": '2.0.1',
    "display_name": 'Identify strategic initiatives Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify strategic initiatives status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81e43e4f7032681f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyStrategicInitiatives'
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
    print(AdaptiveCardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
