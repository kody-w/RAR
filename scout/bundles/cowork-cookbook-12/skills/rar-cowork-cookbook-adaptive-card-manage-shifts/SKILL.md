---
name: "rar-cowork-cookbook-adaptive-card-manage-shifts"
description: "Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_shifts", "rar_sha256": "56a0e7b20e00a36d1084b3d301a4ffbc549abf2592a6415dc01f1fcf4230abee", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_shifts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_shifts_agent.py` and in the RCI capsule.

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

Manage shifts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 56a0e7b20e00a36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_shifts_agent.py` first:

```bash
python3 adaptive_card_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_shifts_agent.py   # or on stdin
python3 adaptive_card_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_shifts',
    "version": '2.0.1',
    "display_name": 'Manage shifts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5ef494ef30dca259',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageShifts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageShifts'
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
    print(AdaptiveCardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
