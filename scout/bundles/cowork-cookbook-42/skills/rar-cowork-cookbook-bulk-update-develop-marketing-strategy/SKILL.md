---
name: "rar-cowork-cookbook-bulk-update-develop-marketing-strategy"
description: "Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_marketing_strategy", "rar_sha256": "335a468f3f5e4e0834eae8fb7d68b790eae2023bfa9a9c75c642c31bbf0c4ab9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_marketing_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_marketing_strategy_agent.py` and in the RCI capsule.

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

Develop marketing strategy Bulk Field Update — Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 335a468f3f5e4e08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_marketing_strategy_agent.py` first:

```bash
python3 bulk_update_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_marketing_strategy_agent.py   # or on stdin
python3 bulk_update_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Bulk Field Update — Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_marketing_strategy',
    "version": '2.0.1',
    "display_name": 'Develop marketing strategy Bulk Field Update',
    "description": 'Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01a4f08b1fadbd08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopMarketingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMarketingStrategy'
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
    print(BulkUpdateDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
