---
name: "rar-cowork-cookbook-ppt-exec-plan-risks-and-opportunities"
description: "Generates an executive-ready PowerPoint deck on plan risks and opportunities status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_risks_and_opportunities", "rar_sha256": "0fcc4a4cc39af35a4414666715ccaf8819813037193ba2737c5a5cd471dacacd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_risks_and_opportunities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-risks-and-opportunities:a69b46b518ae7315c73e32ebb50960f9777dddb06b3d5280b8bb481375047238", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_risks_and_opportunities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_risks_and_opportunities_agent.py` is
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
