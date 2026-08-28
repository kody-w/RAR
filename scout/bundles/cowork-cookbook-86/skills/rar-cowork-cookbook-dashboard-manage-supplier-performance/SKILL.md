---
name: "rar-cowork-cookbook-dashboard-manage-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_performance", "rar_sha256": "1e27bfc90a792a5131cd4cffad04a02b9797c8601dd4e5c1754fc7ed16179685", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 1e27bfc90a792a51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_performance_agent.py` first:

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
    "version": '2.0.0',
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
