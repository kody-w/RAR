---
name: "rar-cowork-cookbook-adaptive-card-measure-business-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_measure_business_performance", "rar_sha256": "ab8672c5a7bce13f56962108a98e2c49a35fd03a4a27005082936619280f8a94", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_measure_business_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-measure-business-performance:17cbff0d237c11ea8177005e8efe548f70f5e813a11c930eaa09593bc8003eca", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_measure_business_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_measure_business_performance_agent.py` is
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

Measure business performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 ab8672c5a7bce13f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_measure_business_performance_agent.py` first:

```bash
python3 adaptive_card_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_measure_business_performance_agent.py   # or on stdin
python3 adaptive_card_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_measure_business_performance',
    "version": '2.0.0',
    "display_name": 'Measure business performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of measure business performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '679ee90cba66841a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMeasureBusinessPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMeasureBusinessPerformance'
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
    print(AdaptiveCardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
