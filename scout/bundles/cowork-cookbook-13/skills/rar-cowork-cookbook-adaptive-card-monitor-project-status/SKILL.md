---
name: "rar-cowork-cookbook-adaptive-card-monitor-project-status"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_project_status", "rar_sha256": "24892a54665cf4691eec585057bcff979393df763a59cb7024526fbc5eb60428", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_project_status`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_project_status_agent.py` and in the RCI capsule.

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

Monitor project status Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 24892a54665cf469…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_project_status_agent.py` first:

```bash
python3 adaptive_card_monitor_project_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_project_status_agent.py   # or on stdin
python3 adaptive_card_monitor_project_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project status Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_project_status',
    "version": '2.0.1',
    "display_name": 'Monitor project status Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-monitor-project-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-project-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf473351ed6cc839',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-status'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-monitor-project-status', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMonitorProjectStatus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorProjectStatus'
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
    print(AdaptiveCardMonitorProjectStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
