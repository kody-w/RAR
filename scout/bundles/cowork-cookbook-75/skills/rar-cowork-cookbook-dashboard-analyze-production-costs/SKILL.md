---
name: "rar-cowork-cookbook-dashboard-analyze-production-costs"
description: "Produces a self-contained interactive HTML dashboard for analyze production costs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_production_costs", "rar_sha256": "dcacc0b60da54dc3cbf0e6ca2b12eb565f8eb6fc3e76b27979d24890f1f81d99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_analyze_production_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-analyze-production-costs:ff2a2925095be9b00a660635ff23da817c89b6b6e6e66dc4398b265fb98e9772", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_analyze_production_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_analyze_production_costs_agent.py` is
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
