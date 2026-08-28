---
name: "rar-cowork-cookbook-teams-update-establish-support-subscription"
description: "Drafts a Teams channel post on establish support subscription status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_support_subscription", "rar_sha256": "2eed7fd5eb08a6e8036a315bd4bb0d22dc5eb6256fd482d05b12b139a088dbaa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 2eed7fd5eb08a6e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_support_subscription_agent.py` first:

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
    "version": '2.0.1',
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
