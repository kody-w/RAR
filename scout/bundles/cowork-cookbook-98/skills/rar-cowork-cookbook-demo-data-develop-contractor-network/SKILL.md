---
name: "rar-cowork-cookbook-demo-data-develop-contractor-network"
description: "Generates and creates realistic demo records for develop contractor network in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_contractor_network", "rar_sha256": "b13ffd98f2724487fa1fdfec2ef6097b35cbd8b977fdfafc58373dfd710b6cc8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_contractor_network_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-contractor-network:3c44aa8f8c37a183ec25b3f50b327cfaa90cafea5b225e4a3a3028c163f2e469", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_contractor_network`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_contractor_network_agent.py` is
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
