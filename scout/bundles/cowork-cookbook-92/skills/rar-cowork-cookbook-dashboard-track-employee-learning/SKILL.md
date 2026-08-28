---
name: "rar-cowork-cookbook-dashboard-track-employee-learning"
description: "Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_track_employee_learning", "rar_sha256": "f09853a16ad97170abdd40ab1c9807fbb6760768a9a7b59668b8f495aadca406", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_track_employee_learning`. The original RAPP
agent is preserved byte-for-byte in `dashboard_track_employee_learning_agent.py` and in the RCI capsule.

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

Track employee learning Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-track-employee-learning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 f09853a16ad97170…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_track_employee_learning_agent.py` first:

```bash
python3 dashboard_track_employee_learning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_track_employee_learning_agent.py   # or on stdin
python3 dashboard_track_employee_learning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track employee learning Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-track-employee-learning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_track_employee_learning',
    "version": '2.0.1',
    "display_name": 'Track employee learning Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-track-employee-learning',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-track-employee-learning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '398aaebf6aa271f1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/track-employee-learning'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-track-employee-learning', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardTrackEmployeeLearning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTrackEmployeeLearning'
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
    print(DashboardTrackEmployeeLearning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
