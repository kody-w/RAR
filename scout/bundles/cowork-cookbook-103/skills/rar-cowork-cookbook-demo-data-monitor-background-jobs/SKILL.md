---
name: "rar-cowork-cookbook-demo-data-monitor-background-jobs"
description: "Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_background_jobs", "rar_sha256": "6bbe02d53a3336a709d4bf840ac486cc24e9bf155085cb21e721dc13294f973a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_monitor_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-monitor-background-jobs:e36c79e49634208c82936fa3a8813d2271e67a8f5b0da9019e19601adf43ffee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_monitor_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_monitor_background_jobs_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
