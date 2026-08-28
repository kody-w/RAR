---
name: "rar-cowork-cookbook-dashboard-conduct-exit-interviews"
description: "Produces a self-contained interactive HTML dashboard for conduct exit interviews - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_conduct_exit_interviews", "rar_sha256": "828e84070c9a90f35dee67bcbabe1e01e5ed9ddf69e3ae2c0b57ca1b6ce26edb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 828e84070c9a90f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_conduct_exit_interviews_agent.py` first:

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
    "version": '2.0.1',
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
