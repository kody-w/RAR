---
name: "rar-cowork-cookbook-ppt-exec-allocate-budgets"
description: "Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_allocate_budgets", "rar_sha256": "95aa0231a754f5af3a778c5c86357ba10e25cef4afd46eb691423cb808f59499", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_allocate_budgets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_allocate_budgets_agent.py` and in the RCI capsule.

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

Allocate budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 95aa0231a754f5af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_allocate_budgets_agent.py` first:

```bash
python3 ppt_exec_allocate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_allocate_budgets_agent.py   # or on stdin
python3 ppt_exec_allocate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate budgets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_allocate_budgets',
    "version": '2.0.0',
    "display_name": 'Allocate budgets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-allocate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-allocate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cf00eb39599cf3b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/allocate-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-allocate-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecAllocateBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAllocateBudgets'
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
    print(PptExecAllocateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
