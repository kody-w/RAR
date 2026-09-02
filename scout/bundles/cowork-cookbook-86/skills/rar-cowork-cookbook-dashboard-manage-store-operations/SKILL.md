---
name: "rar-cowork-cookbook-dashboard-manage-store-operations"
description: "Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_store_operations", "rar_sha256": "c099aee5776d0bba02f6a4350d88aa340f6d20cfab22a35e9bc0d044d20d9cf8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_store_operations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-store-operations:f547f38f3abb8407498c6425eaabc583954e9620acff7dc97cd9096820fd1b75", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_store_operations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_store_operations_agent.py` is
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

Manage store operations Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_store_operations_agent.py` and embedded as the fenced Python below (sha256 c099aee5776d0bba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_store_operations_agent.py` first:

```bash
python3 dashboard_manage_store_operations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_store_operations_agent.py   # or on stdin
python3 dashboard_manage_store_operations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage store operations Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-store-operations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_store_operations',
    "version": '2.0.0',
    "display_name": 'Manage store operations Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage store operations - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-store-operations',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-store-operations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '218d35fed7c19591',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-store-operations'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-manage-store-operations', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageStoreOperations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageStoreOperations'
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
    print(DashboardManageStoreOperations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
