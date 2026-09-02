---
name: "rar-cowork-cookbook-teams-update-engage-in-conversations-with-customers"
description: "Drafts a Teams channel post on engage in conversations with customers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_engage_in_conversations_with_customers", "rar_sha256": "66e3c6903851c97941a5973d01ed35035231c954caf38be52c43e0137488c60a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_engage_in_conversations_with_customers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-engage-in-conversations-with-customers:2fecbad1a63a38dac82ec0dbb205125c439e746a16ccda0cb7dbae788f0576fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_engage_in_conversations_with_customers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_engage_in_conversations_with_customers_agent.py` is
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
