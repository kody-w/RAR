---
name: "rar-cowork-cookbook-adaptive-card-monitor-storage-capacity"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor storage capacity status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_storage_capacity", "rar_sha256": "3c02a12167d11af5b4b1577ada4c3bdc9bc63d855b8efdd2b765db88e70eca40", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_monitor_storage_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-monitor-storage-capacity:7cee177c01a6b64828e756d81cf60c3f1a86518e973f0d416e950ccb5948c54b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_monitor_storage_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_monitor_storage_capacity_agent.py` is
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
