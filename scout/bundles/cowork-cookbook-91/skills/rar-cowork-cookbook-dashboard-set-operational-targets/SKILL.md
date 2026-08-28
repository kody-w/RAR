---
name: "rar-cowork-cookbook-dashboard-set-operational-targets"
description: "Produces a self-contained interactive HTML dashboard for set operational targets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_operational_targets", "rar_sha256": "5a010e2d7597519529845e128e37778c53fe676afbe78522358296fee7e81f9a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 5a010e2d75975195…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_operational_targets_agent.py` first:

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
    "version": '2.0.1',
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
