---
name: "rar-cowork-cookbook-dashboard-dispose-of-obsolete-inventory"
description: "Produces a self-contained interactive HTML dashboard for dispose of obsolete inventory - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_dispose_of_obsolete_inventory", "rar_sha256": "9ab28b05d04b7d7ccdbb2a80aa075a0e5ee31b57247977997f8c84c16fc9a6cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_dispose_of_obsolete_inventory_agent.py` and embedded as the fenced Python below (sha256 9ab28b05d04b7d7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_dispose_of_obsolete_inventory_agent.py` first:

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
    "version": '2.0.1',
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
