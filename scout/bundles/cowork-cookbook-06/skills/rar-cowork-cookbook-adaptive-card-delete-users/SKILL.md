---
name: "rar-cowork-cookbook-adaptive-card-delete-users"
description: "Produces a reusable Adaptive Card JSON snapshot of delete users status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_delete_users", "rar_sha256": "64f96a76345008b348939cb707efc2204b84fd5a08f3253b3c2ad118832b43eb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_delete_users_agent.py` and embedded as the fenced Python below (sha256 64f96a76345008b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_delete_users_agent.py` first:

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
    "version": '2.0.1',
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
