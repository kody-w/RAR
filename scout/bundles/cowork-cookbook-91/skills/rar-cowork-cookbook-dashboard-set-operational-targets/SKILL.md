---
name: "rar-cowork-cookbook-dashboard-set-operational-targets"
description: "Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_operational_targets", "rar_sha256": "8033c75a96a4b9a55d513dc073f57e9fccd32ae70e502fc15f0444d482c95d8b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_set_operational_targets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_set_operational_targets_agent.py` and in the RCI capsule.

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

Set operational targets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 8033c75a96a4b9a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_operational_targets_agent.py` first:

```bash
python3 dashboard_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_operational_targets_agent.py   # or on stdin
python3 dashboard_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_operational_targets',
    "version": '2.0.0',
    "display_name": 'Set operational targets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cb8987ce2cd89391',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardSetOperationalTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetOperationalTargets'
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
    print(DashboardSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
