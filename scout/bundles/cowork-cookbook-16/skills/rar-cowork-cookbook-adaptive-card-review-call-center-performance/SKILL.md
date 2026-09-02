---
name: "rar-cowork-cookbook-adaptive-card-review-call-center-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_call_center_performance", "rar_sha256": "45c5494595505e7094398d16269f753dae31d88221ec70f012c5b620b0c658b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_review_call_center_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-review-call-center-performance:843c479dc3f7f3a6ceb79f0893a999fe475a8cd6d46d2afb7d060e35a35042fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_review_call_center_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_review_call_center_performance_agent.py` is
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

Review call center performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 45c5494595505e70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_call_center_performance_agent.py` first:

```bash
python3 adaptive_card_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_review_call_center_performance_agent.py   # or on stdin
python3 adaptive_card_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_review_call_center_performance',
    "version": '2.0.0',
    "display_name": 'Review call center performance Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '583827d0d92a41a4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardReviewCallCenterPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReviewCallCenterPerformance'
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
    print(AdaptiveCardReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
