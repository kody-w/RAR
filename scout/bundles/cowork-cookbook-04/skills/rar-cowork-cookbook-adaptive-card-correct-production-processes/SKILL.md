---
name: "rar-cowork-cookbook-adaptive-card-correct-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_correct_production_processes", "rar_sha256": "feec705f8c7cb49ff802cbbf4adaeed66970a640d701e650dd056edaa3a8ba2e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_correct_production_processes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_correct_production_processes_agent.py` and in the RCI capsule.

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

Correct production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 feec705f8c7cb49f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_correct_production_processes_agent.py` first:

```bash
python3 adaptive_card_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_correct_production_processes_agent.py   # or on stdin
python3 adaptive_card_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_correct_production_processes',
    "version": '2.0.1',
    "display_name": 'Correct production processes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af24e4888ad5e13f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardCorrectProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCorrectProductionProcesses'
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
    print(AdaptiveCardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
