---
name: "rar-cowork-cookbook-demo-data-evaluate-supplier-bids"
description: "Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_evaluate_supplier_bids", "rar_sha256": "f2c7c4c4451544048ef0732a5aef9cc156d52dd35f14ab4c3adde3f94aedfba9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_evaluate_supplier_bids`. The original RAPP
agent is preserved byte-for-byte in `demo_data_evaluate_supplier_bids_agent.py` and in the RCI capsule.

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

Evaluate supplier bids Demo Data Generator — Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 f2c7c4c445154404…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_evaluate_supplier_bids_agent.py` first:

```bash
python3 demo_data_evaluate_supplier_bids_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_evaluate_supplier_bids_agent.py   # or on stdin
python3 demo_data_evaluate_supplier_bids_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier bids Demo Data Generator — Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_evaluate_supplier_bids',
    "version": '2.0.0',
    "display_name": 'Evaluate supplier bids Demo Data Generator',
    "description": 'Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-evaluate-supplier-bids',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51b8d1908e9e4244',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/evaluate-supplier-bids'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-evaluate-supplier-bids', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataEvaluateSupplierBids(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEvaluateSupplierBids'
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
    print(DemoDataEvaluateSupplierBids().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
