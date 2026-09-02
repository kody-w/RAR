---
name: "rar-cowork-cookbook-adaptive-card-analyze-marketing-trends"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze marketing trends status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_marketing_trends", "rar_sha256": "d3f7b6c8e4412047b281c01fb8d6c98d5ba819be2975e5c289cc0789d237b75e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_analyze_marketing_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-analyze-marketing-trends:0b349fb8ed7b9c1928c7a1480d3a3cd1e0301c6e00a3fac2acad58731c859616", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_analyze_marketing_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_analyze_marketing_trends_agent.py` is
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
