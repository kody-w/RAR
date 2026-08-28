---
name: "rar-cowork-cookbook-demo-data-recognize-employees"
description: "Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_recognize_employees", "rar_sha256": "c4c93bc2a2eb8497d8b812d57af4160bdd37e4484471f3b89946442ba505dde7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_recognize_employees`. The original RAPP
agent is preserved byte-for-byte in `demo_data_recognize_employees_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 c4c93bc2a2eb8497…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_recognize_employees_agent.py` first:

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
    "version": '2.0.1',
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
