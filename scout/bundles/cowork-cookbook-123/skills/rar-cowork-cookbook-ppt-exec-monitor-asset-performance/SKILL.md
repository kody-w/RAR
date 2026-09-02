---
name: "rar-cowork-cookbook-ppt-exec-monitor-asset-performance"
description: "Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_asset_performance", "rar_sha256": "ffdc5f4b48f52de50ac889584520e9ee7affc41d7f14e1d5868a84a7694c4855", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_asset_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-asset-performance:43833f7cb5200653dae71d64b95a27a9a5ce5104ba7ea63ffe3a264d44a36b60", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_asset_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_asset_performance_agent.py` is
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
