---
name: "rar-cowork-cookbook-demo-data-define-service-contracts"
description: "Generates and creates realistic demo records for define service contracts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_service_contracts", "rar_sha256": "2384cc4718323e119ef321eed81bf8d9fb7a4b8c2fc7297c888acf9a91d20207", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_service_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-service-contracts:1e2334c4f6af2677af12f1a5fc7fdaba067a820dfb08a6a0bcd15161e9c5b8b0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_service_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_service_contracts_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
