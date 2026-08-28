---
name: "rar-cowork-cookbook-dashboard-identify-strategic-initiatives"
description: "Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_strategic_initiatives", "rar_sha256": "d6d9d074fe00d521f3b35e27626829d0b05a62a4b6c76a4485ac3cd95866b8b4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 d6d9d074fe00d521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_strategic_initiatives_agent.py` first:

```bash
python3 dashboard_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_strategic_initiatives_agent.py   # or on stdin
python3 dashboard_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_strategic_initiatives',
    "version": '2.0.1',
    "display_name": 'Identify strategic initiatives Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify strategic initiatives - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad51f0be9fc19d9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyStrategicInitiatives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyStrategicInitiatives'
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
    print(DashboardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
