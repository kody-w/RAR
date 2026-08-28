---
name: "rar-cowork-cookbook-teams-update-monitor-product-feedback"
description: "Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_product_feedback", "rar_sha256": "164cb46643a924dcb55f241434673e5ea40cd815241ff5cc46a38fba481df59b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_product_feedback`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_product_feedback_agent.py` and in the RCI capsule.

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

Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 164cb46643a924dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_product_feedback_agent.py` first:

```bash
python3 teams_update_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_product_feedback_agent.py   # or on stdin
python3 teams_update_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_product_feedback',
    "version": '2.0.0',
    "display_name": 'Monitor product feedback Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f61b82d5d522ff0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorProductFeedback(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorProductFeedback'
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
    print(TeamsUpdateMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
