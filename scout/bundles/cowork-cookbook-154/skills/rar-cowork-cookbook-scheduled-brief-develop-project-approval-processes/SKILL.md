---
name: "rar-cowork-cookbook-scheduled-brief-develop-project-approval-processes"
description: "Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_project_approval_processes", "rar_sha256": "574cbf059edf307c276d3fca619660a3596439d94208fbdcb5c7b4edcf6c827a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_project_approval_processes`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_project_approval_processes_agent.py` and in the RCI capsule.

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

Develop project approval processes Scheduled Email Brief — Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 574cbf059edf307c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_project_approval_processes_agent.py` first:

```bash
python3 scheduled_brief_develop_project_approval_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_project_approval_processes_agent.py   # or on stdin
python3 scheduled_brief_develop_project_approval_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project approval processes Scheduled Email Brief — Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_project_approval_processes',
    "version": '2.0.1',
    "display_name": 'Develop project approval processes Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-project-approval-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-project-approval-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc2f2fc68f98a324',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-approval-processes'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-develop-project-approval-processes', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopProjectApprovalProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProjectApprovalProcesses'
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
    print(ScheduledBriefDevelopProjectApprovalProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
