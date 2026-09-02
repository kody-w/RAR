---
name: "rar-cowork-cookbook-demo-data-recognize-employees"
description: "Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_recognize_employees", "rar_sha256": "bc450791b8c4b8e0c9c43136376711db6093b1c8b0077f3cfd611c0b5660f779", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_recognize_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-recognize-employees:7065f828cb4511d36e1abcf85c6503d8ab5a294943bea6f1a75a07abe0fb9158", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_recognize_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_recognize_employees_agent.py` is
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

Recognize employees Demo Data Generator — Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-recognize-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 bc450791b8c4b8e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_recognize_employees_agent.py` first:

```bash
python3 demo_data_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_recognize_employees_agent.py   # or on stdin
python3 demo_data_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Demo Data Generator — Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_recognize_employees',
    "version": '2.0.0',
    "display_name": 'Recognize employees Demo Data Generator',
    "description": 'Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4700a6720fada83b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataRecognizeEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecognizeEmployees'
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
    print(DemoDataRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
