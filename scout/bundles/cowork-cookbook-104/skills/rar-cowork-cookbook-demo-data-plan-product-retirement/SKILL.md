---
name: "rar-cowork-cookbook-demo-data-plan-product-retirement"
description: "Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_product_retirement", "rar_sha256": "cadb3ace96793f53b48adf3bf7cd53cfd51c9b32c069f0211b9f1831a59b203e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_product_retirement`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_product_retirement_agent.py` and in the RCI capsule.

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

Plan product retirement Demo Data Generator — Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 cadb3ace96793f53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_product_retirement_agent.py` first:

```bash
python3 demo_data_plan_product_retirement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_product_retirement_agent.py   # or on stdin
python3 demo_data_plan_product_retirement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product retirement Demo Data Generator — Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-product-retirement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_product_retirement',
    "version": '2.0.1',
    "display_name": 'Plan product retirement Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-plan-product-retirement',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-product-retirement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bfef5a0875b843bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-retirement'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-plan-product-retirement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPlanProductRetirement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProductRetirement'
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
    print(DemoDataPlanProductRetirement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
