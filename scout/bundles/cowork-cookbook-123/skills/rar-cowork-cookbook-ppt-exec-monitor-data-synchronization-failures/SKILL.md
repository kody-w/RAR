---
name: "rar-cowork-cookbook-ppt-exec-monitor-data-synchronization-failures"
description: "Generates an executive-ready PowerPoint deck on monitor data synchronization failures status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_data_synchronization_failures", "rar_sha256": "53c8b4ee202fe0537ac3ba5e2aa322d1f455ef8bd1f0891282254602f46d7fed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 53c8b4ee202fe053…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_data_synchronization_failures_agent.py` first:

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
    "version": '2.0.1',
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
