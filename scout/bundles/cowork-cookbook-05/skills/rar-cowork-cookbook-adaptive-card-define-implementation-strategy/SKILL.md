---
name: "rar-cowork-cookbook-adaptive-card-define-implementation-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define implementation strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_implementation_strategy", "rar_sha256": "ed40df4ca5d7dc82bec03b9a82c4fbfa7eb5c30a207699b10d0cd0e5f54fa832", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_implementation_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-implementation-strategy:60e25144c3d63b959e3dc2924cae247e6984c6fe7683351104d3cb6f7b9d9b4c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_implementation_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_implementation_strategy_agent.py` is
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
