---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-payable-policies"
description: "Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_payable_policies", "rar_sha256": "f7b52c976bf72b5db6cc71b98a2bf7a60f46eee8826e487da5eb0ccf6b87a757", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 f7b52c976bf72b5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_payable_policies_agent.py` first:

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
    "version": '2.0.0',
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
