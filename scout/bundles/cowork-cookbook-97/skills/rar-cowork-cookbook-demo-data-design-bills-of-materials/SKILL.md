---
name: "rar-cowork-cookbook-demo-data-design-bills-of-materials"
description: "Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_design_bills_of_materials", "rar_sha256": "55fe5bee556582bf2ecffa3b0ce64f7d6e9c88e7654afccba7220de5e429ff8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_design_bills_of_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-design-bills-of-materials:522caf4de8ce853dfce225a6edb2c819988706295112b906a6cb62db95f672a0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_design_bills_of_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_design_bills_of_materials_agent.py` is
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

Design bills of materials Demo Data Generator — Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 55fe5bee556582bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_design_bills_of_materials_agent.py` first:

```bash
python3 demo_data_design_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_design_bills_of_materials_agent.py   # or on stdin
python3 demo_data_design_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design bills of materials Demo Data Generator — Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_design_bills_of_materials',
    "version": '2.0.0',
    "display_name": 'Design bills of materials Demo Data Generator',
    "description": 'Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-design-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-design-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '053a2891ae685882',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-bills-of-materials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-design-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDesignBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDesignBillsOfMaterials'
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
    print(DemoDataDesignBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
