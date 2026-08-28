---
name: "rar-cowork-cookbook-teams-update-negotiate-project-contracts"
description: "Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_negotiate_project_contracts", "rar_sha256": "1b2e3bfdb4675419de83221f72b0eb285fb85e22f684eb074e60b0b31c13677b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_negotiate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `teams_update_negotiate_project_contracts_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 1b2e3bfdb4675419…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_negotiate_project_contracts_agent.py` first:

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
    "version": '2.0.1',
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
