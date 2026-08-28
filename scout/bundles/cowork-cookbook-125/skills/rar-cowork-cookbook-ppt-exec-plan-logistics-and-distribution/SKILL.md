---
name: "rar-cowork-cookbook-ppt-exec-plan-logistics-and-distribution"
description: "Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_logistics_and_distribution", "rar_sha256": "f87950f6411bf5c24b9d2f236b7fe2ee0cf6cbd35404b03a06e3d05b825f701f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 f87950f6411bf5c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_logistics_and_distribution_agent.py` first:

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
    "version": '2.0.1',
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
