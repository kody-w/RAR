---
name: "rar-cowork-cookbook-scheduled-brief-set-product-prices"
description: "Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_set_product_prices", "rar_sha256": "1e6d7d1e6956935f16c878c5e6160f3b86e91bca8f3e0fdd0be3e73107d2fb73", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_set_product_prices`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_set_product_prices_agent.py` and in the RCI capsule.

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

Set product prices Scheduled Email Brief — Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 1e6d7d1e6956935f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_set_product_prices_agent.py` first:

```bash
python3 scheduled_brief_set_product_prices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_set_product_prices_agent.py   # or on stdin
python3 scheduled_brief_set_product_prices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set product prices Scheduled Email Brief — Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_set_product_prices',
    "version": '2.0.1',
    "display_name": 'Set product prices Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-set-product-prices',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-set-product-prices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01f3e4448fe42ab9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/set-product-prices'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-set-product-prices', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefSetProductPrices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSetProductPrices'
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
    print(ScheduledBriefSetProductPrices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
