---
name: "rar-cowork-cookbook-teams-update-update-product-assortments"
description: "Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_product_assortments", "rar_sha256": "fe76e73de9b537e003f1c7ddc8718048e5c0dd65d10eb6dfd18df1a3c7389c78", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_product_assortments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_product_assortments_agent.py` and in the RCI capsule.

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

Update product assortments Teams Channel Update — Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 fe76e73de9b537e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_product_assortments_agent.py` first:

```bash
python3 teams_update_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_product_assortments_agent.py   # or on stdin
python3 teams_update_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Teams Channel Update — Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_product_assortments',
    "version": '2.0.1',
    "display_name": 'Update product assortments Teams Channel Update',
    "description": 'Drafts a Teams channel post on update product assortments status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a99ee589b7c31dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateUpdateProductAssortments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateProductAssortments'
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
    print(TeamsUpdateUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
