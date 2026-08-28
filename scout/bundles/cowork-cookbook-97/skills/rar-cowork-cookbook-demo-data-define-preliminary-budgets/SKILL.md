---
name: "rar-cowork-cookbook-demo-data-define-preliminary-budgets"
description: "Generates and creates realistic demo records for define preliminary budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_preliminary_budgets", "rar_sha256": "80b9d6331558bac909c5956fdc67ef5533791371d8d2e5c38f3c2a42cfb76278", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 80b9d6331558bac9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_preliminary_budgets_agent.py` first:

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
    "version": '2.0.0',
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
