---
name: "rar-cowork-cookbook-dashboard-define-performance-strategy"
description: "Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_performance_strategy", "rar_sha256": "7d9a850b5910bfff62f5cb1f41edfad903bc54e678a5cbcc571f98add5eb5150", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 7d9a850b5910bfff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_performance_strategy_agent.py` first:

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
    "version": '2.0.0',
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
