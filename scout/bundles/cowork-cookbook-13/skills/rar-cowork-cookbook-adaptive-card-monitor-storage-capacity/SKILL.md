---
name: "rar-cowork-cookbook-adaptive-card-monitor-storage-capacity"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_storage_capacity", "rar_sha256": "ca050ad963b92bd85269799c9bca255b3c87d9a0f834aba7900951002b98b264", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 ca050ad963b92bd8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_storage_capacity_agent.py` first:

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
    "version": '2.0.1',
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
