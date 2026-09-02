---
name: "rar-cowork-cookbook-bulk-update-monitor-system-usage"
description: "Applies a bulk field update across monitor system usage records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_system_usage", "rar_sha256": "9786c57c176e356af47703180b3962d9711f3e6edc10176d70bb795da711a85d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_monitor_system_usage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-monitor-system-usage:1d0b0ea43314b63cd16934ec534c156b48c573dd2803c73e7cf80ab41e1f82f0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_monitor_system_usage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_monitor_system_usage_agent.py` is
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
