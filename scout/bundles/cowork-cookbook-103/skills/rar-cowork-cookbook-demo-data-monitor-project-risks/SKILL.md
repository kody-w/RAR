---
name: "rar-cowork-cookbook-demo-data-monitor-project-risks"
description: "Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_project_risks", "rar_sha256": "2e8a17e70125b12c59c60c9b47e79fa6e6b5ce865e3b25e4b577f6626d0135d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_project_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_project_risks_agent.py` and in the RCI capsule.

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

Monitor project risks Demo Data Generator — Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-project-risks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 2e8a17e70125b12c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_project_risks_agent.py` first:

```bash
python3 demo_data_monitor_project_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_project_risks_agent.py   # or on stdin
python3 demo_data_monitor_project_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project risks Demo Data Generator — Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-project-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_project_risks',
    "version": '2.0.0',
    "display_name": 'Monitor project risks Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-project-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-project-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45df551d33406b05',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-monitor-project-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMonitorProjectRisks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorProjectRisks'
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
    print(DemoDataMonitorProjectRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
