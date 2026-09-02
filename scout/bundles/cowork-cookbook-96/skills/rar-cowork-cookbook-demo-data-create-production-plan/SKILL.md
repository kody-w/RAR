---
name: "rar-cowork-cookbook-demo-data-create-production-plan"
description: "Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_production_plan", "rar_sha256": "ff97129c25f9a6a153c582102ce6bf183562e1cf8e2d0769e197be340daa6114", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_create_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-create-production-plan:9bbbb01eadd4c1c007379238dce9a23252b48ce622f81e84870e2e54db32c091", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_create_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_create_production_plan_agent.py` is
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

Create production plan Demo Data Generator — Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 ff97129c25f9a6a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_production_plan_agent.py` first:

```bash
python3 demo_data_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_production_plan_agent.py   # or on stdin
python3 demo_data_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Demo Data Generator — Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_production_plan',
    "version": '2.0.0',
    "display_name": 'Create production plan Demo Data Generator',
    "description": 'Generates and creates realistic demo records for create production plan in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b1dc776c3fe8213',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCreateProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateProductionPlan'
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
    print(DemoDataCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
