---
name: "rar-cowork-cookbook-adaptive-card-monitor-project-status"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor project status status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_project_status", "rar_sha256": "45dc6addb2033428583c6fbc49cc036835e2d702b75fb8e6acee03e71ad6b886", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 45dc6addb2033428…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_project_status_agent.py` first:

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
    "version": '2.0.0',
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
