---
name: "rar-cowork-cookbook-dashboard-develop-project-governance-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_project_governance_strategy", "rar_sha256": "f7dc758783a35d436a55f4128840939d437378877866f2d9c726410f4eda07fe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_project_governance_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_project_governance_strategy_agent.py` and in the RCI capsule.

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

Develop project governance strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 f7dc758783a35d43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_project_governance_strategy_agent.py` first:

```bash
python3 dashboard_develop_project_governance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_project_governance_strategy_agent.py   # or on stdin
python3 dashboard_develop_project_governance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project governance strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_project_governance_strategy',
    "version": '2.0.1',
    "display_name": 'Develop project governance strategy Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-project-governance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-project-governance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27a244aff53cc008',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-governance-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-develop-project-governance-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopProjectGovernanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopProjectGovernanceStrategy'
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
    print(DashboardDevelopProjectGovernanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
