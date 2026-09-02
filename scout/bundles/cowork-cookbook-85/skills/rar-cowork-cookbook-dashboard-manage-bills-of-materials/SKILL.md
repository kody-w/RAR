---
name: "rar-cowork-cookbook-dashboard-manage-bills-of-materials"
description: "Produces a self-contained interactive HTML dashboard for manage bills of materials - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_bills_of_materials", "rar_sha256": "30f62c1364f1e02176a0896dfafe14b3b820d5ead5173e3d7cbe73be499e0a53", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_bills_of_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-bills-of-materials:4ef6f07b97d1cf9d4e3f06c5b6eb91498c3d37b5283a636648a7329d10a34034", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_bills_of_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_bills_of_materials_agent.py` is
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
