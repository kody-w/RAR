---
name: "rar-cowork-cookbook-ppt-exec-analyze-order-management-processes"
description: "Generates an executive-ready PowerPoint deck on analyze order management processes status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_order_management_processes", "rar_sha256": "d22dac1db83ff6ad2c7b8e3e4feb5331a8ee8d040179b0a1138bf169aa605105", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 d22dac1db83ff6ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_order_management_processes_agent.py` first:

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
    "version": '2.0.1',
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
