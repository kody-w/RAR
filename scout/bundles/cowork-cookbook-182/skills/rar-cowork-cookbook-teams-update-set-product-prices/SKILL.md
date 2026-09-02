---
name: "rar-cowork-cookbook-teams-update-set-product-prices"
description: "Drafts a Teams channel post on set product prices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_set_product_prices", "rar_sha256": "3986ef52207c0bd0e5148a5955aa0fcb95243fb7d94fd162ab5f6603f8f4e193", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_set_product_prices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-set-product-prices:3b31e7ec52394dfb72fd6786789ffec4765dd91dd9c8e325a870acaa776f3286", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_set_product_prices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_set_product_prices_agent.py` is
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
