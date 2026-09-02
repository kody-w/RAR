---
name: "rar-cowork-cookbook-dashboard-set-employee-growth-goals"
description: "Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_employee_growth_goals", "rar_sha256": "3830df1a6c11e9423c128cb46842c521452504cfe16b3c65d56514654f381ad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_set_employee_growth_goals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-set-employee-growth-goals:029c592d4fbbbe17a1bc73791d4688a843ad8f0fe446825765f4eb44cd5d9f7d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_set_employee_growth_goals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_set_employee_growth_goals_agent.py` is
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

Set employee growth goals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 3830df1a6c11e942…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_employee_growth_goals_agent.py` first:

```bash
python3 dashboard_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_employee_growth_goals_agent.py   # or on stdin
python3 dashboard_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_employee_growth_goals',
    "version": '2.0.0',
    "display_name": 'Set employee growth goals Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13c80fc5bd768cdb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSetEmployeeGrowthGoals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetEmployeeGrowthGoals'
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
    print(DashboardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
