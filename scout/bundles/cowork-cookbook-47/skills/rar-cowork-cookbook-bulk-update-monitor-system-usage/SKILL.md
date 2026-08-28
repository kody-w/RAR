---
name: "rar-cowork-cookbook-bulk-update-monitor-system-usage"
description: "Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_system_usage", "rar_sha256": "103089122c306554f3c8cce89f4a6d7edcc3458f422a43c88f35996cecba5314", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_system_usage`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_system_usage_agent.py` and in the RCI capsule.

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

Monitor system usage Bulk Field Update — Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 103089122c306554…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_system_usage_agent.py` first:

```bash
python3 bulk_update_monitor_system_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_system_usage_agent.py   # or on stdin
python3 bulk_update_monitor_system_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system usage Bulk Field Update — Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_system_usage',
    "version": '2.0.1',
    "display_name": 'Monitor system usage Bulk Field Update',
    "description": 'Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-system-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-system-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7ce5e8132f71f333',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-usage'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-monitor-system-usage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorSystemUsage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorSystemUsage'
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
    print(BulkUpdateMonitorSystemUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
