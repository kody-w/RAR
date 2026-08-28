---
name: "rar-cowork-cookbook-demo-data-maintain-contacts-and-accounts"
description: "Generates and creates realistic demo records for maintain contacts and accounts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_contacts_and_accounts", "rar_sha256": "d84d52d74aef10dd71b78dc4b6d3c86dfdf6bc0d2d1418bac09988b01f321588", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 d84d52d74aef10dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_contacts_and_accounts_agent.py` first:

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
    "version": '2.0.1',
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
