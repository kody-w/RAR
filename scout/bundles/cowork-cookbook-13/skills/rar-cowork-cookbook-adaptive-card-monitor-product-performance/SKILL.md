---
name: "rar-cowork-cookbook-adaptive-card-monitor-product-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_product_performance", "rar_sha256": "ee3ae5924785099a13d4caf88c4cb91839ba339865b2258735e12439cb8da0a6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 ee3ae5924785099a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_product_performance_agent.py` first:

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
    "version": '2.0.1',
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
