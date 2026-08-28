---
name: "rar-cowork-cookbook-ppt-exec-pay-employees"
description: "Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pay_employees", "rar_sha256": "e6276b46f602427b6b749ccaf2bd14f2985d57b67b15e15f7128d0074808b540", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pay_employees_agent.py` and embedded as the fenced Python below (sha256 e6276b46f602427b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pay_employees_agent.py` first:

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
    "version": '2.0.0',
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
