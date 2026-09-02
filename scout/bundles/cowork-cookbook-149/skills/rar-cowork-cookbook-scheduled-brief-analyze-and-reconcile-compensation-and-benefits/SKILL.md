---
name: "rar-cowork-cookbook-scheduled-brief-analyze-and-reconcile-compensation-and-benefits"
description: "Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "12adb210b268681ad631e05bce2476966708147e23094477d9ee8fcd698e7470", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-and-reconcile-compensation-and-benefits:933fb851656d5329e23a3e6f4fc8a031006db47db2309ab0a0d2aea1cd09f718", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` is
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

Analyze and reconcile compensation and benefits Scheduled Email Brief — Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 12adb210b268681a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Scheduled Email Brief — Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits',
    "version": '2.0.0',
    "display_name": 'Analyze and reconcile compensation and benefits Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ce4b9558c285d583',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits'
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
    print(ScheduledBriefAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
