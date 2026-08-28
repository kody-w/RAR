---
name: "rar-cowork-cookbook-adaptive-card-control-project-scope"
description: "Produces a reusable Adaptive Card JSON snapshot of control project scope status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_control_project_scope", "rar_sha256": "5675620bca86cec6b3e9a37c7a610a9c5eec079b5e557cf074b995eaffebb84e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 5675620bca86cec6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_control_project_scope_agent.py` first:

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
    "version": '2.0.0',
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
