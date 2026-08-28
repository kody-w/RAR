---
name: "rar-cowork-cookbook-demo-data-recognize-employees"
description: "Generates and creates realistic demo records for recognize employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_recognize_employees", "rar_sha256": "bc450791b8c4b8e0c9c43136376711db6093b1c8b0077f3cfd611c0b5660f779", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
