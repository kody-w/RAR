---
name: "rar-cowork-cookbook-demo-data-define-preliminary-budgets"
description: "Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_preliminary_budgets", "rar_sha256": "300f25663d2d73ee1386f50de40283b37f4d963394cfac12a355047edf6cdda4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_preliminary_budgets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_preliminary_budgets_agent.py` and in the RCI capsule.

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

Define preliminary budgets Demo Data Generator — Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 300f25663d2d73ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_preliminary_budgets_agent.py` first:

```bash
python3 demo_data_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_preliminary_budgets_agent.py   # or on stdin
python3 demo_data_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Demo Data Generator — Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_preliminary_budgets',
    "version": '2.0.1',
    "display_name": 'Define preliminary budgets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b8c6ac49e54667b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefinePreliminaryBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefinePreliminaryBudgets'
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
    print(DemoDataDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
