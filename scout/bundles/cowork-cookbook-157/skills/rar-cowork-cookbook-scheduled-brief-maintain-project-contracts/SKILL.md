---
name: "rar-cowork-cookbook-scheduled-brief-maintain-project-contracts"
description: "Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_project_contracts", "rar_sha256": "8734d7a7930e8c042439bfabf587066b39cde359c048dced1c764ef071cfd5ed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 8734d7a7930e8c04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_project_contracts_agent.py` first:

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
    "version": '2.0.1',
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
