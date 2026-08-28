---
name: "rar-cowork-cookbook-dashboard-implement-project-governance-approach"
description: "Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_project_governance_approach", "rar_sha256": "dc1815453f26c98798d1815572a14ab4390efa4ee1a1f0a5d3cf7bb05bad13a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_implement_project_governance_approach`. The original RAPP
agent is preserved byte-for-byte in `dashboard_implement_project_governance_approach_agent.py` and in the RCI capsule.

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

Implement project governance approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 dc1815453f26c987…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_project_governance_approach_agent.py` first:

```bash
python3 dashboard_implement_project_governance_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_implement_project_governance_approach_agent.py   # or on stdin
python3 dashboard_implement_project_governance_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement project governance approach Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_implement_project_governance_approach',
    "version": '2.0.1',
    "display_name": 'Implement project governance approach Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-implement-project-governance-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-implement-project-governance-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9451820fa3df0809',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-project-governance-approach'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-implement-project-governance-approach', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardImplementProjectGovernanceApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardImplementProjectGovernanceApproach'
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
    print(DashboardImplementProjectGovernanceApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
