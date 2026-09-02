---
name: "rar-cowork-cookbook-demo-data-monitor-project-risks"
description: "Generates and creates realistic demo records for monitor project risks in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_project_risks", "rar_sha256": "2e8a17e70125b12c59c60c9b47e79fa6e6b5ce865e3b25e4b577f6626d0135d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_monitor_project_risks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-monitor-project-risks:ec55e4352b74e745452ca2fd96b1c88ce2804e88275724c8922cc441cee9cd2b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_monitor_project_risks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_monitor_project_risks_agent.py` is
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
