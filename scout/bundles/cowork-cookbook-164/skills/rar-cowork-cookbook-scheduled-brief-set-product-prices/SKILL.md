---
name: "rar-cowork-cookbook-scheduled-brief-set-product-prices"
description: "Schedulable morning-brief email summarizing set product prices for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_set_product_prices", "rar_sha256": "55bf0fe9c1d44ff3c1ff30f967c49995c6f12148f6e08118c033ddf14bd152bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_set_product_prices_agent.py` and embedded as the fenced Python below (sha256 55bf0fe9c1d44ff3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_set_product_prices_agent.py` first:

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
    "version": '2.0.0',
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
