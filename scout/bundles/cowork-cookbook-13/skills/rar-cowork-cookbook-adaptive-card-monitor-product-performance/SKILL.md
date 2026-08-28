---
name: "rar-cowork-cookbook-adaptive-card-monitor-product-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_product_performance", "rar_sha256": "f15f52e7c5d6b01da5c2102cb89d63a53aa82f2ff57c2c991ab678ad95be4e51", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_product_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_product_performance_agent.py` and in the RCI capsule.

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

Monitor product performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 f15f52e7c5d6b01d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_product_performance_agent.py` first:

```bash
python3 adaptive_card_monitor_product_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_product_performance_agent.py   # or on stdin
python3 adaptive_card_monitor_product_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_product_performance',
    "version": '2.0.0',
    "display_name": 'Monitor product performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-monitor-product-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae33de003a8ae550',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-monitor-product-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMonitorProductPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorProductPerformance'
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
    print(AdaptiveCardMonitorProductPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
