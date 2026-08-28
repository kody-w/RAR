---
name: "rar-cowork-cookbook-demo-data-define-costing-policies"
description: "Generates and creates realistic demo records for define costing policies in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_costing_policies", "rar_sha256": "466bd212fc2b5258699e0c2b8e2bec62de71ded47c2c3db03adcd33edfee5161", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_costing_policies_agent.py` and embedded as the fenced Python below (sha256 466bd212fc2b5258…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_costing_policies_agent.py` first:

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
    "version": '2.0.0',
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
