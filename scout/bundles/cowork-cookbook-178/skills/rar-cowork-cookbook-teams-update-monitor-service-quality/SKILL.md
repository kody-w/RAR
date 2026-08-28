---
name: "rar-cowork-cookbook-teams-update-monitor-service-quality"
description: "Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_service_quality", "rar_sha256": "7faf13f3eb52ea74afe1234fadeacea603e66b30758ab8145b94f2e7be15ae79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 7faf13f3eb52ea74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_service_quality_agent.py` first:

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
    "version": '2.0.0',
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
