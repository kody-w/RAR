---
name: "rar-cowork-cookbook-dashboard-develop-tax-strategy"
description: "Produces a self-contained interactive HTML dashboard for develop tax strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_tax_strategy", "rar_sha256": "606e0f6981726e477f3751a72f228d91a82de0a56d14e59b94de653b34df9aef", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_tax_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 606e0f6981726e47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_tax_strategy_agent.py` first:

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
    "version": '2.0.1',
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
