---
name: "rar-cowork-cookbook-dashboard-evaluate-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for evaluate supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_evaluate_supplier_performance", "rar_sha256": "39bc4179cc2c1c2d9b17067ce485840275d6b6f881c0607ad88421274168917d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_evaluate_supplier_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-evaluate-supplier-performance:2711e3d2ce21e0bfc3a22e380df04803c6b4d4d1421086b4b4fb490f7e80dce7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_evaluate_supplier_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_evaluate_supplier_performance_agent.py` is
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
