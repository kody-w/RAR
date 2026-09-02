---
name: "rar-cowork-cookbook-dashboard-monitor-asset-performance"
description: "Produces a self-contained interactive HTML dashboard for monitor asset performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_asset_performance", "rar_sha256": "698bf1d069ede4ac1561a05d1d5c6a5a978f2203b01e7338ebff1d0328f35873", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_asset_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-asset-performance:4f2f07f19bb6f45f32420dc2aa017b1c4a0e70f6ad1d4a993f013b158c1ad41b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_asset_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_asset_performance_agent.py` is
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
