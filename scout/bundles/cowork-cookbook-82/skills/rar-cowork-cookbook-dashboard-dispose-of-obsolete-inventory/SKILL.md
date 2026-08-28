---
name: "rar-cowork-cookbook-dashboard-dispose-of-obsolete-inventory"
description: "Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_dispose_of_obsolete_inventory", "rar_sha256": "ae778115b7a8e732a8bea6d0d58672aa82ab3d24e36a4876840a6235f8484535", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_dispose_of_obsolete_inventory`. The original RAPP
agent is preserved byte-for-byte in `dashboard_dispose_of_obsolete_inventory_agent.py` and in the RCI capsule.

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
