---
name: "rar-cowork-cookbook-adaptive-card-develop-sales-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of develop sales strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_sales_strategy", "rar_sha256": "2f4f136722559804ad0623a453c40c3abe1dec1bbfc184cb6200a42b2616ec7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_sales_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_sales_strategy_agent.py` and in the RCI capsule.

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
