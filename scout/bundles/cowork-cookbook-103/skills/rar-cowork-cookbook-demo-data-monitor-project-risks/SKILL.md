---
name: "rar-cowork-cookbook-demo-data-monitor-project-risks"
description: "Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_project_risks", "rar_sha256": "cae25e6a1717ce5d10223b98dca32d4f74379eede18f1f23b684e5a6f32b6339", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 cae25e6a1717ce5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_project_risks_agent.py` first:

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
    "version": '2.0.1',
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
