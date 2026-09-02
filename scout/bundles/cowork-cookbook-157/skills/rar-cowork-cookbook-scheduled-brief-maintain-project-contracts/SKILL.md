---
name: "rar-cowork-cookbook-scheduled-brief-maintain-project-contracts"
description: "Schedulable morning-brief email summarizing maintain project contracts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_project_contracts", "rar_sha256": "407e6f0eb5b07ed9ceb2c9a2591fa80e57bc28329057a4e42f55015ef3389235", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_maintain_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-maintain-project-contracts:a783dffad1648a43296638547c2114ea86b8df6e3d7e6cf89bf616b6200ca82c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_maintain_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_maintain_project_contracts_agent.py` is
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
