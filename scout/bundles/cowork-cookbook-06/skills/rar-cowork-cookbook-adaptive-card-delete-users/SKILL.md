---
name: "rar-cowork-cookbook-adaptive-card-delete-users"
description: "Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_delete_users", "rar_sha256": "22d86ca4608592c0bc0b4513ad661265b4b2497522ec00d08d43e39f189103b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_delete_users_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-delete-users:c069e5feeee11234badd99c5a36e64a751606765d957a38f2b90b55acc5cbf41", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_delete_users`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_delete_users_agent.py` is
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

Delete users Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_delete_users_agent.py` and embedded as the fenced Python below (sha256 22d86ca4608592c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_delete_users_agent.py` first:

```bash
python3 adaptive_card_delete_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_delete_users_agent.py   # or on stdin
python3 adaptive_card_delete_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Delete users Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-delete-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_delete_users',
    "version": '2.0.0',
    "display_name": 'Delete users Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-delete-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-delete-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ed3b0c8a16e525a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/delete-users'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-delete-users', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDeleteUsers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeleteUsers'
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
    print(AdaptiveCardDeleteUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
