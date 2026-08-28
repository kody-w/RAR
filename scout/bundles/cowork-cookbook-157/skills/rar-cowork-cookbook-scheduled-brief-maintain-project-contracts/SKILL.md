---
name: "rar-cowork-cookbook-scheduled-brief-maintain-project-contracts"
description: "Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_project_contracts", "rar_sha256": "407e6f0eb5b07ed9ceb2c9a2591fa80e57bc28329057a4e42f55015ef3389235", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_maintain_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_maintain_project_contracts_agent.py` and in the RCI capsule.

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

Maintain project contracts Scheduled Email Brief — Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 407e6f0eb5b07ed9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_project_contracts_agent.py` first:

```bash
python3 scheduled_brief_maintain_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_project_contracts_agent.py   # or on stdin
python3 scheduled_brief_maintain_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain project contracts Scheduled Email Brief — Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_project_contracts',
    "version": '2.0.0',
    "display_name": 'Maintain project contracts Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-maintain-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a568b54533ce8e17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/maintain-project-contracts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-maintain-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMaintainProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainProjectContracts'
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
    print(ScheduledBriefMaintainProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
