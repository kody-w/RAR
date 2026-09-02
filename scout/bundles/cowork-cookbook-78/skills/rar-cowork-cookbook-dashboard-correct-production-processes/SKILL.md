---
name: "rar-cowork-cookbook-dashboard-correct-production-processes"
description: "Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_production_processes", "rar_sha256": "2743fbb338ef9e47f71c0de9eef6679579066bfbf730012484644bfacc654d0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_correct_production_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-correct-production-processes:cf27f39436ad7e9157e19cfa92e67927f25cfdff9f41515ffc36fc716cfe714c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_correct_production_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_correct_production_processes_agent.py` is
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

Correct production processes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 2743fbb338ef9e47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_correct_production_processes_agent.py` first:

```bash
python3 dashboard_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_correct_production_processes_agent.py   # or on stdin
python3 dashboard_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_correct_production_processes',
    "version": '2.0.0',
    "display_name": 'Correct production processes Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6df2df1b57822181',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCorrectProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCorrectProductionProcesses'
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
    print(DashboardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
