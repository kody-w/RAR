---
name: "rar-cowork-cookbook-adaptive-card-develop-production-processes"
description: "Produces a reusable Adaptive Card JSON snapshot of develop production processes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_production_processes", "rar_sha256": "0100b2804d3491e8da141bf26470ffb02d4e0a35060486b1176232dcb68ef06c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 0100b2804d3491e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_production_processes_agent.py` first:

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
    "version": '2.0.1',
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
