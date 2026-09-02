---
name: "rar-cowork-cookbook-demo-data-plan-asset-leases"
description: "Generates and creates realistic demo records for plan asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_asset_leases", "rar_sha256": "71e1275461037f235ceb2d8e28431b68d3be6cf7ae243a1c8d035d0c23620c96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_plan_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-plan-asset-leases:61bbee6182c4ec0d33e8bd0eccc1bd9bf1450a3e77a1460522664f280757db46", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_plan_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_plan_asset_leases_agent.py` is
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
