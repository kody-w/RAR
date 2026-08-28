---
name: "rar-cowork-cookbook-ppt-exec-plan-logistics-and-distribution"
description: "Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_logistics_and_distribution", "rar_sha256": "462e9dbd98897fe55500de6c639cc79eb0f633d54ed34cfc5c6dfdab0f27a1ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_logistics_and_distribution`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_logistics_and_distribution_agent.py` and in the RCI capsule.

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

Plan logistics and distribution Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 462e9dbd98897fe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_logistics_and_distribution_agent.py` first:

```bash
python3 ppt_exec_plan_logistics_and_distribution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_logistics_and_distribution_agent.py   # or on stdin
python3 ppt_exec_plan_logistics_and_distribution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan logistics and distribution Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_logistics_and_distribution',
    "version": '2.0.0',
    "display_name": 'Plan logistics and distribution Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-logistics-and-distribution',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-logistics-and-distribution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '784ff6e1d0cc5f91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-logistics-and-distribution'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-logistics-and-distribution', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPlanLogisticsAndDistribution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanLogisticsAndDistribution'
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
    print(PptExecPlanLogisticsAndDistribution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
