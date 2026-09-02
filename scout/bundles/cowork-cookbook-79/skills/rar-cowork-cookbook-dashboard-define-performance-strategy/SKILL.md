---
name: "rar-cowork-cookbook-dashboard-define-performance-strategy"
description: "Produces a self-contained interactive HTML dashboard for define performance strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_performance_strategy", "rar_sha256": "7d9a850b5910bfff62f5cb1f41edfad903bc54e678a5cbcc571f98add5eb5150", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_performance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-performance-strategy:8fd6ee540d6e74b5e9e4e38c7e22ea6d30c64f3fdc4096b2cd46628090cf1c86", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_performance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_performance_strategy_agent.py` is
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
