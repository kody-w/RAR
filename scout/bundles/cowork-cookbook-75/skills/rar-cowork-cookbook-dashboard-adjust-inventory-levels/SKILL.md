---
name: "rar-cowork-cookbook-dashboard-adjust-inventory-levels"
description: "Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_adjust_inventory_levels", "rar_sha256": "6bebaad56adb787aeea31983d73ef0132b32756a6af8daa2af48bf32ba095173", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_adjust_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-adjust-inventory-levels:880ac73a3bbe284612756f52573a12bbf85756686d69dbb76ba4739fdbc0bbb1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_adjust_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_adjust_inventory_levels_agent.py` is
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

Adjust inventory levels Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 6bebaad56adb787a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_adjust_inventory_levels_agent.py` first:

```bash
python3 dashboard_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_adjust_inventory_levels_agent.py   # or on stdin
python3 dashboard_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_adjust_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Adjust inventory levels Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0d677d76519f6d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAdjustInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAdjustInventoryLevels'
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
    print(DashboardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
