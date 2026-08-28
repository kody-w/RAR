---
name: "rar-cowork-cookbook-teams-update-define-accounts-payable-policies"
description: "Drafts a Teams channel post on define accounts payable policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_accounts_payable_policies", "rar_sha256": "a9da69a3347d77766d2ae9d10a1a245b423d3eaec29568a1ff1711dacbfbf94e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 a9da69a3347d7776…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_accounts_payable_policies_agent.py` first:

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
    "version": '2.0.1',
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
