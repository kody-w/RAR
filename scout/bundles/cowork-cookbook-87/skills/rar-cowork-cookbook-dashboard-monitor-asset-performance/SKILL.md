---
name: "rar-cowork-cookbook-dashboard-monitor-asset-performance"
description: "Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_asset_performance", "rar_sha256": "698bf1d069ede4ac1561a05d1d5c6a5a978f2203b01e7338ebff1d0328f35873", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 698bf1d069ede4ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_asset_performance_agent.py` first:

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
    "version": '2.0.0',
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
