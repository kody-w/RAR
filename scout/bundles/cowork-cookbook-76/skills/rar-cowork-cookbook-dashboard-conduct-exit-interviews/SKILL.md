---
name: "rar-cowork-cookbook-dashboard-conduct-exit-interviews"
description: "Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_conduct_exit_interviews", "rar_sha256": "72280e6a8f6a9283acaef79b33def4e8033abf73e0fd89c7e298f687a608e377", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_conduct_exit_interviews`. The original RAPP
agent is preserved byte-for-byte in `dashboard_conduct_exit_interviews_agent.py` and in the RCI capsule.

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

Conduct exit interviews Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 72280e6a8f6a9283…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_conduct_exit_interviews_agent.py` first:

```bash
python3 dashboard_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_conduct_exit_interviews_agent.py   # or on stdin
python3 dashboard_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_conduct_exit_interviews',
    "version": '2.0.0',
    "display_name": 'Conduct exit interviews Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c5d872df35cbaa0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConductExitInterviews(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConductExitInterviews'
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
    print(DashboardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
