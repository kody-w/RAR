---
name: "rar-cowork-cookbook-demo-data-rework-defective-inventory"
description: "Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_rework_defective_inventory", "rar_sha256": "2fb675fa9f1d3c5cd085771353ca9d8c082db7f12abde45c8a9e71e8fda7daf3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_rework_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_rework_defective_inventory_agent.py` and in the RCI capsule.

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

Rework defective inventory Demo Data Generator — Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_rework_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 2fb675fa9f1d3c5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_rework_defective_inventory_agent.py` first:

```bash
python3 demo_data_rework_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_rework_defective_inventory_agent.py   # or on stdin
python3 demo_data_rework_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rework defective inventory Demo Data Generator — Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_rework_defective_inventory',
    "version": '2.0.0',
    "display_name": 'Rework defective inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-rework-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-rework-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '134b32f75bd85902',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/rework-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-rework-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataReworkDefectiveInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReworkDefectiveInventory'
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
    print(DemoDataReworkDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
