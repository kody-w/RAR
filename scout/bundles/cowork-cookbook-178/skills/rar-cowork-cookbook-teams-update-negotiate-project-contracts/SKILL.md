---
name: "rar-cowork-cookbook-teams-update-negotiate-project-contracts"
description: "Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_negotiate_project_contracts", "rar_sha256": "1c95eeac1f0db458a63c10ff1dd26ca779ba69e1f86ef2b4c828f8b79e7cb02e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_negotiate_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-negotiate-project-contracts:554e769b30118d94fd71b9727e8c2f23a90e800f2b960643aec1aa99739c17da", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_negotiate_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_negotiate_project_contracts_agent.py` is
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

Negotiate project contracts Teams Channel Update — Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 1c95eeac1f0db458…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_negotiate_project_contracts_agent.py` first:

```bash
python3 teams_update_negotiate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_negotiate_project_contracts_agent.py   # or on stdin
python3 teams_update_negotiate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate project contracts Teams Channel Update — Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_negotiate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Negotiate project contracts Teams Channel Update',
    "description": 'Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-negotiate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-negotiate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4918429d5a58bce6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/negotiate-project-contracts'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-negotiate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateNegotiateProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateNegotiateProjectContracts'
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
    print(TeamsUpdateNegotiateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
