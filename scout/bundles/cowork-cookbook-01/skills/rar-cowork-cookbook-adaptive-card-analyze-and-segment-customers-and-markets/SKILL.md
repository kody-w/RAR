---
name: "rar-cowork-cookbook-adaptive-card-analyze-and-segment-customers-and-markets"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze and segment customers and markets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets", "rar_sha256": "59500d13fac16ccad5ee49730020f0408891d2be6c886aa496c567f5198668e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_analyze_and_segment_customers_and_markets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-analyze-and-segment-customers-and-markets:7da58c3dd75faf1fc479dfa630f4b143528885a3f484cbd0a1391ec45c195287", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` is
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
