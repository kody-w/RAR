---
name: "rar-cowork-cookbook-demo-data-monitor-storage-capacity"
description: "Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_storage_capacity", "rar_sha256": "1bcb678afc46a7b52138f9b325079bbb710c722e9e79d54381f7d17ec2c9d802", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_monitor_storage_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-monitor-storage-capacity:67acecba0d72228e1dcc9e2e5b8ff5dc5416591d1bf5643cd76e057f77927176", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_monitor_storage_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_monitor_storage_capacity_agent.py` is
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

Monitor storage capacity Demo Data Generator — Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 1bcb678afc46a7b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_storage_capacity_agent.py` first:

```bash
python3 demo_data_monitor_storage_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_storage_capacity_agent.py   # or on stdin
python3 demo_data_monitor_storage_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor storage capacity Demo Data Generator — Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_storage_capacity',
    "version": '2.0.0',
    "display_name": 'Monitor storage capacity Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-storage-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93ad4a29e3db8fc1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-storage-capacity'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-storage-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMonitorStorageCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorStorageCapacity'
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
    print(DemoDataMonitorStorageCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
