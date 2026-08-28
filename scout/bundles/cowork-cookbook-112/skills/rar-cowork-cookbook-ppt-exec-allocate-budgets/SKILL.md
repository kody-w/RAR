---
name: "rar-cowork-cookbook-ppt-exec-allocate-budgets"
description: "Generates an executive-ready PowerPoint deck on allocate budgets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_allocate_budgets", "rar_sha256": "a0bfe311cac79e8c7dd7748e17f436cf243a7840c5f35a8178bf71a83cd6c0c4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_allocate_budgets_agent.py` and embedded as the fenced Python below (sha256 a0bfe311cac79e8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_allocate_budgets_agent.py` first:

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
    "version": '2.0.1',
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
