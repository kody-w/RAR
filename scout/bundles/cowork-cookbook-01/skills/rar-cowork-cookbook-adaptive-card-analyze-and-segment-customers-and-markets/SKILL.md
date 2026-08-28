---
name: "rar-cowork-cookbook-adaptive-card-analyze-and-segment-customers-and-markets"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets", "rar_sha256": "a08b872d4593128545e7f28df965b17b6cbdadaf6e8a7ac605df11244d005e89", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 a08b872d45931285…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` first:

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
    "version": '2.0.1',
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
