---
name: "rar-cowork-cookbook-adaptive-card-review-call-center-performance"
description: "Produces a reusable Adaptive Card JSON snapshot of review call center performance status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_call_center_performance", "rar_sha256": "ce0399e6963d59e2fd3fe4417d2898b128684d659c7dad032c07f9d97439608c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 ce0399e6963d59e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_call_center_performance_agent.py` first:

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
    "version": '2.0.1',
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
