---
name: "rar-cowork-cookbook-dashboard-purchase-project-materials"
description: "Produces a self-contained interactive HTML dashboard for purchase project materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purchase_project_materials", "rar_sha256": "057a2d689b06b73d7df6f904cb9db9a07bbaf9246f41fd3743b1130c746e7bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_purchase_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-purchase-project-materials:8188f02f4d5db7c2e67ae35cd6ee4a10ae308213ae964c8501bd5114a7398e6c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_purchase_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_purchase_project_materials_agent.py` is
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
