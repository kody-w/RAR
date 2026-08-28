---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-payable-policies"
description: "Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_payable_policies", "rar_sha256": "b250da6d1668b096254f1e8defc1e76f71d8770cf2d708e9d62dc42967dd0667", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_accounts_payable_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_accounts_payable_policies_agent.py` and in the RCI capsule.

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

Define accounts payable policies Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 b250da6d1668b096…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_payable_policies_agent.py` first:

```bash
python3 scheduled_brief_define_accounts_payable_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_accounts_payable_policies_agent.py   # or on stdin
python3 scheduled_brief_define_accounts_payable_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts payable policies Scheduled Email Brief — Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_accounts_payable_policies',
    "version": '2.0.1',
    "display_name": 'Define accounts payable policies Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-accounts-payable-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8769839eba4cce23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/define-accounts-payable-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-define-accounts-payable-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineAccountsPayablePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineAccountsPayablePolicies'
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
    print(ScheduledBriefDefineAccountsPayablePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
