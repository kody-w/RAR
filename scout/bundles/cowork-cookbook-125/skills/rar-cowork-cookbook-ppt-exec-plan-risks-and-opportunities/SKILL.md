---
name: "rar-cowork-cookbook-ppt-exec-plan-risks-and-opportunities"
description: "Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_risks_and_opportunities", "rar_sha256": "afa662bc03d2eb746b78e68fee61dd78dd43806a2f5193c9bd80f9a87df6d826", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 afa662bc03d2eb74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_risks_and_opportunities_agent.py` first:

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
    "version": '2.0.1',
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
