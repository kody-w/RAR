---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-strategy"
description: "Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_strategy", "rar_sha256": "bea234f04b385eb0eaf9bd13dca60d451ebe9211770822287b4b08c757d9b51a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_product_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_product_strategy_agent.py` and in the RCI capsule.

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

Develop product strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 bea234f04b385eb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_strategy_agent.py` first:

```bash
python3 scheduled_brief_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_product_strategy_agent.py   # or on stdin
python3 scheduled_brief_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Scheduled Email Brief — Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_product_strategy',
    "version": '2.0.1',
    "display_name": 'Develop product strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e2bace9a49a50497',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopProductStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopProductStrategy'
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
    print(ScheduledBriefDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
