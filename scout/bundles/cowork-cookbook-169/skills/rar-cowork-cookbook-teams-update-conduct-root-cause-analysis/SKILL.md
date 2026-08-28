---
name: "rar-cowork-cookbook-teams-update-conduct-root-cause-analysis"
description: "Drafts a Teams channel post on conduct root cause analysis status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_conduct_root_cause_analysis", "rar_sha256": "8b741b54e32584283c1abc561ddc46046f5f0e732ad98f1463185127a7cc2618", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 8b741b54e3258428…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_conduct_root_cause_analysis_agent.py` first:

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
    "version": '2.0.1',
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
