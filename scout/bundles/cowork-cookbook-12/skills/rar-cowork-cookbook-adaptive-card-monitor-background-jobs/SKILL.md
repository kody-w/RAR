---
name: "rar-cowork-cookbook-adaptive-card-monitor-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_background_jobs", "rar_sha256": "5f5978346dd372e146bce071abd8419abe6fbcf7021987675ae77fd158d4f511", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 5f5978346dd372e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_background_jobs_agent.py` first:

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
    "version": '2.0.0',
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
