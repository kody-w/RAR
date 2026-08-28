---
name: "rar-cowork-cookbook-adaptive-card-define-performance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_performance_strategy", "rar_sha256": "7c78c5ae1c260749f575e690d0f98e935de539c53c223801f35e5546d2da89f7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_performance_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_performance_strategy_agent.py` and in the RCI capsule.

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

Define performance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 7c78c5ae1c260749…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_performance_strategy_agent.py` first:

```bash
python3 adaptive_card_define_performance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_performance_strategy_agent.py   # or on stdin
python3 adaptive_card_define_performance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define performance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_performance_strategy',
    "version": '2.0.1',
    "display_name": 'Define performance strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-performance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd33dc7aa8d17a5b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-performance-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-performance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefinePerformanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePerformanceStrategy'
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
    print(AdaptiveCardDefinePerformanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
