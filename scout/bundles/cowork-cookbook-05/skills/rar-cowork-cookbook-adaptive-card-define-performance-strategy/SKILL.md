---
name: "rar-cowork-cookbook-adaptive-card-define-performance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_performance_strategy", "rar_sha256": "f0d84f31540b1f1e0d9a4db3f92ba02a6bfec349e8ae63416fabb70575167514", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 f0d84f31540b1f1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_performance_strategy_agent.py` first:

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
    "version": '2.0.0',
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
