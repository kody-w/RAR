---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-payable-policies"
description: "Schedulable morning-brief email summarizing define accounts payable policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_payable_policies", "rar_sha256": "f7b52c976bf72b5db6cc71b98a2bf7a60f46eee8826e487da5eb0ccf6b87a757", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_accounts_payable_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-accounts-payable-policies:c51a4c26f6c6150b87386bddfce318d8aad6b1e5d0ebeabf2f309cb3c4d31211", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_accounts_payable_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_accounts_payable_policies_agent.py` is
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
