---
name: "rar-cowork-cookbook-dashboard-purchase-project-materials"
description: "Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purchase_project_materials", "rar_sha256": "5f9920f4ca90cb0b9ab573811d9b50e38b835e1bf3d762149cc48612eced9167", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_purchase_project_materials`. The original RAPP
agent is preserved byte-for-byte in `dashboard_purchase_project_materials_agent.py` and in the RCI capsule.

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

Purchase project materials Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purchase-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 5f9920f4ca90cb0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purchase_project_materials_agent.py` first:

```bash
python3 dashboard_purchase_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_purchase_project_materials_agent.py   # or on stdin
python3 dashboard_purchase_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase project materials Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purchase-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_purchase_project_materials',
    "version": '2.0.1',
    "display_name": 'Purchase project materials Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-purchase-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-purchase-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e94c541b50bdfad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/purchase-project-materials'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-purchase-project-materials', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPurchaseProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPurchaseProjectMaterials'
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
    print(DashboardPurchaseProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
