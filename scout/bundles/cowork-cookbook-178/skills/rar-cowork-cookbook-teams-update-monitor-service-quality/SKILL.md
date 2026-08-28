---
name: "rar-cowork-cookbook-teams-update-monitor-service-quality"
description: "Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_service_quality", "rar_sha256": "9f9bc517306856d6117d71cbff0d48e7a80bdc87ab12c0832d76d6423d219d1d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_service_quality`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_service_quality_agent.py` and in the RCI capsule.

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

Monitor service quality Teams Channel Update — Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 9f9bc517306856d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_service_quality_agent.py` first:

```bash
python3 teams_update_monitor_service_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_service_quality_agent.py   # or on stdin
python3 teams_update_monitor_service_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service quality Teams Channel Update — Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_service_quality',
    "version": '2.0.1',
    "display_name": 'Monitor service quality Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-service-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-service-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db85b2ce9f36e546',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/monitor-service-quality'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-monitor-service-quality', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorServiceQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorServiceQuality'
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
    print(TeamsUpdateMonitorServiceQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
