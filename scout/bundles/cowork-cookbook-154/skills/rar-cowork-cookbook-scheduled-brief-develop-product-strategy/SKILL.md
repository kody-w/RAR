---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-strategy"
description: "Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_strategy", "rar_sha256": "42d36f533af409ec021a140853fd71911c8754b5650a1d46f21bd738acb22441", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_product_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-product-strategy:b32f5de2e0c41dd3b5dab836d6d68e32377b5e7fcb6ee932443ddf2c978df4e5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_product_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_product_strategy_agent.py` is
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

Develop product strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 42d36f533af409ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_strategy',
    "version": '2.0.0',
    "display_name": 'Develop product strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e2bace9a49a50497',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopProductStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductStrategy'
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
    print(ScheduledBriefDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
