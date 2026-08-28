---
name: "rar-cowork-cookbook-teams-update-end-product-sales"
description: "Drafts a Teams channel post on end product sales status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_end_product_sales", "rar_sha256": "3761e7100019a4375458264fe82dcb43c781c0f78a8cb17d6bfab129c9f4f494", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_end_product_sales_agent.py` and embedded as the fenced Python below (sha256 3761e7100019a437…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_end_product_sales_agent.py` first:

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
    "version": '2.0.1',
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
