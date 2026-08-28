---
name: "rar-cowork-cookbook-demo-data-design-bills-of-materials"
description: "Generates and creates realistic demo records for design bills of materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_design_bills_of_materials", "rar_sha256": "55fe5bee556582bf2ecffa3b0ce64f7d6e9c88e7654afccba7220de5e429ff8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
