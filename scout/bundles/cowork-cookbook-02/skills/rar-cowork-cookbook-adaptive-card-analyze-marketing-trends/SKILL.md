---
name: "rar-cowork-cookbook-adaptive-card-analyze-marketing-trends"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_marketing_trends", "rar_sha256": "f5726175e7bfc973edc733351b5f9aab164c2dfcf9d8c678603188d86c36891f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_marketing_trends`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_marketing_trends_agent.py` and in the RCI capsule.

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

Analyze marketing trends Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 f5726175e7bfc973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_marketing_trends_agent.py` first:

```bash
python3 adaptive_card_analyze_marketing_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_marketing_trends_agent.py   # or on stdin
python3 adaptive_card_analyze_marketing_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze marketing trends Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_marketing_trends',
    "version": '2.0.1',
    "display_name": 'Analyze marketing trends Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-marketing-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-marketing-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ec530e0e87eb43c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-analyze-marketing-trends', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeMarketingTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeMarketingTrends'
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
    print(AdaptiveCardAnalyzeMarketingTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
