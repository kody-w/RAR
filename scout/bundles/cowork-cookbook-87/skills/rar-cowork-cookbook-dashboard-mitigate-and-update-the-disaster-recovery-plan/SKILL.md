---
name: "rar-cowork-cookbook-dashboard-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "f7ba9923639ed1d3346e2dffda6a8e5463c7733c14fd3f7ae3f0354aaae2d342", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-mitigate-and-update-the-disaster-recovery-plan:5e3b661a9f48705b27c8f8fbc79455ba894d1b0c56934882bcaa2bda903f1b03", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` is
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

Mitigate and update the disaster recovery plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 f7ba9923639ed1d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

```bash
python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py   # or on stdin
python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mitigate and update the disaster recovery plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Mitigate and update the disaster recovery plan Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b05ddac286ed9a54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/mitigate-and-update-the-disaster-recovery-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-mitigate-and-update-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardMitigateAndUpdateTheDisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMitigateAndUpdateTheDisasterRecoveryPlan'
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
    print(DashboardMitigateAndUpdateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
