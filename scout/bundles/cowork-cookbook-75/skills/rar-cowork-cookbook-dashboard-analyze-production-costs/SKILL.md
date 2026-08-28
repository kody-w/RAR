---
name: "rar-cowork-cookbook-dashboard-analyze-production-costs"
description: "Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_production_costs", "rar_sha256": "dcacc0b60da54dc3cbf0e6ca2b12eb565f8eb6fc3e76b27979d24890f1f81d99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_production_costs`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_production_costs_agent.py` and in the RCI capsule.

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

Analyze production costs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 dcacc0b60da54dc3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_production_costs_agent.py` first:

```bash
python3 dashboard_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_production_costs_agent.py   # or on stdin
python3 dashboard_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_production_costs',
    "version": '2.0.0',
    "display_name": 'Analyze production costs Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b8bb1b6a440ce95',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardAnalyzeProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeProductionCosts'
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
    print(DashboardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
