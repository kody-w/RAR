---
name: "rar-cowork-cookbook-adaptive-card-produce-project-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_produce_project_materials", "rar_sha256": "f062dab0b37864841aaa09982f3b36f7e809c32aca635a79276e8f42754b0c88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 f062dab0b3786484…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_produce_project_materials_agent.py` first:

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
    "version": '2.0.0',
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
