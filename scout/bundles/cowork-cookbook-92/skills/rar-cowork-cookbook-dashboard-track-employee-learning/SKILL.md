---
name: "rar-cowork-cookbook-dashboard-track-employee-learning"
description: "Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_track_employee_learning", "rar_sha256": "bc5a0fc1a7e36dad3456916c272338d6a128e1221cfe5c20aa0dccf20dd8bdb8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 bc5a0fc1a7e36dad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_track_employee_learning_agent.py` first:

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
    "version": '2.0.0',
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
