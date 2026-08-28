---
name: "rar-cowork-cookbook-demo-data-maintain-contacts-and-accounts"
description: "Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_contacts_and_accounts", "rar_sha256": "5a08cbc100757428a9031ec3aaf72d4f26e71644c93c7f599fd3ab79f55dc78a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_maintain_contacts_and_accounts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_maintain_contacts_and_accounts_agent.py` and in the RCI capsule.

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
