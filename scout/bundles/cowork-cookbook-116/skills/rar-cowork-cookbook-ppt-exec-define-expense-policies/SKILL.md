---
name: "rar-cowork-cookbook-ppt-exec-define-expense-policies"
description: "Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_expense_policies", "rar_sha256": "3c973faad8364f4745b009c8c1a16bed80d362238062ff59ced91b4b31d8a25f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 3c973faad8364f47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_expense_policies_agent.py` first:

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
    "version": '2.0.0',
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
