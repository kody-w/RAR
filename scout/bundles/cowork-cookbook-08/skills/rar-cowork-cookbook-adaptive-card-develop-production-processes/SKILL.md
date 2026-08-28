---
name: "rar-cowork-cookbook-adaptive-card-develop-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_production_processes", "rar_sha256": "a4859cd17de95b933668fd1f7c0f32835aadd063a9c1ee51a372eb3d1860d618", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_production_processes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_production_processes_agent.py` and in the RCI capsule.

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
