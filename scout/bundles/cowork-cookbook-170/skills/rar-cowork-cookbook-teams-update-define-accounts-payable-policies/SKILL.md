---
name: "rar-cowork-cookbook-teams-update-define-accounts-payable-policies"
description: "Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_accounts_payable_policies", "rar_sha256": "33f92ffff22902b63f495d614d0421bfe5261f7e6a383615647e3ef3b889dacb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_accounts_payable_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-accounts-payable-policies:3825e2c83eb8ec42af2e4d3f0e91658df7b15148614eb9ea9e87e76047f53733", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_accounts_payable_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_accounts_payable_policies_agent.py` is
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

Define accounts payable policies Teams Channel Update — Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 33f92ffff22902b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_accounts_payable_policies_agent.py` first:

```bash
python3 teams_update_define_accounts_payable_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_accounts_payable_policies_agent.py   # or on stdin
python3 teams_update_define_accounts_payable_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts payable policies Teams Channel Update — Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_accounts_payable_policies',
    "version": '2.0.0',
    "display_name": 'Define accounts payable policies Teams Channel Update',
    "description": 'Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-accounts-payable-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-accounts-payable-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c40bc5893c140292',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/define-accounts-payable-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-define-accounts-payable-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineAccountsPayablePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineAccountsPayablePolicies'
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
    print(TeamsUpdateDefineAccountsPayablePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
