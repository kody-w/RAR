---
name: "rar-cowork-cookbook-scheduled-brief-estimate-the-cost-of-production"
description: "Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production", "rar_sha256": "ff9e8b307416967376b333afdf7735d5063807a7700a6c29e4138c90112933dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_estimate_the_cost_of_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-estimate-the-cost-of-production:96f6c996359ed85c03d349229eec609732f78f6b137731c4028c1f68ee2945ee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_estimate_the_cost_of_production_agent.py` is
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

Estimate the cost of production Scheduled Email Brief — Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 ff9e8b3074169673…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_estimate_the_cost_of_production_agent.py` first:

```bash
python3 scheduled_brief_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_estimate_the_cost_of_production_agent.py   # or on stdin
python3 scheduled_brief_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Scheduled Email Brief — Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production',
    "version": '2.0.0',
    "display_name": 'Estimate the cost of production Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e808c70ffdc5b9b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefEstimateTheCostOfProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEstimateTheCostOfProduction'
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
    print(ScheduledBriefEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
