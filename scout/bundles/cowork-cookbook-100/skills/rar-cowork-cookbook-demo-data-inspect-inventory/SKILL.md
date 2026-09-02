---
name: "rar-cowork-cookbook-demo-data-inspect-inventory"
description: "Generates and creates realistic demo records for inspect inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_inspect_inventory", "rar_sha256": "bd76a96b04cc215e97408de96407d30dd051924685e5704872259846baa9e143", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_inspect_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-inspect-inventory:3c4d343bab9fba8b8812d5d110c048893f53c70c4a174f5028dd279aab610439", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_inspect_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_inspect_inventory_agent.py` is
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
