---
name: "rar-cowork-cookbook-adaptive-card-design-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_design_bills_of_materials", "rar_sha256": "7d55f3b6af8ec1adf7cf34159d8c1f47164dadccf4cf33863ad87b04bf5a3040", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 7d55f3b6af8ec1ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_design_bills_of_materials_agent.py` first:

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
    "version": '2.0.0',
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
