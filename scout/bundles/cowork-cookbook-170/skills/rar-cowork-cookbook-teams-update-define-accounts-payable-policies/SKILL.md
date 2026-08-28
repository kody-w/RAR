---
name: "rar-cowork-cookbook-teams-update-define-accounts-payable-policies"
description: "Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_accounts_payable_policies", "rar_sha256": "33f92ffff22902b63f495d614d0421bfe5261f7e6a383615647e3ef3b889dacb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_accounts_payable_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_accounts_payable_policies_agent.py` and in the RCI capsule.

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
