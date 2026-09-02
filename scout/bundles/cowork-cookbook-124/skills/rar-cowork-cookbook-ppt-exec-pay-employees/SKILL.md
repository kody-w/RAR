---
name: "rar-cowork-cookbook-ppt-exec-pay-employees"
description: "Generates an executive-ready PowerPoint deck on pay employees status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pay_employees", "rar_sha256": "e6276b46f602427b6b749ccaf2bd14f2985d57b67b15e15f7128d0074808b540", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_pay_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-pay-employees:d1d06961340a81226e1647181a6729a7cdfecf0e44481629745c2d7dafa12867", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_pay_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_pay_employees_agent.py` is
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
