---
name: "rar-cowork-cookbook-demo-data-evaluate-supplier-bids"
description: "Generates and creates realistic demo records for evaluate supplier bids in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_evaluate_supplier_bids", "rar_sha256": "f2c7c4c4451544048ef0732a5aef9cc156d52dd35f14ab4c3adde3f94aedfba9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_evaluate_supplier_bids_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-evaluate-supplier-bids:8d294cba910bab291338101fd201d7b3752273b4bcae1a6258284aa74982ed8c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_evaluate_supplier_bids`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_evaluate_supplier_bids_agent.py` is
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
