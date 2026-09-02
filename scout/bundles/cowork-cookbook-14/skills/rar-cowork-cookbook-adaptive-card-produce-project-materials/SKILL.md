---
name: "rar-cowork-cookbook-adaptive-card-produce-project-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of produce project materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_produce_project_materials", "rar_sha256": "f062dab0b37864841aaa09982f3b36f7e809c32aca635a79276e8f42754b0c88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_produce_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-produce-project-materials:cf8f16df46a160f95b7677fe9f2f408a0a7d0e8309417fbf59b0ba0b5989355e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_produce_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_produce_project_materials_agent.py` is
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
