---
name: "rar-cowork-cookbook-dashboard-manage-supplier-pricing"
description: "Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_pricing", "rar_sha256": "604f551d1bea7a83933e7ac5313975f2f0674144109afb6571f31146cc92925c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_supplier_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-supplier-pricing:a8701727ec1b2f60d4d4dc3608854f554cbc854d7f935c4eaa08c76b4fd01366", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_supplier_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_supplier_pricing_agent.py` is
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

Manage supplier pricing Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 604f551d1bea7a83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_pricing_agent.py` first:

```bash
python3 dashboard_manage_supplier_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_supplier_pricing_agent.py   # or on stdin
python3 dashboard_manage_supplier_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier pricing Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_supplier_pricing',
    "version": '2.0.0',
    "display_name": 'Manage supplier pricing Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-supplier-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '444cd4d293bdf6f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-pricing'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-supplier-pricing', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageSupplierPricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageSupplierPricing'
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
    print(DashboardManageSupplierPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
