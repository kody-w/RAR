---
name: "rar-cowork-cookbook-demo-data-appropriate-budgets"
description: "Generates and creates realistic demo records for appropriate budgets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_appropriate_budgets", "rar_sha256": "aa6886f42ad8c69e48194cb22222999ce4b5f9d2c9fb98d529e43391dbc47a1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_appropriate_budgets_agent.py` and embedded as the fenced Python below (sha256 aa6886f42ad8c69e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_appropriate_budgets_agent.py` first:

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
    "version": '2.0.0',
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
