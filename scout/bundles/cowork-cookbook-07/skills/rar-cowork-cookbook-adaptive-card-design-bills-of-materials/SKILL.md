---
name: "rar-cowork-cookbook-adaptive-card-design-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_design_bills_of_materials", "rar_sha256": "f7604896f5e6bd13dcb3f2810f0601357d1d086535f74780f2ca44d0615b2301", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_design_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_design_bills_of_materials_agent.py` and in the RCI capsule.

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

Design bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 f7604896f5e6bd13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_design_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_design_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_design_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_design_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_design_bills_of_materials',
    "version": '2.0.1',
    "display_name": 'Design bills of materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-design-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '498ac3992bbe93e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-design-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDesignBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDesignBillsOfMaterials'
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
    print(AdaptiveCardDesignBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
