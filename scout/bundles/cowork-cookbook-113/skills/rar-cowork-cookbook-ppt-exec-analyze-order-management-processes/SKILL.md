---
name: "rar-cowork-cookbook-ppt-exec-analyze-order-management-processes"
description: "Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_order_management_processes", "rar_sha256": "0b2198cc34eacfd80afd9d3e53f5f635c3e4ae7f9b2088c18a707a5846fe8095", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_order_management_processes_agent.py` and in the RCI capsule.

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
