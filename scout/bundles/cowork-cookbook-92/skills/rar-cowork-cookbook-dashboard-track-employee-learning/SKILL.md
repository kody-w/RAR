---
name: "rar-cowork-cookbook-dashboard-track-employee-learning"
description: "Produces a self-contained interactive HTML dashboard for track employee learning - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_track_employee_learning", "rar_sha256": "bc5a0fc1a7e36dad3456916c272338d6a128e1221cfe5c20aa0dccf20dd8bdb8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_track_employee_learning_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-track-employee-learning:4f162d7eaca6b60ea1cf0e0227ded5782245063e6b27b5c033ff41fbe1e965cf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_track_employee_learning`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_track_employee_learning_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
