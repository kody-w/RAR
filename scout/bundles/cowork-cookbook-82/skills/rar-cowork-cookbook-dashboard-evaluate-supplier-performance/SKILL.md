---
name: "rar-cowork-cookbook-dashboard-evaluate-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_evaluate_supplier_performance", "rar_sha256": "7323b95f9dd4b945dbdac6a558ba9efee7a24e42f9f96dd7d93824f0c0a68467", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 7323b95f9dd4b945…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_evaluate_supplier_performance_agent.py` first:

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
    "version": '2.0.1',
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
