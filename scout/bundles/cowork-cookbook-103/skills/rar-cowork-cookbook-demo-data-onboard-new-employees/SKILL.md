---
name: "rar-cowork-cookbook-demo-data-onboard-new-employees"
description: "Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_onboard_new_employees", "rar_sha256": "404193e6b7c80654ca96b20fa3478d834a604e6b9e45ca3120a55ec7fe67b401", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_onboard_new_employees`. The original RAPP
agent is preserved byte-for-byte in `demo_data_onboard_new_employees_agent.py` and in the RCI capsule.

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

Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_onboard_new_employees_agent.py` and embedded as the fenced Python below (sha256 404193e6b7c80654…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_onboard_new_employees_agent.py` first:

```bash
python3 demo_data_onboard_new_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_onboard_new_employees_agent.py   # or on stdin
python3 demo_data_onboard_new_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new employees Demo Data Generator — Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-onboard-new-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_onboard_new_employees',
    "version": '2.0.0',
    "display_name": 'Onboard new employees Demo Data Generator',
    "description": 'Generates and creates realistic demo records for onboard new employees in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-onboard-new-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-onboard-new-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0263795c7214d6a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-employees'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-onboard-new-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataOnboardNewEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOnboardNewEmployees'
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
    print(DemoDataOnboardNewEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
