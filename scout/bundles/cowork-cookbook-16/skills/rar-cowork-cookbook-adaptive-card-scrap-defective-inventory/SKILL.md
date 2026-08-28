---
name: "rar-cowork-cookbook-adaptive-card-scrap-defective-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of scrap defective inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_scrap_defective_inventory", "rar_sha256": "5823d16a1301b9cd052ba1045745207436ecce51b915ba0a3ca51355097eb90f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_scrap_defective_inventory_agent.py` and in the RCI capsule.

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
