---
name: "rar-cowork-cookbook-scheduled-brief-analyze-maintenance-costs"
description: "Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_maintenance_costs", "rar_sha256": "a675d65b56c4f9df54eb2259b34b44f63de31b48779f1851d2d1203e74b4d0b0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_maintenance_costs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_maintenance_costs_agent.py` and in the RCI capsule.

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

Analyze maintenance costs Scheduled Email Brief — Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 a675d65b56c4f9df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_maintenance_costs_agent.py` first:

```bash
python3 scheduled_brief_analyze_maintenance_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_maintenance_costs_agent.py   # or on stdin
python3 scheduled_brief_analyze_maintenance_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze maintenance costs Scheduled Email Brief — Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_maintenance_costs',
    "version": '2.0.0',
    "display_name": 'Analyze maintenance costs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-analyze-maintenance-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-maintenance-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e471e47b543643f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-maintenance-costs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-analyze-maintenance-costs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefAnalyzeMaintenanceCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeMaintenanceCosts'
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
    print(ScheduledBriefAnalyzeMaintenanceCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
