---
name: "rar-cowork-cookbook-demo-data-consolidate-requisitions"
description: "Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_requisitions", "rar_sha256": "3e93c8593f61efd3c422b25dbf88086bbdf6cdfe48f15166a32a1baea19d79cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_consolidate_requisitions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_consolidate_requisitions_agent.py` and in the RCI capsule.

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

Consolidate requisitions Demo Data Generator — Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 3e93c8593f61efd3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_requisitions_agent.py` first:

```bash
python3 demo_data_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_consolidate_requisitions_agent.py   # or on stdin
python3 demo_data_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Demo Data Generator — Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_consolidate_requisitions',
    "version": '2.0.1',
    "display_name": 'Consolidate requisitions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50c2b806e5bfba6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConsolidateRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConsolidateRequisitions'
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
    print(DemoDataConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
