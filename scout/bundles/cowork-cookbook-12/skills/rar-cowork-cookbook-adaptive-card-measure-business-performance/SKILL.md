---
name: "rar-cowork-cookbook-adaptive-card-measure-business-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_measure_business_performance", "rar_sha256": "ab8672c5a7bce13f56962108a98e2c49a35fd03a4a27005082936619280f8a94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 ab8672c5a7bce13f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_measure_business_performance_agent.py` first:

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
    "version": '2.0.0',
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
