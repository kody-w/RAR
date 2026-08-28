---
name: "rar-cowork-cookbook-demo-data-define-service-contracts"
description: "Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_service_contracts", "rar_sha256": "2384cc4718323e119ef321eed81bf8d9fb7a4b8c2fc7297c888acf9a91d20207", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 2384cc4718323e11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_service_contracts_agent.py` first:

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
    "version": '2.0.0',
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
