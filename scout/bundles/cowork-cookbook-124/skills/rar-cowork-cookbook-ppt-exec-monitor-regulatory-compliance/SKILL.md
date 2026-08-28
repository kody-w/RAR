---
name: "rar-cowork-cookbook-ppt-exec-monitor-regulatory-compliance"
description: "Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_regulatory_compliance", "rar_sha256": "195881c1e6aa9fa763dcfb096760691b403c850c0659b955fac84bed11ff0aaa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_regulatory_compliance_agent.py` and in the RCI capsule.

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

Monitor regulatory compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 195881c1e6aa9fa7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_regulatory_compliance_agent.py` first:

```bash
python3 ppt_exec_monitor_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_regulatory_compliance_agent.py   # or on stdin
python3 ppt_exec_monitor_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor regulatory compliance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_regulatory_compliance',
    "version": '2.0.1',
    "display_name": 'Monitor regulatory compliance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42e1cdb2cacad103',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-regulatory-compliance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-monitor-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMonitorRegulatoryCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorRegulatoryCompliance'
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
    print(PptExecMonitorRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
