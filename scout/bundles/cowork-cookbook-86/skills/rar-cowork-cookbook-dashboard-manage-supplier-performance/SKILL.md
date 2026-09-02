---
name: "rar-cowork-cookbook-dashboard-manage-supplier-performance"
description: "Produces a self-contained interactive HTML dashboard for manage supplier performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_performance", "rar_sha256": "1e27bfc90a792a5131cd4cffad04a02b9797c8601dd4e5c1754fc7ed16179685", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_supplier_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-supplier-performance:fbb14ba42ca2d487bc2fcd5e727d447a4d049519d08da2f85d8ae039ddca8282", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_supplier_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_supplier_performance_agent.py` is
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
