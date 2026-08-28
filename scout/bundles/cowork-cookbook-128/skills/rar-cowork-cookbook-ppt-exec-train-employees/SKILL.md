---
name: "rar-cowork-cookbook-ppt-exec-train-employees"
description: "Generates an executive-ready PowerPoint deck on train employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_train_employees", "rar_sha256": "a7706cc408dacd6b16ab9406cf090a45ed1d1e484d68be25b340f12f47d1da66", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_train_employees_agent.py` and embedded as the fenced Python below (sha256 a7706cc408dacd6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_train_employees_agent.py` first:

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
    "version": '2.0.1',
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
