---
name: "rar-cowork-cookbook-ppt-exec-monitor-asset-performance"
description: "Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_asset_performance", "rar_sha256": "ffdc5f4b48f52de50ac889584520e9ee7affc41d7f14e1d5868a84a7694c4855", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 ffdc5f4b48f52de5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_asset_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_asset_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_asset_performance',
    "version": '2.0.0',
    "display_name": 'Monitor asset performance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0deb4da2dc1a8e73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecMonitorAssetPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorAssetPerformance'
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
    print(PptExecMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
