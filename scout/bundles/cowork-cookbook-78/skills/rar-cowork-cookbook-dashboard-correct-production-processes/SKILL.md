---
name: "rar-cowork-cookbook-dashboard-correct-production-processes"
description: "Produces a self-contained interactive HTML dashboard for correct production processes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_correct_production_processes", "rar_sha256": "2743fbb338ef9e47f71c0de9eef6679579066bfbf730012484644bfacc654d0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_correct_production_processes`. The original RAPP
agent is preserved byte-for-byte in `dashboard_correct_production_processes_agent.py` and in the RCI capsule.

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
