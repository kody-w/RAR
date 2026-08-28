---
name: "rar-cowork-cookbook-ppt-exec-define-expense-policies"
description: "Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_expense_policies", "rar_sha256": "5b2082fd0cccd065651642ad1c4553caf85c078e5776cf35ad85c3d223a190b3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_expense_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_expense_policies_agent.py` and in the RCI capsule.

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

Define expense policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 5b2082fd0cccd065…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_expense_policies_agent.py` first:

```bash
python3 ppt_exec_define_expense_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_expense_policies_agent.py   # or on stdin
python3 ppt_exec_define_expense_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define expense policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_expense_policies',
    "version": '2.0.1',
    "display_name": 'Define expense policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-define-expense-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-expense-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd4c2af05252132a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-expense-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-expense-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineExpensePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineExpensePolicies'
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
    print(PptExecDefineExpensePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
