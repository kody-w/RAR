---
name: "rar-cowork-cookbook-ppt-exec-train-employees"
description: "Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_train_employees", "rar_sha256": "84512a4694f8a77c672897aba5e329b5dbd087080fcf0bf244daf11493aeb1b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_train_employees`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_train_employees_agent.py` and in the RCI capsule.

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
