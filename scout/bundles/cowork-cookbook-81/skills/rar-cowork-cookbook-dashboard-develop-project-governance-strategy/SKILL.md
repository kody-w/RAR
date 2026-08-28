---
name: "rar-cowork-cookbook-dashboard-develop-project-governance-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_project_governance_strategy", "rar_sha256": "b7afac13fb3b133064e92d9c6676b40012d78198eab7968ad184b9a7d7c9646f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 b7afac13fb3b1330…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_project_governance_strategy_agent.py` first:

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
    "version": '2.0.0',
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
