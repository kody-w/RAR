---
name: "rar-cowork-cookbook-dashboard-define-performance-strategy"
description: "Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_performance_strategy", "rar_sha256": "bfb7badffdf4bbca0facf6fcc23a49be3b164cd969e91e6b865aabd808e34c29", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_performance_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_performance_strategy_agent.py` and in the RCI capsule.

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

Define performance strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-performance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 bfb7badffdf4bbca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_performance_strategy_agent.py` first:

```bash
python3 dashboard_define_performance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_performance_strategy_agent.py   # or on stdin
python3 dashboard_define_performance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define performance strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-performance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_performance_strategy',
    "version": '2.0.1',
    "display_name": 'Define performance strategy Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-define-performance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-performance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8567cee74ef67614',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-performance-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-define-performance-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefinePerformanceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefinePerformanceStrategy'
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
    print(DashboardDefinePerformanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
