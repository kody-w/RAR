---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_materials", "rar_sha256": "efa4285852a26950157e8c140c2d2c038122210e8c3d300d8c223469372c4907", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_bills_of_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-bills-of-materials:be3368d93ac76c1a9736cba3a83736ec02433d045fe32c63c2c63dad22a0006a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_bills_of_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_bills_of_materials_agent.py` is
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

Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 efa4285852a26950…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_materials',
    "version": '2.0.0',
    "display_name": 'Manage bills of materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage bills of materials status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72b9e7b8cc16d629',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfMaterials'
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
    print(AdaptiveCardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
