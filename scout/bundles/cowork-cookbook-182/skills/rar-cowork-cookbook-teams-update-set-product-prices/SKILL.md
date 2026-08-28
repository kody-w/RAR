---
name: "rar-cowork-cookbook-teams-update-set-product-prices"
description: "Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_product_prices", "rar_sha256": "3986ef52207c0bd0e5148a5955aa0fcb95243fb7d94fd162ab5f6603f8f4e193", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 3986ef52207c0bd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_set_product_prices_agent.py` first:

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
    "version": '2.0.0',
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
