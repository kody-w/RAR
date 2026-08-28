---
name: "rar-cowork-cookbook-adaptive-card-review-call-center-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_call_center_performance", "rar_sha256": "45c5494595505e7094398d16269f753dae31d88221ec70f012c5b620b0c658b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_review_call_center_performance_agent.py` and in the RCI capsule.

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
