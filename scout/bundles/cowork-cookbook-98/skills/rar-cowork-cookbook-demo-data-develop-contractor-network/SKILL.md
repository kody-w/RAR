---
name: "rar-cowork-cookbook-demo-data-develop-contractor-network"
description: "Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_contractor_network", "rar_sha256": "b13ffd98f2724487fa1fdfec2ef6097b35cbd8b977fdfafc58373dfd710b6cc8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 b13ffd98f2724487…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_contractor_network_agent.py` first:

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
    "version": '2.0.0',
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
