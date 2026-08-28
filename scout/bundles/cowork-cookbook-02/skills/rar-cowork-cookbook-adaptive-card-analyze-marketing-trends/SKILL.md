---
name: "rar-cowork-cookbook-adaptive-card-analyze-marketing-trends"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_marketing_trends", "rar_sha256": "d3f7b6c8e4412047b281c01fb8d6c98d5ba819be2975e5c289cc0789d237b75e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 d3f7b6c8e4412047…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_marketing_trends_agent.py` first:

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
    "version": '2.0.0',
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
