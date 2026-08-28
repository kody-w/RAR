---
name: "rar-cowork-cookbook-scheduled-brief-estimate-the-cost-of-production"
description: "Schedulable morning-brief email summarizing estimate the cost of production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_estimate_the_cost_of_production", "rar_sha256": "3880d35a21a6a51efc41ea0d79926d26d2dda62c91c7bd945bd13ebb8c80e714", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 3880d35a21a6a51e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_estimate_the_cost_of_production_agent.py` first:

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
    "version": '2.0.1',
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
