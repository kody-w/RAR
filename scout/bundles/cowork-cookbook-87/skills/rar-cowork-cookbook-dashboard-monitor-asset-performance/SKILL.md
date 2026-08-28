---
name: "rar-cowork-cookbook-dashboard-monitor-asset-performance"
description: "Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_asset_performance", "rar_sha256": "a16dcb65a8d4d69f148ec83dda1722cceba98133a457f8cebd1cd0a1959553cd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 a16dcb65a8d4d69f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_asset_performance_agent.py` first:

```bash
python3 dashboard_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_asset_performance_agent.py   # or on stdin
python3 dashboard_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_asset_performance',
    "version": '2.0.1',
    "display_name": 'Monitor asset performance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6681e0ffce4bdd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMonitorAssetPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorAssetPerformance'
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
    print(DashboardMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
