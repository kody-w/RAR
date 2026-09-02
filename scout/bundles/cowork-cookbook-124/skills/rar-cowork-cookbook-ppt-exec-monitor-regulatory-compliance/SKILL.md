---
name: "rar-cowork-cookbook-ppt-exec-monitor-regulatory-compliance"
description: "Generates an executive-ready PowerPoint deck on monitor regulatory compliance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_regulatory_compliance", "rar_sha256": "e5a2fac8660854bc7be558be52d5d1d26137bab96c21a65a1317019252972494", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_monitor_regulatory_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-monitor-regulatory-compliance:b92eb033aa9b61c48c1ae40aaf1f6bb1b6dbae9e22b66c4099e0301e7667d30d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_monitor_regulatory_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_monitor_regulatory_compliance_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 e5a2fac8660854bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_regulatory_compliance_agent.py` first:

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
    "version": '2.0.0',
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
