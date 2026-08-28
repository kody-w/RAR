---
name: "rar-cowork-cookbook-bulk-update-monitor-system-usage"
description: "Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_system_usage", "rar_sha256": "9786c57c176e356af47703180b3962d9711f3e6edc10176d70bb795da711a85d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 9786c57c176e356a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_system_usage_agent.py` first:

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
    "version": '2.0.0',
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
