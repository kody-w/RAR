---
name: "rar-cowork-cookbook-dashboard-develop-a-business-continuity-plan"
description: "Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_a_business_continuity_plan", "rar_sha256": "a6956d1ce9952d940036c42b92b22dcafcadd639b1078cf27d33f5839522ee88", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 a6956d1ce9952d94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_a_business_continuity_plan_agent.py` first:

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
    "version": '2.0.1',
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
