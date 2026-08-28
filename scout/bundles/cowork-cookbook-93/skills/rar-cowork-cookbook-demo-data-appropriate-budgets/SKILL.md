---
name: "rar-cowork-cookbook-demo-data-appropriate-budgets"
description: "Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_appropriate_budgets", "rar_sha256": "380617aae8081ffc533e6a839a471227f248987e7d5a7cd25111377d8596cb28", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_appropriate_budgets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_appropriate_budgets_agent.py` and in the RCI capsule.

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

Appropriate budgets Demo Data Generator — Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 380617aae8081ffc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_appropriate_budgets_agent.py` first:

```bash
python3 demo_data_appropriate_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_appropriate_budgets_agent.py   # or on stdin
python3 demo_data_appropriate_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Appropriate budgets Demo Data Generator — Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-appropriate-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_appropriate_budgets',
    "version": '2.0.1',
    "display_name": 'Appropriate budgets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-appropriate-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-appropriate-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '993295cf5c3b2419',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/appropriate-budgets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-appropriate-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAppropriateBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAppropriateBudgets'
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
    print(DemoDataAppropriateBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
