---
name: "rar-cowork-cookbook-demo-data-manage-the-initial-synchronization-of-data"
description: "Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data", "rar_sha256": "8b88291be4c3cee5f3732cecf21e6a46dbf838adf79a0b1fc412be68b162079f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 8b88291be4c3cee5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data',
    "version": '2.0.1',
    "display_name": 'Manage the initial synchronization of data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d3321d0db81c317',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageTheInitialSynchronizationOfData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageTheInitialSynchronizationOfData'
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
    print(DemoDataManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
