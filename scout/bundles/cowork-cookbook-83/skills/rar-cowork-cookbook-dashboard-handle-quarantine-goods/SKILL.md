---
name: "rar-cowork-cookbook-dashboard-handle-quarantine-goods"
description: "Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_handle_quarantine_goods", "rar_sha256": "3ced2d9a7573ecd23055767840700a3ac5f55cb0515a4b13196ebee18f58a288", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_handle_quarantine_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-handle-quarantine-goods:02b2ed145b6c27030df0baa203e70e7d291cf08abb63e41af09314e5ab6f34f1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_handle_quarantine_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_handle_quarantine_goods_agent.py` is
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

Handle quarantine goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 3ced2d9a7573ecd2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_handle_quarantine_goods_agent.py` first:

```bash
python3 dashboard_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_handle_quarantine_goods_agent.py   # or on stdin
python3 dashboard_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_handle_quarantine_goods',
    "version": '2.0.0',
    "display_name": 'Handle quarantine goods Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1313ca5585b7c314',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardHandleQuarantineGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardHandleQuarantineGoods'
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
    print(DashboardHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
