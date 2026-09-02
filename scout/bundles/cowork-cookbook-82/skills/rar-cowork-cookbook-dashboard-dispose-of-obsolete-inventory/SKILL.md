---
name: "rar-cowork-cookbook-dashboard-dispose-of-obsolete-inventory"
description: "Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_dispose_of_obsolete_inventory", "rar_sha256": "ae778115b7a8e732a8bea6d0d58672aa82ab3d24e36a4876840a6235f8484535", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_dispose_of_obsolete_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-dispose-of-obsolete-inventory:e5d6f0c24f108a48f26d66fd0324d6323a463e2d3b52fbc72ebe5ae7392a5475", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_dispose_of_obsolete_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_dispose_of_obsolete_inventory_agent.py` is
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

Dispose of obsolete inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 ae778115b7a8e732…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_dispose_of_obsolete_inventory_agent.py` first:

```bash
python3 dashboard_dispose_of_obsolete_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_dispose_of_obsolete_inventory_agent.py   # or on stdin
python3 dashboard_dispose_of_obsolete_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispose of obsolete inventory Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_dispose_of_obsolete_inventory',
    "version": '2.0.0',
    "display_name": 'Dispose of obsolete inventory Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-dispose-of-obsolete-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-dispose-of-obsolete-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87758678d29f07ab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/dispose-of-obsolete-inventory'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-dispose-of-obsolete-inventory', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDisposeOfObsoleteInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDisposeOfObsoleteInventory'
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
    print(DashboardDisposeOfObsoleteInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
