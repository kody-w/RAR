---
name: "rar-cowork-cookbook-demo-data-plan-product-retirement"
description: "Generates and creates realistic demo records for plan product retirement in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_product_retirement", "rar_sha256": "7fae08421e4a34f27c98a2aa6d8ad9cc9104e001c8945e322fb7a6e18b3c3691", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_product_retirement_agent.py` and embedded as the fenced Python below (sha256 7fae08421e4a34f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_product_retirement_agent.py` first:

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
    "version": '2.0.0',
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
