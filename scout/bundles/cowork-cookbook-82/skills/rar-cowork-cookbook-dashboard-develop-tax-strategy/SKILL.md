---
name: "rar-cowork-cookbook-dashboard-develop-tax-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_tax_strategy", "rar_sha256": "5502821e9c0ba5add78a1fb267b4a42cdc677056a360607c7c6d49f48cb57cca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_tax_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-tax-strategy:32b875d757125cf63547e6c893ca24781c13b82dbd082f5cad5d9ed4db530b37", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_tax_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_tax_strategy_agent.py` is
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

Develop tax strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 5502821e9c0ba5ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_tax_strategy_agent.py` first:

```bash
python3 dashboard_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_tax_strategy_agent.py   # or on stdin
python3 dashboard_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_tax_strategy',
    "version": '2.0.0',
    "display_name": 'Develop tax strategy Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b06e3d358790bd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardDevelopTaxStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopTaxStrategy'
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
    print(DashboardDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
