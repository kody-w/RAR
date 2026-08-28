---
name: "rar-cowork-cookbook-demo-data-monitor-background-jobs"
description: "Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_background_jobs", "rar_sha256": "6bbe02d53a3336a709d4bf840ac486cc24e9bf155085cb21e721dc13294f973a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_background_jobs_agent.py` and in the RCI capsule.

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

Monitor background jobs Demo Data Generator — Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 6bbe02d53a3336a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_background_jobs_agent.py` first:

```bash
python3 demo_data_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_background_jobs_agent.py   # or on stdin
python3 demo_data_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Demo Data Generator — Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_background_jobs',
    "version": '2.0.0',
    "display_name": 'Monitor background jobs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5c27f16a20e64e82',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMonitorBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorBackgroundJobs'
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
    print(DemoDataMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
