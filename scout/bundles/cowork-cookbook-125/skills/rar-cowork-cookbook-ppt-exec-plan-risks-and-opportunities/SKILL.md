---
name: "rar-cowork-cookbook-ppt-exec-plan-risks-and-opportunities"
description: "Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_risks_and_opportunities", "rar_sha256": "0fcc4a4cc39af35a4414666715ccaf8819813037193ba2737c5a5cd471dacacd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_risks_and_opportunities`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_risks_and_opportunities_agent.py` and in the RCI capsule.

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

Plan risks and opportunities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 0fcc4a4cc39af35a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_risks_and_opportunities_agent.py` first:

```bash
python3 ppt_exec_plan_risks_and_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_risks_and_opportunities_agent.py   # or on stdin
python3 ppt_exec_plan_risks_and_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan risks and opportunities Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_risks_and_opportunities',
    "version": '2.0.0',
    "display_name": 'Plan risks and opportunities Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-plan-risks-and-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0ef4faf09f1a9d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-risks-and-opportunities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-risks-and-opportunities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPlanRisksAndOpportunities(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanRisksAndOpportunities'
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
    print(PptExecPlanRisksAndOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
