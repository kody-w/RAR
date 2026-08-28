---
name: "rar-cowork-cookbook-demo-data-design-bills-of-materials"
description: "Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_design_bills_of_materials", "rar_sha256": "93ef7f3fa24738eba952d7f9ec88ecff255121dc17030da8a9cdfae2e1648351", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_design_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_design_bills_of_materials_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 93ef7f3fa24738eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_design_bills_of_materials_agent.py` first:

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
    "version": '2.0.1',
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
