---
name: "rar-cowork-cookbook-scheduled-brief-estimate-the-cost-of-production"
description: "Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production", "rar_sha256": "ff9e8b307416967376b333afdf7735d5063807a7700a6c29e4138c90112933dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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
