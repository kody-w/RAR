---
name: "rar-cowork-cookbook-teams-update-establish-support-subscription"
description: "Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_support_subscription", "rar_sha256": "739095eb5fd2b76e531852e874d2f4c78412ce2729ef0667154b3b564d5d351a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_establish_support_subscription`. The original RAPP
agent is preserved byte-for-byte in `teams_update_establish_support_subscription_agent.py` and in the RCI capsule.

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
