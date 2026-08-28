---
name: "rar-cowork-cookbook-dashboard-develop-frontline-team"
description: "Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_frontline_team", "rar_sha256": "4438e76806e7a9379f82f72b8e710cd827e5c91b81274a94f3d5579fca82d974", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_frontline_team`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_frontline_team_agent.py` and in the RCI capsule.

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

Develop frontline team Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 4438e76806e7a937…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_frontline_team_agent.py` first:

```bash
python3 dashboard_develop_frontline_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_frontline_team_agent.py   # or on stdin
python3 dashboard_develop_frontline_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop frontline team Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-frontline-team
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_frontline_team',
    "version": '2.0.1',
    "display_name": 'Develop frontline team Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-frontline-team',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-frontline-team',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '49a54781ec72cb65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-frontline-team'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-frontline-team', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopFrontlineTeam(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopFrontlineTeam'
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
    print(DashboardDevelopFrontlineTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
