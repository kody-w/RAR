---
name: "rar-cowork-cookbook-bulk-update-develop-regulatory-compliance-strategy"
description: "Applies a bulk field update across develop regulatory compliance strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy", "rar_sha256": "7292f4e0d5eca70924270f681cfc8c7af0649235845af1f69a86997513188a93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_regulatory_compliance_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-regulatory-compliance-strategy:2a2050db50465771e0ccf9da282b49e1cfd567d15c76c98caaa902d3757534c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_regulatory_compliance_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_regulatory_compliance_strategy_agent.py` is
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
