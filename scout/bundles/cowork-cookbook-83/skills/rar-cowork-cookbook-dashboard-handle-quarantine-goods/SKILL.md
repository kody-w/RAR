---
name: "rar-cowork-cookbook-dashboard-handle-quarantine-goods"
description: "Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_handle_quarantine_goods", "rar_sha256": "3ced2d9a7573ecd23055767840700a3ac5f55cb0515a4b13196ebee18f58a288", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_handle_quarantine_goods`. The original RAPP
agent is preserved byte-for-byte in `dashboard_handle_quarantine_goods_agent.py` and in the RCI capsule.

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
