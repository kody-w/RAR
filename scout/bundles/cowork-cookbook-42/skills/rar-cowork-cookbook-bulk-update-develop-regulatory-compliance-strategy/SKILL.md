---
name: "rar-cowork-cookbook-bulk-update-develop-regulatory-compliance-strategy"
description: "Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy", "rar_sha256": "6cd0d68626b3397ce3437bf250ccd66d0d95e767caf8d7ad20c8ec116f480125", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_regulatory_compliance_strategy_agent.py` and embedded as the fenced Python below (sha256 6cd0d68626b3397c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_regulatory_compliance_strategy_agent.py` first:

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
    "version": '2.0.1',
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
