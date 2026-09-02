---
name: "rar-cowork-cookbook-demo-data-maintain-contacts-and-accounts"
description: "Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_contacts_and_accounts", "rar_sha256": "5a08cbc100757428a9031ec3aaf72d4f26e71644c93c7f599fd3ab79f55dc78a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_maintain_contacts_and_accounts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-maintain-contacts-and-accounts:0a30331e2132da88760c658551be545c61d213cc62310b75a5f446e5a5403e23", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_maintain_contacts_and_accounts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_maintain_contacts_and_accounts_agent.py` is
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

Maintain contacts and accounts Demo Data Generator — Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 5a08cbc100757428…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 demo_data_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 demo_data_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Demo Data Generator — Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_maintain_contacts_and_accounts',
    "version": '2.0.0',
    "display_name": 'Maintain contacts and accounts Demo Data Generator',
    "description": 'Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5de9ae5905cd83b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMaintainContactsAndAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMaintainContactsAndAccounts'
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
    print(DemoDataMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
