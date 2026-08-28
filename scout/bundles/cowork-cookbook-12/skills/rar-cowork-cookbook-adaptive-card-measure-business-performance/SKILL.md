---
name: "rar-cowork-cookbook-adaptive-card-measure-business-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_measure_business_performance", "rar_sha256": "9bc83b1ee4595499037c098e112d8f7ff18a219333aa5a5e41ca595e60890466", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_measure_business_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_measure_business_performance_agent.py` and in the RCI capsule.

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

Measure business performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 9bc83b1ee4595499…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_measure_business_performance_agent.py` first:

```bash
python3 adaptive_card_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_measure_business_performance_agent.py   # or on stdin
python3 adaptive_card_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_measure_business_performance',
    "version": '2.0.1',
    "display_name": 'Measure business performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '679ee90cba66841a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMeasureBusinessPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMeasureBusinessPerformance'
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
    print(AdaptiveCardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
