---
name: "rar-cowork-cookbook-dashboard-record-cost-of-quality"
description: "Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_cost_of_quality", "rar_sha256": "321ef529614e21ea698d8ed1099df3a528bd62726288c38068da0fe6294e9e17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_record_cost_of_quality`. The original RAPP
agent is preserved byte-for-byte in `dashboard_record_cost_of_quality_agent.py` and in the RCI capsule.

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

Record cost of quality Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 321ef529614e21ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_cost_of_quality_agent.py` first:

```bash
python3 dashboard_record_cost_of_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_record_cost_of_quality_agent.py   # or on stdin
python3 dashboard_record_cost_of_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost of quality Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_record_cost_of_quality',
    "version": '2.0.0',
    "display_name": 'Record cost of quality Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-record-cost-of-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-record-cost-of-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7a14b2627ec3f95',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/record-cost-of-quality'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-record-cost-of-quality', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRecordCostOfQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRecordCostOfQuality'
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
    print(DashboardRecordCostOfQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
