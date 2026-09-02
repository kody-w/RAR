---
name: "rar-cowork-cookbook-demo-data-plan-projects-resources"
description: "Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_projects_resources", "rar_sha256": "4c765f23fa98565ed26c00e10104ce45bc7ba51b7aa9a064925e1a558ef47d75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_plan_projects_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-plan-projects-resources:3c6ffe287993bdf299eb80305baa7b57d16690d01f289514aa93501b8e2093fa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_plan_projects_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_plan_projects_resources_agent.py` is
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

Plan projects resources Demo Data Generator — Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 4c765f23fa98565e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_projects_resources_agent.py` first:

```bash
python3 demo_data_plan_projects_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_projects_resources_agent.py   # or on stdin
python3 demo_data_plan_projects_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects resources Demo Data Generator — Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_projects_resources',
    "version": '2.0.0',
    "display_name": 'Plan projects resources Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-projects-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-projects-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a33ef3c7f8f5e1a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-projects-resources'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-plan-projects-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPlanProjectsResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProjectsResources'
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
    print(DemoDataPlanProjectsResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
