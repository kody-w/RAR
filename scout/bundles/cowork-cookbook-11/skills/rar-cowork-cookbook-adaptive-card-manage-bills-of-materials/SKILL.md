---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_materials", "rar_sha256": "efa4285852a26950157e8c140c2d2c038122210e8c3d300d8c223469372c4907", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_bills_of_materials_agent.py` and in the RCI capsule.

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

Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 efa4285852a26950…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_materials',
    "version": '2.0.0',
    "display_name": 'Manage bills of materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72b9e7b8cc16d629',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardManageBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfMaterials'
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
    print(AdaptiveCardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
