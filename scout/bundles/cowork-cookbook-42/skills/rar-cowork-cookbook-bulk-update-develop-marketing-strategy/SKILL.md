---
name: "rar-cowork-cookbook-bulk-update-develop-marketing-strategy"
description: "Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_marketing_strategy", "rar_sha256": "61693a862c5ebae1e5055e9a218bde2a330aba90f0b2b30a524cd403361844b4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 61693a862c5ebae1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_marketing_strategy_agent.py` first:

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
    "version": '2.0.0',
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
