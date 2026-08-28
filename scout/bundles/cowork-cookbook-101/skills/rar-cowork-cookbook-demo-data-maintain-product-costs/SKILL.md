---
name: "rar-cowork-cookbook-demo-data-maintain-product-costs"
description: "Generates and creates realistic demo records for maintain product costs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_product_costs", "rar_sha256": "0a9fbbef7b4a2a48481e8b816b52f3aec0cf92ad3122bc4c65b7876dc53a9e0d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 0a9fbbef7b4a2a48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_product_costs_agent.py` first:

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
    "version": '2.0.1',
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
