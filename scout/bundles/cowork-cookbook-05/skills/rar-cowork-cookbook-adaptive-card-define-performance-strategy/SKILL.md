---
name: "rar-cowork-cookbook-adaptive-card-define-performance-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_performance_strategy", "rar_sha256": "f0d84f31540b1f1e0d9a4db3f92ba02a6bfec349e8ae63416fabb70575167514", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_performance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-performance-strategy:3fd87d66ffa15d0ea6e490e71e0635b6af96aaa232abaf7dd80fe69d519d6492", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_performance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_performance_strategy_agent.py` is
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

Define performance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 f0d84f31540b1f1e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_performance_strategy_agent.py` first:

```bash
python3 adaptive_card_define_performance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_performance_strategy_agent.py   # or on stdin
python3 adaptive_card_define_performance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define performance strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_performance_strategy',
    "version": '2.0.0',
    "display_name": 'Define performance strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define performance strategy status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-performance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd33dc7aa8d17a5b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-performance-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-performance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDefinePerformanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePerformanceStrategy'
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
    print(AdaptiveCardDefinePerformanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
