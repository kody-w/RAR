---
name: "rar-cowork-cookbook-demo-data-define-costing-policies"
description: "Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_costing_policies", "rar_sha256": "5ed6c1dbc891eb46b4c83221e0cc7573d00483d0d6cf3a6c67e78910840b9763", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_costing_policies`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_costing_policies_agent.py` and in the RCI capsule.

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

Define costing policies Demo Data Generator — Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 5ed6c1dbc891eb46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_costing_policies_agent.py` first:

```bash
python3 demo_data_define_costing_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_costing_policies_agent.py   # or on stdin
python3 demo_data_define_costing_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define costing policies Demo Data Generator — Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-costing-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_costing_policies',
    "version": '2.0.1',
    "display_name": 'Define costing policies Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-define-costing-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-costing-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c2dd57fb11e2aee6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-costing-policies'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-define-costing-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineCostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCostingPolicies'
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
    print(DemoDataDefineCostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
