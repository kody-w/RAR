---
name: "rar-cowork-cookbook-scheduled-brief-analyze-and-reconcile-compensation-and-benefits"
description: "Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "12adb210b268681ad631e05bce2476966708147e23094477d9ee8fcd698e7470", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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
