---
name: "rar-cowork-cookbook-demo-data-define-service-contracts"
description: "Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_service_contracts", "rar_sha256": "3e843a4d20cbad587a8ea0890025b56aa070d611298437734a717f2c0e68ef4f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_service_contracts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_service_contracts_agent.py` and in the RCI capsule.

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

Define service contracts Demo Data Generator — Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-service-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 3e843a4d20cbad58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_service_contracts_agent.py` first:

```bash
python3 demo_data_define_service_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_service_contracts_agent.py   # or on stdin
python3 demo_data_define_service_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service contracts Demo Data Generator — Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-service-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_service_contracts',
    "version": '2.0.1',
    "display_name": 'Define service contracts Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-service-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-service-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c9d9ff23a6cc346',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-contracts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-define-service-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineServiceContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineServiceContracts'
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
    print(DemoDataDefineServiceContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
