---
name: "rar-cowork-cookbook-teams-update-monitor-product-feedback"
description: "Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_product_feedback", "rar_sha256": "a453f760b7c6142c37e9159a73940f1417b1569a4651eaa02297507ab7cbac59", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_product_feedback`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_product_feedback_agent.py` and in the RCI capsule.

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

Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 a453f760b7c6142c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_product_feedback_agent.py` first:

```bash
python3 teams_update_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_product_feedback_agent.py   # or on stdin
python3 teams_update_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Teams Channel Update — Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_product_feedback',
    "version": '2.0.1',
    "display_name": 'Monitor product feedback Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor product feedback status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f61b82d5d522ff0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorProductFeedback(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorProductFeedback'
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
    print(TeamsUpdateMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
