---
name: "rar-cowork-cookbook-dashboard-set-operational-targets"
description: "Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_operational_targets", "rar_sha256": "8033c75a96a4b9a55d513dc073f57e9fccd32ae70e502fc15f0444d482c95d8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_set_operational_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-set-operational-targets:886b0911ddf8b379445f0cb35c882a09b50bb09d18b821711c5959681f01a8ef", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_set_operational_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_set_operational_targets_agent.py` is
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

Set operational targets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 8033c75a96a4b9a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_operational_targets_agent.py` first:

```bash
python3 dashboard_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_operational_targets_agent.py   # or on stdin
python3 dashboard_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_operational_targets',
    "version": '2.0.0',
    "display_name": 'Set operational targets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb8987ce2cd89391',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSetOperationalTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetOperationalTargets'
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
    print(DashboardSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
