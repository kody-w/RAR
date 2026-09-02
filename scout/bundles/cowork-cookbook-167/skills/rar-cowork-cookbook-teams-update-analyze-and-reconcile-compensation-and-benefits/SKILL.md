---
name: "rar-cowork-cookbook-teams-update-analyze-and-reconcile-compensation-and-benefits"
description: "Drafts a Teams channel post on analyze and reconcile compensation and benefits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits", "rar_sha256": "4ad772f55a98a6f5ea356dbd30b2590b378f5643856f500961ea205cb768cf35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-analyze-and-reconcile-compensation-and-benefits:13c0114947143a5ff4a6ce818842b4199e564950f7ccddb344a594c5ce0efa18", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_analyze_and_reconcile_compensation_and_benefits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` and embedded as the fenced Python below (sha256 4ad772f55a98a6f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_analyze_and_reconcile_compensation_and_benefits_agent.py` first:

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
    "version": '2.0.0',
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
