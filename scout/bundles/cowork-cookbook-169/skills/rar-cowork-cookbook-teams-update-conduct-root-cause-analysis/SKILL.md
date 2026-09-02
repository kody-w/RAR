---
name: "rar-cowork-cookbook-teams-update-conduct-root-cause-analysis"
description: "Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_root_cause_analysis", "rar_sha256": "81364704ab6164ad25d13aa44293f4c317bfa9b0aebf537fa7d3893751713bb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_conduct_root_cause_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-conduct-root-cause-analysis:87cd350409aba0cfcc2edfe4a5821c76ccdc2a0c831513b3ce409db38f73672d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_conduct_root_cause_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_conduct_root_cause_analysis_agent.py` is
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

Conduct root cause analysis Teams Channel Update — Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 81364704ab6164ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_root_cause_analysis_agent.py` first:

```bash
python3 teams_update_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_conduct_root_cause_analysis_agent.py   # or on stdin
python3 teams_update_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Teams Channel Update — Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_conduct_root_cause_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct root cause analysis Teams Channel Update',
    "description": 'Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07a4999c915a08e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateConductRootCauseAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConductRootCauseAnalysis'
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
    print(TeamsUpdateConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
