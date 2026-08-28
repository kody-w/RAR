---
name: "rar-cowork-cookbook-demo-data-develop-contractor-network"
description: "Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_contractor_network", "rar_sha256": "5e5a94e135ac12a6b2ec9a8da36f6b8c397c8f59d8481dd4ec96db9c742d50d4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Demo Data Generator — Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 5e5a94e135ac12a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_contractor_network_agent.py` first:

```bash
python3 demo_data_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_contractor_network_agent.py   # or on stdin
python3 demo_data_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Demo Data Generator — Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_contractor_network',
    "version": '2.0.1',
    "display_name": 'Develop contractor network Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7088d2751c8ad5f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopContractorNetwork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContractorNetwork'
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
    print(DemoDataDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
