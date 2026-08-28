---
name: "rar-cowork-cookbook-dashboard-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a self-contained interactive HTML dashboard for mitigate and update the disaster recovery plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "68b9e7e56f750717824454feeaab3250c5dbed313b14a2a992b2a75b9919153a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 68b9e7e56f750717…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.1',
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
