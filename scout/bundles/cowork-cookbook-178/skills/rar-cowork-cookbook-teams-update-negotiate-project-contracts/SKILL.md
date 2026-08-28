---
name: "rar-cowork-cookbook-teams-update-negotiate-project-contracts"
description: "Drafts a Teams channel post on negotiate project contracts status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_negotiate_project_contracts", "rar_sha256": "1c95eeac1f0db458a63c10ff1dd26ca779ba69e1f86ef2b4c828f8b79e7cb02e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
