---
name: "rar-cowork-cookbook-teams-update-conduct-root-cause-analysis"
description: "Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_root_cause_analysis", "rar_sha256": "81364704ab6164ad25d13aa44293f4c317bfa9b0aebf537fa7d3893751713bb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_conduct_root_cause_analysis`. The original RAPP
agent is preserved byte-for-byte in `teams_update_conduct_root_cause_analysis_agent.py` and in the RCI capsule.

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
