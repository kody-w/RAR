---
name: "rar-cowork-cookbook-adaptive-card-monitor-storage-capacity"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_storage_capacity", "rar_sha256": "3c02a12167d11af5b4b1577ada4c3bdc9bc63d855b8efdd2b765db88e70eca40", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_storage_capacity`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_storage_capacity_agent.py` and in the RCI capsule.

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

Monitor storage capacity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 3c02a12167d11af5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_storage_capacity_agent.py` first:

```bash
python3 adaptive_card_monitor_storage_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_storage_capacity_agent.py   # or on stdin
python3 adaptive_card_monitor_storage_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor storage capacity Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_storage_capacity',
    "version": '2.0.0',
    "display_name": 'Monitor storage capacity Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-monitor-storage-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-storage-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f58a493cdbda91d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-storage-capacity'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-monitor-storage-capacity', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardMonitorStorageCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorStorageCapacity'
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
    print(AdaptiveCardMonitorStorageCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
