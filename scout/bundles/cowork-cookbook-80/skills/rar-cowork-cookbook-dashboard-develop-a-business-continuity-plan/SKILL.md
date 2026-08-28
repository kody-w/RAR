---
name: "rar-cowork-cookbook-dashboard-develop-a-business-continuity-plan"
description: "Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_a_business_continuity_plan", "rar_sha256": "7d98d9fcdb6e63560835a845f960fac665939c7a36b03f6180bf60ae2e5de9d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Develop a business continuity plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 7d98d9fcdb6e6356…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 dashboard_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 dashboard_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_a_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Develop a business continuity plan Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ddb9bc8bffd5769',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopABusinessContinuityPlan'
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
    print(DashboardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
