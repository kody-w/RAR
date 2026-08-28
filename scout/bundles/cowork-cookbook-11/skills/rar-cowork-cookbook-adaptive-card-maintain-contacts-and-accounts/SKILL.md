---
name: "rar-cowork-cookbook-adaptive-card-maintain-contacts-and-accounts"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts", "rar_sha256": "a34e594093820c8d7bd24e5dfc6a88c50c3a04265ca11d171efbe2d8033c1e9d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_contacts_and_accounts_agent.py` and in the RCI capsule.

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

Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 a34e594093820c8d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 adaptive_card_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 adaptive_card_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts',
    "version": '2.0.0',
    "display_name": 'Maintain contacts and accounts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44265f0fe26455c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardMaintainContactsAndAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainContactsAndAccounts'
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
    print(AdaptiveCardMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
