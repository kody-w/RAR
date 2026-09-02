---
name: "rar-cowork-cookbook-adaptive-card-scrap-defective-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_scrap_defective_inventory", "rar_sha256": "5823d16a1301b9cd052ba1045745207436ecce51b915ba0a3ca51355097eb90f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_scrap_defective_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-scrap-defective-inventory:fa5e6d3cac26c696f2d4e272ddd12bd5f5ef3e780916b1e7549ebf28ca22ad09", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_scrap_defective_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_scrap_defective_inventory_agent.py` is
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

Scrap defective inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 5823d16a1301b9cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_scrap_defective_inventory_agent.py` first:

```bash
python3 adaptive_card_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_scrap_defective_inventory_agent.py   # or on stdin
python3 adaptive_card_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_scrap_defective_inventory',
    "version": '2.0.0',
    "display_name": 'Scrap defective inventory Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a1f2bd2a12b6e657',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardScrapDefectiveInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardScrapDefectiveInventory'
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
    print(AdaptiveCardScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
