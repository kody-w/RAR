---
name: "rar-cowork-cookbook-demo-data-plan-asset-leases"
description: "Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_asset_leases", "rar_sha256": "7726a1961447283c5de36527818f1c92f9b5057350e0be9fb11680b39c16ad10", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_asset_leases_agent.py` and in the RCI capsule.

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

Plan asset leases Demo Data Generator — Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 7726a1961447283c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_asset_leases_agent.py` first:

```bash
python3 demo_data_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_asset_leases_agent.py   # or on stdin
python3 demo_data_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Demo Data Generator — Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_asset_leases',
    "version": '2.0.1',
    "display_name": 'Plan asset leases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '206d3b15ecf3e22a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPlanAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanAssetLeases'
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
    print(DemoDataPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
