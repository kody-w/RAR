---
name: "rar-cowork-cookbook-teams-update-end-product-sales"
description: "Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_end_product_sales", "rar_sha256": "d1269ab87c458bf068fb22887615f9058c71a5fc8d2e7fabd9c5bba01c7f11a4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_end_product_sales`. The original RAPP
agent is preserved byte-for-byte in `teams_update_end_product_sales_agent.py` and in the RCI capsule.

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

End product sales Teams Channel Update — Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 d1269ab87c458bf0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_end_product_sales_agent.py` first:

```bash
python3 teams_update_end_product_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_end_product_sales_agent.py   # or on stdin
python3 teams_update_end_product_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
End product sales Teams Channel Update — Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-end-product-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_end_product_sales',
    "version": '2.0.0',
    "display_name": 'End product sales Teams Channel Update',
    "description": 'Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-end-product-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-end-product-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5feb0d5918816ca5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/end-product-sales'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-end-product-sales', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateEndProductSales(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEndProductSales'
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
    print(TeamsUpdateEndProductSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
