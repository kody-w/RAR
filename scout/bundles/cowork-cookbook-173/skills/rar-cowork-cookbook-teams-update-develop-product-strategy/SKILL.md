---
name: "rar-cowork-cookbook-teams-update-develop-product-strategy"
description: "Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_strategy", "rar_sha256": "f2c9dc4b56ce02e16d5a6a946d78d02cda2a859cf9832f55a33e1a8bb5287d08", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_product_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-product-strategy:cd9a71d2df6820b658f10dbc0b2f8b2a5b6791e24d13c894d29def09ebed38aa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_product_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_product_strategy_agent.py` is
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

Develop product strategy Teams Channel Update — Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 f2c9dc4b56ce02e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_strategy_agent.py` first:

```bash
python3 teams_update_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_strategy_agent.py   # or on stdin
python3 teams_update_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Teams Channel Update — Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_strategy',
    "version": '2.0.0',
    "display_name": 'Develop product strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2462aa0d27b90da1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopProductStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductStrategy'
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
    print(TeamsUpdateDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
