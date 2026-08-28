---
name: "rar-cowork-cookbook-teams-update-analyze-and-reconcile-compensation-and-benefits"
description: "Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "46127eab0197e1796842476c2fd2e4d73dfdf40710b51f3ade2219d8577ec464", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and in the RCI capsule.

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

Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 46127eab0197e179…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

```bash
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py   # or on stdin
python3 teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and reconcile compensation and benefits Teams Channel Update — Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits',
    "version": '2.0.1',
    "display_name": 'Analyze and reconcile compensation and benefits Teams Channel Update',
    "description": 'Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-analyze-and-reconcile-compensation-and-benefits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7d197ccf89fd467',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-and-reconcile-compensation-and-benefits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-analyze-and-reconcile-compensation-and-benefits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits'
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
    print(TeamsUpdateAnalyzeAndReconcileCompensationAndBenefits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
