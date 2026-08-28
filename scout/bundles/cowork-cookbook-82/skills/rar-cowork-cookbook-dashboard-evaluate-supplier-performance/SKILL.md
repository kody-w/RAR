---
name: "rar-cowork-cookbook-dashboard-evaluate-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_evaluate_supplier_performance", "rar_sha256": "39bc4179cc2c1c2d9b17067ce485840275d6b6f881c0607ad88421274168917d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_evaluate_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_evaluate_supplier_performance_agent.py` and in the RCI capsule.

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

Evaluate supplier performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 39bc4179cc2c1c2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_evaluate_supplier_performance_agent.py` first:

```bash
python3 dashboard_evaluate_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_evaluate_supplier_performance_agent.py   # or on stdin
python3 dashboard_evaluate_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_evaluate_supplier_performance',
    "version": '2.0.0',
    "display_name": 'Evaluate supplier performance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-evaluate-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-evaluate-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e38e222b9eea3fdd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/evaluate-supplier-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-evaluate-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardEvaluateSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEvaluateSupplierPerformance'
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
    print(DashboardEvaluateSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
