---
name: "rar-cowork-cookbook-dashboard-develop-frontline-team"
description: "Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_frontline_team", "rar_sha256": "e52c3f1e41731d181e57042e87070716c69fe1c440551f280a197e9dc572cc1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_frontline_team_agent.py` and embedded as the fenced Python below (sha256 e52c3f1e41731d18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_frontline_team_agent.py` first:

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
    "version": '2.0.0',
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
