---
name: "rar-cowork-cookbook-adaptive-card-analyze-and-segment-customers-and-markets"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets", "rar_sha256": "59500d13fac16ccad5ee49730020f0408891d2be6c886aa496c567f5198668e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` and in the RCI capsule.

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

Analyze and segment customers and markets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 59500d13fac16cca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` first:

```bash
python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py   # or on stdin
python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment customers and markets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets',
    "version": '2.0.0',
    "display_name": 'Analyze and segment customers and markets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-analyze-and-segment-customers-and-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46aecd55ade25e36',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-customers-and-markets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-analyze-and-segment-customers-and-markets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets'
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
    print(AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
