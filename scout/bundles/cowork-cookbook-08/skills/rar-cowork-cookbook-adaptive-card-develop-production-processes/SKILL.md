---
name: "rar-cowork-cookbook-adaptive-card-develop-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_production_processes", "rar_sha256": "a4859cd17de95b933668fd1f7c0f32835aadd063a9c1ee51a372eb3d1860d618", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_production_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-production-processes:9e5602e25638685272a5e1143310e75ec9ea683dbc9ab4be55e90cc58f4140f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_production_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_production_processes_agent.py` is
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

Develop production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 a4859cd17de95b93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_production_processes_agent.py` first:

```bash
python3 adaptive_card_develop_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_production_processes_agent.py   # or on stdin
python3 adaptive_card_develop_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_production_processes',
    "version": '2.0.0',
    "display_name": 'Develop production processes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5539ac6afe6d78f1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-production-processes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-develop-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductionProcesses'
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
    print(AdaptiveCardDevelopProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
