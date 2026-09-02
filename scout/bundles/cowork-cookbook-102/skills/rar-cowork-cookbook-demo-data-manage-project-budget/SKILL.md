---
name: "rar-cowork-cookbook-demo-data-manage-project-budget"
description: "Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_project_budget", "rar_sha256": "84a278256788bea2bb3e22736bb718d997a2f66d5b7637de3589368bed0e536e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_project_budget_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-project-budget:cd7c9d4128cd0d8e41ebbf02d12b930e3844033bcc377b9314043be055d809bc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_project_budget`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_project_budget_agent.py` is
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

Manage project budget Demo Data Generator — Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 84a278256788bea2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_project_budget_agent.py` first:

```bash
python3 demo_data_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_project_budget_agent.py   # or on stdin
python3 demo_data_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Demo Data Generator — Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_project_budget',
    "version": '2.0.0',
    "display_name": 'Manage project budget Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5edc64f507583617',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageProjectBudget(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageProjectBudget'
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
    print(DemoDataManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
