---
name: "rar-cowork-cookbook-demo-data-plan-asset-leases"
description: "Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_asset_leases", "rar_sha256": "71e1275461037f235ceb2d8e28431b68d3be6cf7ae243a1c8d035d0c23620c96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 71e1275461037f23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_asset_leases_agent.py` first:

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
    "version": '2.0.0',
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
