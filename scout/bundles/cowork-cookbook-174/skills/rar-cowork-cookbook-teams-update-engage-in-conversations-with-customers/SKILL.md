---
name: "rar-cowork-cookbook-teams-update-engage-in-conversations-with-customers"
description: "Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_engage_in_conversations_with_customers", "rar_sha256": "66e3c6903851c97941a5973d01ed35035231c954caf38be52c43e0137488c60a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_engage_in_conversations_with_customers_agent.py` and embedded as the fenced Python below (sha256 66e3c6903851c979…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_engage_in_conversations_with_customers_agent.py` first:

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
    "version": '2.0.0',
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
