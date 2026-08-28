---
name: "rar-cowork-cookbook-dashboard-purchase-project-materials"
description: "Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purchase_project_materials", "rar_sha256": "057a2d689b06b73d7df6f904cb9db9a07bbaf9246f41fd3743b1130c746e7bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 057a2d689b06b73d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purchase_project_materials_agent.py` first:

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
    "version": '2.0.0',
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
