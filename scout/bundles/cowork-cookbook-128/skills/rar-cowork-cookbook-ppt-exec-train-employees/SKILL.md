---
name: "rar-cowork-cookbook-ppt-exec-train-employees"
description: "Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_train_employees", "rar_sha256": "84512a4694f8a77c672897aba5e329b5dbd087080fcf0bf244daf11493aeb1b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_train_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-train-employees:73b8691f4c5b9bcba0960db417e7ac8de0ec6a82ad0035308feab15df1a509f0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_train_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_train_employees_agent.py` is
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

Train employees Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-train-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_train_employees_agent.py` and embedded as the fenced Python below (sha256 84512a4694f8a77c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_train_employees_agent.py` first:

```bash
python3 ppt_exec_train_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_train_employees_agent.py   # or on stdin
python3 ppt_exec_train_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Train employees Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-train-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_train_employees',
    "version": '2.0.0',
    "display_name": 'Train employees Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-train-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-train-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf4a233723903eec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/train-employees'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-train-employees', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecTrainEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTrainEmployees'
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
    print(PptExecTrainEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
