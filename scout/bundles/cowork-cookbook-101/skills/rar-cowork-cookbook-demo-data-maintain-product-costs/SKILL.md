---
name: "rar-cowork-cookbook-demo-data-maintain-product-costs"
description: "Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_product_costs", "rar_sha256": "c3a01655635641b863c1169a21fcb613782c3282db877ceaf8540a591e568197", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_maintain_product_costs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_maintain_product_costs_agent.py` and in the RCI capsule.

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

Maintain product costs Demo Data Generator — Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 c3a01655635641b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_product_costs_agent.py` first:

```bash
python3 demo_data_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_maintain_product_costs_agent.py   # or on stdin
python3 demo_data_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Demo Data Generator — Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_maintain_product_costs',
    "version": '2.0.0',
    "display_name": 'Maintain product costs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '213e696742c445b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMaintainProductCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMaintainProductCosts'
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
    print(DemoDataMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
