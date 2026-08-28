---
name: "rar-cowork-cookbook-adaptive-card-monitor-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_background_jobs", "rar_sha256": "81ca590a15c4ffe9c2c12cf644b0a378876d3e49ae60b40f519ccc137e514ed7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_background_jobs_agent.py` and in the RCI capsule.

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

Monitor background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 81ca590a15c4ffe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_background_jobs_agent.py` first:

```bash
python3 adaptive_card_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_background_jobs_agent.py   # or on stdin
python3 adaptive_card_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_background_jobs',
    "version": '2.0.1',
    "display_name": 'Monitor background jobs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51fce9282dbb24fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardMonitorBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorBackgroundJobs'
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
    print(AdaptiveCardMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
