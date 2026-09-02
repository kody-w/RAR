---
name: "rar-cowork-cookbook-dashboard-develop-project-governance-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop project governance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_project_governance_strategy", "rar_sha256": "b7afac13fb3b133064e92d9c6676b40012d78198eab7968ad184b9a7d7c9646f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_project_governance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-project-governance-strategy:15e4a1d63f8f5f8926a0bc7a967fde7c40acbfea54c8b7bcd7d7e19ccd107387", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_project_governance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_project_governance_strategy_agent.py` is
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
