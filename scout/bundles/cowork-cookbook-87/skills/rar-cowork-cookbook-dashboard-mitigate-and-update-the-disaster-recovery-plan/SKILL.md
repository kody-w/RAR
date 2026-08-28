---
name: "rar-cowork-cookbook-dashboard-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "f7ba9923639ed1d3346e2dffda6a8e5463c7733c14fd3f7ae3f0354aaae2d342", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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
