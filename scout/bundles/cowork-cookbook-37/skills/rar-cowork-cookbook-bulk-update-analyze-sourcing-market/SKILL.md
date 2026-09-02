---
name: "rar-cowork-cookbook-bulk-update-analyze-sourcing-market"
description: "Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_sourcing_market", "rar_sha256": "2901fe3860393c0e9eb779962d9a3ffea7f079930145ebf3c2019887687b646d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_sourcing_market_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-sourcing-market:b5f859d1487f49c1abb62d3e06560351f43cfdf2ee5ca020704a3998ae73385c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_sourcing_market`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_sourcing_market_agent.py` is
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

Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 2901fe3860393c0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_sourcing_market_agent.py` first:

```bash
python3 bulk_update_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_sourcing_market_agent.py   # or on stdin
python3 bulk_update_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Bulk Field Update — Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_sourcing_market',
    "version": '2.0.0',
    "display_name": 'Analyze sourcing market Bulk Field Update',
    "description": 'Applies a bulk field update across analyze sourcing market records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5555bf89a931efa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeSourcingMarket(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeSourcingMarket'
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
    print(BulkUpdateAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
