---
name: "rar-cowork-cookbook-scheduled-brief-analyze-and-reconcile-compensation-and-benefits"
description: "Schedulable morning-brief email summarizing analyze and reconcile compensation and benefits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "1927b7b3d701b6f2afbf0fca52e31ad6eb62c8c9c006d1ca752912270522c729", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 1927b7b3d701b6f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

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
    "version": '2.0.1',
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
