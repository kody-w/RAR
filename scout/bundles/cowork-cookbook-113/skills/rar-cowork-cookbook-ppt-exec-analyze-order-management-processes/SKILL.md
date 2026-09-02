---
name: "rar-cowork-cookbook-ppt-exec-analyze-order-management-processes"
description: "Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_order_management_processes", "rar_sha256": "0b2198cc34eacfd80afd9d3e53f5f635c3e4ae7f9b2088c18a707a5846fe8095", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_analyze_order_management_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-analyze-order-management-processes:6336bc2ba67d04b5271002a62c0caa834300e165f93c8419a86b09fda31e13e0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_analyze_order_management_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_analyze_order_management_processes_agent.py` is
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

Analyze order management processes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 0b2198cc34eacfd8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_order_management_processes_agent.py` first:

```bash
python3 ppt_exec_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_order_management_processes_agent.py   # or on stdin
python3 ppt_exec_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_order_management_processes',
    "version": '2.0.0',
    "display_name": 'Analyze order management processes Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28fc4d17942ea08f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecAnalyzeOrderManagementProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeOrderManagementProcesses'
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
    print(PptExecAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
