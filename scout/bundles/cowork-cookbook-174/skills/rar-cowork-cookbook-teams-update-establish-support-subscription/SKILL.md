---
name: "rar-cowork-cookbook-teams-update-establish-support-subscription"
description: "Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_support_subscription", "rar_sha256": "739095eb5fd2b76e531852e874d2f4c78412ce2729ef0667154b3b564d5d351a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_establish_support_subscription_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-establish-support-subscription:d97c2dd69614c8e4198afc52a64292f9b8bc76d91db5ff7c587780bc19c2c154", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_establish_support_subscription`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_establish_support_subscription_agent.py` is
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

Establish support subscription Teams Channel Update — Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-support-subscription
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 739095eb5fd2b76e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_support_subscription_agent.py` first:

```bash
python3 teams_update_establish_support_subscription_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_establish_support_subscription_agent.py   # or on stdin
python3 teams_update_establish_support_subscription_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support subscription Teams Channel Update — Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-support-subscription
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_establish_support_subscription',
    "version": '2.0.0',
    "display_name": 'Establish support subscription Teams Channel Update',
    "description": 'Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-establish-support-subscription',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-establish-support-subscription',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6030133386229fe6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-subscription'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-establish-support-subscription', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateEstablishSupportSubscription(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstablishSupportSubscription'
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
    print(TeamsUpdateEstablishSupportSubscription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
