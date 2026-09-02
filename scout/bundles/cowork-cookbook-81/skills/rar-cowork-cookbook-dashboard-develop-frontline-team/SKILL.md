---
name: "rar-cowork-cookbook-dashboard-develop-frontline-team"
description: "Produces a self-contained interactive HTML dashboard for develop frontline team - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_frontline_team", "rar_sha256": "e52c3f1e41731d181e57042e87070716c69fe1c440551f280a197e9dc572cc1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_frontline_team_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-frontline-team:fc6afe517e44e025e30f86f054f2434cc1a6cbae48ffcfe74f424774e5098969", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_frontline_team`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_frontline_team_agent.py` is
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
