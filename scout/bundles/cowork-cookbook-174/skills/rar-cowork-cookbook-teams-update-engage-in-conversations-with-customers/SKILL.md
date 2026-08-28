---
name: "rar-cowork-cookbook-teams-update-engage-in-conversations-with-customers"
description: "Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_engage_in_conversations_with_customers", "rar_sha256": "bc4c06aa6d7d0d1ab9402301e6243ac79eb0b5c863dc2e02af255b2f3aee7bec", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_engage_in_conversations_with_customers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_engage_in_conversations_with_customers_agent.py` and in the RCI capsule.

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

Engage in conversations with customers Teams Channel Update — Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 bc4c06aa6d7d0d1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_engage_in_conversations_with_customers_agent.py` first:

```bash
python3 teams_update_engage_in_conversations_with_customers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_engage_in_conversations_with_customers_agent.py   # or on stdin
python3 teams_update_engage_in_conversations_with_customers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engage in conversations with customers Teams Channel Update — Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_engage_in_conversations_with_customers',
    "version": '2.0.1',
    "display_name": 'Engage in conversations with customers Teams Channel Update',
    "description": 'Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-engage-in-conversations-with-customers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-engage-in-conversations-with-customers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0130496b94322db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/engage-in-conversations-with-customers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-engage-in-conversations-with-customers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateEngageInConversationsWithCustomers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEngageInConversationsWithCustomers'
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
    print(TeamsUpdateEngageInConversationsWithCustomers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
