---
name: "rar-cowork-cookbook-scheduled-brief-develop-project-approval-processes"
description: "Schedulable morning-brief email summarizing develop project approval processes for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_project_approval_processes", "rar_sha256": "f7212a4cdf82884a10199f586aa48d3109a8418525954ff8f953c68c19b83828", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_project_approval_processes_agent.py` and embedded as the fenced Python below (sha256 f7212a4cdf82884a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_project_approval_processes_agent.py` first:

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
    "version": '2.0.0',
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
