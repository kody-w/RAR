---
name: "rar-cowork-cookbook-adaptive-card-monitor-product-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor product performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_product_performance", "rar_sha256": "f15f52e7c5d6b01da5c2102cb89d63a53aa82f2ff57c2c991ab678ad95be4e51", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_monitor_product_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-monitor-product-performance:d6e07d6a92992fbaf6c9a2ec8765626272ca0ad87f4348b8a13ae29151bf6ac4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_monitor_product_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_monitor_product_performance_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
