---
name: "rar-cowork-cookbook-dashboard-record-cost-of-quality"
description: "Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_cost_of_quality", "rar_sha256": "0b9a1ee9873db8e72ad726014dea8247023f6ec30161485d16dc8bb66ee599e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 0b9a1ee9873db8e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_record_cost_of_quality_agent.py` first:

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
    "version": '2.0.1',
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
