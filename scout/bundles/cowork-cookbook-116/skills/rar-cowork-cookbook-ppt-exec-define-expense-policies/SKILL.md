---
name: "rar-cowork-cookbook-ppt-exec-define-expense-policies"
description: "Generates an executive-ready PowerPoint deck on define expense policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_expense_policies", "rar_sha256": "3c973faad8364f4745b009c8c1a16bed80d362238062ff59ced91b4b31d8a25f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_expense_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-expense-policies:fb5a977d910b5690cc6e9c9cd42a1425346a4cab3653f7c7694966e434ad1179", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_expense_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_expense_policies_agent.py` is
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
