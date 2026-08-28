---
name: "rar-cowork-cookbook-adaptive-card-manage-shifts"
description: "Produces a reusable Adaptive Card JSON snapshot of manage shifts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_shifts", "rar_sha256": "387b33ee9553fed500d5a5e21ffcf356c1d2e291872201fb43bb430ba41a85fc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 387b33ee9553fed5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_shifts_agent.py` first:

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
    "version": '2.0.0',
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
