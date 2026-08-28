---
name: "rar-cowork-cookbook-adaptive-card-define-implementation-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_implementation_strategy", "rar_sha256": "ed40df4ca5d7dc82bec03b9a82c4fbfa7eb5c30a207699b10d0cd0e5f54fa832", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_implementation_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_implementation_strategy_agent.py` and in the RCI capsule.

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

Define implementation strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_implementation_strategy_agent.py` and embedded as the fenced Python below (sha256 ed40df4ca5d7dc82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_implementation_strategy_agent.py` first:

```bash
python3 adaptive_card_define_implementation_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_implementation_strategy_agent.py   # or on stdin
python3 adaptive_card_define_implementation_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define implementation strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_implementation_strategy',
    "version": '2.0.0',
    "display_name": 'Define implementation strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-implementation-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-implementation-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '958e913397b5fe5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-implementation-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-implementation-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDefineImplementationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineImplementationStrategy'
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
    print(AdaptiveCardDefineImplementationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
