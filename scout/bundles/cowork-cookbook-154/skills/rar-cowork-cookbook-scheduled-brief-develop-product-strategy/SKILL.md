---
name: "rar-cowork-cookbook-scheduled-brief-develop-product-strategy"
description: "Schedulable morning-brief email summarizing develop product strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_product_strategy", "rar_sha256": "42d36f533af409ec021a140853fd71911c8754b5650a1d46f21bd738acb22441", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 42d36f533af409ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_product_strategy_agent.py` first:

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
    "version": '2.0.0',
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
