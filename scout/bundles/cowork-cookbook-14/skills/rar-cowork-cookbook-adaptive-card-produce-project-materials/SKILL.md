---
name: "rar-cowork-cookbook-adaptive-card-produce-project-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_produce_project_materials", "rar_sha256": "621c37ae2d92f47ccd5478ac81dde04555eb64f156dcdf900b48898f88197a99", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_produce_project_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_produce_project_materials_agent.py` and in the RCI capsule.

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

Produce project materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 621c37ae2d92f47c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_produce_project_materials_agent.py` first:

```bash
python3 adaptive_card_produce_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_produce_project_materials_agent.py   # or on stdin
python3 adaptive_card_produce_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce project materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_produce_project_materials',
    "version": '2.0.1',
    "display_name": 'Produce project materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-produce-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4673df020e6f6b08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/produce-project-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-produce-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardProduceProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProduceProjectMaterials'
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
    print(AdaptiveCardProduceProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
