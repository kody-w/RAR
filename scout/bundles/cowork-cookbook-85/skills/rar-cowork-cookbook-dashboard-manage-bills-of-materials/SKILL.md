---
name: "rar-cowork-cookbook-dashboard-manage-bills-of-materials"
description: "Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_bills_of_materials", "rar_sha256": "19a703083967cee346271de4ce6f2f6d12a2f4a6ba6363ec321249dd2c335b98", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 19a703083967cee3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_bills_of_materials_agent.py` first:

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
    "version": '2.0.1',
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
