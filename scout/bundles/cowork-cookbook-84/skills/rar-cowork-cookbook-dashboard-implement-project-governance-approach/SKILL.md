---
name: "rar-cowork-cookbook-dashboard-implement-project-governance-approach"
description: "Produces a self-contained interactive HTML dashboard for implement project governance approach - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_implement_project_governance_approach", "rar_sha256": "751d973b017d6c97c2a59abc7b0021edec3018a1133a4a18f7cb5cc620b839f9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_implement_project_governance_approach_agent.py` and embedded as the fenced Python below (sha256 751d973b017d6c97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_implement_project_governance_approach_agent.py` first:

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
    "version": '2.0.0',
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
