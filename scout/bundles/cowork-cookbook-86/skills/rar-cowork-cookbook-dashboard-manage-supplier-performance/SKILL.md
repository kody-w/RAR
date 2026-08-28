---
name: "rar-cowork-cookbook-dashboard-manage-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_performance", "rar_sha256": "a4eb2b814c3cf7504a87564e1ff0f786fe520176c8ca54c1555b5d2c34c5bfaa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_supplier_performance_agent.py` and in the RCI capsule.

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

Manage supplier performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 a4eb2b814c3cf750…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_performance_agent.py` first:

```bash
python3 dashboard_manage_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_supplier_performance_agent.py   # or on stdin
python3 dashboard_manage_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_supplier_performance',
    "version": '2.0.1',
    "display_name": 'Manage supplier performance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6486c1a726318ead',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-supplier-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageSupplierPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageSupplierPerformance'
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
    print(DashboardManageSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
