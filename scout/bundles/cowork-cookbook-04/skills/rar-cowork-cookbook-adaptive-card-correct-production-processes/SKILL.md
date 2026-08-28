---
name: "rar-cowork-cookbook-adaptive-card-correct-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of correct production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_correct_production_processes", "rar_sha256": "4db0fbba4a41f4982a2503c386def931fb43a327bf56295eaeb19fdb5f5d5f5f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 4db0fbba4a41f498…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_correct_production_processes_agent.py` first:

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
    "version": '2.0.0',
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
