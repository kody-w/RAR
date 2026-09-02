---
name: "rar-cowork-cookbook-dashboard-record-cost-of-quality"
description: "Produces a self-contained interactive HTML dashboard for record cost of quality - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_record_cost_of_quality", "rar_sha256": "321ef529614e21ea698d8ed1099df3a528bd62726288c38068da0fe6294e9e17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_record_cost_of_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-record-cost-of-quality:35ad0f844e050d9dee825bd035f2beff62e8081fd6ea85ef35608e5b14831f5e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_record_cost_of_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_record_cost_of_quality_agent.py` is
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
