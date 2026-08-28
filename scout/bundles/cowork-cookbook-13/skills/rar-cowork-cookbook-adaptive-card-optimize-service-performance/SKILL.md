---
name: "rar-cowork-cookbook-adaptive-card-optimize-service-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_optimize_service_performance", "rar_sha256": "9bd7788872e8d2694a3167a6bd0e8ef82a12315c0920fa23970047e3f698a2fb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_optimize_service_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_optimize_service_performance_agent.py` and in the RCI capsule.

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

Optimize service performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 9bd7788872e8d269…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_optimize_service_performance_agent.py` first:

```bash
python3 adaptive_card_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_optimize_service_performance_agent.py   # or on stdin
python3 adaptive_card_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_optimize_service_performance',
    "version": '2.0.1',
    "display_name": 'Optimize service performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2a33be94c80b864',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardOptimizeServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardOptimizeServicePerformance'
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
    print(AdaptiveCardOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
