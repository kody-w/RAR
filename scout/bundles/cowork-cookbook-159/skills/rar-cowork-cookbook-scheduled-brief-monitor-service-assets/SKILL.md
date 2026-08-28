---
name: "rar-cowork-cookbook-scheduled-brief-monitor-service-assets"
description: "Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_service_assets", "rar_sha256": "6aa5cfc4259114a0a1accaf92433d96e14109cbd84af88e6ecb0a876b235899a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 6aa5cfc4259114a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_service_assets_agent.py` first:

```bash
python3 scheduled_brief_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_service_assets_agent.py   # or on stdin
python3 scheduled_brief_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_service_assets',
    "version": '2.0.1',
    "display_name": 'Monitor service assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b39251510a4eaee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorServiceAssets'
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
    print(ScheduledBriefMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
