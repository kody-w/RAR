---
name: "rar-cowork-cookbook-teams-update-set-product-prices"
description: "Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_product_prices", "rar_sha256": "7e69432aac201053a1698b2ec20d38b7dac590289a538bf0387beddf896911d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_set_product_prices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_set_product_prices_agent.py` and in the RCI capsule.

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

Set product prices Teams Channel Update — Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-product-prices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 7e69432aac201053…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_product_prices_agent.py` first:

```bash
python3 teams_update_set_product_prices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_set_product_prices_agent.py   # or on stdin
python3 teams_update_set_product_prices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set product prices Teams Channel Update — Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-set-product-prices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_set_product_prices',
    "version": '2.0.1',
    "display_name": 'Set product prices Teams Channel Update',
    "description": 'Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-set-product-prices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-set-product-prices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70fa83079647099f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/set-product-prices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-set-product-prices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateSetProductPrices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSetProductPrices'
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
    print(TeamsUpdateSetProductPrices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
