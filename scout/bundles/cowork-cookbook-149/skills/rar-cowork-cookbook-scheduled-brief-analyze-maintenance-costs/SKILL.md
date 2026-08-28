---
name: "rar-cowork-cookbook-scheduled-brief-analyze-maintenance-costs"
description: "Schedulable morning-brief email summarizing analyze maintenance costs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_maintenance_costs", "rar_sha256": "8d372bcf15d70163659d85d35a3d745e6d232956dd6aadc19becab403adb0798", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_maintenance_costs_agent.py` and embedded as the fenced Python below (sha256 8d372bcf15d70163…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_maintenance_costs_agent.py` first:

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
    "version": '2.0.1',
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
