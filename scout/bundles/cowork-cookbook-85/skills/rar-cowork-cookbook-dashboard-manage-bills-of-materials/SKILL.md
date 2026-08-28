---
name: "rar-cowork-cookbook-dashboard-manage-bills-of-materials"
description: "Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_bills_of_materials", "rar_sha256": "30f62c1364f1e02176a0896dfafe14b3b820d5ead5173e3d7cbe73be499e0a53", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_bills_of_materials_agent.py` and in the RCI capsule.

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

Manage bills of materials Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 30f62c1364f1e021…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_bills_of_materials_agent.py` first:

```bash
python3 dashboard_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_bills_of_materials_agent.py   # or on stdin
python3 dashboard_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_bills_of_materials',
    "version": '2.0.0',
    "display_name": 'Manage bills of materials Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4606106dfb36a982',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageBillsOfMaterials'
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
    print(DashboardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
