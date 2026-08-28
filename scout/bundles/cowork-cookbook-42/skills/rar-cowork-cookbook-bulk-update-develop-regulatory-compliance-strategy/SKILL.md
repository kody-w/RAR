---
name: "rar-cowork-cookbook-bulk-update-develop-regulatory-compliance-strategy"
description: "Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy", "rar_sha256": "7292f4e0d5eca70924270f681cfc8c7af0649235845af1f69a86997513188a93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_regulatory_compliance_strategy_agent.py` and in the RCI capsule.

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

Develop regulatory compliance strategy Bulk Field Update — Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 7292f4e0d5eca709…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_regulatory_compliance_strategy_agent.py` first:

```bash
python3 bulk_update_develop_regulatory_compliance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_regulatory_compliance_strategy_agent.py   # or on stdin
python3 bulk_update_develop_regulatory_compliance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop regulatory compliance strategy Bulk Field Update — Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy',
    "version": '2.0.0',
    "display_name": 'Develop regulatory compliance strategy Bulk Field Update',
    "description": 'Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-regulatory-compliance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-regulatory-compliance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd874fb5ce0ac343',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-regulatory-compliance-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-develop-regulatory-compliance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopRegulatoryComplianceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopRegulatoryComplianceStrategy'
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
    print(BulkUpdateDevelopRegulatoryComplianceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
