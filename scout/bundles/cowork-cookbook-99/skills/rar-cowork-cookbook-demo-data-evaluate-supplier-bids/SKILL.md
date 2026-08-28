---
name: "rar-cowork-cookbook-demo-data-evaluate-supplier-bids"
description: "Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_evaluate_supplier_bids", "rar_sha256": "805112fac8d1c86cf29e438f03e6694564af5fc6eac979ba7ab543a55b16612e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 805112fac8d1c86c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_evaluate_supplier_bids_agent.py` first:

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
    "version": '2.0.1',
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
