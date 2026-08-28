---
name: "rar-cowork-cookbook-adaptive-card-control-project-scope"
description: "Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_control_project_scope", "rar_sha256": "90382e7dd90aa720a4aafa5ae578118000e8f5c9472446474788377f65e5d32f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_control_project_scope`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_control_project_scope_agent.py` and in the RCI capsule.

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

Control project scope Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 90382e7dd90aa720…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_control_project_scope_agent.py` first:

```bash
python3 adaptive_card_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_control_project_scope_agent.py   # or on stdin
python3 adaptive_card_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_control_project_scope',
    "version": '2.0.1',
    "display_name": 'Control project scope Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57de7c0c0db0367c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardControlProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardControlProjectScope'
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
    print(AdaptiveCardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
