---
name: "rar-cowork-cookbook-demo-data-consolidate-requisitions"
description: "Generates and creates realistic demo records for consolidate requisitions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_consolidate_requisitions", "rar_sha256": "3d7a46202e6d2983b0931b54651e15e073ab7dacc43aca5a17d6609ed041ff83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 3d7a46202e6d2983…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_consolidate_requisitions_agent.py` first:

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
    "version": '2.0.0',
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
