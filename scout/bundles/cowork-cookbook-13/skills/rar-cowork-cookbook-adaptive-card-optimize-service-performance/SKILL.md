---
name: "rar-cowork-cookbook-adaptive-card-optimize-service-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of optimize service performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_optimize_service_performance", "rar_sha256": "f740e92c770489aa642ba4923bb338eb0dd16a33d3daa85a032f0e99913415b8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 f740e92c770489aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_optimize_service_performance_agent.py` first:

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
    "version": '2.0.0',
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
