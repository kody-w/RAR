---
name: "rar-cowork-cookbook-demo-data-monitor-storage-capacity"
description: "Generates and creates realistic demo records for monitor storage capacity in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_storage_capacity", "rar_sha256": "ca81ec5d52eb519f59d6e2140ac8a4f6e476fca5e1f129e24044f3a41eabf8ed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 ca81ec5d52eb519f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_storage_capacity_agent.py` first:

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
    "version": '2.0.1',
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
