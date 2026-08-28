---
name: "rar-cowork-cookbook-ppt-exec-monitor-data-synchronization-failures"
description: "Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures", "rar_sha256": "b97469677697893b6174dccb5e5f63263eae5985ba6544bd06e76a1d1685d5c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_data_synchronization_failures_agent.py` and in the RCI capsule.

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
