---
name: "rar-cowork-cookbook-demo-data-rework-defective-inventory"
description: "Generates and creates realistic demo records for rework defective inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_rework_defective_inventory", "rar_sha256": "2fb675fa9f1d3c5cd085771353ca9d8c082db7f12abde45c8a9e71e8fda7daf3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_rework_defective_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-rework-defective-inventory:52928c2e3f6f71e39501a7ad3c39f0ced6fb95fe346d9272944322742aa30004", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_rework_defective_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_rework_defective_inventory_agent.py` is
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
