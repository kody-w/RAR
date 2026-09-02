---
name: "rar-cowork-cookbook-ppt-exec-plan-logistics-and-distribution"
description: "Generates an executive-ready PowerPoint deck on plan logistics and distribution status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_logistics_and_distribution", "rar_sha256": "462e9dbd98897fe55500de6c639cc79eb0f633d54ed34cfc5c6dfdab0f27a1ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_logistics_and_distribution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-logistics-and-distribution:fd7d1732dd1096629bd33a91eff33f34a34bc610a8fe46024b331e606d4d17b2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_logistics_and_distribution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_logistics_and_distribution_agent.py` is
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
