---
name: "rar-cowork-cookbook-demo-data-inspect-inventory"
description: "Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_inspect_inventory", "rar_sha256": "bd76a96b04cc215e97408de96407d30dd051924685e5704872259846baa9e143", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_inspect_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_inspect_inventory_agent.py` and in the RCI capsule.

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

Inspect inventory Demo Data Generator — Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_inspect_inventory_agent.py` and embedded as the fenced Python below (sha256 bd76a96b04cc215e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_inspect_inventory_agent.py` first:

```bash
python3 demo_data_inspect_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_inspect_inventory_agent.py   # or on stdin
python3 demo_data_inspect_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inspect inventory Demo Data Generator — Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-inspect-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_inspect_inventory',
    "version": '2.0.0',
    "display_name": 'Inspect inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-inspect-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-inspect-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1aebb71234df1c27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/inspect-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-inspect-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataInspectInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataInspectInventory'
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
    print(DemoDataInspectInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
