---
name: "rar-cowork-cookbook-demo-data-monitor-storage-capacity"
description: "Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_storage_capacity", "rar_sha256": "1bcb678afc46a7b52138f9b325079bbb710c722e9e79d54381f7d17ec2c9d802", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_storage_capacity`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_storage_capacity_agent.py` and in the RCI capsule.

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
