---
name: "rar-cowork-cookbook-ppt-exec-monitor-data-synchronization-failures"
description: "Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures", "rar_sha256": "b97469677697893b6174dccb5e5f63263eae5985ba6544bd06e76a1d1685d5c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_data_synchronization_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-data-synchronization-failures:8aad5271f3cf3502f8533f5f3c297a11304596563e30d9c7b437dfc808a143e6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_data_synchronization_failures_agent.py` is
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

Monitor data synchronization failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 b97469677697893b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_data_synchronization_failures_agent.py` first:

```bash
python3 ppt_exec_monitor_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_data_synchronization_failures_agent.py   # or on stdin
python3 ppt_exec_monitor_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor data synchronization failures Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures',
    "version": '2.0.0',
    "display_name": 'Monitor data synchronization failures Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f4af38fd289c6c15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/monitor-data-synchronization-failures'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-monitor-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMonitorDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorDataSynchronizationFailures'
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
    print(PptExecMonitorDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
