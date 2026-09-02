---
name: "rar-cowork-cookbook-adaptive-card-analyze-production-costs"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_production_costs", "rar_sha256": "52912eac50178da0ec983a91d7def47caed89e52fd5fbc0fd8d425c48a1a2a82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_analyze_production_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-analyze-production-costs:b6988c11de0aa95545e6610c33b41b599ab1ba04f7f88a5e4aa91db6f1ed0df2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_analyze_production_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_analyze_production_costs_agent.py` is
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

Analyze production costs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 52912eac50178da0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_production_costs_agent.py` first:

```bash
python3 adaptive_card_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_production_costs_agent.py   # or on stdin
python3 adaptive_card_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_production_costs',
    "version": '2.0.0',
    "display_name": 'Analyze production costs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed9ebef808b9d724',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeProductionCosts'
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
    print(AdaptiveCardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
