---
name: "rar-cowork-cookbook-adaptive-card-delete-users"
description: "Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_delete_users", "rar_sha256": "22d86ca4608592c0bc0b4513ad661265b4b2497522ec00d08d43e39f189103b1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_delete_users`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_delete_users_agent.py` and in the RCI capsule.

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
