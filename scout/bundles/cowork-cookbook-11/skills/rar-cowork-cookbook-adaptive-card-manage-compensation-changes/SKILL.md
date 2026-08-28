---
name: "rar-cowork-cookbook-adaptive-card-manage-compensation-changes"
description: "Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_compensation_changes", "rar_sha256": "3784ea2c120dcad3fcad5c4a6b9f53e609eb48056d6b77d1c126b149c74e23d9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_compensation_changes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_compensation_changes_agent.py` and in the RCI capsule.

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

Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 3784ea2c120dcad3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_compensation_changes_agent.py` first:

```bash
python3 adaptive_card_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_compensation_changes_agent.py   # or on stdin
python3 adaptive_card_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_compensation_changes',
    "version": '2.0.1',
    "display_name": 'Manage compensation changes Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage compensation changes status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2049405bac09391a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageCompensationChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageCompensationChanges'
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
    print(AdaptiveCardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
