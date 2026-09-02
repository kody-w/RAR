---
name: "rar-cowork-cookbook-adaptive-card-develop-sales-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_sales_strategy", "rar_sha256": "2f4f136722559804ad0623a453c40c3abe1dec1bbfc184cb6200a42b2616ec7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_sales_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-sales-strategy:f657db02fd6e0b7584bb3e5b774ee4c0b8e1a6928060d3cb6d5da79d8352f23c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_sales_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_sales_strategy_agent.py` is
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

Develop sales strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_sales_strategy_agent.py` and embedded as the fenced Python below (sha256 2f4f136722559804…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_sales_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_sales_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_sales_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_sales_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_sales_strategy',
    "version": '2.0.0',
    "display_name": 'Develop sales strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-develop-sales-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-sales-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77068d7b46c48b37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-sales-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-develop-sales-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDevelopSalesStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopSalesStrategy'
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
    print(AdaptiveCardDevelopSalesStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
