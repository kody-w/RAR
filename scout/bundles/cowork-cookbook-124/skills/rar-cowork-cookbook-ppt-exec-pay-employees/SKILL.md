---
name: "rar-cowork-cookbook-ppt-exec-pay-employees"
description: "Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pay_employees", "rar_sha256": "b444648a030364f7148215cd7bdc52bdb8f8b9b33a27a173c63c64d424178ebf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_pay_employees`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_pay_employees_agent.py` and in the RCI capsule.

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

Pay employees Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pay-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pay_employees_agent.py` and embedded as the fenced Python below (sha256 b444648a030364f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pay_employees_agent.py` first:

```bash
python3 ppt_exec_pay_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_pay_employees_agent.py   # or on stdin
python3 ppt_exec_pay_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay employees Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pay-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_pay_employees',
    "version": '2.0.1',
    "display_name": 'Pay employees Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-pay-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-pay-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e1e4b9b6caf06d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/pay-employees'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-pay-employees', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPayEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPayEmployees'
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
    print(PptExecPayEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
