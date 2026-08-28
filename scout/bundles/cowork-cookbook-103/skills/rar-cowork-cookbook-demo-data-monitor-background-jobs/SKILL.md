---
name: "rar-cowork-cookbook-demo-data-monitor-background-jobs"
description: "Generates and creates realistic demo records for monitor background jobs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_background_jobs", "rar_sha256": "eb4c929f028a3177906609934e5185a921bab76040d95a413ac88c26e391551b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 eb4c929f028a3177…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_background_jobs_agent.py` first:

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
    "version": '2.0.1',
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
